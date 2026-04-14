# copywriting-engine

> 🇰🇷 [한국어 README](./README.ko.md)

**A full-stack copywriting engine that maps 27 copy types × 12 theory frameworks × 3 tone levels, with dedicated C8 mode for creator-focused products.**

## Prerequisites

- **Claude Cowork or Claude Code** environment

## Goal

Most teams write copy by gut feeling, producing inconsistent messaging across app UI, marketing pages, emails, and docs. This skill turns copywriting into a structured discipline — each of the 27 copy types gets its own purpose, theory, tone, benchmarks, and quality checks. It consumes hit-skill (why people react) and human-skill (behavioral mechanisms) to ground every line of copy in proven psychology.

## When & How to Use

Triggers on any copy-related request: "write copy", "diagnose this copy", "카피 써줘", "카피 진단해줘". Automatically detects the copy type (A1-A10 app, B1-B5 docs, C1-C10 marketing, D1-D3 CRM) and selects the right theory + tone. Say "C8" or "Cre8orClub" to activate hip creator mode.

## Use Cases

| Scenario | Prompt | What Happens |
|---|---|---|
| App onboarding copy | `"C8 온보딩 카피 써줘"` | Detects A1 type, loads hip tone + Hook Model theory, produces creator-native copy |
| Landing page diagnosis | `"이 랜딩페이지 카피 진단해줘"` | Detects C3 type, runs PAS/AIDA analysis, benchmarks against Stripe/Linear, outputs improvement plan |
| Multi-channel campaign | `"C8 캠페인 카피 한글+영문으로 써줘"` | Loads localization guard, produces parallel Korean + English copy (re-creation, not translation) |
| Email sequence strategy | `"이메일 시퀀스 설계해줘"` | Detects C6, applies funnel theory + Stone's 7-step, designs nurture sequence with tone shifts |

## Key Features

- **27 Copy Types** — App UI (A1-A10), Strategy Docs (B1-B5), Marketing (C1-C10), CRM (D1-D3), each with distinct purpose, style, and constraints
- **12 Theory Frameworks** — SUCCESs, STEPPS, AIDA, PAS, Cialdini, SB7, Hook Model, Positioning, Ogilvy, Stone, Schwartz 5-Level, Bly 4S — auto-mapped to copy types
- **3 Tone Levels** — 🔵 Hip (creator-native), ⚪ Standard (clear/trustworthy), 🟡 Experimental (rule-breaking) — with persona variants for designers, developers, video creators, writers
- **C8 Mode** — Dedicated mode for creative tools with hip-by-default tone, creator persona targeting, and benchmarks from Linear, Arc, VSCO, 29CM
- **copy_router.py** — Python router for type detection, theory mapping, tone recommendation, and spoke routing
- **6 Guard Rails** — Localization, legal compliance, versioning, persona targeting, competitive analysis, quality control

## Works With

- **[hit-skill](https://github.com/jasonnamii/hit-skill)** — Upstream: provides human mechanism axes and stimulus design formulas for copy grounding
- **[human-skill](https://github.com/jasonnamii/human-skill)** — Upstream: provides behavioral psychology axes for CTA and persuasion design
- **[design-skill](https://github.com/jasonnamii/design-skill)** — Collaboration: visual hierarchy alignment for UI and marketing copy

## Installation

```bash
git clone https://github.com/jasonnamii/copywriting-engine.git ~/.claude/skills/copywriting-engine
```

## Update

```bash
cd ~/.claude/skills/copywriting-engine && git pull
```

Skills placed in `~/.claude/skills/` are automatically available in Claude Code and Cowork sessions.

## Part of Cowork Skills

This is one of 25+ custom skills. See the full catalog: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## License

MIT License — feel free to use, modify, and share.