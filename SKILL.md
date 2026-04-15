---
name: copywriting-engine
description: |
  카피라이팅 엔진. 27유형(앱A·문서B·마케팅C·CRM D) × 12이론 × 3톤(힙/표준/실험) × C8모드+범용모드. hit-skill·human-skill 하류 소비. 진단·설계·생산 3모드.
  P1: 카피라이팅, copywriting, 카피, 카피엔진, UX라이팅, 마케팅카피, 앱카피, 광고카피, CTA, 랜딩카피, 이메일카피, SNS카피, 브랜드보이스, 톤앤매너, 카피진단.
  P2: 카피 써줘, 카피 만들어줘, 카피 진단해줘, 카피 바꿔줘, write copy, diagnose copy, fix copy.
  P3: copywriting engine, UX writing, marketing copy, brand voice, tone of voice, copy diagnosis.
  P5: 카피로, 카피시트로, .md로.
  NOT: 순수 디자인(→design-skill), 순수 행동분석(→human-skill), 순수 히트패턴(→hit-skill), 문서 구조, BP(→bp-guide).
"@uses":
  # 벤치마크 (4)
  - references/benchmarks-app.md
  - references/benchmarks-marketing.md
  - references/benchmarks-strategy.md
  - references/benchmarks-crm.md
  # 이론 (4)
  - references/theories-sticky.md
  - references/theories-funnel.md
  - references/theories-persuasion.md
  - references/theories-product.md
  # 톤 (4)
  - references/tone-hip.md
  - references/tone-standard.md
  - references/tone-experimental.md
  - references/tone-persona-variants.md
  # 횡단축 (6)
  - references/cross-tone-system.md
  - references/cross-brand-voice.md
  - references/cross-funnel-map.md
  - references/cross-channel-matrix.md
  - references/cross-length-constraints.md
  - references/cross-ab-testing.md
  # 가드레일 (6)
  - references/guard-localization.md
  - references/guard-legal.md
  - references/guard-versioning.md
  - references/guard-persona.md
  - references/guard-competitive.md
  - references/guard-qc.md
  # 상류 인터페이스 (3)
  - references/interface-hit.md
  - references/interface-human.md
  - references/interface-design.md
---

# Copywriting Engine — 카피라이팅 엔진

27개 카피 유형 × 12개 이론 프레임워크 × 3개 톤 레벨을 조합하여 카피를 진단·설계·생산하는 실행 도구. hit-skill(반응 원리)과 human-skill(행동 메커니즘)을 하류에서 소비하고, design-skill(시각 문법)과 협업한다.

---

## ⛔ 절대 규칙

| # | 규칙 |
|---|---|
| 1 | **스포크 없이 기억으로 실행 금지** — 해당 이론/톤/벤치마크 상세가 필요하면 반드시 `@uses` 레퍼런스 로드 |
| 2 | **모드 전환 확인 필수** — C8/Cre8orClub 키워드 감지 시 C8 모드, 그 외 범용 모드. B계열은 항상 범용 |
| 3 | **전수 스캔 금지** — 1차 스크리닝으로 관련 유형·이론·톤만 식별 → 해당 스포크만 로드 |
| 4 | **QC 생략 금지** — 카피 산출 후 `references/guard-qc.md` 체크 필수. 미실행 = FAIL |

---

## §1. 모드 자동 판별 (2축)

### 축1: 실행 모드

| 입력 유형 | 모드 | 판별 기준 |
|---|---|---|
| 완성된 카피 | **진단** | 기존 카피가 존재 + "진단/분석/리뷰" 요청 |
| 목표·브리프만 | **설계** | 카피 없이 "이 상황에 맞는 카피 전략?" |
| 초안 + 의도 | **생산** | "이걸 써줘/바꿔줘/만들어줘" |

복합 시: 진단→설계→생산 순서 파이프라인. 애매 시 형에 확인.

### 축2: 제품 모드

| 키워드 | 모드 | 톤 기본값 | 적용 계열 |
|--------|------|----------|----------|
| "C8", "Cre8orClub" | **C8 모드** | 🔵 Hip | A, C, D |
| 그 외 | **범용 모드** | ⚪ Standard | A, B, C, D |

**B계열(전략·기획 문서)은 항상 범용 모드.** C8 모드에서도 B계열 카피 요청 시 자동으로 범용 톤 적용.

---

## §2. 1차 스크리닝 — 유형·이론·톤 빠른 판별

입력물을 3축으로 빠르게 스캔. **각 항목 = 1줄 판정.**

**실질 스크리닝 2축:**
- **유형 판별 → 이론 자동매핑:** 유형이 정해지면 §이론 매핑 테이블에 따라 1차·보강 이론이 자동 선정. 3축 독립 판별 아님.
- **모드(C8/범용) → 톤 결정:** 제품 모드가 정해지면 기본 톤 값이 자동 결정. 3축 독립이 아니라 **유형→이론 연쇄 + 모드→톤 연쇄로 실행.**

### 유형 판별 — 27개 중 어디?

```bash
# Python 라우터 우선 (토큰 절약)
python scripts/copy_router.py type "입력 텍스트 또는 브리프 설명"
```

| 계열 | 유형 코드 | 이름 |
|------|----------|------|
| A 앱 | A1~A10 | 온보딩·빈상태·에러·CTA·툴팁·알림·법적·화면·로딩·성공피드백 |
| B 문서 | B1~B5 | 기획안·전략문서·PRD·내부보고서·제안서 |
| C 마케팅 | C1~C10 | 캠페인·이벤트·랜딩·퍼포먼스광고·브랜딩광고·이메일·SNS·PR·SEO·ASO |
| D CRM | D1~D3 | 리텐션이메일·CS응대·리뷰유도 |

### 이론 자동 매핑

```bash
python scripts/copy_router.py theory A1  # 유형→이론 매핑
```

| 목적 유형 | 1차 이론 | 보강 이론 | 스포크 |
|----------|---------|----------|--------|
| 전파 목적 (C1, C7, D3) | STEPPS | SUCCESs | theories-sticky.md |
| 전환 목적 (C3, C4, C6) | PAS/AIDA | 5단계 인식 | theories-funnel.md |
| 습관 목적 (A1, A6, A10) | Hook Model | Cialdini | theories-product.md |
| 설득 목적 (C2, B5, D1) | Cialdini | SB7 | theories-persuasion.md |
| 포지셔닝 (C5, C10, B2) | Positioning | SB7 | theories-persuasion.md + theories-product.md |
| 명세 목적 (B3, B4) | 4S QC | — | theories-product.md |

### 톤 판별

```bash
python scripts/copy_router.py tone A1 c8  # 유형+모드→톤 추천
```

| 판별 축 | 🔵 Hip | ⚪ Standard | 🟡 Experimental |
|---------|--------|------------|----------------|
| 사용자 감정 | 흥분·기대 | 중립·탐색 | 흥분·기대 |
| 노출 빈도 | 고빈도(매일) | 중빈도 | 저빈도(첫 경험) |
| 비즈 임팩트 | 브랜드 각인 | 전환 직결 | 학습·실험 |
| 에러/법적/결제 | ⚪로 강제 전환 | 기본값 | 🔴 금지 |

→ 상세: `references/cross-tone-system.md`

---

## §3. 상세 로딩 — 스포크 라우팅

**원칙:** 필요한 스포크만 로드. 27파일 전부 로드하지 않는다.

```bash
# 스크리닝 결과로 필요 스포크 자동 매핑
python scripts/copy_router.py spokes A1 c8 hip
```

| 스크리닝 결과 | 로드할 스포크 |
|-------------|-------------|
| 유형 = A계열 | benchmarks-app.md + 해당 톤 파일 |
| 유형 = C계열 + 전환 목적 | benchmarks-marketing.md + theories-funnel.md |
| C8 모드 | tone-hip.md + cross-brand-voice.md |
| 범용 모드 | tone-standard.md |
| 상류 필요 | interface-hit.md / interface-human.md / interface-design.md |
| 다국어 | guard-localization.md |
| 법적 민감 | guard-legal.md |
| A/B 테스트 요청 | cross-ab-testing.md |

---

## §4. 모드별 실행

### 진단 모드

```
①유형 판별 → ②현재 톤 분석(4차원) → ③이론 정합성 체크 → ④벤치마크 대비 → ⑤개선점 도출 → ⑥QC 체크 → ⑦리포트
```

### 설계 모드

```
①브리프 분석(목표·타겟·맥락) → ②유형 판별 → ③이론 선택 → ④톤 결정 → ⑤상류 스킬 호출(필요시) → ⑥카피 전략 수립 → ⑦리포트
```

### 생산 모드

```
①브리프 분석 → ②유형·이론·톤 판별(§2) → ③스포크 로드(§3) → ④상류 활성화(필요시) → ⑤카피 작성 → ⑥QC(guard-qc.md) → ⑦길이 검증(cross-length-constraints.md) → ⑧최종 산출
```

---

## §4.5. 출력 포맷 — 심플 기본, 상세는 요청 시

**원칙:** 카피가 주인공. 분석 과정은 뒤로. 형이 "왜?", "상세", "근거" 요청 시에만 펼침.

### 생산 모드 출력

```
{유형코드} {유형명} · {모드} · {톤이모지}{톤명} · {이론명}

한글: "{카피}"
영문: "{카피}"

근거: {1-2문장. 핵심 메커니즘 + 왜 이 표현인지}
```

**예시:**
```
A1 온보딩 · C8 · 🔵Hip · Hook Model

한글: "만들어봐."
영문: "Build something."

근거: 빈 캔버스에서 행동 트리거 → 3글자로 인지부하 최소화(축7) + 마침표가 무게감(Hip 패턴)
```

변형(A/B, 다국어) 요청 시 같은 포맷으로 변형만 추가.

### 진단 모드 출력

```
{유형코드} {유형명} · {모드} · 현재톤: {판정}

강점: {1줄}
약점: {1줄}
처방: {1줄 — 구체적 수정 방향}
```

"상세" 요청 시 → 이론 분석, 벤치마크 대비, 4차원 톤 분석 펼침.

### 설계 모드 출력

```
{유형코드} {유형명} · {모드} · {톤} · {이론}

핵심메시지: "{1문장}"
전략: {2-3줄. 어떤 메커니즘을 왜 활용하는지}
```

"상세" 요청 시 → 채널별 변형, 퍼널 매핑, 상류 분석 펼침.

### 금지 패턴

| ✗ 금지 | ✓ 대신 |
|--------|--------|
| 유형을 왜 A1으로 판별했는지 3줄 설명 | 헤더에 `A1 온보딩` 1줄 |
| 이론 선택 과정 해설 | 헤더에 `Hook Model` 1단어 |
| 벤치마크 나열 ("Linear는 이렇고 토스는 저렇고") | 근거에 핵심 1줄만 |
| QC 체크 결과 전체 출력 | 통과 시 생략. 문제 시에만 표시 |
| "추가로 A/B 테스트도 가능합니다" 같은 제안 | 형이 요청할 때만 |

**⚠️ 상류 스킬 활성화 기준:**
- hit-skill: C계열(마케팅), 전환·전파 목적 카피 → `references/interface-hit.md` 참조 후 hit-skill 호출
- human-skill: 높은 이해관계 카피(C3 랜딩, C4 광고, D1 리텐션) → `references/interface-human.md` 참조
- design-skill: UI 카피(A계열), 비주얼 페이지(C1-C4) → `references/interface-design.md` 참조

---

## §5. QC — 생략 불가

모든 모드의 마지막 단계. `references/guard-qc.md` 로드 후 실행.

### 3-tier QC

| Tier | 내용 | 필수 여부 |
|------|------|----------|
| 1 자동 | 길이 체크, 금지어, 톤 키워드, 법적 플래그 | 항상 |
| 2 자가 | 10점 체크리스트 (4S + 맥락 + 톤 정합) | 항상 |
| 3 피어 | 외부 리뷰 가이드 (형에게 확인 포인트 제시) | 고위험 카피 시 |

### C8 모드 추가 QC

- 힙-클리어 밸런스: 힙하되 이해 가능한가?
- 크리에이터 이탈 체크: 특정 페르소나를 소외시키지 않는가?
- → `references/tone-persona-variants.md` 크로스체크

---

## §6. 채널 분기 (생산 모드 확장)

같은 캠페인의 카피를 다채널로 분기해야 할 때:

```
코어 메시지 (1문장)
  ├→ 유형별 변형 (§2 유형 판별로 분기)
  ├→ 채널별 변형 (cross-channel-matrix.md)
  ├→ 길이별 변형 (cross-length-constraints.md)
  └→ A/B 변형 (cross-ab-testing.md)
```

→ 상세: `references/cross-channel-matrix.md`

---

## §7. 가드레일 — 상황별 자동 로드

| 상황 | 자동 로드 스포크 |
|------|----------------|
| 한글+영문 동시 요청 | guard-localization.md |
| 광고·약관·개인정보 | guard-legal.md |
| 버전 관리 언급 | guard-versioning.md |
| 크리에이터 페르소나 특정 | guard-persona.md |
| 경쟁사 언급 | guard-competitive.md |
| 최종 검수 | guard-qc.md (§5에서 항상 로드) |

---

## Gotchas

| # | 실패 패턴 | 방지 |
|---|----------|------|
| 1 | 유형 판별 없이 카피 작성 | §2 스크리닝 필수. 유형이 다르면 목적·스타일·길이·이론 전부 다름 |
| 2 | C8 모드에서 B계열도 힙하게 | B계열은 항상 범용. C8 모드라도 전략문서는 ⚪ Standard |
| 3 | 톤 파일 전부 로드 | 판별된 톤 파일 1개만 로드. 비교 필요 시 최대 2개 |
| 4 | 이론 전부 적용 | 유형당 1차 이론 1개 + 보강 1개가 상한. 전부 적용 = 초점 분산 |
| 5 | 한글 카피를 영문 번역 | guard-localization.md 필수. 번역 ≠ 재창작 |
| 6 | QC 생략 | 어떤 모드든 §5 QC 필수. 미실행 = FAIL |
| 7 | 상류 스킬 무조건 호출 | 기준 충족 시에만 호출 (§4 활성화 기준 참조) |
| 8 | 에러/법적/결제 맥락에서 🟡 Experimental | 이 맥락은 ⚪ Standard 강제. 예외 없음 |
