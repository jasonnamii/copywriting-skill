#!/usr/bin/env python3
"""copywriting-skill self-check.

스킬 자체 건강 진단. skill-doctor의 자식 버전. 외부 파일 없이 SKILL.md·references·evals 정합성만 검증.

사용:
    python scripts/self_check.py [skill_root]

반환: exit 0 = PASS, exit 1 = FAIL
"""

import json
import os
import re
import sys
from pathlib import Path


ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()


def check_skill_md_size(root: Path) -> tuple[bool, str]:
    skill = root / "SKILL.md"
    if not skill.exists():
        return False, "SKILL.md 없음"
    size = skill.stat().st_size
    if size > 10_240:
        return False, f"SKILL.md {size}B > 10KB (축소 필요)"
    return True, f"SKILL.md {size}B ≤ 10KB"


def check_description_length(root: Path) -> tuple[bool, str]:
    skill = root / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    m = re.search(r"^---\n(.*?)^---", text, re.S | re.M)
    if not m:
        return False, "frontmatter 없음"
    fm = m.group(1)
    desc_m = re.search(r"^description:\s*\|\s*\n((?:  .*\n)+)", fm, re.M)
    if not desc_m:
        desc_m = re.search(r"^description:\s*(.+)$", fm, re.M)
        if not desc_m:
            return False, "description 필드 없음"
        desc = desc_m.group(1)
    else:
        desc = desc_m.group(1)
    chars = len(desc.strip())
    if chars > 500:
        return False, f"description {chars}자 > 500자"
    return True, f"description {chars}자 ≤ 500자"


def check_at_uses_exist(root: Path) -> tuple[bool, str]:
    skill = root / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    refs = re.findall(r"-\s+(references/[^\s]+\.md)", text)
    missing = [r for r in refs if not (root / r).exists()]
    if missing:
        return False, f"@uses 깨진 경로 {len(missing)}: {missing[:3]}"
    return True, f"@uses 경로 {len(refs)}개 모두 유효"


def check_evals_exists(root: Path) -> tuple[bool, str]:
    cases = root / "evals" / "cases.json"
    if not cases.exists():
        return False, "evals/cases.json 없음"
    try:
        data = json.loads(cases.read_text(encoding="utf-8"))
    except Exception as e:
        return False, f"evals/cases.json 파싱 실패: {e}"
    n = len(data.get("cases", []))
    if n < 3:
        return False, f"샘플 케이스 {n}개 < 3개"
    return True, f"evals/cases.json {n}개 샘플"


def check_scripts(root: Path) -> tuple[bool, str]:
    scripts = root / "scripts"
    if not scripts.exists():
        return True, "scripts/ 없음 (선택)"
    py = list(scripts.glob("*.py"))
    return True, f"scripts/ {len(py)}개 Python"


def check_changelog(root: Path) -> tuple[bool, str]:
    cl = root / "CHANGELOG.md"
    if not cl.exists():
        return False, "CHANGELOG.md 없음"
    return True, "CHANGELOG.md 존재"


def check_version_in_frontmatter(root: Path) -> tuple[bool, str]:
    skill = root / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    m = re.search(r"^version:\s*(.+)$", text, re.M)
    if not m:
        return False, "frontmatter에 version 없음"
    return True, f"version: {m.group(1).strip()}"


CHECKS = [
    ("SKILL.md 크기", check_skill_md_size),
    ("description 길이", check_description_length),
    ("@uses 경로", check_at_uses_exist),
    ("evals 존재", check_evals_exists),
    ("scripts 존재", check_scripts),
    ("CHANGELOG 존재", check_changelog),
    ("version 필드", check_version_in_frontmatter),
]


def main() -> int:
    print(f"=== copywriting-skill self-check ({ROOT}) ===")
    failed = 0
    for name, fn in CHECKS:
        ok, msg = fn(ROOT)
        mark = "PASS" if ok else "FAIL"
        print(f"[{mark}] {name}: {msg}")
        if not ok:
            failed += 1
    print(f"\n결과: {len(CHECKS) - failed}/{len(CHECKS)} PASS")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
