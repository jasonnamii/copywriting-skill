# Benchmarks — Strategy/Planning Doc Copy

> Mode tags: 🌐 Universal only

## B1 Planning Document Structure

### Amazon 6-Pager Model (narrative style, no bullets)
**Opening/Context:**
- **Copy format:** "Last quarter, we launched [feature]. Users adopted it at 2x our projection. This raised a critical question: are we solving the right problem for the right customer at the right time?"
- **Language:** EN
- **Mode:** 🌐
- **Why it works:** Hooks with data surprise; positions memo as answer to a specific tension; narrative setup creates urgency and intellectual investment; "critical question" frames as strategic, not operational.

**Tenets section:**
- **Copy example:** "Customer obsession trumps internal efficiency. We optimize for their long-term value, not our short-term margin."
- **Language:** EN
- **Mode:** 🌐
- **Why it works:** Philosophically grounded (not just tactical); creates internal alignment through values; "trumps" establishes hierarchy when tradeoffs emerge; testable against decisions.

### Google DORA Report (research document intro)
- **Copy format:** "High-performing teams deploy 208 times more frequently than low performers. What's the difference? We analyzed 4,000+ organizations to answer this question."
- **Language:** EN
- **Mode:** 🌐
- **Why it works:** Shocking statistic (208x) creates attention; sample size (4,000+) builds credibility; "we analyzed" = research authority; positions report as answer key, not white paper.

## B2 Executive Summary / Project Charter

### Stripe — Internal project charter (reconstructed)
- **Copy:** "Problem: Merchants lose 2-3% of revenue to failed payment retries. Recovery is currently 40% manual, expensive, and error-prone. Solution: Introduce intelligent retry optimization that uses machine learning to time retries based on customer behavior. Expected impact: 30% reduction in failed transactions, 90% automated recovery. Timeline: Q2 ship, Q3 measure impact."
- **Language:** EN
- **Mode:** 🌐
- **Why it works:** Problem → quantified loss; current state diagnosis with 3-point detail (40% manual, expensive, error-prone); solution as logical next step; specific, measurable outcomes; calendar-anchored timeline.

### 토스 (Toss) — Product strategy memo (reconstructed)
- **Copy:** "Why loan origination needs redesign: 67% of our applicants abandon at the credit check screen. Exit interviews show confusion (3 fields vs. one question on competitors) and distrust (asks for too much upfront). Opportunity: Single-field smart intake that asks one question and infers the rest. Hypothesis: Completion rate climbs to 85%. We'll test with 10K users in Seoul first, then Korea-wide."
- **Language:** KR/EN mixed (strategy mix)
- **Mode:** 🌐
- **Why it works:** Abandonment rate (67%) = data-backed urgency; user research synthesis (three specific findings); root cause analysis (confusion/distrust); hypothesis is testable and scoped; geographic rollout = risk management.

## B3 Product Requirements Document (PRD)

### Linear — PRD style narrative (reconstructed)
- **Copy opening:** "Today, teams coordinate across Slack, emails, and Linear. Important context gets lost between channels. Engineers miss dependency updates. Managers lack visibility. Proposal: Create a 'Linked Issues' feature that shows work across silos. When Issue A blocks Issue B, you see that relationship in both issues. Real-time updates notify affected teams."
- **Language:** EN
- **Mode:** 🌐
- **Why it works:** Status quo frustration (silos, lost context); specific pain points (engineers miss updates, managers lack visibility); feature as coherence solution; benefit is relationship clarity, not just a UI element.

**Success metrics section:**
- **Copy:** "We'll measure success three ways: (1) Adoption—25% of teams linking issues by month two. (2) Friction removal—50% reduction in context-gathering comments. (3) Speed—5% faster cycle time for dependent work."
- **Language:** EN
- **Mode:** 🌐
- **Why it works:** Triangulation (adoption + friction + speed); specific targets with timelines; metrics are observable, not subjective; each metric answers "better for whom?"

## B4 Internal Proposal / Business Case

### Figma — Design system initiative proposal (reconstructed)
- **Copy:** "Today, Figma ships components slower than competitors because we don't have a shared design system. New features require 40% rework when another team already built similar components. Cost: 2 months lost per major feature. Proposal: Invest one quarter in a canonical design system. Expected benefit: 30% faster shipping, reduced rework, consistent UI. Estimated ROI: 2.5x in year one."
- **Language:** EN
- **Mode:** 🌐
- **Why it works:** Quantified inefficiency (40% rework, 2 months lost); cost is clear (opportunity cost of speed); investment framed as concentrated, time-boxed (one quarter); ROI is specific and forward-looking; wins as efficiency + differentiation.

### 당근마켓 (Carrot Market) — Marketplace trust initiative (reconstructed)
- **Copy:** "User trust is our moat, but it's fragile. Transaction disputes rose 8% last quarter. Root cause: no clear escalation path when trust breaks. We have ratings but no referee system. Proposal: Hire 20 community moderators (Q2) and build dispute resolution flow. Cost: $200K annually. Expected outcome: Dispute resolution time drops from 7 days to 1 day. Trust score improves 15%."
- **Language:** KR
- **Mode:** 🌐
- **Why it works:** Moat framing (trust = competitive advantage); quantified deterioration (8% rise); root cause diagnosis (no referee); solution is human + process; cost is explicit; outcomes are measurable and timely.

## B5 Quarterly / Periodic Review Document

### Stripe — Q3 business review (reconstructed)
- **Copy:** "Q2 targets: 15% growth, 92% retention. Actual: 17% growth (beat by 2pp), 89% retention (miss by 3pp). What drove the beat? Enterprise sales of Sigma grew 40%—stronger than projected. What caused the miss? Churn in mid-market increased, mostly from pricing sensitivity post-acquisition (larger deal sizes, higher COGS). Action items: (1) Launch mid-market retention playbook by month 2. (2) Audit pricing model for sub-$50K ARR segment."
- **Language:** EN
- **Mode:** 🌐
- **Why it works:** Transparent vs. plan comparison (beat/miss with deltas); diagnosis per outcome (why Sigma succeeded, why mid-market churned); not just reporting, but causal analysis; forward actions are specific and diagnostic.

### HubSpot — Annual strategy document excerpt (reconstructed)
- **Copy:** "2024 theme: Profitability over growth. Last year, we prioritized land-and-expand at margin cost. Result: 35% ARR growth but only 12% margin growth. This year, we shift to profitable expansion. Changes: (1) Reduce free trial length 30→14 days. (2) Bundle pricing (increase mix of multi-product customers). (3) Optimize churn in low-value cohorts. Target: Maintain 25% ARR growth while reaching 20% net margins by Q4."
- **Language:** EN
- **Mode:** 🌐
- **Why it works:** Theme articulates strategic priority shift (growth → profitability); trades off are explicit (why the change); diagnosis is data-backed (35% ARR, 12% margin = weak leverage); three levers are concrete; targets are specific and time-bound.

---

**Collection notes on strategy doc writing style:**
- Strategy docs prioritize diagnosis over prescription; show the work, not just the answer
- Quantified inefficiencies drive urgency (never "slow" or "hard"; use "2 months lost" or "40% rework")
- Root cause is always stated before solution (not "we need X" but "because Y is broken, we'll do X")
- Comparison to status quo keeps audience grounded (what's true now vs. what we propose)
- Outcomes are observable and timely (not "better retention" but "drops from 7 days to 1 day")
- Universal mode: clarity and credibility matter more than personality; let data carry tone
