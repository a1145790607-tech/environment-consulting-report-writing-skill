#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scan Chinese environmental consulting report text for weak expressions."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


BUILT_IN_PATTERNS: list[tuple[str, str]] = [
    (r"不是.{0,30}而是", "慎用否定式转折，建议改为直接正向表述。"),
    (r"并非.{0,30}而是", "慎用解释性转折，建议直接写技术定位或结论。"),
    (r"不能理解为.{0,30}应理解为", "解释过重，建议改为正向定义。"),
    (r"确保达标", "绝对化表述，建议改为“具备达标条件”或“有助于稳定达标”。"),
    (r"完全没有影响|无影响", "绝对化表述，建议写明影响范围、增量和判断条件。"),
    (r"不存在风险|无风险", "绝对化表述，建议改为“风险具备管控条件”。"),
    (r"总体可控", "结论偏空，建议写明风险对象、管控措施和成立条件。"),
    (r"影响较小", "判断偏空，建议写明影响对象、范围、指标增量和依据。"),
    (r"具有重要意义", "价值判断偏空，建议说明对哪一项判断、措施或管理要求有作用。"),
    (r"提供有力支撑", "支撑对象不清，建议说明支撑的技术判断或管理用途。"),
    (r"科学合理|切实可行", "结论过泛，建议补充标准、设计条件、运行条件或技术依据。"),
    (r"进一步加强|持续推进|不断完善", "措施偏空，建议写明对象、措施、频次、触发条件或责任方向。"),
    (r"相关要求|有关规划", "依据不清，建议写明具体法规、标准、规划或文件名称。"),
]


def read_docx(path: Path) -> str:
    try:
        import docx  # type: ignore
    except ImportError as exc:
        raise SystemExit("Reading .docx requires python-docx: pip install python-docx") from exc

    document = docx.Document(str(path))
    return "\n".join(paragraph.text for paragraph in document.paragraphs)


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        return read_docx(path)

    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def load_csv_patterns(skill_root: Path) -> list[tuple[str, str]]:
    csv_path = skill_root / "data" / "avoid_phrases.csv"
    if not csv_path.exists():
        return []

    patterns: list[tuple[str, str]] = []
    with csv_path.open("r", encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            phrase = (row.get("phrase") or "").strip()
            issue = (row.get("issue") or "").strip()
            direction = (row.get("preferred_direction") or "").strip()
            if phrase:
                patterns.append((re.escape(phrase), f"{issue}；建议：{direction}"))
    return patterns


def line_col(text: str, index: int) -> tuple[int, int]:
    line = text.count("\n", 0, index) + 1
    prev = text.rfind("\n", 0, index)
    col = index + 1 if prev == -1 else index - prev
    return line, col


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python scripts/check_report_style.py path/to/report.txt|docx")
        return 2

    report_path = Path(argv[1])
    if not report_path.exists():
        print(f"File not found: {report_path}")
        return 2

    skill_root = Path(__file__).resolve().parents[1]
    patterns = BUILT_IN_PATTERNS + load_csv_patterns(skill_root)
    text = read_text(report_path)
    findings: list[tuple[int, int, str, str]] = []
    seen: set[tuple[int, str]] = set()

    for pattern, message in patterns:
        for match in re.finditer(pattern, text):
            line, col = line_col(text, match.start())
            key = (match.start(), message)
            if key in seen:
                continue
            seen.add(key)
            findings.append((line, col, match.group(0), message))

    if not findings:
        print("No high-frequency weak expressions were found by the built-in rules.")
        return 0

    print(f"Found {len(findings)} possible issue(s):\n")
    for index, (line, col, snippet, message) in enumerate(findings, 1):
        print(f"{index}. Line {line}, column {col}: {snippet}")
        print(f"   {message}\n")

    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
