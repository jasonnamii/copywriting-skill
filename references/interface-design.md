# Interface: Design-Skill Co-dependency
## How copywriting-engine works WITH design-skill

---

## COPY-DESIGN CO-DEPENDENCY MATRIX

For each of 27 copy types, design is rated by dependency level.

### TYPE A: App UI Text (Copy IS the interface)
| Type | Purpose | Design Dependency | Reason | Handoff |
|------|---------|-------------------|--------|---------|
| A1 | Onboarding flow | **HIGH** | Micro-copy positions buttons, explains affordances | Copy flow + wireframe sequence |
| A2 | CTA buttons | **HIGH** | Button text IS the action signal | 1-3 word buttons, icon position |
| A3 | Empty states | **HIGH** | Copy fills design void, prevents cognitive gap | Emotional reassurance + next action |
| A4 | Notifications | **MEDIUM** | Copy drives action from external trigger | Max 8 words, visual context |
| A5 | Error messages | **HIGH** | Copy explains + recovers from failure state | Problem + solution + retry path |
| A6 | Tooltips/Help | **MEDIUM** | Copy explains UI element (may be alt to design clarity) | Context-specific, < 15 words |
| A7 | Loading states | **LOW** | Copy entertains/reassures during wait | Tone consistency, no claims |
| A8 | Success messages | **MEDIUM** | Copy reinforces completion feeling | Celebratory tone, clear next step |
| A9 | Premium upsell | **MEDIUM** | Copy positions upgrade value in-app | Visual diff (badge/highlight) + copy |
| A10 | Onboarding premium tier | **HIGH** | Copy positions exclusivity + ease | Design must feel premium (typography, whitespace) |

**Key insight:** A types are different from other copy. They're interaction design first. Copy must fit the layout, not extend it.

---

### TYPE B: Strategy & Internal (Text-only contexts)
| Type | Purpose | Design Dependency | Reason | Handoff |
|------|---------|-------------------|--------|---------|
| B1 | Strategic narrative | **NONE** | Internal persuasion, no visual design needed | Markdown structure only |
| B2 | Internal playbooks | **LOW** | Visual breaks help scannability (optional) | Structured copy + lists |
| B3 | Meeting docs | **NONE** | Format is standard (slides or docs) | Compliance-driven structure |
| B4 | Internal reports | **NONE** | Dense information, design minimal | Data tables, text only |
| B5 | Policy/governance | **NONE** | Legal compliance, no design expression | Structured legal language |

**Key insight:** B types never need design-skill. They're persuasion through logic, not visual impact.

---

### TYPE C: Marketing & Public (Mixed dependency)
| Type | Purpose | Design Dependency | Reason | Handoff |
|------|---------|-------------------|--------|---------|
| C1 | Brand narrative | **MEDIUM** | Brand identity visual (color, typography) aligns with tone | Tone + visual guidelines |
| C2 | Homepage | **HIGH** | 4-layer design (hero, value, social proof, CTA) must align with copy hierarchy | Wireframe + copy blocks |
| C3 | Landing page | **HIGH** | Single-conversion focus: design guides eye to CTA, copy justifies | Layout-driven (copy follows structure) |
| C4 | Ad creative | **HIGH** | Headline + image + CTA must co-design for platform (Instagram/TikTok/LinkedIn) | Platform specs + copy constraints |
| C5 | Social posts | **MEDIUM** | Visual context changes copy length (image-only vs text+image) | Channel-specific format |
| C6 | Email | **MEDIUM** | Email design (template) constrains copy width, section breaks | Template structure + copy fit |
| C7 | Email nurture series | **LOW** | Sequential story, design minimal (template consistency) | Narrative flow > visual design |
| C8 | Thought leadership | **MEDIUM-HIGH** | Creator aesthetic + copy tone must align (minimal design = minimal copy) | Platform (Medium/Substack) + copy tone |
| C9 | SEO/content | **LOW** | Blog design minimal, copy is king | Heading structure (H1, H2, H3) only |
| C10 | Case study | **MEDIUM** | Visual breaks (images, quotes) structure narrative | Story arc + visual anchor points |

**Key insight:** C3-C4 are highest design-copy co-dependency. C1, C2, C8 require aesthetic alignment. C7, C9 are copy-first.

---

### TYPE D: Customer Lifecycle (Relationship depth)
| Type | Purpose | Design Dependency | Reason | Handoff |
|------|---------|-------------------|--------|---------|
| D1 | Retention email | **MEDIUM** | Design template consistency matters (brand recognition) | Branded template + copy personalization |
| D2 | Upsell offer | **MEDIUM** | Visual emphasis (color, whitespace) highlights offer value | Offer callout design + copy |
| D3 | Winback/reactivation | **LOW** | Emotional appeal dominates; design secondary | Copy-driven, minimal design |

**Key insight:** D1 needs design consistency (user recognizes the brand). D2 needs visual hierarchy to show value. D3 is pure copy (emotion + urgency).

---

## VISUAL HIERARCHY ↔ COPY HIERARCHY

### Design-Skill's 4-Layer System

Design-skill maps content → design across 4 layers:
1. **Hero/Headline** (largest, most visual)
2. **Section (Subheads/Value)**
3. **Detail (Body copy, supporting)**
4. **Metadata (Captions, footer, small type)**

### Copy Must Align to Visual Hierarchy

**Principle:** Information importance = visual size. If headline is big, copy must be short.

| Layer | Visual | Copy | Example |
|-------|--------|------|---------|
| **Hero** | Large type, high contrast | **< 10 words** | "Creators grow 3x faster" |
| **Section** | Medium type, supporting | **1-3 sentences** | "No editing skills needed. AI handles it. You focus on ideas." |
| **Detail** | Small type, gray text | **2-3 paragraphs** | Full explanation, data, proof |
| **Meta** | Tiny, very light gray | **< 20 words** | Attribution, legal, secondary info |

**Bad example (copy violates hierarchy):**
```
VISUAL: Large hero image, minimal text space
COPY: "Our proprietary artificial intelligence leverages 
      machine learning to optimize your content..."
PROBLEM: Too many words for visual space, violates cognitive hierarchy
```

**Good example (copy honors hierarchy):**
```
VISUAL: Large hero image
COPY: "AI editing. More time for ideas."
DETAIL: "Our system handles the technical work..."
RESULT: Copy size matches visual size
```

### Typography ↔ Copy Density

**Principle:** Larger type = fewer words. Design enforces copy concision.

| Typography | Word Limit | Example |
|------------|-----------|---------|
| Hero (72pt+) | 3-5 words | "Grow. Stay authentic." |
| Large (48-64pt) | 5-10 words | "Your audience grows while you sleep" |
| Medium (28-36pt) | 10-20 words | "Save 2 hours daily on editing, reclaim time for ideas" |
| Body (16-18pt) | No limit | Full paragraphs allowed |
| Small (12-14pt) | 1-2 sentences | Supporting detail, captions |

**Implementation note:** If design gives 36pt space for headline and copy is 20 words, that's a mismatch. Copywriting-engine must shorten or design must enlarge.

---

### Whitespace as Punctuation

Design-skill emphasizes minimal design (Apple approach). This affects copy:
- More whitespace = copy must be shorter (looks awkward if dense)
- Minimal design = copy must be more crafted (every word is visible)
- Visual breathing room = copy breathing room (short sentences/paragraphs)

**Example: Minimal Design Requires Minimal Copy**

Minimal design (lots of white):
```
[Large hero image - 70% of screen]

Grow faster.

[Some whitespace]

Try free. No credit card.
```

Dense design (visual elements throughout):
```
[Hero image 40%] [Copy 60%]
Grow faster with AI editing.
Your competitors are already moving. 
Here's how: [explanation]. Join 50k creators.
[Social proof row]
```

---

## CO-CREATION WORKFLOW

### Decision: Write Copy First or Design First?

**COPY FIRST (Content-driven):**
When copy is the primary value driver
- **B types** (strategy docs, playbooks): Pure copy
- **C6** (email): Narrative + proof is star
- **C9** (SEO): Search intent + explanation
- **Workflow:** Write copy brief → Iterate structure → Pass to design for template
- **Handoff:** Structured copy blocks (H1, H2, H3 levels) + approval before design

**DESIGN FIRST (Layout-driven):**
When visual layout is the constraint/opportunity
- **C1-C3** (brand, homepage, landing): Visual system is locked
- **C4** (ads): Platform specs (Instagram square, TikTok vertical, LinkedIn standard)
- **A1-A2, A5** (onboarding, CTAs, errors): Interface constraints are real
- **Workflow:** Design wireframes → Pass constraints to copy → Copywriting-engine fits copy to slots
- **Handoff:** Wireframe with text placeholders (max word counts per section) → Copy fills slots

**CO-CREATE (Simultaneous, iterative):**
When copy and design must evolve together
- **A types** (all app UI copy): Copy IS the interface
- **C2** (homepage): Design system + messaging system must align
- **C8** (thought leadership): Tone + aesthetic must match
- **Workflow:** Sketch copy angle + design direction simultaneously. Iterate in 2-week cycles.
- **Handoff:** Copy draft + design direction → Review alignment → Iterate together

---

### Workflow Templates

#### Template 1: Copy-First (B & C6)
```
STEP 1: Write copy brief
STEP 2: Draft 3 copy variants (structure + tone)
STEP 3: Get stakeholder feedback on messaging
STEP 4: Lock copy structure (H1, H2, subheads, body sections)
STEP 5: Pass to design-skill with:
         - Final copy blocks
         - Suggested visual breaks (images, testimonials)
         - Tone (playful, serious, data-driven)
STEP 6: Design applies template/visual system
STEP 7: Review: Does design honor copy hierarchy?
STEP 8: Ship
```

#### Template 2: Design-First (C1-C4)
```
STEP 1: Design-skill produces wireframes (structure, visual hierarchy)
STEP 2: Extract copy constraints from wireframe:
         - Hero: max 10 words
         - Section 1: max 30 words
         - Section 2: max 50 words
         - CTA: max 5 words
STEP 3: Pass wireframe + constraints to copywriting-engine
STEP 4: Copywriting-engine writes 3 copy variants that fit constraints
STEP 5: Review: Does copy honor design intent?
STEP 6: Iterate (design may expand if copy needs space)
STEP 7: Ship
```

#### Template 3: Co-Create (A & C2, C8)
```
STEP 1: Brief alignment (product, positioning, audience)
STEP 2: Parallel work:
         - Design: Sketch 2-3 visual directions
         - Copy: Draft 2-3 messaging angles
STEP 3: Alignment meeting:
         - Which design + copy combo works best?
         - Does tone match aesthetic?
         - Does hierarchy align?
STEP 4: Chosen direction (1 design + 1 copy direction)
STEP 5: Detailed iteration:
         - Design: Finalize typography, layout, color
         - Copy: Finalize wording, emotional resonance, proof points
         - Weekly check-ins: Visual + copy must stay in sync
STEP 6: QA:
         - Copy: Reads well, persuasive, audience-relevant
         - Design: Supports copy hierarchy, feels premium/on-brand
         - Together: Do they feel like one system, not separate parts?
STEP 7: Ship
```

---

## HANDOFF FORMAT

### What Copywriting-Engine Delivers to Design-Skill

**For Copy-First workflow:**
```markdown
# Copy Brief: [Project Name]

## Structure
- Hero: [Final copy, max 10 words]
- Section 1: [Final copy, [word count]]
- Section 2: [Final copy, [word count]]
- CTA: [Final copy, < 5 words]

## Tone
[1 sentence: playful, data-driven, aspirational, etc.]

## Visual Guidance
- Imagery: [What images enhance copy? Product, user, before/after]
- Social proof placement: [Testimonial/data point to highlight]
- Emotional anchor: [Visual that reinforces key feeling]

## Copy Hierarchy (for designer)
- H1 (Hero): 72pt → 10 words
- H2 (Section header): 48pt → 15 words
- Body: 18pt → full paragraphs OK
- CTA: 28pt → 5 words max
```

**For Design-First workflow:**
```markdown
# Copy Variants: [Landing Page]

## Constraint Review
- Hero box: max 10 words? YES (9 words: "Creators grow 3x faster")
- Body section: max 50 words? YES (47 words)
- CTA slot: max 5 words? YES (4 words: "Try free, 14 days")

## Variant 1: [Emotion-First]
[Full copy with emotion-focused hook]

## Variant 2: [Data-First]
[Full copy with metric-first hook]

## Variant 3: [Story-First]
[Full copy with narrative hook]

## Recommendation
Recommend [Variant X] because [tone/positioning reason].

## Notes
- Copy assumes [audience knowledge level]
- Design should emphasize [key section] visually
- Proof points: [list data/testimonials to call out]
```

---

## C8 MODE: CREATOR AESTHETIC + COPY INTEGRATION

### The C8 Challenge

Creator audiences (TikTok, Instagram, YouTube Community) respond to specific design + copy alignment:
- **Design aesthetic:** "Authentic," "raw," "minimal," "trend-aware"
- **Copy tone:** Conversational, specific to creator pain, actionable, not corporate

**If design and copy don't align, audience disengages immediately.**

### C8 Design Rules

From design-skill, C8 mode emphasizes:
1. **Minimal visual** (whitespace-heavy, minimal decoration)
2. **Raw materials** (unpolished photos, authentic moments vs. professional stock)
3. **Typography only** (often no images at all—just type)
4. **Trend-aware formats** (vertical video, TikTok caption length, Instagram captions)

### C8 Copy Must Match Aesthetic

| Design | Copy | Example |
|--------|------|---------|
| Minimal (lots of white) | Minimal (short, punchy) | "Too much copy looks corporate. Nope." |
| Raw photo (unpolished) | Raw quote (authentic voice) | "I was terrified to post this." |
| Typography only | Conversational tone | "okay so real talk..." (not "Let me explain...") |
| Trend format (vertical) | Platform-native language | TikTok captions, YouTube Community voice |

### C8 Co-Dependency: Hip Design = Hip Copy

**Bad: Misaligned C8**
```
DESIGN: Minimal, raw, trending aesthetic (very hip)
COPY: "Leveraging our proprietary algorithm to optimize..." (corporate)
RESULT: Feels inauthentic, loses audience immediately
```

**Good: Aligned C8**
```
DESIGN: Minimal, raw, trending aesthetic
COPY: "I tested 50 posting times. Here's what actually works." (specific, actionable, conversational)
RESULT: Feels real, audience engages
```

### C8 Implementation Checklist

- [ ] Copy tone matches design aesthetic (minimal design = minimal copy)
- [ ] No corporate language (replace "optimize" with "does better")
- [ ] Specific to creator context (mention actual struggles)
- [ ] Conversational (contractions, fragments OK)
- [ ] Actionable (1 takeaway per post/section)
- [ ] Authentic voice (could be founder/creator saying this, not marketing dept)
- [ ] Platform-native (TikTok ≠ LinkedIn, copy adapts)
- [ ] Design and copy both feel "current" (same era aesthetic)

### C8 Copy Patterns by Platform

#### TikTok
- Max 150 chars per caption
- Copy should reference video content (not standalone)
- Trend-aware language (use current slang if authentic to voice)
- CTA: "duet this," "reply," "tag someone who..."

**Example:**
```
Caption: "everyone was wrong about the algorithm... here's proof 👀"
(Comment thread: Full explanation, creator authenticity)
```

#### Instagram
- Caption can be longer (300+ chars)
- First line is crucial (before "more")
- Hashtags are searchable (not spammy, 5-10 max)
- CTA: "Slide 3 changed my life," "Save this," "Tag..."

**Example:**
```
"honestly no one talks about this part of growth... 
(swipe to see the actual framework that worked for us)"
```

#### LinkedIn
- Professional but still conversational
- Emoji usage minimal but strategic
- Data/insight first, then story
- CTA: "What's your approach?" "Drop a comment below"

**Example:**
```
"Most creators optimize for reach. Wrong metric.
Here's what successful creators optimize for instead:"
```

### C8 Design Requirement: Density Alignment

**Principle:** Design density ↔ Copy density must match.

| Design Density | Copy Density | Feel | Example |
|---|---|---|---|
| Minimal (lots of white) | Minimal (short lines) | Intentional, curated | TikTok bio |
| Light (some white) | Light (medium length) | Approachable, clear | Instagram caption |
| Medium (balanced) | Medium (full body copy) | Substantive, readable | LinkedIn post |

If design is minimal but copy is dense, it feels cluttered. If design is dense but copy is sparse, it feels empty.

---

## INTEGRATION EXAMPLES

### Example 1: C3 Landing Page

**Workflow: Design-First**

Design-skill provides wireframe:
```
[Section 1: Hero - 50% visual, 50% text]
  Left: Large hero image
  Right: Headline (48pt), subhead (24pt), CTA button

[Section 2: 3-column value props]
  Left: Icon + title + description
  Middle: Icon + title + description
  Right: Icon + title + description

[Section 3: Proof]
  Quote + attribution + logo row
  
[Section 4: CTA + urgency]
  Large CTA button (28pt), supporting urgency text
```

Design extracts copy constraints:
- Hero headline: max 10 words, 48pt
- Hero subhead: max 25 words, 24pt
- Value prop titles: max 5 words each
- Value prop descriptions: max 30 words each
- Proof quote: max 50 words
- CTA: max 5 words
- Urgency text: max 15 words

Copywriting-engine delivers:
```
Hero Headline (8 words, 48pt):
"Creators grow 3x faster. Actually."

Hero Subhead (23 words, 24pt):
"AI handles editing. You handle ideas. 
Every creator from Twitch to TikTok see 20%+ month growth."

Value Props:
- Title (4 words): "Edit in 30 seconds"
- Description (28 words): "Drop your raw footage. AI cuts, color grades, and syncs to music. You review in 3 clicks."

- Title (5 words): "Keep your unique voice"
- Description (30 words): "Not a bot doing your editing. A tool that learns your style. Your voice stays yours. Always."

- Title (4 words): "Publish more confidently"
- Description (29 words): "Spend less time on technical details, more on creative ones. Result: 40% more content shipped monthly."

Proof Quote (49 words):
"I was spending 4 hours editing each 10-minute video. Now, 30 minutes. That freed me to post 3x weekly. Revenue jumped. Switching was the best decision I made this year." — Maya, 250k followers

CTA (4 words):
"Try free. 14 days."

Urgency Text (14 words):
"No credit card. Ends Friday. 50 spots claimed of 100."
```

Design Review: ✓ Copy fits hierarchy, honors constraints, sounds like creator voice

---

### Example 2: A1 Onboarding (Co-create Workflow)

Copy and design must evolve together because copy IS the interface.

**Onboarding flow (co-designed):**

**Step 1: Sign up**
```
Design: Text input field (basic)
Copy headline (instructional): "What's your goal?" (4 words)
Copy subhead (contextualize): "Help us customize your experience." (5 words)
Copy instruction (under input): "Creator? Freelancer? Agency?" (3 words as example)
```

**Step 2: Channel connect**
```
Design: Auth buttons (Instagram, TikTok, YouTube)
Copy headline: "Connect your biggest channel." (4 words)
Copy subhead: "We'll pull your analytics to tune recommendations." (7 words)
Copy error (if auth fails): "Try again or skip." (4 words)
```

**Step 3: Success**
```
Design: Checkmark animation, whitespace-heavy
Copy headline (celebratory): "You're set!" (2 words)
Copy body (emotional): "Your audience data is loading. First recommendation in 30 seconds." (10 words)
Copy CTA (curiosity): "See what awaits →" (4 words)
```

**Co-review:**
- Design: Minimal, whitespace-heavy, icons + text
- Copy: Short, instructional, few words per screen
- Together: Lightweight, delightful, not overwhelming

---

### Example 3: C8 TikTok Creator Post (C8 Mode)

**Design: Minimal aesthetic**
```
Video: Raw footage, unpolished, quick cuts
Text overlay: Max 4 lines, large sans serif, white on dark
Music: Trending sound
Format: 9:16 vertical
```

**Copy: Minimal, conversational, actionable**
```
Video hook (first 2 sec): "everyone's doing this wrong 😅"

Text overlay (line 1): "the algorithm doesn't care"
Text overlay (line 2): "about posting time anymore"
Text overlay (line 3): "(tested 50 times, i have proof)"
Text overlay (line 4): "here's what actually works"

Caption: "the metric everyone ignores that changes everything 👇 swipe for the framework i tested 2 months"

Hashtags: #creatoreconomy #growthtips #tiktoktruth
```

**Design + Copy alignment check:**
- Design: Raw, trend-aware ✓
- Copy: Conversational, specific, actionable ✓
- Together: Feels authentic, not corporate ✓
- Platform-native: TikTok format + caption style ✓

---

## QA: Copy-Design Alignment

Before shipping, check:

### Visual Hierarchy
- [ ] Largest text contains fewest words (headline)
- [ ] Copy size decreases as content detail increases
- [ ] No dense paragraph in large type

### C8 Aesthetic (if creator-focused)
- [ ] Design and copy from same era (both minimal, both raw, or both polished)
- [ ] No corporate language in creator-facing copy
- [ ] Platform-native tone (TikTok ≠ LinkedIn)

### Constraint Fit
- [ ] Copy words fit within visual space (no overflow)
- [ ] CTA is visually emphasized (size, color, position)
- [ ] Social proof is visible and attributed

### Emotional Impact
- [ ] Design creates the emotional context
- [ ] Copy activates and transmits that emotion
- [ ] Together they reinforce the same feeling

### Functionality
- [ ] All CTAs are clickable/interactive
- [ ] Mobile experience works (text doesn't overflow)
- [ ] Whitespace supports scanning on small screens

---

## Co-Dependency Summary Table

| Aspect | High Co-Dependency | Medium | Low | Notes |
|--------|---|---|---|---|
| **Types** | A (all), C1-C4, C8 | C5-C7, D1-D2 | B, C9, D3 | A is design-first. B is copy-only. C is mixed. |
| **Workflow** | Co-create or design-first | Either order | Copy-first | Choose based on primary value driver. |
| **Handoff** | Weekly alignment meetings | Async with review | One-way (copy → design) | More meetings = higher co-dependency. |
| **Revision cycle** | Design + copy iterate together | Sequential | Copy locked early | Tight feedback loops needed for high co-dep. |
| **Risk** | Misalignment kills impact | Design/copy mismatch | Copy mismatch only | A types: misalignment = usability issue. |
| **C8 alignment** | Critical (aesthetic + tone) | Important | Not applicable | Creator audiences sense misalignment instantly. |

---

## When to Escalate to Design-Skill

Call design-skill when:

1. **Copy isn't fitting visual space** → Design needs to expand layout
2. **Hierarchy feels inverted** → Design should increase headline size, decrease body
3. **Tone feels corporate but design is minimal** → Copy and design are misaligned, need co-revision
4. **C8 mode aesthetic looks dated** → Design needs refresh to match current trends
5. **Mobile experience is broken** → Design needs responsive optimization for small screens
6. **CTA isn't visually clear** → Design should increase button contrast/size
7. **Whitespace feels wrong** → Design density doesn't match copy density

**Do NOT escalate if:** Copy is just too long. Copywriting-engine shortens it. That's our job, not design-skill's.
