# copywriting-engine

> 🇺🇸 [English README](./README.md)

**27유형(앱A·문서B·마케팅C·CRM D) × 12이론 × 3톤(힙/표준/실험) × C8모드+범용모드 카피라이팅 엔진. hit-skill·human-skill 하류 소비.**

## 사전 요구

- **Claude Cowork 또는 Claude Code** 환경

## 목표

대부분의 팀은 카피를 감으로 쓴다. 앱 UI, 마케팅 페이지, 이메일, 문서마다 톤이 다르고 일관성이 없다. 이 스킬은 카피라이팅을 구조화된 체계로 전환한다 — 27개 유형 각각에 목적, 이론, 톤, 벤치마크, QC가 매핑된다. hit-skill(반응 원리)과 human-skill(행동 메커니즘)을 소비하여 모든 카피를 검증된 심리학에 근거시킨다.

## 사용 시점 & 방법

카피 관련 요청에 자동 발동: "카피 써줘", "카피 진단해줘", "write copy". 유형(A1-A10 앱, B1-B5 문서, C1-C10 마케팅, D1-D3 CRM)을 자동 판별하고 적합한 이론+톤을 선택한다. "C8" 또는 "Cre8orClub" 언급 시 힙한 크리에이터 모드 활성화.

## 사용 사례

| 상황 | 프롬프트 | 동작 |
|---|---|---|
| 앱 온보딩 카피 | `"C8 온보딩 카피 써줘"` | A1 유형 판별, Hip 톤 + Hook Model 이론 로드, 크리에이터 네이티브 카피 생산 |
| 랜딩페이지 진단 | `"이 랜딩페이지 카피 진단해줘"` | C3 유형 판별, PAS/AIDA 분석, Stripe/Linear 벤치마크 대비, 개선안 산출 |
| 다채널 캠페인 | `"C8 캠페인 카피 한글+영문으로 써줘"` | 로컬라이제이션 가드 로드, 한글+영문 병렬 재창작 (번역이 아닌 재창작) |
| 이메일 시퀀스 전략 | `"이메일 시퀀스 설계해줘"` | C6 판별, 퍼널 이론 + Stone 7단계 적용, 톤 변화가 설계된 너처링 시퀀스 |

## 주요 기능

- **27개 카피 유형** — 앱 UI(A1-A10), 전략문서(B1-B5), 마케팅(C1-C10), CRM(D1-D3). 각각 고유한 목적·스타일·제약
- **12개 이론 프레임워크** — SUCCESs, STEPPS, AIDA, PAS, Cialdini, SB7, Hook Model, Positioning, Ogilvy, Stone, Schwartz 5단계, Bly 4S — 유형별 자동 매핑
- **3개 톤 레벨** — 🔵 힙한(크리에이터 네이티브), ⚪ 일반적(명확·신뢰), 🟡 새로운시도(관행 파괴) — 디자이너/개발자/영상/글쓰기 페르소나별 변형 포함
- **C8 모드** — 크리에이터 도구 전용 모드. Hip 톤 기본값, 크리에이터 페르소나 타겟팅, Linear·Arc·VSCO·29CM 벤치마크
- **copy_router.py** — 유형 판별, 이론 매핑, 톤 추천, 스포크 라우팅 Python 자동화
- **6개 가드레일** — 로컬라이제이션, 법적 제약, 버전관리, 페르소나, 경쟁사 분석, QC

## 연동 스킬

- **[hit-skill](https://github.com/jasonnamii/hit-skill)** — 상류: 인간 메커니즘 16축 + 자극 설계 6공식으로 카피 근거 제공
- **[human-skill](https://github.com/jasonnamii/human-skill)** — 상류: 행동심리 16축으로 CTA·설득 설계 근거 제공
- **[design-skill](https://github.com/jasonnamii/design-skill)** — 협업: UI·마케팅 카피의 시각 계층 정합

## 설치

```bash
git clone https://github.com/jasonnamii/copywriting-engine.git ~/.claude/skills/copywriting-engine
```

## 업데이트

```bash
cd ~/.claude/skills/copywriting-engine && git pull
```

`~/.claude/skills/`에 배치된 스킬은 Claude Code 및 Cowork 세션에서 자동으로 사용 가능합니다.

## Cowork Skills

25개 이상의 커스텀 스킬 중 하나입니다. 전체 카탈로그: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## 라이선스

MIT License — 자유롭게 사용, 수정, 공유 가능합니다.