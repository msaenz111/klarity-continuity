# Throughline

> **The AI memory layer between therapy sessions.**
> Built for the Klarity Health AI Challenge.

**Live demo:** https://klarity-continuity-epq7zblk7m7pd2scofxptz.streamlit.app
**Repo:** https://github.com/msaenz111/klarity-continuity

---

## The hook

> *"I'm allowed to celebrate my wins."*
> A patient said that out loud for the first time in their life, in session four.
> Seventy percent of patients like them never make it to session five.
> **This is the AI that changes that.**

---

## The problem

70% of mental health patients drop by session three. The reason isn't the therapist — it's everything that *doesn't* happen between sessions:

- Patients re-tell their story to every new provider
- Therapists start each session cold from "how are you doing?"
- Treatment drifts, then patients drop
- Each lost patient costs Klarity's network ~$500–2K in LTV
- For Klarity's 3,000 practices: **~$50M/yr walking out the door**

## The wedge

**Every AI in mental health is pointed at the therapist's note. We point it at the patient's sentence.**

Most AI tools in mental health automate documentation, billing, or summaries — they serve the *clinician*. Throughline serves the *patient*. We capture the breakthrough sentence the patient said in session, in their own words, and we hold it for them — and for their therapist — all the way to the next session.

## What we built

A patient-owned AI continuity layer with three agents:

1. **Scribe** — extracts 2-3 takeaway candidates from a session in the patient's own language. Therapist approves with one tap.
2. **Pattern** — surfaces when a patient is circling on a topic across multiple sessions. Suggests breakthrough resources.
3. **Brief** — composes a 1-paragraph pre-session briefing for the therapist from the week's signals.

Plus the **anchor card** — the patient's approved breakthrough sentence, delivered to their phone Tuesday morning.

## How it works (the demo flow)

| When | Who | What happens |
|---|---|---|
| End of Session 4 | Therapist (Dr. Chen) | Scribe surfaces 3 candidate takeaways. Dr. Chen taps to approve *"I'm allowed to celebrate my wins."* |
| Tuesday morning | Patient #247 | Opens phone. Sees their own sentence — their breakthrough, their voice. |
| Friday | Therapist | Pattern Agent flags: 4 of last 5 sessions circling on work boundaries. |
| Monday morning | Therapist | Brief Agent gives Dr. Chen a one-paragraph note before Session 5. |
| Session 5 | Both | Starts 30% further down the field. Continuity was already there. |

## Architecture

Dual-layer, patient-controlled:
- **Patient Story** — portable, patient-owned, travels between providers
- **Clinical Record** — therapist-authored, patient grants sharing access

Default: clinical record stays with the provider unless the patient opts to share.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the **Demo Control** view in the sidebar and click **▶ Play full demo (auto)** — the whole story unfolds across the Therapist and Patient views.

## Tech

- Python + Streamlit
- Mock agent responses (designed for real Claude/Anthropic API integration)
- No DB — in-memory mocks for the demo

## What's next

- Real Claude API integration for the three agents
- Treatment-scope + checkpoint reassessment
- Soft re-engagement / "3-month check-in" termination
- Cross-state therapist matching
- Insurance/coverage continuity alerts

## Built for

**Klarity Health AI Challenge** — pitching partnership with Victor Zhou and the Klarity team.

We're not the therapist. We're the continuity.

---

*Throughline — built in a one-hour hackathon.*
