---
name: copywriting-skill
version: 1.4.0
license: Proprietary. LICENSE.txt has complete terms
vault_dependency: OPTIONAL
description: |
  카피엔진 v1.4. 27유형×12이론×3톤+코퍼스(한25·영22·KIWI11·100선). 5축핑퐁→힙3게이트→PRE_WRITE→KIWI17. 진단·설계·생산. 한1568+영1000+ 박제.
  P1: 카피라이팅, copywriting, 카피, 카피엔진, UX라이팅, 광고카피, CTA, 랜딩카피, 브랜드보이스, 톤앤매너, 힙카피, 슬로건, 헤드라인, 태그라인, KIWI.
  P2: 카피 써줘, 만들어줘, 진단해줘, 바꿔줘, 힙하게, write copy.
  P3: copywriting, UX writing, brand voice, brand slogan, headline, tagline.
  P5: 카피로, 슬로건으로.
  NOT: 디자인(→design-skill), 행동(→human-skill), 히트(→hit-skill), BP(→bp-guide).
"@uses":
  # 핵심 운영 (v1.4 신규)
  - references/phase0-pingpong.md
  - references/pre-write-detail.md
  - references/cascade-rules.md
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
  # 코퍼스 박제
  - references/corpus-ko-patterns.md
  - references/corpus-en-slogans.md
  - references/corpus-writing-rules-KIWI.md
  - references/corpus-hall-of-fame.md
---

# Copywriting Engine v1.4

27유형 × 12이론 × 3톤 조합으로 카피를 **진단·설계·생산**. 5축 핑퐁 → 힙톤 3게이트 → PRE_WRITE → QC 4단 흐름.

---

## ⛔ 절대 규칙 (4개)

| # | 규칙 | 이유 |
|---|---|---|
| 1 | **5축 핑퐁 선행** — 누구·어디·CTA 미수집 시 카피 생성 차단. AskUserQuestion으로 결손축 핑퐁. fast-path 예외는 `→ phase0-pingpong.md` | 엉뚱·일반함의 80% 원인 = 맥락 미수집 |
| 2 | **힙톤 3게이트 강제** — 🔵 Hip 진입 시 human → hit → 진실필터 순서. 1게이트 스킵 = 엉뚱 카피 | 힙 ≠ 기발. 힙 = "이 브랜드만의 정확한 관찰" |
| 3 | **PRE_WRITE 사전 가드 + 사후 QC 둘 다** — 생산 모드에서 6룰을 *작성 시점에* 강제 + §5 QC. `→ pre-write-detail.md` | 사후교정만 의존 = AI 흔적·번역투 잔존 |
| 4 | **paper-engine MUST cascade + 형 CONFIRM_GATE** — 산출물은 paper-engine 경유 + 송출 직전 형 컨펌. `→ cascade-rules.md` | 단독 출력 = 자가신고 우회·품질 누수 |

> 그 외(QC 생략·전수 스캔·모드 혼동·에러 프로토콜 등) = 본문 권고 + Gotchas.

---

## §0. Phase 0 — 5축 핑퐁

**필수 3축:** 누구(구체 장면) · 어디(채널) · CTA(행동 1개). **선택 2축:** 직전상태 · 진실(Hip 필수, 경쟁사 못 하는 우리만의 관찰).

**판정:** 필수 3축 충족 → §1 / 미충족 → AskUserQuestion으로 결손축 1회 핑퐁. 상세(질문템플릿·fast-path·진단모드) → `phase0-pingpong.md`

---

## §1. 모드 자동 판별

**실행 모드:** 완성카피+"진단" → 진단 / 브리프만 → 설계 / 초안+"써줘·바꿔줘" → 생산. 복합=파이프라인.
**제품 모드:** "C8·Cre8orClub" → C8(🔵 Hip 기본) / 그 외 → 범용(⚪ Standard). B계열은 항상 범용.

---

## §2. 1차 스크리닝

```bash
python scripts/copy_router.py type "입력 텍스트"
python scripts/copy_router.py theory A1
python scripts/copy_router.py tone A1 c8
```

**유형 27개:** A 앱(A1~A10) · B 문서(B1~B5) · C 마케팅(C1~C10) · D CRM(D1~D3)

**이론 자동 매핑:** 전파(C1·C7·D3) → STEPPS / 전환(C3·C4·C6) → PAS/AIDA / 습관(A1·A6·A10) → Hook Model / 설득(C2·B5·D1) → Cialdini / 포지셔닝(C5·C10·B2) → Positioning / 명세(B3·B4) → 4S QC. → theories-{sticky·funnel·product·persuasion}

**톤 판별:** 🔵 Hip(흥분·고빈도·진실축 필수) / ⚪ Standard(중립·중빈도·진실축 권장) / 🟡 Experimental(흥분·저빈도). **강제전환:** 에러·법적·결제 → ⚪ Standard.

---

## §2.5 힙톤 3게이트 (🔵 Hip 진입 시)

**G1 human-skill 진단:** 동기2·사회3축 메커니즘 1개+ → **G2 hit-skill 3층:** G1결과→자극설계→전파구조 → **G3 진실필터:** "관찰↔진실축 일치?" YES. 1게이트 FAIL = 재실행(max 2). 비교: ❌"월요일은 원래 망하는 날"(G3 FAIL) / ✅"월요일 9시, 당신만 늦게 출근해도 되는 이유"(재택SaaS 진실+G1·G2·G3).

---

## §2.6 코퍼스 인덱스 (한국 1568+ · 영문 1000+)

**자동 로드:** 한국어 카피 → corpus-ko-patterns(25패턴) / 영문 슬로건 → corpus-en-slogans(22구조) / 한국어 송출 직전 → corpus-writing-rules-KIWI(11법칙) / 명카피 검증 → corpus-hall-of-fame(100선) / "광고카피·슬로건" 호출 → 4개 모두.

**KIWI 11법칙 = 한국어 송출 게이트:** 추상→구체 / 강조어 문장 끝 / 동사 정곡·부사 절제 / '것·도·등' 자제 / 주어 반복 ✗ / 단어 중복 ✗ / 과잉 수사 ✗ / 한 문장 1주어 / 자신없는 표현 ✗ / 조사 빼라.

상세 (정량 분포·슈퍼 패턴) → `corpus-ko-patterns.md`

---

## §2.7 PRE_WRITE — 6룰 (생산 모드 직전 강제)

| # | 룰 | 한 줄 정의 |
|---|---|---|
| 1 | 단문 | 헤로 ≤15자·CTA ≤8자·본문 ≤25자 |
| 2 | 단일약속 | 진실축 1개 = 백본 |
| 3 | 시그니처 자연주입 | "X는 Y가 아니다"·구어체 |
| 4 | 문장당 1명제 | AND·OR 묶기 ✗ |
| 5 | AI식 사전회피 | "여러분의 일상에"·"진정한 가치" 차단 |
| 6 | Intent-Quote | 일반어 재정의 시 작은따옴표 |

상세 (유형별 길이·Hip추가룰·SCOPE_OUT·자체검증) → `pre-write-detail.md`

---

## §3. 스포크 라우팅 (필요분만)

`python scripts/copy_router.py spokes {유형} {모드} {톤}`

A계열 → benchmarks-app+톤 / C전환 → benchmarks-marketing+theories-funnel / C8 → tone-hip+cross-brand-voice / 🔵 Hip → **interface-human+interface-hit (3게이트 강제)** / 다국어 → guard-localization / 법적 → guard-legal / A/B → cross-ab-testing.

**전수 로드 ✗.** 1차 스크리닝 → 해당 스포크만.

---

## §4. 모드별 실행

```
[진단] §0 핑퐁 → 유형판별 → 톤분석 → 이론정합성 → 벤치마크 → 개선점 → §5 QC → 리포트
[설계] §0 → 브리프 → 유형 → 이론 → 톤 → [Hip시 §2.5] → 상류호출 → 전략 → 리포트
[생산] §0 → 브리프 → 유형·이론·톤 → [Hip시 §2.5] → §2.6 코퍼스 → §2.7 PRE_WRITE → 스포크 → 작성 → PRE_WRITE 자체검증 → §5 QC → 산출
```

**출력 포맷 (생산):** `{유형}·{모드}·{톤}·{이론}` + `📌 5축` + `한글/영문` + `근거 1-2문장(Hip시 G1·G2·G3)`. 상세 → `output-formats.md`

---

## §4.8 UX_WRITING_MODE (A·D계열 필수)

**발동:** A1~A10 · D1~D3 · C계열 내 에러·안내. **스킵:** B계열·C 브랜딩.

**4원리 코어:** N2(MATCH_REAL) · N5(ERR_PREV) · N9(ERR_REC 3요소) · N10(HELP).

**게이트:** 4원리 모두 PASS → §5 QC. 1개+ FAIL → 재작성. → `ux-writing-mode.md`

---

## §5. QC (생략 ✗)

T1 자동(길이·금지어·톤·법적, 항상) / T2 자가(10점 체크: 4S+맥락+톤·5축 정합, 항상) / T3 피어(외부 리뷰, 고위험). **🔵 Hip:** G3 재검증. **C8:** 힙-클리어 밸런스 → `tone-persona-variants.md`. → `guard-qc.md`

---

## §6. 채널 분기 (생산 확장)

코어 메시지 1문장 → 유형별(§2) · 채널별(cross-channel-matrix·§0 "어디서") · 길이별(cross-length-constraints) · A/B(cross-ab-testing) 변형.

---

## §7. 가드레일 (자동 로드)

한·영 동시 → guard-localization / 광고·약관·개인정보 → guard-legal / 버전관리 → guard-versioning / 크리에이터 페르소나 → guard-persona / 경쟁사 언급 → guard-competitive / 최종 검수 → guard-qc(§5 항상).

---

## §8. 자체 점검

`python scripts/self_check.py .` (7축: SKILL.md·description·@uses·evals·scripts·CHANGELOG·version). 수정 후 PASS 확인 → `evals/cases.json` 회귀 대조 권장.

---

## 형 코퍼스 박제

`references/jason-corpus-examples.md`(1.05MB·PT17·IR2·BP verbatim) · `VAULT/Agent-Ops/_refs/jason_lexicon_{BAN,GOOD}.md`(AI식 28 BAN·시그니처 50+ GOOD)

---

## Gotchas

1. §0 핑퐁 스킵 후 즉시 카피 → 필수 3축 미수집 = 차단·AskUserQuestion
2. 🔵 Hip 진입했는데 3게이트 스킵 → §2.5 G1·G2·G3 순서 강제
3. 진실축 없이 힙 카피 → G3 FAIL → reject
4. 톤·이론 전부 로드 → 톤 1개·이론 1차+보강 1 상한
5. 한글 카피를 영문 번역 → guard-localization. 번역 ≠ 재창작
6. 에러·법적·결제에서 🟡 Experimental → ⚪ Standard 강제
7. A·D계열에서 UX_WRITING_MODE 스킵 → §4.8 4원리 필수
8. 한국어 송출 직전 KIWI 11법칙 미통과 → §2.6 KIWI 17체크 강제

상세 19개(시스템 용어·self_check 미실행·Intent-Quote 누락 등) → `corpus-writing-rules-KIWI.md` + 가드레일 스포크.
