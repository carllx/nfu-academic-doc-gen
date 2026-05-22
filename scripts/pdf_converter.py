"""
pdf_converter.py — LibreOffice headless PDF 转换工具

提供 docx → PDF 的转换能力，供 generate.py 在生成 docx 后调用。
底层使用 LibreOffice headless 模式，保证排版一致性。

使用方式:
    from scripts.pdf_converter import convert_to_pdf, batch_convert_to_pdf

    # 单文件转换
    pdf_path = convert_to_pdf(Path("output.docx"))

    # 批量转换
    pdf_paths = batch_convert_to_pdf([Path("a.docx"), Path("b.docx")])
"""

import os
import subprocess
import time
from pathlib import Path
from typing import List, Optional

# LibreOffice 可执行文件路径（macOS Homebrew 安装）
SOFFICE_PATH = "/opt/homebrew/bin/soffice"

# 默认超时时间（秒）— 单文件转换
DEFAULT_TIMEOUT = 60

# 指数退避重试配置
MAX_RETRIES = 5
BASE_DELAY = 1.0  # 秒


def _find_soffice() -> str:
    """查找 LibreOffice soffice 可执行文件路径。

    优先使用硬编码路径，若不存在则尝试 PATH 查找。

    Returns:
        soffice 可执行文件的绝对路径。

    Raises:
        FileNotFoundError: 未找到 soffice。
    """
    if os.path.isfile(SOFFICE_PATH):
        return SOFFICE_PATH

    # 回退：从 PATH 中查找
    import shutil
    path = shutil.which("soffice")
    if path:
        return path

    raise FileNotFoundError(
        "未找到 LibreOffice (soffice)。请确认已安装：brew install --cask libreoffice"
    )


def convert_to_pdf(
    docx_path: Path,
    output_dir: Optional[Path] = None,
    timeout: int = DEFAULT_TIMEOUT,
) -> Optional[Path]:
    """使用 LibreOffice headless 将单个 docx 转为 PDF。

    Args:
        docx_path: 源 .docx 文件路径。
        output_dir: PDF 输出目录。默认为源文件所在目录。
        timeout: 单次转换超时时间（秒）。

    Returns:
        生成的 PDF 文件路径。转换失败返回 None。
    """
    docx_path = Path(docx_path).resolve()
    if not docx_path.exists():
        print(f"    ⚠️ [PDF] 源文件不存在: {docx_path}")
        return None

    if output_dir is None:
        output_dir = docx_path.parent
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    soffice = _find_soffice()
    expected_pdf = output_dir / docx_path.with_suffix('.pdf').name

    # 指数退避重试
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            cmd = [
                soffice,
                "--headless",
                "--convert-to", "pdf",
                "--outdir", str(output_dir),
                str(docx_path),
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
            )

            if result.returncode == 0 and expected_pdf.exists() and expected_pdf.stat().st_size > 0:
                return expected_pdf

            # 转换命令成功但 PDF 未生成或为空
            if attempt < MAX_RETRIES:
                delay = BASE_DELAY * (2 ** (attempt - 1))
                print(f"    ⚠️ [PDF] 转换未成功 (attempt {attempt}/{MAX_RETRIES}), "
                      f"{delay:.1f}s 后重试...")
                if result.stderr:
                    print(f"        stderr: {result.stderr.strip()[:200]}")
                time.sleep(delay)
            else:
                print(f"    ❌ [PDF] 转换失败 ({MAX_RETRIES} 次重试后): {docx_path.name}")
                if result.stderr:
                    print(f"        stderr: {result.stderr.strip()[:200]}")
                return None

        except subprocess.TimeoutExpired:
            if attempt < MAX_RETRIES:
                delay = BASE_DELAY * (2 ** (attempt - 1))
                print(f"    ⚠️ [PDF] 转换超时 (>{timeout}s, attempt {attempt}/{MAX_RETRIES}), "
                      f"{delay:.1f}s 后重试...")
                time.sleep(delay)
            else:
                print(f"    ❌ [PDF] 转换超时 ({MAX_RETRIES} 次重试后): {docx_path.name}")
                return None

        except FileNotFoundError:
            print(f"    ❌ [PDF] LibreOffice 未安装或路径错误: {soffice}")
            return None

    return None


def batch_convert_to_pdf(
    docx_paths: List[Path],
    output_dir: Optional[Path] = None,
    timeout: int = DEFAULT_TIMEOUT,
) -> List[Path]:
    """批量将 docx 文件转换为 PDF。

    逐个调用 convert_to_pdf()，带进度输出。
    转换失败的文件会被跳过并报告。

    Args:
        docx_paths: 源 .docx 文件路径列表。
        output_dir: PDF 输出目录。None 表示各文件输出到其所在目录。
        timeout: 单个文件的超时时间（秒）。

    Returns:
        成功生成的 PDF 路径列表。
    """
    if not docx_paths:
        return []

    total = len(docx_paths)
    print(f"\n  📄 开始 PDF 转换 ({total} 个文件)...")

    results = []
    failed = []

    for idx, docx_path in enumerate(docx_paths, 1):
        docx_path = Path(docx_path)
        # 如果未指定统一输出目录，则输出到源文件所在目录
        target_dir = output_dir if output_dir else docx_path.parent

        print(f"    [{idx}/{total}] {docx_path.name}", end=" → ", flush=True)

        pdf = convert_to_pdf(docx_path, target_dir, timeout)
        if pdf:
            print(f"✅ {pdf.name} ({pdf.stat().st_size / 1024:.0f} KB)")
            results.append(pdf)
        else:
            print(f"❌ 失败")
            failed.append(docx_path)

    # 汇总
    print(f"\n  📊 PDF 转换完成: {len(results)}/{total} 成功", end="")
    if failed:
        print(f", {len(failed)} 失败:")
        for f in failed:
            print(f"      ❌ {f.name}")
    else:
        print()

    return results
