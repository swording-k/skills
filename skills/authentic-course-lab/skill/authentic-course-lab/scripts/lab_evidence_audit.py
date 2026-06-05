#!/usr/bin/env python3
"""清点课程实验交付物，并提示常见真实性与完整性风险。"""

from __future__ import annotations

import argparse
import struct
import zipfile
from collections import defaultdict
from pathlib import Path


RISK_WORDS = (
    "fake",
    "mock",
    "generated",
    "simulated",
    "synthetic",
    "伪造",
    "假截图",
    "生成截图",
)
IGNORED_DIRS = {".git", "__pycache__", ".idea", ".vscode", "node_modules"}
IGNORED_FILES = {".DS_Store"}

CATEGORIES = {
    "源代码": {
        ".py", ".java", ".c", ".h", ".cpp", ".hpp", ".cs", ".js", ".jsx",
        ".ts", ".tsx", ".swift", ".go", ".rs", ".m", ".r", ".scala", ".kt",
    },
    "工程与配置": {
        ".slx", ".mdl", ".m", ".circ", ".sch", ".kicad_sch", ".kicad_pcb",
        ".prj", ".project", ".ino", ".ipynb", ".json", ".yaml", ".yml", ".toml",
        ".xml", ".ini", ".conf", ".properties", ".env", ".sql",
    },
    "数据与结果": {
        ".csv", ".tsv", ".xlsx", ".xls", ".mat", ".npy", ".npz", ".dat", ".txt",
        ".log", ".out", ".pcap", ".pcapng", ".cap", ".db", ".sqlite", ".sqlite3",
        ".wav", ".mp3", ".mp4", ".mov", ".avi",
    },
    "截图与图像": {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".webp"},
    "报告与说明": {".docx", ".pdf", ".md", ".pptx", ".odt"},
    "启动与自动化": {".sh", ".bat", ".cmd", ".ps1", ".command", ".makefile"},
}
IMAGE_SUFFIXES = CATEGORIES["截图与图像"]
REPORT_SUFFIXES = {".docx", ".pdf"}


def png_size(path: Path) -> tuple[int, int] | None:
    try:
        with path.open("rb") as handle:
            header = handle.read(24)
        if header[:8] == b"\x89PNG\r\n\x1a\n":
            return struct.unpack(">II", header[16:24])
    except OSError:
        pass
    return None


def docx_media_count(path: Path) -> int | None:
    try:
        with zipfile.ZipFile(path) as archive:
            return sum(
                name.startswith("word/media/") and not name.endswith("/")
                for name in archive.namelist()
            )
    except (OSError, zipfile.BadZipFile):
        return None


def risk_words(path: Path) -> list[str]:
    lowered = str(path).lower()
    return [word for word in RISK_WORDS if word in lowered]


def should_include(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    return (
        path.is_file()
        and not any(part in IGNORED_DIRS for part in relative.parts)
        and path.name not in IGNORED_FILES
        and not path.name.startswith(".~")
    )


def classify(path: Path) -> str:
    suffix = path.suffix.lower()
    if path.name.lower() in {"makefile", "dockerfile"}:
        return "启动与自动化"
    for category, suffixes in CATEGORIES.items():
        if suffix in suffixes:
            return category
    return "其他证据"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path, help="实验交付目录")
    parser.add_argument("--output", type=Path, help="将审计结果写入 Markdown 文件")
    args = parser.parse_args()

    root = args.workspace.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"实验目录不存在或不是目录: {root}")

    files = sorted(path for path in root.rglob("*") if should_include(path, root))
    grouped: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        grouped[classify(path)].append(path)

    risky = [
        (path, risk_words(path.relative_to(root)))
        for path in files
        if risk_words(path.relative_to(root))
    ]

    lines = [
        "# 课程实验交付物审计",
        "",
        f"- 实验目录：`{root}`",
        f"- 文件总数：{len(files)}",
        f"- 风险命名文件：{len(risky)}",
        "",
        "## 分类汇总",
        "",
        "| 类别 | 数量 |",
        "|---|---:|",
    ]
    for category in [*CATEGORIES, "其他证据"]:
        lines.append(f"| {category} | {len(grouped[category])} |")

    lines.extend(["", "## 报告检查"])
    reports = [path for path in files if path.suffix.lower() in REPORT_SUFFIXES]
    if not reports:
        lines.append("- 未发现 DOCX 或 PDF 实验报告，请确认指导书是否要求提交报告。")
    for report in reports:
        relative = report.relative_to(root)
        media = docx_media_count(report) if report.suffix.lower() == ".docx" else None
        detail = f"，内嵌媒体 {media} 个" if media is not None else ""
        lines.append(f"- `{relative}`：{report.stat().st_size} 字节{detail}")

    lines.extend(["", "## 截图与图像检查"])
    images = grouped["截图与图像"]
    if not images:
        lines.append("- 未发现截图或图像，请确认是否已为关键实验步骤保存原生截图。")
    for image in images:
        relative = image.relative_to(root)
        size = png_size(image)
        detail = f"{size[0]}x{size[1]}" if size else "尺寸需人工检查"
        lines.append(f"- `{relative}`：{detail}")

    lines.extend(["", "## 风险命名"])
    if risky:
        for path, words in risky:
            lines.append(f"- `{path.relative_to(root)}`：命中 {', '.join(words)}")
    else:
        lines.append("- 未发现带有常见伪造或生成证据风险词的文件名。")

    lines.extend(
        [
            "",
            "## 必须人工核验",
            "",
            "- 将指导书每项要求映射到实际执行步骤与权威证据。",
            "- 检查每一步记录是否包含操作、输入、实际结果和对应截图。",
            "- 目视检查截图，确认来自真实软件或设备界面；尺寸不能证明真实性。",
            "- 确认指导书指定的软件、设备或 GUI 确实被操作过。",
            "- 改变输入或参数重新运行，确认程序、模型或实验结果会真实变化。",
            "- 确认报告中的步骤、数据、结论与当前工程和证据一致。",
            "- 从交付目录重新打开工程并完整走一遍教师现场演示。",
            "",
            "## 结论",
            "",
            (
                "- 自动审计发现风险命名文件，必须人工确认后再提交。"
                if risky
                else "- 自动审计未发现风险命名；仍需完成上述人工真实性与完整性核验。"
            ),
        ]
    )

    output = "\n".join(lines) + "\n"
    if args.output:
        args.output.expanduser().resolve().write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 1 if risky else 0


if __name__ == "__main__":
    raise SystemExit(main())
