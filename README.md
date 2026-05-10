# Continuity — The AI Layer for Mental Health Practices

> *Submitted to the Klarity Health AI Challenge*

**The thesis:** Most AI in mental health is trying to replace the therapist. We're building the layer *in between sessions* — the continuity that holds a patient's story, language, and breakthroughs together.

## The problem

70% of mental health patients drop out by session 3. The reason isn't the therapist — it's everything that *doesn't* happen between sessions:
- Patients re-tell their story to every new provider (3-5 times during fit-shopping)
- Therapists start each session from "how are you doing?"
- Treatment has no scope — patients drift, drop, never come back
- Termination is a ghost — no door left open

## What we built

A patient-owned AI continuity layer with two features:

1. **The Continuity Loop** — Scribe → Anchor → Brief
   - Scribe Agent extracts takeaways in the *patient's own language* (not generic summaries)
   - Therapist approves with one tap
   - Patient receives a daily anchor card — their breakthrough phrase, on their phone
   - Brief Agent pre-briefs the therapist before each session

2. **The Circling-Back Detector**
   - Pattern Agent surfaces when a patient is circling on a topic across multiple sessions
   - Suggests breakthrough resources — measurement-based care without making patients fill out scales

## Architecture

Dual-layer, patient-controlled:
- **Patient Story** — portable, patient-owned, travels between providers
- **Clinical Record** — therapist-authored, patient grants sharing access

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Demo flow

Open the **Demo Control** sidebar to walk through the patient journey:
1. End Session 4 → Scribe surfaces takeaways → Therapist approves
2. Tuesday morning → Patient gets the anchor card
3. Friday → Pattern Agent flags circling on "work boundaries"
4. Session 5 prep → Brief Agent generates 1-paragraph briefing

## Tech

Python + Streamlit. Mock agent responses (designed for real Claude/Anthropic API integration). No DB — in-memory mocks for the demo.

## What's next (roadmap)

- Treatment-scope + checkpoint reassessment
- Soft re-engagement / "3-month check-in" termination
- Cross-state therapist matching
- Voice-note feedback for failed matches
- Insurance/coverage continuity alerts

## Built for

Klarity Health AI Challenge — for partnership with Victor Zhou and the Klarity team.
