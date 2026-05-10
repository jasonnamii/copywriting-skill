# Cascade Rules — paper-engine 경유·CONFIRM_GATE·NO_WORK_LABEL

## 1. paper-engine MUST cascade

이 스킬의 모든 리포트·산출물 = paper-engine 허브 MUST 경유. 단독 md/html 출력 = FAIL.

- **진입점:** 모드별 분석 완료 후, 산출물 생성 직전 paper-engine 발동
- **paper-engine 책임:** MODE_S/M/L · NYT구조 · 3패스삭제 · 4항밀도QC · design-skill cascade 강제
- **DEFAULT_RENDER = 순수 마크다운:** `.md` 산출 시 `<div>`·`<span>`·`style=` 등 인라인 HTML 전면 금지. 헤더·불릿·표·인용(`>`)·이모지만 허용
- **예외:** 사용자가 "HTML로"·"박스로"·"벤토로"·"시각화"·"카드로" 명시 시에만 html-div-style·apple-box-design cascade 경유
- **위반 감지:** md 파일에 `<div style>`·`<span style>` 삽입 = 위반 → 재작성

## 2. CONFIRM_GATE — 송출 직전 형 컨펌

**목적:** PRE_WRITE 자가신고 우회 차단. 자체검증 통과 ≠ 송출. 형 컨펌 후 송출.

**발동:** 산출물 송출 *직전* 1회.

**형식 (verbatim):**
```
🔍 송출 전 검토 부탁드려요. AI 티·번역투·장황 있나요?
[OK / 수정 / 재작성]
```

**규칙:**
- 형 OK → 최종 송출
- 형 수정 → 형 지적 부분만 PRE_WRITE 재진입 → 재출력
- 형 재작성 → 모드 처음부터 재실행

**SCOPE_OUT (컨펌 면제):**
- ≤5줄 답변·단답·확인성·실행보고
- 진단 본문 (대화 내 분석, 산출물 ✗)
- 일반대화·핑퐁·컨펌게이트 자체

**CHECK:** 산출물 송출인데 컨펌게이트 미발동 = FAIL → 송출 폐기·재출력.

## 3. NO_WORK_LABEL — 산출물·대화 본질 보호

| 항목 | 정의 |
|---|---|
| RULE | 산출물·대화 = 인간 언어. 작업 라벨 ZERO. (1만 페이지 1단어 = FAIL) |
| 판정 | "이 단어, 이 대화 밖 사람이 사전 없이 읽을 수 있나?" NO → 작업 라벨 → 금지 |
| ALLOW | 업계 전문용어(CTA·UX·KPI·SNS·USP·UVP) · 고유명사(브랜드명·캠페인명) · 법조문 |
| CONVERT | 라벨 발견 → 실명·평문 풀어쓰기. "27유형×12이론×3톤·C8/범용·Phase 0 핑퐁" → 결과만 노출 / "human→hit→진실필터 3게이트" → 본문 비노출 / "힙톤·보수·일반" → 톤 결과 평문 |
| SELF_CHECK | 최종 카피 출력 직전 자체 스캔. 1개라도 발견 = 차단·재작성. paper-engine cascade 경유 시 자동 적용 |
