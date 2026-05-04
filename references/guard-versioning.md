# Guard: Copy Version Management

**Core Principle:** Copy is not static. A/B tests, seasonal updates, tone shifts, regulatory changes, and performance degradation all require systematic version tracking. Without versioning, you cannot rollback, learn, or audit.

---

## Why Copy Needs Versioning

### The 5 Scenarios That Break Unversioned Copy

1. **A/B Testing**
   - You ship variant A. Performance dips 20%. Did variant B work better?
   - Without version history: Can't compare. Can't rollback. You're flying blind.

2. **Seasonal Updates**
   - Copy for Q1 launch differs from Q3 back-to-school positioning
   - Without versioning: Overwrite old copy, then panic when Q1 returns and you don't have the original

3. **Regulatory Changes**
   - Apple updates App Store review guidelines → Your copy gets flagged
   - Legal changes (GDPR, FTC) → Copy needs rewrite
   - Without history: You lose what passed review before. No audit trail.

4. **Tone Evolution**
   - Brand tone shifts from corporate → hip (C8)
   - Old messaging still referenced in partnerships, case studies
   - Without versioning: Current website and old collateral contradict each other

5. **Performance Degradation**
   - Copy worked great for 6 months, then conversions drop 15%
   - Did algorithm change? Did audience shift? Did copy get stale?
   - Without history: Can't isolate what changed. Can't run comparative A/B.

---

## Version Naming Convention

**Format:** `{TYPE}-v{MAJOR.MINOR}-{VARIANT}-{LANGUAGE}`

### Examples

```
A1-v1.0-baseline-EN
A1-v1.1-hipA-EN          (baseline + tested hip variant)
A1-v2.0-onboarding-EN    (major rewrite for new flow)

B2-v3.0-H1-2026-EN       (brand strategy, Q1 2026)

C4-v1.2-socialA-KR       (social campaign variant A, Korean)
C4-v1.2-socialB-KR       (social campaign variant B, Korean)

D1-v2.1-welcome-EN       (onboarding email, minor update)
D1-v2.1-welcome-KR       (same update, Korean version)
```

### Naming Rules

| Component | Rules | Why |
|-----------|-------|-----|
| **TYPE** | A/B/C/D (required) | Groups copy by type for filtering |
| **MAJOR** | Increment on complete rewrite | Change if >50% new copy |
| **MINOR** | Increment on tweaks, regulatory fixes | Change if <50% new copy, same structure |
| **VARIANT** | Describe the test/update briefly (optional) | Label helps prioritize in library |
| **LANGUAGE** | EN/KR (required) | Version per language independently |

---

## Copy Changelog Protocol

### What to Record EVERY TIME Copy Changes

**Metadata (auto-captured):**
- Author (who wrote it?)
- Date (YYYY-MM-DD)
- Version (A1-v1.2)

**Change Summary (human):**
```
[TYPE]: {Change reason}
[VARIANT]: {Variant name if A/B test}
[IMPACT]: {What changed & why}
[DATA]: {Performance data if available}
[STATUS]: {Draft/Review/Approved/Live/Archived}
```

### Changelog Template (in CHANGELOG.md)

```markdown
## A1-v1.0 → A1-v1.1
**Date:** 2026-01-15
**Author:** Jason
**Reason:** A/B test hip tone variant
**Impact:** 
  - Replaced formal "You can now..." with casual "Just..."
  - 87 words → 73 words
  - 40% reduction in jargon
**Performance:** 
  - Click-through: 2.3% → 2.8% (21% improvement)
  - Status: Approved for rollout

## A1-v1.1 → A1-v2.0
**Date:** 2026-02-28
**Author:** Design team
**Reason:** Onboarding flow redesigned; copy no longer fits
**Impact:**
  - Removed 3-step copy, replaced with 1-step
  - Tone shifted from instructional → inspirational
  - Full rewrite (v1.1 was ~60% reused, v2.0 is 10% reused)
**Performance:**
  - Onboarding drop-off: 32% → 18% (44% improvement)
  - Status: Live
```

---

## Seasonal Copy Calendar

### Frequency by Type

| Type | Frequency | Trigger | Example |
|------|-----------|---------|---------|
| **A (UI)** | Quarterly review | Flow changes, platform updates, regulatory | "New GDPR copy needed" |
| **A (Emergency)** | As-needed | App Store rejection, legal flagged | "Remove health claims" |
| **B (Strategy)** | Per-project | New product, rebrand, mission shift | "2026 brand platform launch" |
| **B (Refresh)** | Annual | Light tone update, new market entry | "Expand to Japanese market" |
| **C (Campaign)** | Weekly to monthly | Campaign calendar, trend response | "Q2 back-to-school push" |
| **C (Seasonal)** | Quarterly | Holiday, seasonal (spring launch, summer promo, holiday) | "Black Friday campaign" |
| **D (Nurture)** | Monthly review | Performance audit, list segmentation changes | "Segment by product usage tier" |
| **D (Regulatory)** | As-needed | Privacy law updates, platform policy change | "New Apple privacy policy" |

### Seasonal Copy Calendar (Annual)

```
Q1 (Jan-Mar):
  - New Year positioning (aspirational tone)
  - Spring launch campaigns (C type refresh)
  - Post-holiday email reset (D type)
  - Annual strategy refresh (B type)

Q2 (Apr-Jun):
  - Back-to-school positioning (early prep)
  - Summer energy (lighter tone)
  - Mid-year review + A/B test learnings (A type)
  - Creator-focused campaigns (C8 mode push)

Q3 (Jul-Sep):
  - Back-to-school main push (highest C activity)
  - Back-to-work positioning
  - Labor Day promos
  - Q3 financial campaign (B2B focus)

Q4 (Oct-Dec):
  - Black Friday/Cyber Monday (highest C volume)
  - Holiday positioning (warm, community tone)
  - Year-end review (gratitude angle)
  - Jan prep begins (A type updates for new year flow)
```

---

## Copy Deprecation Rules

### When to Retire Old Copy

**Immediately Retire (Archive):**
- Version succeeded in A/B test but lost to another variant (v1.2 was beaten by v1.3)
- Legal flagged or platform rejected
- Regulatory change made it non-compliant
- Tone contradicts current brand platform

**Conditional Archive:**
- Performance plateaued for >6 months (still usable, but not optimal)
- Superseded by major version (v1.x → v2.0)
- Audience shifted (kept for reference, not use)

**Never Delete:**
- Versions that passed regulatory review (audit trail needed)
- Versions that won significant A/B tests (benchmark comparison)
- B-type strategy copy (reference value for future projects)

### Deprecation Status in Changelog

```
[STATUS]: Live          ← Currently in use
[STATUS]: Archived     ← Retired, kept for audit/reference
[STATUS]: Superseded   ← Lost A/B test, newer variant in use
[STATUS]: Rejected     ← Legal/platform flagged, don't use
[STATUS]: Draft        ← Under review, not live
```

---

## Copy Library Structure

### Recommended Directory Structure

```
copywriting-skill/
├── library/
│   ├── A-types/
│   │   ├── A1-headline/
│   │   │   ├── A1-v1.0-baseline-EN.md
│   │   │   ├── A1-v1.1-hipA-EN.md
│   │   │   ├── A1-v2.0-onboarding-EN.md
│   │   │   └── A1-CHANGELOG.md
│   │   ├── A2-cta/
│   │   └── A3-error/
│   ├── B-types/
│   │   ├── B1-brand-platform/
│   │   │   ├── B1-v1.0-2025-mission-EN.md
│   │   │   ├── B1-v2.0-2026-mission-EN.md
│   │   │   └── B1-CHANGELOG.md
│   │   └── B2-product-positioning/
│   ├── C-types/
│   │   ├── C1-landing-page/
│   │   │   ├── C1-v1.0-baseline-EN.md
│   │   │   ├── C1-v1.0-baseline-KR.md
│   │   │   ├── C1-v1.1-testA-EN.md
│   │   │   ├── C1-v1.1-testB-EN.md
│   │   │   └── C1-CHANGELOG.md
│   │   └── C4-social/
│   ├── D-types/
│   │   ├── D1-welcome-email/
│   │   │   ├── D1-v1.0-baseline-EN.md
│   │   │   ├── D1-v1.1-legal-update-EN.md
│   │   │   └── D1-CHANGELOG.md
│   │   └── D3-promotional-email/
│   └── MASTER-INDEX.md
└── references/
    ├── guard-versioning.md
    ├── guard-legal.md
    └── ...
```

### MASTER-INDEX.md Purpose

Single source of truth. Maps all copy types → current live versions.

```markdown
# Copy Library Master Index

## A Types (UI/UX)
| Component | Current Version | Language | Status | Last Updated |
|-----------|-----------------|----------|--------|--------------|
| Headline | A1-v2.0-onboarding-EN | EN | Live | 2026-02-28 |
| Headline | A1-v2.0-onboarding-KR | KR | Live | 2026-03-05 |
| CTA | A2-v1.2-conversion-EN | EN | Live | 2026-03-10 |
| Error Message | A3-v1.0-baseline-EN | EN | Live | 2025-10-12 |

## B Types (Strategy)
| Component | Current Version | Language | Status | Last Updated |
|-----------|-----------------|----------|--------|--------------|
| Brand Mission | B1-v2.0-2026-mission-EN | EN | Live | 2026-01-20 |
| Product Positioning | B2-v1.1-designer-focus-EN | EN | Live | 2026-01-15 |

## C Types (Campaign)
| Component | Current Version | Language | Status | Last Updated |
|-----------|-----------------|----------|--------|--------------|
| Landing Hero | C1-v1.1-testB-EN | EN | Live | 2026-03-18 |
| Social Post | C4-v1.0-viral-hook-EN | EN | Draft | 2026-03-20 |

## D Types (Email)
| Component | Current Version | Language | Status | Last Updated |
|-----------|-----------------|----------|--------|--------------|
| Welcome Email | D1-v1.1-legal-update-EN | EN | Live | 2026-02-01 |
| Promo Email | D3-v1.0-blackfriday-EN | EN | Archived | 2025-11-15 |
```

---

## Rollback Protocol: When New Copy Underperforms

### Detection

You notice:
- **Click-through drops 15%+** from baseline
- **Conversions fall 20%+ month-over-month**
- **Email unsubscribe rate spikes** (>0.5% per send)
- **App Store reviews mention confusion** about new messaging
- **Legal flags new version** (needs immediate revert)

### Rollback Decision Tree

```
1. Is new copy live <2 weeks?
   YES → Immediate rollback to previous version
   NO → Proceed to step 2

2. Have you A/B tested new vs old?
   NO → Pause new copy, A/B test before rollback decision
   YES → Proceed to step 3

3. Is performance drop >20%?
   YES → Rollback immediately, investigate
   NO → Monitor 1 more week before deciding

4. Is legal/platform flagged?
   YES → Rollback immediately (non-negotiable)
   NO → Can keep if data trend is unclear
```

### Rollback Execution

**Step 1: Immediate Action**
```markdown
1. Revert to previous version ID (e.g., A1-v1.2-hipA-EN)
2. Update MASTER-INDEX.md → Status: Live
3. Create ROLLBACK log entry
4. Notify stakeholders (Slack: #copywriting-skill)
```

**Step 2: Root Cause Analysis (within 24hrs)**
- What changed between old → new copy?
- Did audience change? (platform algorithm, campaign targeting)
- Did context change? (page redesign, flow change, device shift)
- Was tone misaligned with audience?
- Was claim unsubstantiated? (legal risk)

**Step 3: Changelog Entry**
```
## A1-v1.2 → A1-v1.1 (ROLLBACK)
**Date:** 2026-03-25
**Author:** Jason (initiated), Design team (investigation)
**Reason:** Click-through dropped 18% in first week of v1.2
**Impact:** Reverted to v1.1 (previous best performer)
**Analysis:** 
  - v1.2 removed emotional language (more clinical)
  - Audience respond better to warmth, not precision
  - Fix: v1.3 will test hybrid (warm + clear)
**Performance:** 
  - v1.1 restored: click-through 2.8% (baseline)
  - v1.2 archived for reference (future learning)
```

**Step 4: Forward Plan**
- Ship v1.3 (combines insights from v1.1 + v1.2)
- A/B test v1.3 vs v1.1 before committing

---

## Copy Version Best Practices

### Do's
- [ ] Version every deployment (even small tweaks)
- [ ] Link version to decision/data (why this version?)
- [ ] A/B test before major rollouts (v1.x → v2.0 especially)
- [ ] Archive old versions (never delete, reference value)
- [ ] Review old versions before new projects (avoid repeating failures)
- [ ] Track performance for each version (ROI of copy revision)

### Don'ts
- [ ] Don't overwrite previous versions (always create new file)
- [ ] Don't skip changelog entries (lost audit trail)
- [ ] Don't mix A/B variants in production (confuses data)
- [ ] Don't keep untested hunches live longer than 2 weeks
- [ ] Don't ignore platform/legal rejections (legal liability)
- [ ] Don't assume old copy still works (test it)

---

## Final Checkpoint

Before shipping a new version:

1. **Naming:** Does version follow {TYPE}-v{MAJOR.MINOR}-{VARIANT}-{LANGUAGE}?
2. **Changelog:** Is entry complete? (Date, author, reason, impact, performance)
3. **Testing:** Have I A/B tested vs baseline? (if major change)
4. **Regulatory:** Did legal review? (if B or D type, or claims-heavy C type)
5. **Library:** Updated MASTER-INDEX.md?
6. **Archive:** Is old version properly deprecated (Status: Live/Archived/Rejected)?
7. **Rollback Plan:** Do I know how to revert if this underperforms?

If any fails → fix, then ship.
