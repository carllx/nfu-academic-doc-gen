"""
reading_utils.py — 教材章节引用提取与解析工具

功能概览：
  Phase 0: extract_readings_from_week() — 从周数据提取自由文本引用（教案 R7）
  Phase 2b: resolve_chapter_titles()   — 将自由文本引用解析为带章节标题的标准化引用
                                          （大纲 §三、教案 R1、进度表 列4）

提取优先级（SSOT 原则）：
  1. week['readings'] 显式字段 — 教师手动指定，最高优先级
  2. 正则匹配《书名》+ 章节格式 — 从 objectives/content/steps 中自动提取
  3. 正则匹配已知教材作者姓氏 + ChX 格式 — 利用全局 textbooks 的 author 信息
"""

import re
from typing import Optional, Union


def extract_readings_from_week(
    week: dict,
    textbooks: Optional[list[dict]] = None
) -> list[str]:
    """从单周教学数据中提取课前阅读教材与章节引用。

    Args:
        week: calendar[] 中的单个周对象（含 lessons, content,
              teaching_requirements 等字段）
        textbooks: 全局教材列表，用于提取作者姓氏作为正则锚点。
                   每个元素应含 'author' 和 'title' 键。

    Returns:
        提取到的阅读引用列表。
        示例: ['《信息可视化设计》第一、二章', 'Munzner Ch1']
        无匹配时返回空列表。
    """
    textbooks = textbooks or []

    # ── 优先级 1: 显式字段（SSOT）──
    # 若教师已手动指定 readings，直接返回，不执行正则
    if 'readings' in week and isinstance(week['readings'], list) and week['readings']:
        return list(week['readings'])

    # ── 汇集所有可搜索的文本源 ──
    text_sources = []

    # lessons 中的 objectives 和 steps
    for lesson in week.get('lessons', []):
        text_sources.extend(lesson.get('objectives', []))
        for step in lesson.get('steps', []):
            if 'summary' in step:
                text_sources.append(step['summary'])
            if 'content' in step:
                text_sources.append(step['content'])

    # teaching_requirements（兼容 dict 和 str 两种格式）
    tr = week.get('teaching_requirements')
    if tr is not None:
        if isinstance(tr, dict):
            text_sources.extend([str(v) for v in tr.values()])
        else:
            text_sources.append(str(tr))

    # content 字段
    content = week.get('content', '')
    if content:
        text_sources.append(str(content))

    full_text = '\n'.join(text_sources)
    extracted = []

    # ── 优先级 2: 正则匹配《书名》+ 可选章节 ──
    # 匹配示例: 《信息可视化设计》第一、二章  /  《交互设计》  /  《信息可视化设计》Ch5
    pattern_book = re.compile(
        r'《[^》]+》'
        r'(?:第[\d一二三四五六七八九十、，和及\-\~]+[章部分节]'
        r'|Ch(?:apter)?\s*[\d]+(?:\s*[/,、]\s*Ch(?:apter)?\s*[\d]+)*)?'
    )
    for match in pattern_book.finditer(full_text):
        text = match.group(0).strip()
        if text not in extracted:
            extracted.append(text)

    # ── 优先级 3: 正则匹配 已知作者姓氏 + ChX / 第X章 ──
    # 从全局 textbooks 提取西文作者姓氏用作锚点
    authors = set()
    for tb in textbooks:
        author_str = tb.get('author', '')
        # 按分号、逗号拆分多作者
        for segment in author_str.split(';'):
            for part in segment.split(','):
                cleaned = part.replace('著', '').replace('等译', '').strip()
                tokens = cleaned.split()
                if tokens:
                    last_name = tokens[-1]
                    # 仅保留纯英文姓氏
                    if re.match(r'^[A-Za-z]+$', last_name):
                        authors.add(last_name)

    for author in authors:
        # 匹配示例: Munzner Ch1  /  Munzner Ch5/Ch6  /  Munzner Chapter 11
        pattern_author = re.compile(
            rf'{re.escape(author)}\s+'
            rf'Ch(?:apter)?\s*[\d]+(?:\s*[/,、]\s*Ch(?:apter)?\s*[\d]+)*',
            re.IGNORECASE
        )
        for match in pattern_author.finditer(full_text):
            text = match.group(0).strip()
            if text not in extracted:
                extracted.append(text)

    return extracted


# ═══════════════════════════════════════════════════════════════════════
# Phase 2b: 教材章节标题解析引擎
# ═══════════════════════════════════════════════════════════════════════

# ── 中文数字转换 ──────────────────────────────────────────

_CN_SIMPLE = {
    '一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
    '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
}
_INT_TO_CN = {v: k for k, v in _CN_SIMPLE.items()}


def _cn_to_int(cn: str) -> int:
    """中文数字 → 整数（支持 一~二十一）。"""
    cn = cn.strip()
    if cn in _CN_SIMPLE:
        return _CN_SIMPLE[cn]
    if cn.startswith('二十'):
        return 20 + _CN_SIMPLE.get(cn[2:], 0)
    if cn.startswith('十'):
        return 10 + _CN_SIMPLE.get(cn[1:], 0)
    return 0


def _int_to_cn(n: int) -> str:
    """整数 → 中文数字（支持 1~21）。"""
    if n in _INT_TO_CN:
        return _INT_TO_CN[n]
    if 11 <= n <= 19:
        return f"十{_INT_TO_CN[n - 10]}"
    if n == 20:
        return '二十'
    if n == 21:
        return '二十一'
    return str(n)


def _compress_ranges(numbers: list) -> str:
    """压缩连续整数为范围格式。[1,2,3,5,7,8] → '1-3、5、7-8'"""
    if not numbers:
        return ''
    nums = sorted(set(numbers))
    ranges = []
    start = end = nums[0]
    for n in nums[1:]:
        if n == end + 1:
            end = n
        else:
            ranges.append((start, end))
            start = end = n
    ranges.append((start, end))
    return '、'.join(str(s) if s == e else f"{s}-{e}" for s, e in ranges)


# ── 教材匹配 ──────────────────────────────────────────────

def _match_textbook(
    reading_text: str,
    textbooks: list
) -> tuple:
    """从 reading 文本中匹配教材。

    Returns:
        (textbook_dict, match_type)
        match_type: 'book'（《书名》匹配）或 'author'（作者姓氏匹配）
        未匹配到返回 (None, None)
    """
    # 策略 1：《书名》
    book_match = re.search(r'《([^》]+)》', reading_text)
    if book_match:
        book_name = book_match.group(1)
        for tb in textbooks:
            title = tb.get('title', '')
            if book_name == title or book_name in title or title in book_name:
                return tb, 'book'

    # 策略 2：首个英文单词作为作者姓氏
    author_match = re.match(r'^([A-Za-z]+)\b', reading_text.strip())
    if author_match:
        surname = author_match.group(1).lower()
        for tb in textbooks:
            if surname in tb.get('author', '').lower():
                return tb, 'author'

    return None, None


# ── 章节号提取 ────────────────────────────────────────────

def _extract_chapter_refs(reading_text: str) -> list:
    """从 reading 文本中提取章节号列表。

    返回 list[int|str]，支持：
      - 中文章节号：第一、二章 → [1, 2]；第三~五章 → [3, 4, 5]
      - 阿拉伯数字：Ch1, Ch3-5, Ch5/Ch6 → 对应列表
      - 项目编号：项目2-3 → [2, 3]
    """
    # Pattern 1: 第X章（中文数字）
    cn_match = re.search(
        r'第([一二三四五六七八九十、，和及至\-\~]+)[章部分节]',
        reading_text
    )
    if cn_match:
        cn_str = cn_match.group(1)
        # 范围模式: 一至三 / 一~三 / 一-三
        range_m = re.match(
            r'([一二三四五六七八九十]+)[至\~\-]([一二三四五六七八九十]+)',
            cn_str
        )
        if range_m:
            return list(range(_cn_to_int(range_m.group(1)),
                              _cn_to_int(range_m.group(2)) + 1))
        # 枚举模式: 一、二、三
        parts = re.split(r'[、，和及]', cn_str)
        return [n for p in parts if (n := _cn_to_int(p.strip())) > 0]

    # Pattern 1.5: 第X章（阿拉伯数字，如 第1章 / 第1、2章 / 第1-3章）
    ar_match = re.search(
        r'第(\d+(?:\s*[、，和及\-~]\s*\d+)*)[章部分节]',
        reading_text
    )
    if ar_match:
        ar_str = ar_match.group(1)
        range_m = re.match(r'(\d+)\s*[-~]\s*(\d+)', ar_str)
        if range_m:
            return list(range(int(range_m.group(1)), int(range_m.group(2)) + 1))
        parts = re.split(r'[、，和及]', ar_str)
        return [int(p.strip()) for p in parts if p.strip().isdigit()]

    # Pattern 2: ChX[-Y] / Chapter X
    range_m = re.search(
        r'Ch(?:apter)?\s*(\d+)\s*[-~]\s*(?:Ch(?:apter)?\s*)?(\d+)',
        reading_text, re.IGNORECASE
    )
    if range_m:
        return list(range(int(range_m.group(1)), int(range_m.group(2)) + 1))
    ch_matches = re.findall(r'Ch(?:apter)?\s*(\d+)', reading_text, re.IGNORECASE)
    if ch_matches:
        return [int(m) for m in ch_matches]

    # Pattern 3: 项目X[-Y]
    proj_m = re.search(r'项目\s*(\d+)(?:\s*[-~]\s*(\d+))?', reading_text)
    if proj_m:
        start = int(proj_m.group(1))
        end = int(proj_m.group(2)) if proj_m.group(2) else start
        return list(range(start, end + 1))

    return []


def _match_string_chapters(reading_text: str, toc: list) -> list:
    """字符串型章节反向查找（如 Refactoring UI 的 section group 名）。

    当 _extract_chapter_refs 未能提取到数字章节号时，尝试将
    reading 文本中书名后的残余部分与 TOC 条目进行匹配。

    匹配策略（按优先级）：
      1. 残余文本精确等于某条 toc[].chapter（字符串键）
      2. 残余文本精确等于某条 toc[].title_en（英文原标题）
      3. 残余文本是某条 toc[].chapter 的子串（容错匹配）
    """
    # 剥离书名，提取残余文本
    remainder = re.sub(r'《[^》]+》\s*', '', reading_text).strip()
    if not remainder:
        return []

    for item in toc:
        ch = item.get('chapter', '')
        title_en = item.get('title_en', '')
        # 精确匹配 chapter 键
        if isinstance(ch, str) and ch == remainder:
            return [ch]
        # 精确匹配 title_en
        if title_en and title_en == remainder:
            return [ch]
        # 容错：remainder 是 chapter 键的子串，或反之
        if isinstance(ch, str) and (remainder in ch or ch in remainder):
            return [ch]

    return []


# ── 格式化输出 ────────────────────────────────────────────

def _format_resolved(
    book_title: str,
    toc: list,
    chapters: list,
    match_type: str,
    original_text: str,
    fmt: str = 'full'
) -> str:
    """格式化解析后的引用文本。

    Args:
        book_title: 教材标题
        toc: 目录列表 [{chapter, title, title_en?}]
        chapters: 提取到的章节号列表
        match_type: 'book' 或 'author'
        original_text: 原始 reading 文本
        fmt: 'full'（大纲/教案）或 'short'（进度表）
    """
    if not chapters or not toc:
        return original_text

    # 章节号 → 标题映射
    ch_lookup = {item.get('chapter'): item.get('title', '') for item in toc}

    # 检查是否至少有一个章节找到了标题
    found = [(ch, ch_lookup.get(ch, '')) for ch in chapters]
    if not any(t for _, t in found):
        return original_text

    # ── 短格式（进度表） ──
    if fmt == 'short':
        if all(isinstance(c, int) for c in chapters):
            compressed = _compress_ranges(chapters)
            if match_type == 'book':
                return f"《{book_title}》§{compressed}"
            surname = re.match(r'^([A-Za-z]+)', original_text.strip())
            prefix = surname.group(1) if surname else book_title
            return f"{prefix} §{compressed}"
        # 字符串型章节（如 Refactoring UI）
        titles = [t for _, t in found if t]
        if match_type == 'book':
            return f"《{book_title}》{'、'.join(titles)}"
        return original_text

    # ── 完整格式（大纲/教案） ──
    parts = []
    for ch, title in found:
        if isinstance(ch, int):
            cn = _int_to_cn(ch)
            parts.append(f"第{cn}章 {title}" if title else f"第{cn}章")
        else:
            parts.append(title if title else str(ch))

    if match_type == 'book':
        return f"《{book_title}》{'；'.join(parts)}"

    # author 模式：保留作者姓氏前缀
    surname = re.match(r'^([A-Za-z]+)', original_text.strip())
    prefix = surname.group(1) if surname else book_title
    ch_refs = '/'.join(f"Ch{c}" for c in chapters if isinstance(c, int))
    titles = '；'.join(t for _, t in found if t)
    return f"{prefix} {ch_refs} {titles}".strip()


# ── 主函数 ────────────────────────────────────────────────

def resolve_chapter_titles(
    readings: list,
    textbooks: list,
    fmt: str = 'full'
) -> list:
    """将 readings 中的自由文本引用解析为带教材章节标题的标准化引用。

    Phase 2b 核心引擎：将 calendar[].readings 与 textbooks[].toc 交叉匹配，
    输出带中文章节标题的引用文本。

    Args:
        readings: 自由文本引用列表
            示例: ["《信息可视化设计》第一、二章", "Munzner Ch1"]
        textbooks: 教材列表（含 toc 字段）。支持 dict 或 Pydantic 对象。
        fmt: 输出格式
            'full'  — 完整格式，含章节标题（大纲/教案用）
            'short' — 缩写格式，仅章节号（进度表用）

    Returns:
        解析后的引用列表。未匹配的条目保留原文。
        示例 (full): [
            "《信息可视化设计》第一章 信息的设计与视觉传达；第二章 信息可视化设计的发展",
            "Munzner Ch1 什么是可视化，为什么要做？"
        ]
    """
    if not readings or not textbooks:
        return list(readings) if readings else []

    # 统一转为 dict（兼容 Pydantic 对象）
    tb_dicts = []
    for b in textbooks:
        tb_dicts.append(b if isinstance(b, dict) else b.dict())

    resolved = []
    for reading in readings:
        if not reading or not isinstance(reading, str):
            resolved.append(str(reading) if reading else '')
            continue

        # 1. 匹配教材
        tb, match_type = _match_textbook(reading, tb_dicts)
        if tb is None:
            resolved.append(reading)
            continue

        # 2. 检查 TOC 是否存在
        toc = tb.get('toc') or []
        if not toc:
            resolved.append(reading)
            continue

        # 3. 提取章节号
        chapters = _extract_chapter_refs(reading)
        if not chapters:
            # 3b. 字符串型章节匹配（如 Refactoring UI 的 section group）
            #     从 reading 文本中剥离书名后，用剩余部分在 TOC 中反向查找
            chapters = _match_string_chapters(reading, toc)
        if not chapters:
            resolved.append(reading)
            continue

        # 4. 格式化输出
        result = _format_resolved(
            book_title=tb.get('title', ''),
            toc=toc,
            chapters=chapters,
            match_type=match_type,
            original_text=reading,
            fmt=fmt
        )
        resolved.append(result)

    return resolved
