# Cross-A/B-Testing: Producing Testable Copy Variants

## Variable Taxonomy: What to Test

Choose 1-3 variables per test. Testing everything = signal loss.

### Variable Categories

| Variable | Definition | Impact | Difficulty |
|----------|-----------|--------|-----------|
| **Tone (Dimension)** | Shift on Funny/Casual/Irreverent/Enthusiastic axis | High (40-80% lift) | Medium |
| **Frame** | What angle you lead with (problem vs benefit vs proof) | High (30-70% lift) | Medium |
| **Length** | Character count or word count | Medium (10-25% lift) | Easy |
| **CTA Verb** | Action word (Try, Get, Join, Ship, Start, Learn) | Medium (15-35% lift) | Easy |
| **Social Proof Type** | Which proof (user count, testimonial, data, award) | Medium (15-40% lift) | Medium |
| **Person & Number** | Singular/Plural, first/second/third person (you vs we vs they) | Low-Medium (10-20% lift) | Easy |
| **Specificity** | Generic ("faster") vs specific ("3x faster in 4 weeks") | High (25-60% lift) | Easy |
| **Urgency Signal** | Time pressure (now, this week, limited spots) | High (20-50% lift) | Easy |
| **Emotion** | Which emotion (fear, pride, curiosity, relief) | High (30-60% lift) | Medium |
| **Visual Hook** | Format signaling (emoji, image, video, text-only) | Medium (15-30% lift) | Easy |

---

## Top 3 Recommended Test Variables by Type

### APP TYPES (A1-A10)

| Type | Test 1 | Test 2 | Test 3 |
|------|--------|--------|--------|
| **A1: Feature Launch** | Emotion (excitement vs cool) | Specificity (benefit described vs result shown) | CTA Verb (Try vs Get vs Ship) |
| **A2: Onboarding** | Length (5 steps vs 3 steps) | Person (You can vs We'll help vs It just) | Tone: Enthusiasm (high vs low) |
| **A3: Retention** | Social Proof Type (usage stats vs user testimonial) | Frame (time-saved vs capability-gained) | Urgency (Now vs This week) |
| **A4: Upgrade Prompt** | CTA Verb (Upgrade vs Unlock vs Go Pro) | Specificity (more features vs what you unlock) | Tone: Casual (high vs formal) |
| **A5: Error Message** | Tone: Funny (joke-included vs straight) | Specificity (what went wrong vs how to fix) | Emotion (sympathy vs blame) |
| **A6: Empty State** | Emotion (come on in vs need help vs watch this) | Length (1-liner vs narrative) | CTA Verb (Start vs Explore vs Create) |
| **A7: Push Notification** | Length (20 chars vs 30 chars vs 45 chars) | Urgency Signal (Now vs Today vs This week) | Specificity (what's new vs why it matters) |
| **A8: In-App Message** | Social Proof Type (usage count vs expert quote) | Tone: Casual (high vs formal) | CTA Verb (Try vs Explore vs Get started) |
| **A9: Help/FAQ** | Frame (problem-first vs solution-first) | Length (brief vs detailed) | Person (you should vs we recommend) |
| **A10: Confirmation** | Tone: Enthusiasm (celebrate vs factual) | Length (1 word vs mini-narrative) | Emotion (pride vs relief) |

### STRATEGY TYPES (B1-B5) — Universal Only

| Type | Test 1 | Test 2 | Test 3 |
|------|--------|--------|--------|
| **B1: Positioning** | Frame (vs competitors vs vs status quo) | Specificity (we are X vs we make X possible) | Emotion (aspiration vs belonging) |
| **B2: Value Prop** | Length (1-liner vs 3-point) | Frame (what you gain vs what you avoid) | Specificity (faster vs 3x faster) |
| **B3: Narrative** | Emotion (founder journey vs customer journey) | Frame (origin story vs problem-solved narrative) | Length (short vs long-form) |
| **B4: Objection Handle** | Specificity (general objection vs named objection) | Frame (addressing doubt vs showing proof) | Person (if you're worried vs some worry) |
| **B5: Social Proof** | Proof Type (quantitative vs qualitative vs social) | Specificity (10k users vs trusted by [named companies]) | Person (customers say vs experts say) |

### MARKETING TYPES (C1-C10)

| Type | Test 1 | Test 2 | Test 3 |
|------|--------|--------|--------|
| **C1: Email Subject** | Specificity (Faster vs 3x faster in 30 days) | Curiosity Gap (statement vs question vs number) | Emotion (excitement vs urgency vs curiosity) |
| **C2: Email Body** | Frame (problem-centric vs benefit-centric) | Length (short vs long-form) | Social Proof Type (customer testimonial vs data) |
| **C3: Landing Page Hero** | Tone: Irreverence (conventional vs rule-breaking) | Specificity (better vs 3x better in 2 weeks) | Emotion (aspiration vs relief) |
| **C4: Search Ads** | Specificity (fast vs 3x faster results) | CTA Verb (Learn vs Get vs Try) | Objection Handle (add guarantee vs social proof) |
| **C5: Display Ads** | Visual Hook (image + minimal text vs text-heavy) | Emotion (curiosity vs urgency vs aspiration) | Tone: Funny (playful vs straight) |
| **C6: Social Post** | Length (100 chars vs 200 chars) | Emotion (pride vs entertainment vs FOMO) | Frame (behind-the-scenes vs finished work) |
| **C7: Headline** | Specificity (benefit-generic vs benefit-specific) | Curiosity Gap (statement vs question) | Tone: Irreverence (conventional vs bold) |
| **C8: Creator Hook** | Emotion (aspiration vs entertainment vs education) | Length (short-snappy vs narrative) | Tone: Irreverence (default vs maximum) |
| **C9: ASO (App Store)** | Specificity (what-it-does vs what-you-gain) | Social Proof Type (user count vs rating vs awards) | Tone: Enthusiasm (high vs moderate) |
| **C10: PR Headline** | Specificity (announcement vs news-angle vs story) | Frame (company-centric vs industry-impact) | Newsworthiness (first, unusual, timely element) |

### CRM TYPES (D1-D3)

| Type | Test 1 | Test 2 | Test 3 |
|------|--------|--------|--------|
| **D1: Welcome Series** | Emotion (welcome feeling vs capability unlock) | Frame (here's what you get vs here's who we are) | Length (email 1 short vs narrative) |
| **D2: Re-engagement** | Urgency Signal (come back vs limited offer vs new feature) | Social Proof Type (what others are doing vs new capability) | CTA Verb (Come back vs Try vs Explore) |
| **D3: Win-Back** | Emotion (we miss you vs here's what changed vs special offer) | Specificity (improvements since you left vs 3 named features) | Length (short vs detailed) |

---

## Variant Generation Rules: Create Meaningful Differences

### Minimum Viable Difference (MVD)

Each variant must differ enough to learn from it. Rule of thumb:

- **Tone:** Change ±15 points on 1 dimension (e.g., Funny 40→55, or Casual 60→45)
- **Length:** Change ≥15% (e.g., 100 chars → 120 chars or 85 chars)
- **CTA:** Swap completely different verbs (try vs get vs unlock, not try vs try here)
- **Frame:** Shift which problem/benefit leads the sentence (problem-first vs benefit-first)
- **Emotion:** Pick 2 distinct emotions (curiosity vs urgency, not curiosity vs playfulness)

### MVD Violations (DON'T TEST THESE)

| Bad Test | Why | Better |
|----------|-----|--------|
| "Try now" vs "Try today" | Too similar; 1 word swap | "Try now" vs "Get started" |
| "Faster" vs "More speed" | Synonym swap; not different | "Faster" vs "3x faster in 4 weeks" |
| "We're excited" vs "We're thrilled" | Emotion-synonym, not distinct | "We're excited" vs "Join 10k creators" |
| Casual tone (75) vs Casual tone (78) | Difference too small | Casual tone (75) vs Casual tone (55) |

---

## Control vs Treatment Naming Convention

**NAMING RULE:** Control = baseline (or current), Treatment = variant being tested

### Standard Format
```
Experiment: [Type]_[Variable]_[Week_MonthYear]

Example: C1_Specificity_Week2_Apr2026
  Meaning: Email Subject line test, testing Specificity variable, Week 2 of April 2026

Control:  C1_Specificity_W2_Apr_CONTROL
  "Get started free"

Treatment A:  C1_Specificity_W2_Apr_TRT_Specific
  "Get started free — 10k creators, 3x faster setup"

Treatment B:  C1_Specificity_W2_Apr_TRT_Emotional
  "Your fastest setup ever starts here"
```

### A/A vs A/B vs A/B/C Structure

**A/A Test (Validation):** Same copy in both variants
- Purpose: Verify test infrastructure works (no sample bias)
- Duration: 1-2 days only
- Goal: Statistical tie (p > 0.05)

**A/B Test (Primary):** Control vs 1 Treatment
- Duration: 5-7 days minimum (7-14 typical)
- Sample size: Depends on type (see below)
- Stopping rule: Hit significance OR time limit

**A/B/C Test (Advanced):** Control vs 2+ Treatments
- Use when: Testing 2 competing variables simultaneously
- Sample size: Must increase 30-50% per variant
- Duration: Longer (10-14 days)
- Risk: Longer = more time to significance, but more variants confound learning

---

## Statistical Significance Guidance

### Minimum Sample Sizes by Type (To Detect 20% Lift)

| Type | Audience Type | Min Control Sample | Min Variant Sample | Typical Duration |
|------|---|---|---|---|
| **A1 Feature Launch** | In-app triggered | 500-1000 | 500-1000 | 3-5 days |
| **A7 Push** | All users | 2000+ | 2000+ | 2-3 days (high volume) |
| **C1 Email Subject** | Email list | 1000-5000 | 1000-5000 | 5-7 days |
| **C3 Landing Page Hero** | Paid traffic | 200-500 | 200-500 | 3-5 days |
| **C4 Search Ads** | Paid search | 500+ | 500+ | 5-7 days |
| **C6 Social Post** | Organic social | 3000+ | 3000+ | 7-14 days |
| **D2 Re-engagement** | Low-activity users | 200-500 | 200-500 | 7-14 days |

### Power Analysis Quick Reference

**If you want to detect a 20% improvement with 95% confidence:**

- Small audience (push, in-app): 500 samples per variant
- Medium audience (email, paid traffic): 1,000-2,000 samples
- Large audience (organic social): 3,000+ samples

**If you want to detect only a 50% improvement (much easier):**
- Divide sample sizes above by 4

### Confidence Level by Sample Size (Rule of Thumb)

| Sample Per Variant | Lift Detectable (95% confidence) | Typical Duration |
|---|---|---|
| 100 | 50%+ | 1-2 days |
| 500 | 20-30% | 3-5 days |
| 1,000 | 15-20% | 5-7 days |
| 2,000 | 10-15% | 7-10 days |
| 5,000 | 5-10% | 10-14 days |

---

## Test Prioritization Framework

### Effort vs Impact Matrix

High Impact + Low Effort = **RUN FIRST** (blue cells)

```
                    LOW EFFORT        MEDIUM EFFORT      HIGH EFFORT
HIGH IMPACT     [🟦 RUN NOW]      [Go next]          [Queue after]
MEDIUM IMPACT   [Quick wins]       [Medium priority]  [Low priority]
LOW IMPACT      [Don't bother]     [Don't bother]     [Don't bother]
```

### Specific Prioritization by Type & Variable

#### Highest Priority (Run in Weeks 1-2)
- **C1 Email Subject:** Specificity variable (email subject is bottleneck for opens)
- **C3 Landing Page Hero:** Specificity variable (hero test is fastest to run)
- **C4 Search Ads:** Specificity variable (often 30%+ lift potential)
- **A7 Push:** Length variable (easy, high volume, fast learning)
- **C6 Social:** Length variable (simple edit, good sample size)

#### Medium Priority (Weeks 3-4)
- **C2 Email Body:** Frame variable (harder to test, but high impact)
- **B2 Value Prop:** Specificity variable (supporting layer for hero)
- **D2 Re-engagement:** Urgency signal (medium effort, high impact)
- **A3 Retention:** Social proof type (tied to audience size)

#### Lower Priority (After Quick Wins)
- **B1 Positioning:** Tone variable (slow to affect business metrics)
- **A9 Help/FAQ:** Frame variable (low volume traffic)
- **C10 PR Headline:** Newsworthiness variable (external factor, slow results)

---

## C8 Mode: Experimental Tone as Permanent A/B Test Slot

In C8 mode, one variant is always a "hyper-irreverent" or "hyper-casual" version:

### Standard A/B Structure (Any Type)

**Control:** Type default tone (from cross-tone-system.md)

**Treatment (Tonal Experiment):** 
- Irreverent: +20 points
- Casual: +15 points
- Funny: +15 points
- Enthusiastic: -10 (let irreverence shine)

### Example: C6 Social Post (C8 Mode)

**Control (Type Default):**
"We cut onboarding from 45 to 5 minutes. Here's why that matters for creators."
- Funny: 55, Casual: 80, Irreverent: 60, Enthusiastic: 80

**Treatment (Experimental C8):**
"we deleted 12 things nobody asked for. setup went from 45 min to 5. that's the whole tweet."
- Funny: 70 (+15), Casual: 95 (+15), Irreverent: 75 (+15), Enthusiastic: 70 (-10)

### Purpose
- Not trying to prove irreverence wins (maybe it doesn't)
- Testing: Does hyper-irreverence ever win for this type?
- Learning: When does tone intensity backfire?
- Culture: Keeps C8 experimental DNA alive in testing

### Rotation
Run experimental tone test once per quarter per type. Cycle through:
- Month 1: +Irreverent
- Month 2: +Casual
- Month 3: +Funny
- Month 4: +Enthusiastic

Capture learnings in a "Tone Lift Report" quarterly.

---

## Test Setup Template

```
TEST NAME: [Type]_[Variable]_[Date]

HYPOTHESIS:
  "If we change [variable] to [direction], 
   then [metric] will increase by [expected %]
   because [mechanism]"

Example:
  "If we increase specificity (from generic 'faster' to '3x faster'),
   then email CTR will increase by 25%
   because concrete benefits drive urgency more than abstract claims"

CONTROL COPY:
  [Full control variant]

TREATMENT A COPY:
  [Full treatment variant]
  [CHANGE: What specifically changed]

TREATMENT B COPY (if A/B/C):
  [Full treatment variant]
  [CHANGE: What specifically changed]

SAMPLE SIZE:
  Control: [N] | Treatment: [N] | Duration: [days]

PRIMARY METRIC:
  [CTR / CPA / Conversion Rate / Engagement]

SUCCESS CRITERIA:
  Control vs Treatment A: [X% lift, p < 0.05]
  (Or: Treatment A wins, but doesn't reach sig., still +8% → worth keeping)

DECISION RULE (Before Launch):
  - If Treatment A wins 95%+ confidence: → ship it
  - If Treatment A wins 80-95% confidence: → keep, monitor further
  - If tie or Control wins: → rollback control

SECONDARY METRICS (Exploratory):
  [Retention / Share / Response rate / etc.]

LEARNINGS (Post-Test):
  [What we learned about [variable] for this type]

NEXT TEST:
  [What to test next based on learnings]
```

---

## Test Rotation Schedule (By Type)

### High-Priority Types (Test Monthly)
- C1 Email Subject
- C3 Landing Page Hero
- C4 Search Ads
- A7 Push

### Medium-Priority Types (Test Quarterly)
- C2 Email Body
- C6 Social Post
- B2 Value Prop
- D2 Re-engagement

### Low-Priority Types (Test Annually or On-Demand)
- B1 Positioning
- A9 Help/FAQ
- C10 PR Headline

---

## Failed Test + Quick Pivot Rules

If test shows no significant difference:

**DON'T:** Assume variable doesn't matter
**DO:** Check:
1. Sample size sufficient? (or was test underpowered?)
2. Variable difference obvious enough? (or was MVD too small?)
3. Audience composition changed? (or was test confounded?)
4. Other variables changed simultaneously? (or was test "polluted"?)

**Quick Pivot:** If all above are clear, try:
- Larger effect size (20% change instead of 15%)
- Different variable entirely
- Different copy type that uses same mechanism

---

## A/B Testing Metrics Cheat Sheet by Type

| Type | Primary Metric | Secondary | Tertiary |
|------|---|---|---|
| **A1/A7/A8** | CTR (click rate) | Conversion, Retention | Time-to-action |
| **C1 Subject** | Open Rate | CTR, Unsubscribe | Spam complaint rate |
| **C3 Hero** | Landing Page CTR | Scroll depth, Time-on-page | Conversion rate |
| **C4/C5 Ads** | ROAS (revenue/spend) or CPA | CTR, Conversion rate | Quality score |
| **C6 Social** | Engagement rate (likes+shares+comments) | Reach, Impressions | Share rate |
| **Push/In-app** | CTR | Uninstall rate, Retention | Revenue impact |
| **Email (body)** | Conversion rate | CTR, CPA | Engagement rate |

