---
name: copywriting-engine
version: 1.2.0
vault_dependency: OPTIONAL
description: |
  카피라이팅 엔진. 27유형×12이론×3톤×C8/범용. Phase 0 핑퐁(누구·어디·CTA 필수) 미수집시 차단. 힙톤=human→hit→진실필터 3게이트. 보수·일반=구조엔진. 진단·설계·생산 3모드.
  P1: 카피라이팅, copywriting, 카피, 카피엔진, UX라이팅, 마케팅카피, 앱카피, 광고카피, CTA, 랜딩카피, 이메일카피, SNS카피, 브랜드보이스, 톤앤매너, 카피진단, 힙카피, 힙한카피, 상황카피.
  P2: 카피 써줘, 만들어줘, 진단해줘, 바꿔줘, 힙하게 써줘, write copy, hip copy.
  P3: copywriting engine, UX writing, marketing copy, brand voice, copy diagnosis, hip copy framework.
  P5: 카피로.
  NOT: 순수디자인(→design-skill), 순수행동분석(→human-skill), 순수히트패턴(→hit-skill), BP(→bp-guide).
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
  # 실행 모드 (2)
  - references/output-formats.md
  - references/ux-writing-mode.md
  # UX 원리
  - references/ux-principles.md
---

# Copywriting Engine — 카피라이팅 엔진 v1.2.0

27유형 × 12이론 × 3톤 조합으로 카피를 **진단·설계·생산**. **Phase 0 상황 핑퐁 게이트** 필수. 힙톤은 3게이트(human→hit→진실필터) 강제. hit-skill·human-skill 하류 소비, design-skill 협업.

---

## ⛔ 절대 규칙

| # | 규칙 |
|---|---|
| 1 | **Phase 0 핑퐁 게이트 필수** — 5축(누구·어디·직전상태·CTA·진실) 중 필수 3축(누구·어디·CTA) 미수집 시 카피 생성 차단. AskUserQuestion으로 핑퐁. fast-path 예외는 §0.5 참조 |
| 2 | **힙톤 3게이트 강제** — 🔵 Hip 톤 진입 시 human-skill(메커니즘 진단) → hit-skill(자극설계) → 진실필터(브랜드 진실 self-check) 순서 통과 필수. 1게이트라도 스킵 = FAIL → 엉뚱 카피 차단 |
| 3 | **스포크 없이 기억으로 실행 금지** — 해당 이론/톤/벤치마크 상세가 필요하면 반드시 `@uses` 레퍼런스 로드 |
| 4 | **모드 전환 확인 필수** — C8/Cre8orClub 키워드 감지 시 C8 모드, 그 외 범용 모드. B계열은 항상 범용 |
| 5 | **전수 스캔 금지** — 1차 스크리닝으로 관련 유형·이론·톤만 식별 → 해당 스포크만 로드 |
| 6 | **QC 생략 금지** — 카피 산출 후 `guard-qc.md` 체크 필수. 미실행 = FAIL |
| 7 | **에러 프로토콜** — 스포크 로드 실패·이론 매핑 실패·게이트 실패 시 STOP + 원인 보고. 추측 실행 금지 |

---

## §0. Phase 0 — 상황 핑퐁 게이트 (NEW · 필수 선행)

**목적:** 카피 생성 전 맥락 5축을 수집해 엉뚱·일반함 원인 차단. **모든 모드(진단·설계·생산)의 최선행 단계.**

### 5축 — 필수 3 + 선택 2

| # | 축 | 질문 | 등급 | 미입력 시 |
|---|---|---|---|---|
| 1 | **누구에게** | 타겟의 구체 상황 1줄 (나이·직업 ✗, "월요일 9시 출근길 직장인" 같은 장면) | **필수** | 차단·핑퐁 |
| 2 | **어디서** | 채널·매체 (푸시 1줄·랜딩 헤드라인·이메일 제목·인스타 캡션 등) | **필수** | 차단·핑퐁 |
| 3 | **CTA** | 원하는 다음 행동 1개 (구독·클릭·공유·기억) | **필수** | 차단·핑퐁 |
| 4 | 직전 상태 | 타겟이 이 카피 보기 직전 행동 (피드 스크롤 vs 결제 고민) | 선택 | 추정 후 명시 |
| 5 | 브랜드 진실 | 경쟁사는 못 하고 우리만 할 수 있는 관찰 1개 | **힙톤 필수**·범용 선택 | 힙톤 시 차단 |

### 핑퐁 실행 — AskUserQuestion 활용

**판정 흐름:**
```
입력 받음
  ├─ 필수 3축 충족? → §0.5 fast-path 판정
  └─ 미충족 시 → AskUserQuestion으로 결손축만 묶어 1회 핑퐁
       ├─ 답변 수집 → 5축 확정 → §1 진입
       └─ 거부·스킵 시 → 추정값 명시("추정: ~로 가정함, 다를 시 알려주세요") 후 진행
```

**핑퐁 질문 템플릿 (결손축에만 적용):**
- 누구: "이 카피를 받을 사람의 구체 장면을 1줄로 알려주실래요? 예: '월요일 9시 출근길 30대 직장인'"
- 어디: "어떤 매체에 들어가요? 푸시알림·랜딩헤드라인·이메일제목·인스타·옥외광고 중 어느 쪽?"
- CTA: "받은 사람이 뭘 하길 원해요? 클릭·구독·공유·기억·결제 중 1개로 압축하면?"
- 직전: "이 카피를 보기 직전에 사용자는 뭘 하고 있었을까요? (선택)"
- 진실: "경쟁사는 못 하고 우리만 할 수 있는 관찰 1개? (힙톤 필수)"

### §0.5 fast-path 예외

| 조건 | 처리 |
|---|---|
| 입력에 5축 중 필수 3축이 텍스트로 명시됨 | 핑퐁 스킵·즉시 §1 진입 |
| "예시·샘플·테스트로 아무거나" 명시 | 핑퐁 스킵, 출력 상단에 "📌 추정값" 명시 |
| 진단 모드 (기존 카피 검토만) | 5축 핑퐁 대신 "이 카피의 의도된 5축이 뭐였나요?" 1회 질문 |
| 힙톤 요청 | fast-path 적용 ✗ — 진실축 필수, 항상 핑퐁 |

---

## §1. 모드 자동 판별 (2축)

### 축1: 실행 모드

| 입력 유형 | 모드 | 판별 기준 |
|---|---|---|
| 완성된 카피 | **진단** | 기존 카피 존재 + "진단/분석/리뷰" 요청 |
| 목표·브리프만 | **설계** | 카피 없이 "이 상황에 맞는 카피 전략?" |
| 초안 + 의도 | **생산** | "이걸 써줘/바꿔줘/만들어줘" |

복합 시: 진단→설계→생산 파이프라인. 애매 시 형에 확인.

### 축2: 제품 모드

| 키워드 | 모드 | 톤 기본값 | 적용 계열 |
|--------|------|----------|----------|
| "C8", "Cre8orClub" | **C8 모드** | 🔵 Hip | A, C, D |
| 그 외 | **범용 모드** | ⚪ Standard | A, B, C, D |

**B계열(전략·기획 문서)은 항상 범용 모드.** C8 모드에서도 B계열 카피 요청 시 자동으로 범용 톤 적용.

---

## §2. 1차 스크리닝 — 유형·이론·톤 판별

**전제:** §0 핑퐁 완료. 5축 데이터를 입력으로 활용.

### 유형 판별 — 27개 중 어디?

```bash
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
| 전파 (C1, C7, D3) | STEPPS | SUCCESs | theories-sticky.md |
| 전환 (C3, C4, C6) | PAS/AIDA | 5단계 인식 | theories-funnel.md |
| 습관 (A1, A6, A10) | Hook Model | Cialdini | theories-product.md |
| 설득 (C2, B5, D1) | Cialdini | SB7 | theories-persuasion.md |
| 포지셔닝 (C5, C10, B2) | Positioning | SB7 | theories-persuasion.md + theories-product.md |
| 명세 (B3, B4) | 4S QC | — | theories-product.md |

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
| 진실축 데이터 | **필수** | 권장 | 권장 |

**자동 재확인:** 사용자가 "힙하게"라고 해도 §0 5축 분석이 보수톤 요구하면(예: 에러·법적·결제 유형) 재확인 후 ⚪ Standard 강제.

→ 상세: `cross-tone-system.md`

---

## §2.5 힙톤 3게이트 (NEW · 🔵 Hip 진입 시 강제)

**목적:** 엉뚱·맥락 없는 기발함 차단. 진짜 힙함은 "이 브랜드만이 할 수 있는 정확한 관찰".

| 게이트 | 호출 | 통과 기준 | 실패 시 |
|---|---|---|---|
| **G1 human** | human-skill 진단 모드 | 16축 중 동기2·사회3축 메커니즘 1개 이상 확정 | 카피 생성 차단·핑퐁 |
| **G2 hit** | hit-skill 3층 통과 | 인간메커니즘(G1결과)→자극설계→전파구조 순서 적용 | G2 재실행 (자극설계 단독 ✗) |
| **G3 진실필터** | self-check 1문항 | "이 카피의 관찰이 §0.5 진실축과 일치하는가?" YES | 카피 reject·재생성 |

**3게이트 실행 순서:**
```
§0 5축 수집 (진실축 포함) →
G1 human-skill 발동 → 메커니즘 1개 도출 →
G2 hit-skill 발동 → G1 결과를 인간메커니즘 입력으로 → 자극설계 → 전파구조 →
G3 진실필터 self-check →
PASS → 카피 산출
FAIL → 게이트별 재실행 (max 2회, 초과시 STOP)
```

**엉뚱 카피 vs 힙 카피 비교:**
- ❌ 엉뚱: "월요일은 원래 망하는 날" (제품 무관·진실축 누락·G3 FAIL)
- ✅ 힙: "월요일 9시, 당신만 늦게 출근해도 되는 이유" (재택SaaS 진실 + G1 동기축 + G2 자극·전파)

---

## §3. 상세 로딩 — 스포크 라우팅

**원칙:** 필요한 스포크만 로드(병렬 가능). 31파일 전부 로드 금지.

```bash
python scripts/copy_router.py spokes A1 c8 hip
```

| 스크리닝 결과 | 로드할 스포크 |
|-------------|-------------|
| 유형 = A계열 | benchmarks-app.md + 해당 톤 파일 |
| 유형 = C계열 + 전환 목적 | benchmarks-marketing.md + theories-funnel.md |
| C8 모드 | tone-hip.md + cross-brand-voice.md |
| 범용 모드 | tone-standard.md |
| 🔵 Hip 톤 (모드 무관) | **interface-human.md + interface-hit.md (3게이트 강제)** |
| 상류 필요 | interface-hit.md / interface-human.md / interface-design.md |
| 다국어 | guard-localization.md |
| 법적 민감 | guard-legal.md |
| A/B 테스트 요청 | cross-ab-testing.md |

---

## §4. 모드별 실행

**전제:** 모든 모드는 §0 핑퐁 선행. 🔵 Hip 톤은 §2.5 3게이트 추가.

### 진단 모드
```
§0 핑퐁(의도된 5축) → ①유형 판별 → ②현재 톤 분석 → ③이론 정합성 → ④벤치마크 대비 → ⑤개선점 → ⑥QC → ⑦리포트
```

### 설계 모드
```
§0 핑퐁(5축) → ①브리프 분석 → ②유형 판별 → ③이론 선택 → ④톤 결정 → [Hip시 §2.5] → ⑤상류 호출 → ⑥전략 수립 → ⑦리포트
```

### 생산 모드
```
§0 핑퐁(5축) → ①브리프 분석 → ②유형·이론·톤 판별 → [Hip시 §2.5 3게이트] → ③스포크 로드 → ④상류 활성화 → ⑤카피 작성 → ⑥QC → ⑦길이 검증 → ⑧산출
```

### 출력 포맷

카피가 주인공. 분석 과정은 숨김. "왜?"·"상세" 요청 시만 펼침.

**생산 모드 기본형:**
```
{유형코드} {유형명} · {모드} · {톤이모지}{톤명} · {이론명}

📌 5축: 누구={...} / 어디={...} / CTA={...}{ / 진실={...} (Hip시 필수)}

한글: "{카피}"
영문: "{카피}"

근거: {1-2문장, Hip시 G1·G2·G3 결과 1줄씩}
```

진단·설계 포맷 + 금지 패턴 + 상류 활성화: `→ output-formats.md`

---

## §4.8. UX_WRITING_MODE — A·D계열 필수

**발동:** A계열(A1~A10) · D계열(D1~D3) · C계열 내 에러·안내. **스킵:** B계열·C계열 브랜딩/마케팅.

**4원리 코어:** N2(MATCH_REAL) · N5(ERR_PREV) · N9(ERR_REC 3요소) · N10(HELP).

**🚪 게이트:** 4원리 모두 PASS → §5 QC 진행. 1개+ FAIL → 해당 카피 재작성.

위반 패턴·3요소 예시: `→ ux-writing-mode.md` (+ `ux-principles.md`)

---

## §5. QC — 생략 불가

모든 모드의 마지막 단계. `guard-qc.md` 로드 후 실행.

| Tier | 내용 | 필수 |
|------|------|----|
| 1 자동 | 길이·금지어·톤키워드·법적플래그 | 항상 |
| 2 자가 | 10점 체크(4S + 맥락 + 톤 정합 + 5축 정합) | 항상 |
| 3 피어 | 외부 리뷰 가이드 | 고위험 카피 |

**🔵 Hip 추가:** G3 진실필터 재검증 — 산출 카피가 진실축과 일치하는가? (G3 self-check를 QC 단계에서 한 번 더)
**C8 모드 추가:** 힙-클리어 밸런스 + 크리에이터 이탈 체크 → `tone-persona-variants.md`.

---

## §6. 채널 분기 (생산 모드 확장)

```
코어 메시지 (1문장)
  ├→ 유형별 변형 (§2)
  ├→ 채널별 변형 (cross-channel-matrix.md) ← §0 "어디서" 축이 입력
  ├→ 길이별 변형 (cross-length-constraints.md)
  └→ A/B 변형 (cross-ab-testing.md)
```

---

## §7. 가드레일 — 상황별 자동 로드

| 상황 | 자동 로드 스포크 |
|------|----------------|
| 한글+영문 동시 | guard-localization.md |
| 광고·약관·개인정보 | guard-legal.md |
| 버전 관리 | guard-versioning.md |
| 크리에이터 페르소나 | guard-persona.md |
| 경쟁사 언급 | guard-competitive.md |
| 최종 검수 | guard-qc.md (§5 항상) |

---

## §8. 자체 점검

```bash
python scripts/self_check.py .
# 7축: SKILL.md 크기 · description 길이 · @uses 경로 · evals · scripts · CHANGELOG · version
```

수정 후 self_check.py PASS 확인 → `evals/cases.json` 회귀 대조 권장.

---

## Gotchas

| # | 실패 패턴 | 방지 |
|---|----------|------|
| 1 | **§0 핑퐁 스킵 후 즉시 카피 생성** | 필수 3축 미수집 시 차단·AskUserQuestion 호출 |
| 2 | **🔵 Hip 톤 진입했는데 3게이트 스킵** | §2.5 G1·G2·G3 순서 강제. 자극설계 단독 = 엉뚱 카피 원인 |
| 3 | **진실축 없이 힙 카피 생성** | G3 필터 FAIL → reject 후 진실축 재수집 |
| 4 | 유형 판별 없이 카피 작성 | §2 스크리닝 필수 |
| 5 | C8 모드에서 B계열도 힙하게 | B계열은 항상 범용 |
| 6 | 톤 파일 전부 로드 | 판별된 톤 1개만. 비교 시 최대 2개 |
| 7 | 이론 전부 적용 | 유형당 1차 + 보강 1개가 상한 |
| 8 | 한글 카피를 영문 번역 | guard-localization.md 필수. 번역 ≠ 재창작 |
| 9 | QC 생략 | 어떤 모드든 §5 필수 |
| 10 | 상류 스킬 무조건 호출 | `output-formats.md` 활성화 기준 준수. 단 Hip톤은 §2.5로 강제 |
| 11 | 에러/법적/결제에서 🟡 Experimental | ⚪ Standard 강제. 예외 없음 |
| 12 | A·D계열에서 UX_WRITING_MODE 스킵 | §4.8 4원리 필수 |
| 13 | 시스템 용어 노출 (N2 위반) | "400 Bad Request" → 사용자 언어로 번역 |
| 14 | self_check 미실행 후 배포 | 수정 후 항상 실행. CHANGELOG 갱신 |
| 15 | "아무튼 힙하게" 요청에 핑퐁 강제로 사용성 저하 | §0.5 fast-path는 Hip톤 미적용. 진실축 1줄만 받고 진행 |
