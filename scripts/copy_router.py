#!/usr/bin/env python3
"""
copy_router.py — Copywriting Engine 라우터
유형 판별 · 이론 매핑 · 톤 추천 · 스포크 매핑을 자동화.

Usage:
  python scripts/copy_router.py type "브리프 또는 카피 설명"
  python scripts/copy_router.py theory A1
  python scripts/copy_router.py tone A1 c8
  python scripts/copy_router.py tone A1 universal
  python scripts/copy_router.py spokes A1 c8 hip
  python scripts/copy_router.py --types          # 27유형 전체 목록
  python scripts/copy_router.py --theories       # 이론 매핑 전체
  python scripts/copy_router.py --tones          # 톤 시스템 전체
"""

import sys
import json
import re

# ============================================================
# 27 Copy Types
# ============================================================
TYPES = {
    # A: App Internal Copy
    "A1":  {"name": "온보딩 Onboarding", "series": "A", "purpose": "첫경험→가치인식→완주", "modes": ["c8", "universal"]},
    "A2":  {"name": "빈상태 Empty State", "series": "A", "purpose": "이탈방지→첫행동유발", "modes": ["c8", "universal"]},
    "A3":  {"name": "에러/시스템 Error Message", "series": "A", "purpose": "불안해소→다음행동안내", "modes": ["c8", "universal"]},
    "A4":  {"name": "버튼·CTA Label", "series": "A", "purpose": "클릭/탭 전환", "modes": ["c8", "universal"]},
    "A5":  {"name": "툴팁·가이드 Tooltip", "series": "A", "purpose": "기능이해→사용유도", "modes": ["c8", "universal"]},
    "A6":  {"name": "알림 Push/In-app", "series": "A", "purpose": "재방문·재참여", "modes": ["c8", "universal"]},
    "A7":  {"name": "설정·법적 Legal", "series": "A", "purpose": "신뢰→동의확보", "modes": ["c8", "universal"]},
    "A8":  {"name": "화면설계 Screen Copy", "series": "A", "purpose": "화면흐름맥락전달", "modes": ["c8", "universal"]},
    "A9":  {"name": "로딩/대기 Loading", "series": "A", "purpose": "이탈방지·체감시간단축", "modes": ["c8", "universal"]},
    "A10": {"name": "성공/완료 Success", "series": "A", "purpose": "성취감→다음행동연결", "modes": ["c8", "universal"]},
    # B: Strategy/Planning Docs (Universal only)
    "B1":  {"name": "기획안 Planning Doc", "series": "B", "purpose": "의사결정자설득→승인", "modes": ["universal"]},
    "B2":  {"name": "전략문서 Strategy Doc", "series": "B", "purpose": "방향정렬→실행동기", "modes": ["universal"]},
    "B3":  {"name": "PRD", "series": "B", "purpose": "개발팀정확한이해→구현", "modes": ["universal"]},
    "B4":  {"name": "내부보고서 Internal Report", "series": "B", "purpose": "현황공유→의사결정지원", "modes": ["universal"]},
    "B5":  {"name": "제안서 Proposal", "series": "B", "purpose": "파트너/클라이언트설득", "modes": ["universal"]},
    # C: Marketing/External Copy
    "C1":  {"name": "캠페인페이지 Campaign Page", "series": "C", "purpose": "인지→관심→전환", "modes": ["c8", "universal"]},
    "C2":  {"name": "이벤트페이지 Event Page", "series": "C", "purpose": "참여/등록전환", "modes": ["c8", "universal"]},
    "C3":  {"name": "랜딩페이지 Landing Page", "series": "C", "purpose": "단일CTA전환극대화", "modes": ["c8", "universal"]},
    "C4":  {"name": "퍼포먼스광고 Performance Ad", "series": "C", "purpose": "클릭→유입", "modes": ["c8", "universal"]},
    "C5":  {"name": "브랜딩광고 Brand Ad", "series": "C", "purpose": "인식·연상구축", "modes": ["c8", "universal"]},
    "C6":  {"name": "이메일시퀀스 Email Sequence", "series": "C", "purpose": "단계별너처링→전환", "modes": ["c8", "universal"]},
    "C7":  {"name": "SNS카피 Social Copy", "series": "C", "purpose": "참여(좋아요·공유·댓글)", "modes": ["c8", "universal"]},
    "C8":  {"name": "보도자료 PR/Press", "series": "C", "purpose": "미디어픽업→보도", "modes": ["c8", "universal"]},
    "C9":  {"name": "SEO콘텐츠 SEO Content", "series": "C", "purpose": "검색유입→체류→전환", "modes": ["c8", "universal"]},
    "C10": {"name": "앱스토어 ASO", "series": "C", "purpose": "다운로드전환", "modes": ["c8", "universal"]},
    # D: CRM/Retention
    "D1":  {"name": "리텐션이메일 Retention Email", "series": "D", "purpose": "이탈방지·재활성화", "modes": ["c8", "universal"]},
    "D2":  {"name": "CS응대 CS Template", "series": "D", "purpose": "불만해소→충성전환", "modes": ["c8", "universal"]},
    "D3":  {"name": "리뷰유도 Review Request", "series": "D", "purpose": "UGC확보→사회적증거", "modes": ["c8", "universal"]},
}

# ============================================================
# Theory Mapping: type → primary theory + backup theory
# ============================================================
THEORY_MAP = {
    # Propagation purpose
    "C1": {"primary": "STEPPS", "backup": "SUCCESs", "spoke": "theories-sticky.md"},
    "C7": {"primary": "STEPPS", "backup": "SUCCESs", "spoke": "theories-sticky.md"},
    "D3": {"primary": "STEPPS", "backup": "SUCCESs", "spoke": "theories-sticky.md"},
    # Conversion purpose
    "C3": {"primary": "PAS/AIDA", "backup": "5-Level Awareness", "spoke": "theories-funnel.md"},
    "C4": {"primary": "PAS/AIDA", "backup": "5-Level Awareness", "spoke": "theories-funnel.md"},
    "C6": {"primary": "PAS/AIDA", "backup": "Stone 7-Step", "spoke": "theories-funnel.md"},
    # Habit purpose
    "A1": {"primary": "Hook Model", "backup": "Cialdini", "spoke": "theories-product.md"},
    "A6": {"primary": "Hook Model", "backup": "Cialdini", "spoke": "theories-product.md"},
    "A10": {"primary": "Hook Model", "backup": "Cialdini", "spoke": "theories-product.md"},
    # Persuasion purpose
    "C2": {"primary": "Cialdini", "backup": "SB7", "spoke": "theories-persuasion.md"},
    "B5": {"primary": "Cialdini", "backup": "SB7", "spoke": "theories-persuasion.md"},
    "D1": {"primary": "Cialdini", "backup": "PAS", "spoke": "theories-persuasion.md"},
    # Positioning purpose
    "C5": {"primary": "Positioning", "backup": "SB7", "spoke": "theories-persuasion.md"},
    "C10": {"primary": "Positioning", "backup": "AIDA", "spoke": "theories-product.md"},
    "B2": {"primary": "Positioning", "backup": "SB7", "spoke": "theories-persuasion.md"},
    # Specification purpose
    "B3": {"primary": "4S QC", "backup": "—", "spoke": "theories-product.md"},
    "B4": {"primary": "4S QC", "backup": "—", "spoke": "theories-product.md"},
    # Default for remaining types
    "A2": {"primary": "Hook Model", "backup": "SUCCESs", "spoke": "theories-product.md"},
    "A3": {"primary": "4S QC", "backup": "—", "spoke": "theories-product.md"},
    "A4": {"primary": "Hook Model", "backup": "Cialdini", "spoke": "theories-product.md"},
    "A5": {"primary": "4S QC", "backup": "—", "spoke": "theories-product.md"},
    "A7": {"primary": "4S QC", "backup": "—", "spoke": "theories-product.md"},
    "A8": {"primary": "Hook Model", "backup": "4S QC", "spoke": "theories-product.md"},
    "A9": {"primary": "SUCCESs", "backup": "—", "spoke": "theories-sticky.md"},
    "B1": {"primary": "SB7", "backup": "Ogilvy", "spoke": "theories-persuasion.md"},
    "C8": {"primary": "Ogilvy", "backup": "4S QC", "spoke": "theories-persuasion.md"},
    "C9": {"primary": "SUCCESs", "backup": "AIDA", "spoke": "theories-sticky.md"},
    "D2": {"primary": "4S QC", "backup": "Cialdini", "spoke": "theories-product.md"},
}

# ============================================================
# Tone Recommendation Matrix
# ============================================================
# For each type × mode, recommend tone level
# hip=🔵, standard=⚪, experimental=🟡
TONE_MAP = {
    # A types: C8 mode → hip default, Universal → standard
    "A1":  {"c8": "hip", "universal": "standard"},
    "A2":  {"c8": "hip", "universal": "standard"},
    "A3":  {"c8": "standard", "universal": "standard"},  # Error = always standard
    "A4":  {"c8": "hip", "universal": "standard"},
    "A5":  {"c8": "standard", "universal": "standard"},
    "A6":  {"c8": "hip", "universal": "standard"},
    "A7":  {"c8": "standard", "universal": "standard"},  # Legal = always standard
    "A8":  {"c8": "hip", "universal": "standard"},
    "A9":  {"c8": "experimental", "universal": "standard"},
    "A10": {"c8": "hip", "universal": "standard"},
    # B types: always universal/standard
    "B1":  {"universal": "standard"},
    "B2":  {"universal": "standard"},
    "B3":  {"universal": "standard"},
    "B4":  {"universal": "standard"},
    "B5":  {"universal": "standard"},
    # C types
    "C1":  {"c8": "hip", "universal": "standard"},
    "C2":  {"c8": "hip", "universal": "standard"},
    "C3":  {"c8": "hip", "universal": "standard"},
    "C4":  {"c8": "hip", "universal": "standard"},
    "C5":  {"c8": "experimental", "universal": "standard"},
    "C6":  {"c8": "hip", "universal": "standard"},
    "C7":  {"c8": "experimental", "universal": "standard"},
    "C8":  {"c8": "standard", "universal": "standard"},  # PR = standard
    "C9":  {"c8": "hip", "universal": "standard"},
    "C10": {"c8": "hip", "universal": "standard"},
    # D types
    "D1":  {"c8": "hip", "universal": "standard"},
    "D2":  {"c8": "standard", "universal": "standard"},  # CS = standard base
    "D3":  {"c8": "hip", "universal": "standard"},
}

# ============================================================
# Spoke Routing
# ============================================================
def get_spokes(type_code, mode, tone):
    """Return list of spokes to load based on screening results."""
    spokes = []
    t = TYPES.get(type_code, {})
    series = t.get("series", "")

    # Benchmarks by series
    bench_map = {"A": "benchmarks-app.md", "B": "benchmarks-strategy.md",
                 "C": "benchmarks-marketing.md", "D": "benchmarks-crm.md"}
    if series in bench_map:
        spokes.append(bench_map[series])

    # Theory spoke
    th = THEORY_MAP.get(type_code, {})
    if th.get("spoke"):
        spokes.append(th["spoke"])

    # Tone spoke
    tone_spoke_map = {"hip": "tone-hip.md", "standard": "tone-standard.md",
                      "experimental": "tone-experimental.md"}
    if tone in tone_spoke_map:
        spokes.append(tone_spoke_map[tone])

    # Mode-specific
    if mode == "c8":
        spokes.append("cross-brand-voice.md")
        spokes.append("tone-persona-variants.md")

    # Always load QC
    spokes.append("guard-qc.md")

    return list(dict.fromkeys(spokes))  # deduplicate preserving order

# ============================================================
# Type Detection (keyword-based)
# ============================================================
TYPE_KEYWORDS = {
    "A1": ["온보딩", "onboarding", "첫화면", "시작화면", "welcome", "첫경험"],
    "A2": ["빈상태", "empty", "비어있", "아직없", "no content", "nothing here"],
    "A3": ["에러", "error", "오류", "실패", "문제발생", "something went wrong"],
    "A4": ["버튼", "button", "CTA", "클릭", "탭", "레이블"],
    "A5": ["툴팁", "tooltip", "가이드", "힌트", "help text", "도움말"],
    "A6": ["알림", "push", "notification", "푸시", "리마인더"],
    "A7": ["약관", "법적", "legal", "개인정보", "privacy", "동의", "consent", "설정"],
    "A8": ["화면", "screen", "UI", "인터페이스", "페이지내"],
    "A9": ["로딩", "loading", "대기", "불러오", "처리중"],
    "A10": ["완료", "성공", "success", "done", "축하", "congrats"],
    "B1": ["기획안", "기획서", "planning doc", "제안"],
    "B2": ["전략문서", "전략", "비전", "strategy", "방향"],
    "B3": ["PRD", "요구사항", "명세", "스펙", "specification"],
    "B4": ["보고서", "report", "현황", "분석보고"],
    "B5": ["제안서", "proposal", "외부제안", "파트너"],
    "C1": ["캠페인", "campaign", "브랜드페이지"],
    "C2": ["이벤트", "event", "기획전", "프로모션"],
    "C3": ["랜딩", "landing", "LP"],
    "C4": ["광고카피", "퍼포먼스", "performance ad", "배너광고"],
    "C5": ["슬로건", "브랜딩", "brand", "태그라인", "tagline"],
    "C6": ["이메일", "email", "뉴스레터", "newsletter", "드립"],
    "C7": ["SNS", "소셜", "인스타", "트위터", "틱톡", "social"],
    "C8": ["보도자료", "PR", "press", "언론"],
    "C9": ["SEO", "검색", "블로그", "콘텐츠마케팅"],
    "C10": ["앱스토어", "ASO", "스토어설명", "app store"],
    "D1": ["리텐션", "재활성", "이탈방지", "retention", "win-back"],
    "D2": ["CS", "고객응대", "customer service", "문의답변"],
    "D3": ["리뷰", "review", "후기", "평가요청"],
}

def detect_type(text):
    """Detect copy type from brief text."""
    text_lower = text.lower()
    scores = {}
    for code, keywords in TYPE_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw.lower() in text_lower)
        if score > 0:
            scores[code] = score

    if not scores:
        return {"detected": None, "message": "유형 자동 판별 불가. 수동 지정 필요."}

    sorted_types = sorted(scores.items(), key=lambda x: -x[1])
    top = sorted_types[0]
    result = {
        "detected": top[0],
        "type_name": TYPES[top[0]]["name"],
        "confidence": "high" if top[1] >= 2 else "medium" if top[1] >= 1 else "low",
        "purpose": TYPES[top[0]]["purpose"],
        "modes": TYPES[top[0]]["modes"],
    }
    if len(sorted_types) > 1:
        result["alternatives"] = [
            {"code": s[0], "name": TYPES[s[0]]["name"], "score": s[1]}
            for s in sorted_types[1:4]
        ]
    return result

# ============================================================
# CLI Interface
# ============================================================
def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "--types":
        print("=== 27 Copy Types ===")
        for code in sorted(TYPES.keys(), key=lambda x: (x[0], int(re.search(r'\d+', x).group()))):
            t = TYPES[code]
            modes = ", ".join(t["modes"])
            print(f"  {code:4s} | {t['name']:30s} | {t['purpose']:25s} | [{modes}]")

    elif cmd == "--theories":
        print("=== Theory Mapping ===")
        for code in sorted(THEORY_MAP.keys(), key=lambda x: (x[0], int(re.search(r'\d+', x).group()))):
            th = THEORY_MAP[code]
            print(f"  {code:4s} | 1st: {th['primary']:20s} | 2nd: {th['backup']:20s} | → {th['spoke']}")

    elif cmd == "--tones":
        print("=== Tone Recommendations ===")
        for code in sorted(TONE_MAP.keys(), key=lambda x: (x[0], int(re.search(r'\d+', x).group()))):
            tones = TONE_MAP[code]
            parts = [f"{m}: {t}" for m, t in tones.items()]
            print(f"  {code:4s} | {' | '.join(parts)}")

    elif cmd == "type":
        if len(sys.argv) < 3:
            print("Usage: python copy_router.py type \"brief text\"")
            sys.exit(1)
        text = " ".join(sys.argv[2:])
        result = detect_type(text)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif cmd == "theory":
        if len(sys.argv) < 3:
            print("Usage: python copy_router.py theory A1")
            sys.exit(1)
        code = sys.argv[2].upper()
        if code not in THEORY_MAP:
            print(f"Unknown type: {code}")
            sys.exit(1)
        th = THEORY_MAP[code]
        print(json.dumps({
            "type": code,
            "type_name": TYPES[code]["name"],
            "primary_theory": th["primary"],
            "backup_theory": th["backup"],
            "spoke": th["spoke"],
        }, ensure_ascii=False, indent=2))

    elif cmd == "tone":
        if len(sys.argv) < 4:
            print("Usage: python copy_router.py tone A1 c8|universal")
            sys.exit(1)
        code = sys.argv[2].upper()
        mode = sys.argv[3].lower()
        if code not in TONE_MAP:
            print(f"Unknown type: {code}")
            sys.exit(1)
        tones = TONE_MAP[code]
        if mode not in tones:
            mode = "universal"  # B types fallback
        recommended = tones.get(mode, "standard")
        print(json.dumps({
            "type": code,
            "mode": mode,
            "recommended_tone": recommended,
            "tone_spoke": f"tone-{recommended}.md",
            "override_notes": "에러/법적/결제 맥락은 standard 강제" if recommended != "standard" else "",
        }, ensure_ascii=False, indent=2))

    elif cmd == "spokes":
        if len(sys.argv) < 5:
            print("Usage: python copy_router.py spokes A1 c8 hip")
            sys.exit(1)
        code = sys.argv[2].upper()
        mode = sys.argv[3].lower()
        tone = sys.argv[4].lower()
        spokes = get_spokes(code, mode, tone)
        print(json.dumps({
            "type": code,
            "mode": mode,
            "tone": tone,
            "load_spokes": spokes,
            "count": len(spokes),
        }, ensure_ascii=False, indent=2))

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)

if __name__ == "__main__":
    main()
