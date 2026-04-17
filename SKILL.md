---
name: copywriting-engine
version: 1.1.0
vault_dependency: OPTIONAL
description: |
  카피라이팅 엔진. 27유형(앱A·문서B·마케팅C·CRM D) × 12이론 × 3톤 × C8/범용. hit-skill·human-skill 하류 소비. 진단·설계·생산 3모드.
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
  # 실행 모드 (2)
  - references/output-formats.md
  - references/ux-writing-mode.md
  # UX 원리
  - references/ux-principles.md
---

# Copywriting Engine — 카피라이팅 엔진 v1.1.0

27유형 × 12이론 × 3톤 조합으로 카피를 **진단·설계·생산**. hit-skill(반응)·human-skill(행동) 하류 소비, design-skill(시각) 협업.

---

## ⛔ 절대 규칙

| # | 규칙 |
|---|---|
| 1 | **스포크 없이 기억으로 실행 금지** — 해당 이론/톤/벤치마크 상세가 필요하면 반드시 `@uses` 레퍼런스 로드 |
| 2 | **모드 전환 확인 필수** — C8/Cre8orClub 키워드 감지 시 C8 모드, 그 외 범용 모드. B계열은 항상 범용 |
| 3 | **전수 스캔 금지** — 1차 스크리닝으로 관련 유형·이론·톤만 식별 → 해당 스포크만 로드 |
| 4 | **QC 생략 금지** — 카피 산출 후 `guard-qc.md` 체크 필수. 미실행 = FAIL |
| 5 | **에러 프로토콜** — 스포크 로드 실패·이론 매핑 실패 시 STOP + 원인 보고. 추측 실행 금지 |

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

유형→이론 자동매핑 + 제품모드→톤 자동결정. 2축 연쇄 실행.

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

→ 상세: `cross-tone-system.md`

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
| 상류 필요 | interface-hit.md / interface-human.md / interface-design.md |
| 다국어 | guard-localization.md |
| 법적 민감 | guard-legal.md |
| A/B 테스트 요청 | cross-ab-testing.md |

---

## §4. 모드별 실행

### 진단 모드
```
①유형 판별 → ②현재 톤 분석 → ③이론 정합성 → ④벤치마크 대비 → ⑤개선점 → ⑥QC → ⑦리포트
```

### 설계 모드
```
①브리프 분석 → ②유형 판별 → ③이론 선택 → ④톤 결정 → ⑤상류 호출(필요시) → ⑥전략 수립 → ⑦리포트
```

### 생산 모드
```
①브리프 분석 → ②유형·이론·톤 판별 → ③스포크 로드 → ④상류 활성화 → ⑤카피 작성 → ⑥QC → ⑦길이 검증 → ⑧산출
```

### 출력 포맷

카피가 주인공. 분석 과정은 숨김. "왜?"·"상세" 요청 시만 펼침.

**생산 모드 기본형:**
```
{유형코드} {유형명} · {모드} · {톤이모지}{톤명} · {이론명}

한글: "{카피}"
영문: "{카피}"

근거: {1-2문장}
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
| 2 자가 | 10점 체크(4S + 맥락 + 톤 정합) | 항상 |
| 3 피어 | 외부 리뷰 가이드 | 고위험 카피 |

**C8 모드 추가:** 힙-클리어 밸런스 + 크리에이터 이탈 체크 → `tone-persona-variants.md`.

---

## §6. 채널 분기 (생산 모드 확장)

```
코어 메시지 (1문장)
  ├→ 유형별 변형 (§2)
  ├→ 채널별 변형 (cross-channel-matrix.md)
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
| 1 | 유형 판별 없이 카피 작성 | §2 스크리닝 필수 |
| 2 | C8 모드에서 B계열도 힙하게 | B계열은 항상 범용 |
| 3 | 톤 파일 전부 로드 | 판별된 톤 1개만. 비교 시 최대 2개 |
| 4 | 이론 전부 적용 | 유형당 1차 + 보강 1개가 상한 |
| 5 | 한글 카피를 영문 번역 | guard-localization.md 필수. 번역 ≠ 재창작 |
| 6 | QC 생략 | 어떤 모드든 §5 필수 |
| 7 | 상류 스킬 무조건 호출 | `output-formats.md` 활성화 기준 준수 |
| 8 | 에러/법적/결제에서 🟡 Experimental | ⚪ Standard 강제. 예외 없음 |
| 9 | A·D계열에서 UX_WRITING_MODE 스킵 | §4.8 4원리 필수 |
| 10 | 시스템 용어 노출 (N2 위반) | "400 Bad Request" → 사용자 언어로 번역 |
| 11 | self_check 미실행 후 배포 | 수정 후 항상 실행. CHANGELOG 갱신 |
