# Klarity Hackathon — Shared Brief

> **All agents:** This is the single source of truth. Read this fully before starting your task. Do not contradict this brief — if you disagree, flag it in your output but stick to the spec.

## The Hackathon

- **Sponsor:** Klarity Health (Series B practice management platform for mental health)
- **Klarity scale:** ~3,000 small mental health practices, 40K patient visits/month
- **Klarity does:** scheduling, intake, documentation, billing for behavioral health practices
- **Klarity wants:** AI layer that improves practice metrics; recruiting partners (Victor Zhou, CEO)
- **Time box:** 1 hour to build, 15 min to record 2-min video demo
- **Builder:** Solo

## Judging Rubric

Each scored 0–5:
1. **Innovation** — creative/novel
2. **Technical execution** — completeness, does it work
3. **Design & UX** — polished, usable
4. **Impact / usefulness** — solves a real problem

## The Problem We're Solving

**Patient drop-off in mental health.** ~50% of patients drop after session 1, ~70% by session 3. Each lost patient = $500-2K LTV. For Klarity's network: ~$14M/yr lost revenue + ~$36M/yr in lost LTV = ~$50M/yr addressable.

**Why drop-off happens (from primary user research with a former therapy patient):**
1. **Re-telling the story to every therapist** when shopping for fit (3-5 times)
2. **No continuity between sessions** — therapist starts from "how are you doing?", patient does cognitive labor of re-setting context
3. **Treatment has no scope** — "wait, how many sessions is this?" → drift → drop
4. **Termination is a ghost** — relationship ends abruptly, no door left open, can't tell if it "worked"
5. **No reinforcement between sessions** — patients DIY anchors (phone wallpapers, sticky notes)
6. **Insurance changes (job change) silently kill continuity** — patient doesn't know if they can come back

## The Product Thesis

> **A patient-owned AI continuity layer for mental health.** Captures the patient's own language, briefs the therapist before each session, reinforces takeaways between sessions, detects drop-off patterns, structures treatment planning. Never pretends to be the therapist.

## Architecture — Dual Layer (REVISED)

| Layer | Owner | Sharing model |
|---|---|---|
| **Patient Story** | Patient curates | Always portable, patient-controlled |
| **Clinical Record** | Therapist authors, patient sees | Patient grants access to next provider with one tap |

Default: clinical record stays with provider unless patient opts to share.

## What We're Building (Scope)

### IN SCOPE — 2 features

**Feature 1: The Continuity Loop**
- **Scribe Agent**: takes a (mock) session transcript, extracts 2-3 takeaways in *patient's own language* (NOT generic summary). Therapist reviews, edits, approves.
- **Anchor**: turns approved takeaway into a daily reinforcement card (visual + text), shown in patient app
- **Brief Agent**: composes 1-paragraph pre-session briefing for therapist from week's signals + patient prep notes

**Feature 2: The Circling-Back Detector**
- **Pattern Agent**: analyzes session topics across last 4-5 sessions. Surfaces to therapist when patient is circling: *"Patient has discussed [topic] in 4 of last 5 sessions — consider breakthrough or change of approach. Suggested resources: …"*

### OUT OF SCOPE (mention in roadmap slide only)
- Treatment-scope + checkpoint reassessment
- Soft re-engagement / "3-month check-in" termination
- Therapist matching / state licensure routing
- Voice-note feedback for failed matches
- Insurance/coverage continuity

## Tech Stack

- **Streamlit** (Python) — single-file app, 3 screens
- **Mock Anthropic agents** — hardcoded responses that simulate Claude calls (faster than real API for demo, identical visual outcome)
- **No DB** — Python dicts in memory
- **No auth** — single demo user

## Mock Patient

- **"Patient #247"** (anonymized)
- Profile: working professional, dealing with burnout, has had 4 prior sessions with therapist Dr. Sarah Chen
- Topics circled: work boundaries, perfectionism, "celebrating wins"
- Has shown signs of dropping off (1 reschedule, 1 no-show)
- Mock takeaway from session 4: *"I'm allowed to celebrate my wins"* (patient's own words)

## Three Screens

1. **Therapist View** (Dr. Sarah Chen's app)
   - Pre-session brief for Patient #247
   - Pattern Agent alert: "circling on work boundaries"
   - Suggested takeaway from Session 4 (1-tap approve/edit)
2. **Patient View** (Patient #247's app)
   - Daily anchor card: "I'm allowed to celebrate my wins"
   - Mood check-in widget
   - Upcoming session prep: "Last 4 sessions you discussed X. Want to bring something new?"
3. **Demo Control** (for the live demo flow)
   - Buttons to advance through demo states: "End Session 4", "Tuesday morning", "Friday alert", "Session 5 prep"

## Demo Narrative Arc (for video)

> *"Meet Patient #247. They almost dropped out after Session 4 — like 70% of mental health patients do. Here's what happened instead."*
>
> 1. End of Session 4: Scribe Agent surfaces 3 takeaways → therapist taps to approve "I'm allowed to celebrate my wins"
> 2. Tuesday morning: patient gets anchor card on phone — their own words
> 3. Friday: Pattern Agent flags to therapist: "work boundaries, 4 weeks running"
> 4. Session 5 prep: therapist opens app → 1-paragraph briefing on patient's week
> 5. Session 5 happens 30% more productive
>
> *"This is the AI layer for mental health practices. Not the therapist. The continuity."*

## Design Principles

- **Patient's own language wins** — the magic is reflecting their words back, not generic AI summaries
- **Therapist always in the loop** — agent suggests, human approves
- **Don't replace the therapist** — augment everything around them
- **Radical transparency** — patient sees what the system is doing
- **Soft, warm tone** — not clinical/cold, not corporate

## Files Each Agent Will Write

- Agent A → `talking_points.md`
- Agent B → `ui_spec.md`
- Agent C → `agents.md` (prompts + JSON schemas)
- Agent D → `video_script.md`

All in the project directory.

## Constraints / What NOT to Do

- ❌ Do NOT propose new scope. We're locked.
- ❌ Do NOT make this about US insurance/billing — patient research showed payment was frictionless.
- ❌ Do NOT design a chatbot replacing the therapist.
- ❌ Do NOT use jargon. Klarity's audience = small practices, judges = builders. Plain language.
- ✅ DO push for emotional resonance — this is mental health, not enterprise SaaS.
- ✅ DO ground claims in the user research above.
