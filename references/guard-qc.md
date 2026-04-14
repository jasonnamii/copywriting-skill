# Guard: Copy Quality Control (QC) Checklist

**Core Principle:** Copy fails in production when it passes internal review but breaks in context. QC catches blind spots before shipping. Three tiers of review (automated, self, peer) catch different failures at different speeds.

---

## Universal QC Framework: The Foundations

### Bly's 4S (The Fundamentals)

Every piece of copy should hit these four dimensions:

| S | Definition | Question | Example |
|---|-----------|----------|---------|
| **Specific** | Concrete detail, not abstract claim | Does it name what you're actually getting? | "Save 3 hours per week" not "Save time" |
| **Simple** | One idea, clear structure, no jargon | Can a 12-year-old understand it? | "Fast designs" not "Optimized workflow acceleration" |
| **Sincere** | Honest, not hyperbolic or fake | Would you say this to a friend? | "Easier than Figma" (provable) not "Best tool ever" |
| **Significant** | Matters to the audience | Does the audience care about this benefit? | "Ships 2 days faster" (if designers care) not "Uses 2GB RAM" (they don't) |

### SUCCESs Framework (Stickiness Layer)

Reinforces Bly with what makes copy memorable:

| Dimension | Definition | Question |
|-----------|-----------|----------|
| **Simple** | Core message distilled | Can I explain it in one sentence? |
| **Unexpected** | Surprising, breaks pattern | Does it contradict what I expected? |
| **Concrete** | Real details, not abstract | Does it show, not tell? |
| **Credible** | Believable, supported | Do I trust this claim? |
| **Emotional** | Touches feeling, not just logic | Does it make me feel something? |
| **Stories** | Narrative or specific example | Can I picture what you're describing? |

---

## Tier 1 QC: Automated Checks (Run First, Catch Easy Wins)

### Automated QC Checklist

| Check | Tool/Method | Red Flag | Fix |
|-------|-------------|----------|-----|
| **Length** | Character count | >160 chars for meta description; >40 words for headline | Trim ruthlessly |
| **Prohibited Words** | Keyword filter | "Click here," "guaranteed," "absolutely," weak hedges | Replace with active language |
| **Tone Keyword Scan** | Keyword list by tone | Formal copy uses slang; casual copy uses jargon | Realign |
| **Legal Flag** | Automated pattern match | Superlatives: "best," "only," "unique," "fastest" | Add caveat: "for designers" or show data |
| **Truncation Check** | Screen-width simulation | Headline breaks awkwardly on mobile; CTA cut off | Rewrite for mobile first |
| **Readability Score** | Flesch-Kincaid or equivalent | Reading level >8 (too high for web) | Shorter sentences, simpler words |

### Automated QC Tool Template

```python
# Pseudo-code for automated checks
def qc_automated(copy_text, copy_type, tone_template):
    issues = []
    
    # Length check
    if copy_type == "headline" and len(copy_text) > 40:
        issues.append("⚠️ Headline >40 words (too long)")
    
    # Prohibited words
    prohibited = ["click here", "guaranteed", "absolutely"]
    for word in prohibited:
        if word in copy_text.lower():
            issues.append(f"🚩 Prohibited word: {word}")
    
    # Tone alignment
    if tone_template == "casual" and ("optimize" in copy_text or "leverage" in copy_text):
        issues.append("⚠️ Corporate words in casual copy")
    
    # Superlative check
    superlatives = ["best", "only", "fastest", "unique"]
    for word in superlatives:
        if word in copy_text.lower() and copy_type != "brand_positioning":
            issues.append(f"⚠️ Unsubstantiated superlative: {word}")
    
    # Readability
    fk_score = flesch_kincaid(copy_text)
    if fk_score > 8:
        issues.append(f"⚠️ Reading level too high ({fk_score}). Aim for 6-8")
    
    return issues
```

---

## Tier 2 QC: Self-Review (The Copywriter Audits Own Work)

**Run this before sending to peer review. 10-point checklist.**

### Self-Review Checklist

**Section 1: Bly's 4S Audit**

- [ ] **Specific:** Does every claim include a concrete detail? (Not "faster" → "50% faster")
- [ ] **Simple:** Can I explain this in one sentence without jargon?
- [ ] **Sincere:** Is anything exaggerated or hard to believe?
- [ ] **Significant:** Would my target audience care about this benefit?

**Section 2: Context Alignment**

- [ ] **Tone Match:** Does tone match the tone-template I was given?
- [ ] **UI Context:** If A-type copy, does it fit on the screen without truncation?
- [ ] **Flow:** Does it connect logically to the previous/next copy (if part of sequence)?
- [ ] **Persona:** Does it speak to the right persona (Designer/Dev/Video/Writer/B2B/B2C)?

**Section 3: Production Safety**

- [ ] **Legal:** Any unsubstantiated claims? Any legal review needed?
- [ ] **Localization:** If bilingual (EN/KR), is each version independent + native-sounding?
- [ ] **Formatting:** Does it respect markdown/HTML/platform limits?

**Section 4: Impact & Energy**

- [ ] **Opening:** Does the first 3 words hook? (If not, rewrite first line)
- [ ] **Close:** Does the CTA feel natural or forced?

**Section 5: Anti-Patterns**

- [ ] **Cliché check:** Does this phrase appear in competitor copy? (If yes, reframe)
- [ ] **Passive voice:** Are most verbs active? (Scan for "is," "are," "be")
- [ ] **Jargon leak:** Any internal-only words that escaped into external copy?

---

## Tier 3 QC: Peer Review (Fresh Eyes Audit)

**When:** After self-review passes. Before legal/final review.
**Who:** Another copywriter, designer, or product manager (not the author)
**Time:** 15 minutes per piece

### Peer Reviewer Checklist

**Section 1: First Impression (Read Without Context)**

- [ ] **Does it make sense in isolation?** (Cover context, read copy alone. Does it confuse?)
- [ ] **Is the benefit clear?** (In one read, what am I getting?)
- [ ] **Who's this for?** (Without persona label, who feels spoken to?)

**Section 2: Tone Assessment**

- [ ] **Does tone match intent?** (If meant to be casual, does it feel casual?)
- [ ] **Tone consistency:** If multi-line copy, is tone consistent or mixed?
- [ ] **Persona fit:** Based on language/rhythm, is this for the intended persona?

**Section 3: Credibility & Honesty**

- [ ] **Believable?** Any claims that feel exaggerated or unproven?
- [ ] **Honest framing?** Is this telling the whole story, or hiding downsides?

**Section 4: Production Reality**

- [ ] **Screen test:** (Mock up on actual screen) Does it fit? Does it read?
- [ ] **Truncation:** On mobile, where does it cut off? Does it still make sense?
- [ ] **Emoji/formatting:** Any markdown/HTML that breaks rendering?

**Section 5: Comparison**

- [ ] **Better than last version?** (If variant, compare to baseline)
- [ ] **Different from competitors?** (Based on competitive audit, does this stand out?)

**Section 6: Flag Concerns**

- [ ] **Legal red flag?** Any claims that need verification?
- [ ] **Persona mismatch?** Does this alienate the intended audience?
- [ ] **Localization issue?** (If bilingual) Does English version sound translated from Korean, vice versa?

---

## Type-Specific QC Additions

### A Type (UI/UX Copy) QC

**Additional Checks:**

| Check | Why | Question |
|-------|-----|----------|
| **Context Fit** | A copy lives in a UI; must fit context | Does this make sense where it appears on screen? |
| **Truncation** | Limited space | How many characters before it breaks? Have I tested mobile truncation? |
| **Instruction Clarity** | Users must understand action | Is the instruction unmistakable? (Not "Proceed" → "Send")? |
| **Error Message Helpfulness** | Users are frustrated when errors appear | Does this error message tell them how to fix it? |
| **Consistency** | Users learn language patterns | Do I use "Save" everywhere, or mix "Save/Store/Submit"? |

**Checklist:**

- [ ] Tested on actual screen (not just in doc)?
- [ ] Character count matches design specs?
- [ ] No truncation at 320px width (mobile)?
- [ ] If error message: does it suggest a fix?
- [ ] Verb consistency: same action has same label everywhere?

### B Type (Strategy/Messaging) QC

**Additional Checks:**

| Check | Why | Question |
|-------|-----|----------|
| **Accuracy** | Public statements are amplified; mistakes compound | Is every factual claim verified? |
| **Internal Jargon Leak** | External messaging shouldn't assume internal knowledge | Would a stranger understand this? |
| **Longevity** | Strategy copy lasts years; trends come and go | Will this embarrass us in 5 years? |
| **Board-Ready** | B-type often goes to investors/executives | Would you say this in a boardroom? |

**Checklist:**

- [ ] Every fact checked (data, claims, attributed quotes)?
- [ ] No internal acronyms (if used, defined)?
- [ ] Tone matches brand voice (will still apply in 2-3 years)?
- [ ] Would you defend this publicly, on video?

### C Type (Campaign/Social) QC

**Additional Checks:**

| Check | Why | Question |
|-------|-----|----------|
| **Conversion Focus** | Campaign copy exists to drive action | Is there a clear CTA? Does it feel natural? |
| **Competitive Differentiation** | Campaign lives in crowded feed; must stand out | Does this differ from competitor messaging? |
| **Platform Native** | Social copy must fit platform norms | Does this look/sound right on [LinkedIn/TikTok/Instagram]? |
| **Engagement Signal** | Social feeds reward engagement; engagement comes from surprise/emotion/specificity | Does this invite comment, share, click? |

**Checklist:**

- [ ] CTA is crystal clear (not buried)?
- [ ] Different from competitor posts (not copying language)?
- [ ] Platform-appropriate (tone matches social norms)?
- [ ] Doesn't end with period (social reads better without; looks less formal)?
- [ ] Has hooks (if social): emoji, question, surprise?

### D Type (Email/Nurture) QC

**Additional Checks:**

| Check | Why | Question |
|-------|-----|----------|
| **Personalization Variable Check** | Unresolved {name}, {company} breaks trust and looks cheap | Are all variables ({{first_name}}) resolved, or flagged in template? |
| **Unsubscribe Compliance** | CAN-SPAM requirement | Is unsubscribe link visible, one-click, working? |
| **Preview Text** | Email preview is first impression | Does preview text entice open? (Not just "view in browser") |
| **Mobile Rendering** | 60%+ email opens on mobile | Test on actual mobile device, not just desktop |

**Checklist:**

- [ ] All dynamic fields tested ({{name}} resolves correctly)?
- [ ] Unsubscribe link present, working, one-click?
- [ ] Preview text compelling (not default "If you cannot see this email")?
- [ ] Mobile tested: images load, text readable at small size?
- [ ] Subject line passes spam filters (no ALL CAPS, multiple exclamation marks)?

---

## Common Copy Failures: Top 10 & How to Catch Them

| Failure | Symptom | Why It Happens | How to Catch |
|---------|---------|----------------|------------|
| **1. Benefit Buried** | Headline is feature, not benefit | Copywriter loves the feature, forgets audience cares about outcome | Bly's 4S check: Is this Significant to audience? |
| **2. Passive Voice** | "Can be used to..." | Default writing voice | Search for "is," "are," "be" verbs |
| **3. Jargon Creep** | "Leverage," "synergize," "optimize" | Copying competitor language | Tone check: Does this match target persona's vocabulary? |
| **4. Tone Whiplash** | Formal sentence, then slang | Different sentences written by different people, or tone template ignored | Read aloud: Does tone stay consistent? |
| **5. Unsubstantiated Superlatives** | "Fastest," "best," "only" without proof | Enthusiasm overcomes honesty | Legal flag check: Every superlative needs data or caveat |
| **6. Weak Opening** | First 3 words are forgettable | Assuming reader patience | Hook test: Do first 3 words make you want to keep reading? |
| **7. Orphaned CTA** | Call-to-action feels disconnected | CTA tacked on without logical flow | Does the copy naturally lead to the CTA? Or do you feel whiplashed? |
| **8. Translator's Tone** | Korean copy sounds like English translated back | Writing from one language to another instead of independently creating | Bilingual check: If I cover the English version, does Korean sound native? |
| **9. Context Mismatch** | A-type copy makes sense in docs, confuses on screen | Written without seeing actual UI context | Context fit check: Tested on actual screen/flow? |
| **10. Persona Mismatch** | Copy alienates target audience | Writing for a persona you don't understand | Persona check: Does a real person in that persona feel spoken to? Or dismissed? |

---

## C8 Mode QC: Hip-But-Clear Balance & Creator Alienation

### Hip-But-Clear Balance Test

**The Risk:** Copy is so hip/meme-heavy that non-inside audience is lost. Or so clear/basic that hip audience is bored.

**Test:**

1. **Read to a insider** (someone in C8 community): "Does this hit?"
2. **Read to a outsider** (someone not in community): "Do you understand it? Or is it gatekeeping?"
3. **Read aloud:** Does it sound natural when spoken, or forced?

**Balance Decision:**

- If insider gets it, outsider confused → TOO HIP (add 1-2 words of clarity)
- If outsider gets it, insider bored → NOT HIP ENOUGH (add meme language or rhythm)
- If both get it, both engaged → BALANCED

**Example (C8):**

```
TOO HIP:
"When the algorithm hits different 🔥"
(Insider understands. Outsider: "hits different" = what?)

NOT HIP ENOUGH:
"When the algorithm works really well"
(Clear to everyone. Hip audience: "cringe, corporate")

BALANCED:
"When the algorithm finally gets it"
(Insider: "aha, relatable"; Outsider: "oh, when the algorithm understands what I'm trying to do")
```

### Creator Alienation Checklist (C8)

**Does this copy alienate creators?**

- [ ] **No "influencer" language** (creators hate being called influencers; they say "creators" or "makers")
- [ ] **No condescension** ("even you can do this"; treat creators as pros)
- [ ] **No AI hand-waving** (unless demonstrably useful; "AI-powered" = hype-fatigue)
- [ ] **Respects craft** ("finally a tool that gets what you do")
- [ ] **Authentic community signal** (not "join our community"; more "you're already part of the movement")
- [ ] **No corporate warmth** (overly friendly corporate tone reads as fake to creators)
- [ ] **Specificity over abstraction** ("Edit 2x faster" not "Optimized workflows")

---

## 3-Tier QC Workflow: Full Execution

### Complete QC Flow (24-Hour Turnaround Example)

```
Day 1 - Morning (30 min)
  ↓ Copywriter: Write draft

Day 1 - Afternoon (15 min)
  ↓ Automated QC: Run checks (length, prohibited words, tone, legal flags)
  ↓ Fix critical issues (truncation, legal flags)

Day 1 - Evening (15 min)
  ↓ Self-Review: 10-point checklist
  ↓ Fix: Tone mismatches, passive voice, weak openings
  ↓ Ready for peer review

Day 2 - Morning (15 min)
  ↓ Peer Review: Fresh eyes, context check, persona fit
  ↓ Feedback to copywriter

Day 2 - Midday (30 min)
  ↓ Copywriter: Revisions based on feedback
  ↓ Peer reviewer confirms changes

Day 2 - Afternoon (if needed)
  ↓ Legal Review: (only if B-type, campaign claims, or regulations apply)
  ↓ Final approval

Day 2 - EOD
  ↓ SHIP
```

### Sign-Off Template (Final Gate)

Before publishing, copywriter and peer reviewer both sign off:

```markdown
## FINAL QC SIGN-OFF

**Copy:** [Link to copy file]
**Type:** [A/B/C/D]
**Language:** [EN/KR/Bilingual]
**Persona:** [Designer/Dev/Video/Writer/Universal]

### Tier 1: Automated QC
- [ ] Length within limits
- [ ] No prohibited words
- [ ] Tone keyword scan clean
- [ ] Legal flags addressed
- [ ] Readability 6-8 grade level

### Tier 2: Self-Review
- [ ] Bly's 4S passed (Specific, Simple, Sincere, Significant)
- [ ] Tone matches template
- [ ] UI context verified
- [ ] No jargon leak

### Tier 3: Peer Review
- [ ] First impression clear
- [ ] Tone consistent
- [ ] Persona fit confirmed
- [ ] No production blockers

### Type-Specific QC
- [ ] A-type: Tested on actual screen
- [ ] B-type: Facts checked, no corporate warmth creep
- [ ] C-type: Different from competitors, CTA clear
- [ ] D-type: Variables resolved, unsubscribe present

### Final Checkpoint
- [ ] This copy makes me confident to ship
- [ ] I would defend this publicly

**Copywriter Sign-Off:** ___________________  Date: ________
**Peer Reviewer Sign-Off:** ___________________  Date: ________
**Legal Review:** ___________________  Date: ________  (if required)

**APPROVED FOR SHIP** ✓
```

---

## Final Checkpoint

Before shipping copy, run this final gate:

1. **Automated QC:** All technical checks pass? (length, tone, legal)
2. **Self-Review:** 10-point checklist done?
3. **Peer Review:** Fresh eyes confirmed?
4. **Type-Specific:** A/B/C/D checks done?
5. **Persona Test:** Right audience feels spoken to?
6. **Context Test:** Fits in actual screen/flow?
7. **Bilingual Test:** (If EN/KR) Both versions independent + native-sounding?
8. **Production:** Variables resolved, formatting clean?
9. **Sign-Off:** All reviewers confident?

If any fails → return to relevant QC tier, fix, then ship.
