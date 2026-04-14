# Cross-Channel Matrix: Same Campaign, Multiple Channels

## Core Message → Channel Adaptation Formula

```
CORE MESSAGE (invariant) 
    ↓
    + Channel Constraints (char limit, format, audience context)
    + Channel Psychology (why users read this channel)
    = ADAPTED MESSAGE (channel-specific copy)

Example:
CORE: "We built onboarding in 3 minutes, not 30"
PUSH: "Onboarding: 3 min, not 30 ⏱️" (32 chars)
EMAIL SUBJECT: "Your onboarding just dropped to 3 minutes" (42 chars)
SOCIAL: "spent 6 months cutting 27 min of setup time. now you're up in 180 sec. here's how. [video]" (casual, narrative)
LANDING HERO: "Onboarding in 3 minutes. Not a typo." (formal hero)
```

---

## Channel Specs: Limits, Constraints, Psychology

### 1. APP PUSH NOTIFICATION
**Platform:** iOS + Android (treat separately if different limits)

| Spec | Value |
|------|-------|
| **Char Limit** | 120 total (iOS 11+ changes this mid-message) |
| **Word Limit** | ~20 words |
| **Format** | Title (≤50 chars) + Body (≤70 chars) OR unified |
| **Visual Support** | Icon + badge (no image in base push) |
| **Audience Context** | Interruption (on-lock screen); high friction |
| **Psychology** | FOMO or time-sensitive action (opens app) |
| **Tone Adjustment** | +15 Casual, +10 Enthusiastic (urgency needed) |

**Platform Overrides:**
- iOS: May truncate at 110 chars
- Android: Can handle 240 total, but best practice 120
- Web push: 90-140 chars (web browser norm)

### 2. IN-APP MESSAGE
**Platform:** Overlay, modal, banner, or toast (varies by product)

| Spec | Value |
|------|-------|
| **Char Limit** | 200-400 depending on layout |
| **Word Limit** | 30-60 words typical |
| **Format** | Headline + Subhead + CTA button (usually) |
| **Visual Support** | Illustration, gif, or video (high support) |
| **Audience Context** | Non-intrusive, user is mid-workflow |
| **Psychology** | Timely nudge during relevant moment |
| **Tone Adjustment** | At type default (no urgency needed) |

### 3. EMAIL SUBJECT LINE (C1)
**Platform:** Email client (Gmail, Outlook, Apple Mail, etc.)

| Spec | Value |
|------|-------|
| **Char Limit** | 50 chars (optimal), 65 (max before truncate on mobile) |
| **Word Limit** | 8-10 words |
| **Format** | Plain text only (no formatting) |
| **Visual Support** | Emoji (1-2, test first), subject line only |
| **Audience Context** | Inbox is crowded; competing for attention |
| **Psychology** | Curiosity gap, personalization, urgency trigger open |
| **Tone Adjustment** | +10 Funny (humor = higher open rate) |

### 4. EMAIL BODY (C2)
**Platform:** Email client (varies in HTML support)

| Spec | Value |
|------|-------|
| **Char Limit** | 5,000-10,000 chars practical limit |
| **Word Limit** | 150-300 words optimal (longer = lower completion) |
| **Format** | HTML (test text-only fallback) |
| **Visual Support** | Images, buttons, colors (high support) |
| **Audience Context** | Full attention if opened; desktop + mobile |
| **Psychology** | Trust building, deeper story, commitment |
| **Tone Adjustment** | -5 Casual (slight formality vs push) |

### 5. SOCIAL MEDIA (Instagram, TikTok, Twitter, LinkedIn)
**Platforms:** Treat separately

#### Instagram Post/Reel
| Spec | Value |
|------|-------|
| **Char Limit** | Caption: 2,200 chars (but cut at 125 chars in preview) |
| **Word Limit** | Caption: First 20 words = engagement drivers |
| **Format** | Image/video-first (text secondary) |
| **Visual Support** | Critical (image/video is the message) |
| **Audience Context** | Scroll + skim; visual = 80% of decision |
| **Psychology** | Aesthetic appeal, peer culture, aspiration |
| **Tone Adjustment** | +20 Casual, +15 Funny (culture-first platform) |

#### TikTok
| Spec | Value |
|------|-------|
| **Char Limit** | Caption: 2,200 chars (rarely used; video is message) |
| **Word Limit** | Captions unnecessary; voiceover is primary |
| **Format** | Video-only (15 sec - 10 min) |
| **Visual Support** | Video + sound + text overlay (if needed) |
| **Audience Context** | Feed scroll; attention = first 1 sec |
| **Psychology** | Trends, entertainment, FOMO (native ads look like content) |
| **Tone Adjustment** | +25 Casual, +25 Funny, +15 Irreverent (edgy culture) |

#### Twitter/X
| Spec | Value |
|------|-------|
| **Char Limit** | 280 chars (formerly 140) |
| **Word Limit** | 35-50 words |
| **Format** | Text-first; images/video optional |
| **Visual Support** | Medium (thumbnail visible in feed) |
| **Audience Context** | News cycle fast; replies are conversation |
| **Psychology** | Takes sides, fast opinions, immediacy |
| **Tone Adjustment** | +10 Irreverent, +5 Funny (punchy opinions) |

#### LinkedIn Post
| Spec | Value |
|------|-------|
| **Char Limit** | 3,000 chars (optimal: 1,300-1,500) |
| **Word Limit** | 150-200 words (longer = fewer engagements) |
| **Format** | Text-heavy; document/article format accepted |
| **Visual Support** | Low (text = 70% value; image = supporting) |
| **Audience Context** | Professional; desktop majority; serious reading |
| **Psychology** | Thought leadership, credibility, B2B trust |
| **Tone Adjustment** | -10 Casual, -5 Funny (professionalism) |

### 6. LANDING PAGE HERO (C3)
**Platform:** Web (desktop + mobile optimized)

| Spec | Value |
|------|-------|
| **Char Limit** | Headline: 60-80 chars (visible above fold) |
| **Word Limit** | Headline: 8-12 words; Subhead: 15-20 words |
| **Format** | Headline + Subheading + Visual + CTA |
| **Visual Support** | Critical (hero image/video = 50% of decision) |
| **Audience Context** | Intent is high (came from ad/email); measuring fit |
| **Psychology** | Fast credibility check (3 sec to decide stay/leave) |
| **Tone Adjustment** | At type default or +5 Enthusiastic (hero moment) |

### 7. SEARCH ADS (Google/Bing Ads) (C4)
**Platform:** Google Search, Bing, DuckDuckGo

| Spec | Value |
|------|-------|
| **Char Limit** | Headline 1 (30 chars) + Headline 2 (30 chars) + Headline 3 (30 chars) + Description 1 (90 chars) + Description 2 (90 chars) |
| **Word Limit** | ~50 words total (3 headlines + 2 descriptions) |
| **Format** | 3 headlines + 2 descriptions + URL + display URL |
| **Visual Support** | Favicon only (no images in standard search ads) |
| **Audience Context** | High intent (searching for solution); fast scan |
| **Psychology** | Match keyword intent; signal relevance; clear benefit |
| **Tone Adjustment** | -10 Funny, -5 Casual (professional, benefit-focused) |

### 8. DISPLAY ADS (Programmatic, Retargeting) (C5)
**Platforms:** Google Display Network, Facebook, Programmatic

| Spec | Value |
|------|-------|
| **Char Limit** | Headline: 25-30 chars; Description: 90 chars |
| **Word Limit** | ~20 words total |
| **Format** | 300x250 (square), 728x90 (leaderboard), 160x600 (sidebar), etc. |
| **Visual Support** | Critical (image takes 80%+ of space) |
| **Audience Context** | Low intent (not searching); interruption-based |
| **Psychology** | Visual + fast message; curiosity gap or FOMO |
| **Tone Adjustment** | +20 Funny, +15 Casual (entertainment value matters) |

### 9. APP STORE OPTIMIZATION (C9)
**Platforms:** Apple App Store, Google Play Store

| Spec | Value |
|------|-------|
| **Char Limit** | Title: 30 chars; Subtitle: 30 chars; Description: 170 chars |
| **Word Limit** | 60-70 words total (all fields combined) |
| **Format** | Title + Subtitle + Keywords + Description + Screenshots |
| **Visual Support** | Critical (screenshots + icon = 90% of download decision) |
| **Audience Context** | Consideration stage (browsing before download) |
| **Psychology** | Category/ranking relevance; UI preview; social proof |
| **Tone Adjustment** | +10 Enthusiastic, at Casual (app discovery is emotional) |

### 10. PR/PRESS RELEASE HEADLINE (C10)
**Platform:** Press release distribution, media outlets

| Spec | Value |
|------|-------|
| **Char Limit** | 60-70 chars (journalistic standard) |
| **Word Limit** | 10-12 words |
| **Format** | Headline only (lede is first sentence of body) |
| **Visual Support** | None (text-only) |
| **Audience Context** | Journalists (not consumers); credibility check |
| **Psychology** | News value, authority, clarity of announcement |
| **Tone Adjustment** | -15 Funny, -10 Casual, -10 Irreverent (journalistic) |

---

## Message Consistency Rules: What Stays, What Flexes

### INVARIANT (Never Change)
1. **Core benefit** (the one key takeaway)
2. **Specific number/proof** (if claimed, same in all channels)
3. **Brand voice personality** (tone archetype stays)
4. **CTA destination** (all point to same conversion moment)

### FLEXIBLE (Change Per Channel)
1. **Sentence structure** (push uses fragments; email uses full sentences)
2. **Adjectives/descriptors** (push: "fast"; email: "saves you 3 hours/week")
3. **Social proof type** (push: "Trending"; email: "10k users"; social: "Your friends")
4. **Urgency signal** (push: "Now"; email: "This week"; social: implicit)
5. **Formality level** (search ads: formal; TikTok: slang)

### Example: 1 Campaign, 5 Channels

**CORE MESSAGE:** "5-minute setup instead of 45 minutes"

| Channel | Adapted Copy | Invariant | Flexible |
|---------|---|---|---|
| **Push** | "Setup in 5 min ✨ Try →" | 5-min benefit | Fragment format, emoji, urgency |
| **Email Subject** | "Your setup just got 40 minutes faster" | 40 min saved (same math) | Emotional reframe, open curiosity |
| **Instagram Caption** | "we cut setup from 45 to 5. here's how [link]" | 5-min number | Casual voice, narrative form |
| **Search Ad** | "Setup in 5 minutes. No credit card. Sign up free →" | 5-min benefit | Benefit + objection handle, formal |
| **Landing Hero** | "Setup in 5 minutes. Not a typo." | 5-min number | Question format = pattern interrupt |

---

## Campaign Brief Template: Multi-Channel Planning

```
CAMPAIGN: ________________________
CORE MESSAGE: "____________________________________"
PROOF/NUMBER: ____________________
TARGET AUDIENCE: __________________
MODE: [ ] C8 [ ] Universal

CHANNEL BREAKDOWN:

1. PUSH NOTIFICATION
   Headline: "________________________" (50 chars max)
   Body: "________________________" (70 chars max)
   CTA: [ Button text ]

2. EMAIL SUBJECT
   Subject: "________________________" (50 chars)
   Tone: ___/___/___/___ (Funny/Casual/Irreverent/Enthusiastic)

3. EMAIL BODY
   Openr: ________________________
   Body: ________________________ (200-300 words target)
   CTA: [ Button text ]

4. SOCIAL POST
   Platform: [ ] Instagram [ ] Twitter [ ] TikTok [ ] LinkedIn
   Copy: ________________________ (platform char limit)
   Visual: ________________________

5. SEARCH AD
   Headline 1: "________________________" (30 chars)
   Headline 2: "________________________" (30 chars)
   Description: "________________________" (90 chars)

6. DISPLAY AD
   Format: 300x250 [ ] 728x90 [ ] 160x600 [ ]
   Headline: "________________________" (25 chars)
   Description: "________________________" (90 chars)

CONSISTENCY CHECK:
  [ ] All channels mention core number/benefit
  [ ] Brand voice recognizable in all channels
  [ ] CTA destination aligned (all same conversion moment)
  [ ] Tone grid ±10 across channels
```

---

## Channel Character Limit Cheat Sheet

| Channel | Headline | Body/Description | Total |
|---------|----------|------------------|-------|
| Push | 50 | 70 | 120 |
| Email Subject | 50 | - | 50 |
| Email Body | N/A | 5,000+ | 5,000+ |
| Instagram | 125 | 2,200 | 2,200 |
| TikTok | - | 2,200 (rarely used) | Video |
| Twitter | - | 280 | 280 |
| LinkedIn | - | 1,300-1,500 | 1,300-1,500 |
| Landing Hero | 80 | 150 | 230 |
| Search Ad | 30×3 | 90×2 | 360 |
| Display Ad | 25 | 90 | 115 |
| App Store | 30 + 30 | 170 | 230 |
| PR Headline | - | 70 | 70 |

---

## Cross-Channel Message Decay Check

Before launch, audit all 6-10 channels:

**Question 1: Core Message Clarity**
- Can someone read all channels and extract same benefit? (Yes = ✓)

**Question 2: Tone Consistency**
- Do all channels sound like same brand? (Yes = ✓)

**Question 3: Proof Consistency**
- If using a number, is it same across all channels? (Yes = ✓)

**Question 4: CTA Alignment**
- Do all channels point to same conversion moment? (Yes = ✓)

**Question 5: Platform Appropriateness**
- Does each channel adaptation respect platform norms? (Yes = ✓)

If any question = "No", pull that channel and fix before launch.

