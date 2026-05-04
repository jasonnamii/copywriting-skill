# CHANGELOG


## [1.3.0] — 2026-05-03

**카피 모음 코퍼스 전수학습 박제.** 형 요청("/Users/jason/Library/CloudStorage/Dropbox/Library/카피 모음 전수·정밀학습 → 카피엔진 업데이트") 반영.

### 추가 (Added)
- **§2.6 코퍼스 인덱스** — 광고·브랜드 카피 사전 신설. 한국 1568+영문 1000+ 슬로건 박제 인덱스. 자동 로드 트리거 5종
- `references/corpus-ko-patterns.md` — 한글 카피 25패턴 (코퍼스 1568개 자동 분석 발). A호명·B질문·C명령·D반전·E시리즈·F시간·G수치·H감각·I정의·J역설·K스토리
- `references/corpus-en-slogans.md` — 영문 슬로건 22구조 (Top 100 + 1000+). A명령·B의문·C단정·D대조·E약속·F운율·G슈퍼·H스토리
- `references/corpus-writing-rules-KIWI.md` — 한국어 글쓰기 11법칙 + 17체크 게이트. 송출 직전 자체검증
- `references/corpus-hall-of-fame.md` — 한·영 명카피 100선 벤치마크 (영문 30·한글 70)
- description P1에 키워드 추가: 브랜드슬로건·헤드라인·태그라인·코퍼스카피·KIWI11법칙·명카피
- Gotchas #16~18 신설 (KIWI 미통과·코퍼스 미참조·100선 표절 방지)

### 변경 (Changed)
- 생산 모드 흐름에 `§2.6 코퍼스 인덱스 자동 로드` 단계 명시
- QC에 KIWI 17체크 포함 명시

### 데이터 (Data)
- 코퍼스 8종 14파일 전수 읽기: 광고카피_한글(1956줄)·1600개모음(1568개)·영문Top100·영문카피.xlsx(451행)·영문브랜드슬로건(16산업)·KIWI 11법칙·BusinessWeek 슬로건
- 정량 분포: 영어혼용 19.1%·당신호명 18.1%·느낌표 11.8%·수치 10.7%·감각 5.7%
- 카테고리 분포: 가전 319 / 식품 160 / 화장 158 / 패션 157 / 자동차 148

### 박제 위치
- VAULT: `_skills research/copywriting-skill/` — 5개 노트 (00_corpus_index·01_ko_patterns·02_en_slogan_structures·03_writing_rules_KIWI·04_industry_signatures·05_hall_of_fame)
- 스킬: `references/corpus-*.md` 4개 신규

# CHANGELOG

## [1.2.0] — 2026-04-22

**상황 진단 핑퐁 게이트 + 힙톤 3게이트 도입.** 형 피드백("힙 카피가 엉뚱·불쾌함" + "보수·일반 스킬 필요성 재검토" + "상황 유도 질문 추가") 반영.

### 추가 (Added)
- **§0 Phase 0 핑퐁 게이트** — 카피 생성 전 5축(누구·어디·직전상태·CTA·진실) 수집 필수. 필수 3축 미수집 시 AskUserQuestion 차단
- **§0.5 fast-path 예외** — 5축 명시·예시·진단모드·힙톤별 분기 처리
- **§2.5 힙톤 3게이트** — human-skill(G1 메커니즘) → hit-skill(G2 자극·전파) → 진실필터(G3 self-check) 강제. 엉뚱 카피 차단 장치
- 절대 규칙 #1, #2 신설 — Phase 0 게이트 + 힙톤 3게이트 강제
- Gotcha #1, #2, #3, #15 — 핑퐁 스킵·3게이트 스킵·진실축 누락·fast-path 예외 대응
- 출력 포맷에 📌 5축 명시 섹션 추가

### 변경 (Changed)
- version: 1.1.0 → 1.2.0
- description 갱신 — Phase 0·3게이트·힙톤 조건 반영, 보수·일반은 "구조엔진" 포지셔닝 명시
- P1 키워드 추가: 힙카피·힙한카피·카피상황진단·상황카피
- P2 키워드 추가: 힙하게 써줘·힙한 카피 만들어줘·상황에 맞는 카피
- §2 톤 판별 — 진실축 데이터 필수(Hip)·권장(나머지) 추가. 자동 재확인 규칙 신설
- §3 스포크 라우팅 — Hip 톤은 C8/범용 무관 interface-human·interface-hit 강제 로드
- §4 모드별 실행 — 모든 모드에 §0 핑퐁 선행 명시, Hip 시 §2.5 3게이트 추가
- §5 QC — 10점 체크에 "5축 정합" 축 추가, Hip 시 G3 재검증

### 변경 없음 (Unchanged)
- 27유형 × 12이론 × 3톤 핵심 구조
- C8/범용 모드 판별
- 31 스포크 파일 구조
- QC 3-tier 프로토콜

### 설계 근거
- **보수·일반 카피 스킬 필요성 재검토 결과**: 톤 자체는 LLM 디폴트로 80점 가능, 그러나 27유형 구조·이론 매핑·UX_WRITING_MODE 때문에 스킬 유지 정당화. 단 포지셔닝을 "톤 조정"에서 "구조엔진"으로 이동
- **힙 카피 엉뚱함 진단**: 기존 구조가 자극설계만 단독 실행 → 맥락 없는 기발함 발생. human·hit·진실필터 3게이트로 "브랜드만이 할 수 있는 정확한 관찰"을 강제

## [1.1.0] — 2026-04-17

skill-doctor 진단(🟠 69.4/100) 후속 전방위 수술. 건강지수 상승 + 유지보수 체계 탑재.

### 추가 (Added)
- `references/output-formats.md` — §4.5 출력 포맷 상세를 스포크로 분리
- `references/ux-writing-mode.md` — §4.8 UX_WRITING_MODE 4원리 체크를 스포크로 분리
- `evals/cases.json` — 5개 회귀테스트 샘플 케이스 (진단·생산·설계 모드 × C8·범용 × A·B·C·D 계열)
- `scripts/self_check.py` — 자체 건강 진단 스크립트 (크기·description·@uses·evals·changelog·version 7축)
- `CHANGELOG.md` — 변경 이력 문서
- frontmatter `version: 1.1.0`
- frontmatter `vault_dependency: OPTIONAL`

### 변경 (Changed)
- SKILL.md 축소: 14.3KB → <10KB (§4.5·§4.8 스포크화 + §7 테이블 압축)
- `description` 502자 → 500자 이하 (validate 에러 해소)
- §4.5 출력 포맷 → 1줄 포인터 + output-formats.md 참조
- §4.8 UX_WRITING_MODE → 발동조건·게이트만 남기고 ux-writing-mode.md 참조

### 수정 (Fixed)
- ⑤ 비대-1: SKILL.md >10KB → 압축
- ⑦ 진화불능-1: version 필드 부재 → `version: 1.1.0`
- ⑦ 진화불능-3: evals/ 부재 → cases.json 5개 케이스
- ⑦ 진화불능-4: CHANGELOG 부재 → 본 파일
- ⑧ 무자각-1: self-check 부재 → self_check.py
- ④ 취약-3: vault_dependency 미선언 → OPTIONAL

### 변경 없음 (Unchanged)
- 27유형 × 12이론 × 3톤 핵심 로직
- hit-skill·human-skill·design-skill 상류 소비 방식
- C8/범용 모드 판별 규칙
- §5 3-tier QC 프로토콜

## [1.0.0] — prior

- 초기 릴리즈. 27유형 × 12이론 × 3톤 × C8/범용 모드 엔진 탑재.

## [1.2.0] — 2026-04-22

**상황 진단 핑퐁 게이트 + 힙톤 3게이트 도입.** 형 피드백("힙 카피가 엉뚱·불쾌함" + "보수·일반 스킬 필요성 재검토" + "상황 유도 질문 추가") 반영.

### 추가 (Added)
- **§0 Phase 0 핑퐁 게이트** — 카피 생성 전 5축(누구·어디·직전상태·CTA·진실) 수집 필수. 필수 3축 미수집 시 AskUserQuestion 차단
- **§0.5 fast-path 예외** — 5축 명시·예시·진단모드·힙톤별 분기 처리
- **§2.5 힙톤 3게이트** — human-skill(G1 메커니즘) → hit-skill(G2 자극·전파) → 진실필터(G3 self-check) 강제. 엉뚱 카피 차단 장치
- 절대 규칙 #1, #2 신설 — Phase 0 게이트 + 힙톤 3게이트 강제
- Gotcha #1, #2, #3, #15 — 핑퐁 스킵·3게이트 스킵·진실축 누락·fast-path 예외 대응
- 출력 포맷에 📌 5축 명시 섹션 추가

### 변경 (Changed)
- version: 1.1.0 → 1.2.0
- description 갱신 — Phase 0·3게이트·힙톤 조건 반영, 보수·일반은 "구조엔진" 포지셔닝 명시
- P1 키워드 추가: 힙카피·힙한카피·카피상황진단·상황카피
- P2 키워드 추가: 힙하게 써줘·힙한 카피 만들어줘·상황에 맞는 카피
- §2 톤 판별 — 진실축 데이터 필수(Hip)·권장(나머지) 추가. 자동 재확인 규칙 신설
- §3 스포크 라우팅 — Hip 톤은 C8/범용 무관 interface-human·interface-hit 강제 로드
- §4 모드별 실행 — 모든 모드에 §0 핑퐁 선행 명시, Hip 시 §2.5 3게이트 추가
- §5 QC — 10점 체크에 "5축 정합" 축 추가, Hip 시 G3 재검증

### 변경 없음 (Unchanged)
- 27유형 × 12이론 × 3톤 핵심 구조
- C8/범용 모드 판별
- 31 스포크 파일 구조
- QC 3-tier 프로토콜

### 설계 근거
- **보수·일반 카피 스킬 필요성 재검토 결과**: 톤 자체는 LLM 디폴트로 80점 가능, 그러나 27유형 구조·이론 매핑·UX_WRITING_MODE 때문에 스킬 유지 정당화. 단 포지셔닝을 "톤 조정"에서 "구조엔진"으로 이동
- **힙 카피 엉뚱함 진단**: 기존 구조가 자극설계만 단독 실행 → 맥락 없는 기발함 발생. human·hit·진실필터 3게이트로 "브랜드만이 할 수 있는 정확한 관찰"을 강제

## [1.1.0] — 2026-04-17

skill-doctor 진단(🟠 69.4/100) 후속 전방위 수술. 건강지수 상승 + 유지보수 체계 탑재.

### 추가 (Added)
- `references/output-formats.md` — §4.5 출력 포맷 상세를 스포크로 분리
- `references/ux-writing-mode.md` — §4.8 UX_WRITING_MODE 4원리 체크를 스포크로 분리
- `evals/cases.json` — 5개 회귀테스트 샘플 케이스 (진단·생산·설계 모드 × C8·범용 × A·B·C·D 계열)
- `scripts/self_check.py` — 자체 건강 진단 스크립트 (크기·description·@uses·evals·changelog·version 7축)
- `CHANGELOG.md` — 변경 이력 문서
- frontmatter `version: 1.1.0`
- frontmatter `vault_dependency: OPTIONAL`

### 변경 (Changed)
- SKILL.md 축소: 14.3KB → <10KB (§4.5·§4.8 스포크화 + §7 테이블 압축)
- `description` 502자 → 500자 이하 (validate 에러 해소)
- §4.5 출력 포맷 → 1줄 포인터 + output-formats.md 참조
- §4.8 UX_WRITING_MODE → 발동조건·게이트만 남기고 ux-writing-mode.md 참조

### 수정 (Fixed)
- ⑤ 비대-1: SKILL.md >10KB → 압축
- ⑦ 진화불능-1: version 필드 부재 → `version: 1.1.0`
- ⑦ 진화불능-3: evals/ 부재 → cases.json 5개 케이스
- ⑦ 진화불능-4: CHANGELOG 부재 → 본 파일
- ⑧ 무자각-1: self-check 부재 → self_check.py
- ④ 취약-3: vault_dependency 미선언 → OPTIONAL

### 변경 없음 (Unchanged)
- 27유형 × 12이론 × 3톤 핵심 로직
- hit-skill·human-skill·design-skill 상류 소비 방식
- C8/범용 모드 판별 규칙
- §5 3-tier QC 프로토콜

## [1.0.0] — prior

- 초기 릴리즈. 27유형 × 12이론 × 3톤 × C8/범용 모드 엔진 탑재.
