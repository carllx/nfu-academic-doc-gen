"""
chapter_utils.py — 动态章节命名引擎 (Nomenclature Inference System)

核心职责：
  根据课程学时类型（理论/实践比例）和可选的显式配置，
  自动合成章节标题前缀（"第1章" / "项目一" / "实验一" 等）。

推导优先级链：
  1. course.chapter_nomenclature (显式覆盖，最高优先)
  2. hours.theory == 0 → 推断为纯实践课程
     2a. 课程名含 "实验" → "experiment"
     2b. 课程名含 "实训/实习" → "practice"
     2c. 其余 → "project"
  3. 默认 → "chapter"

输出格式：
  chapter:    "第1章  {title}"   (阿拉伯数字)
  project:    "项目一  {title}"  (中文数字)
  experiment: "实验一  {title}"  (中文数字)
  practice:   "实践一  {title}"  (中文数字)

消费者:
  - gen_syllabus_xml.py  (大纲 "三、课程内容和教学要求")
  - gen_lessonplan_xml.py (教案散页 R0 + 教案封面章节表)
"""

import re

# ═══════════════════════════════════════════════════════════════════════
# 1. 中文数字转换
# ═══════════════════════════════════════════════════════════════════════

_CN_NUMS = '零一二三四五六七八九十'


def _to_cn_num(n: int) -> str:
    """将阿拉伯数字转为中文数字（1-99）。"""
    if n <= 0:
        return str(n)
    if n <= 10:
        return _CN_NUMS[n]
    if n < 20:
        return f'十{_CN_NUMS[n - 10]}' if n > 10 else '十'
    tens = n // 10
    ones = n % 10
    result = f'{_CN_NUMS[tens]}十'
    if ones:
        result += _CN_NUMS[ones]
    return result


# ═══════════════════════════════════════════════════════════════════════
# 2. 命名体系推导
# ═══════════════════════════════════════════════════════════════════════

# 合法的 nomenclature 值
VALID_NOMENCLATURES = {'chapter', 'project', 'experiment', 'practice'}

# 课程名关键词到 nomenclature 的映射（用于纯实践课的自动推断）
_PRACTICE_KEYWORD_MAP = [
    (re.compile(r'实验'), 'experiment'),
    (re.compile(r'实训|实习'), 'practice'),
]

# nomenclature → (前缀词, 是否使用中文数字)
_NOMENCLATURE_FORMAT = {
    'chapter':    ('第{n}章', False),   # 阿拉伯数字: 第1章, 第2章
    'project':    ('项目{n}', True),    # 中文数字: 项目一, 项目二
    'experiment': ('实验{n}', True),    # 中文数字: 实验一, 实验二
    'practice':   ('实践{n}', True),    # 中文数字: 实践一, 实践二
}


def infer_nomenclature(course: dict) -> str:
    """推导课程的章节命名体系。

    优先级链：
      1. course.chapter_nomenclature (显式覆盖)
      2. hours.theory == 0 → 按课程名关键词推断
      3. 默认 → "chapter"

    Args:
        course: course.yaml 中的 course 节点 (dict)

    Returns:
        命名体系标识符: "chapter" | "project" | "experiment" | "practice"
    """
    # 优先级 1: 显式配置
    explicit = course.get('chapter_nomenclature', '')
    if explicit and explicit in VALID_NOMENCLATURES:
        return explicit

    # 优先级 2: 纯实践课推断 (theory == 0)
    hours = course.get('hours', {})
    if isinstance(hours, dict):
        theory = hours.get('theory', -1)
        if theory == 0:
            name = course.get('name', '')
            for pattern, nomenclature in _PRACTICE_KEYWORD_MAP:
                if pattern.search(name):
                    return nomenclature
            # 兜底: 纯实践课默认使用 "chapter" (用户暂定要求改回章节)
            return 'chapter'

    # 优先级 3: 默认
    return 'chapter'


def build_chapter_prefix(nomenclature: str, index: int) -> str:
    """根据命名体系和序号，生成章节前缀字符串。

    Args:
        nomenclature: 命名体系标识符
        index: 章节序号 (1-based)

    Returns:
        前缀字符串，例如 "第1章", "项目一", "实验三"
    """
    fmt_template, use_cn = _NOMENCLATURE_FORMAT.get(
        nomenclature, _NOMENCLATURE_FORMAT['chapter']
    )
    n_str = _to_cn_num(index) if use_cn else str(index)
    return fmt_template.format(n=n_str)


def build_chapter_title(course: dict, week: dict, default_index: int) -> str:
    """合成完整的章节标题（前缀 + 标题文本）。

    这是各生成器应统一调用的公共 API。

    Args:
        course: course.yaml 中的 course 节点
        week: calendar[] 中的单条周数据
        default_index: 1-based 默认序号（当 week.chapter 缺失时使用）

    Returns:
        完整标题字符串，例如:
          "第1章  交互体系概论基础"
          "项目一  交互体系概论基础"
    """
    # 确定标题文本（优先 chapter_title，回退 topic）
    title_text = week.get('chapter_title', '') or week.get('topic', '')
    if not title_text:
        return ''

    # 确定序号
    chapter_num = week.get('chapter')
    if chapter_num is not None:
        try:
            index = int(chapter_num)
        except (ValueError, TypeError):
            index = default_index
    else:
        index = default_index

    # 推导命名体系并合成前缀
    nomenclature = infer_nomenclature(course)
    prefix = build_chapter_prefix(nomenclature, index)

    # 使用两个全角空格分隔前缀与标题（与教务文档模板一致）
    return f"{prefix}  {title_text}"
