# CHANGELOG

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
