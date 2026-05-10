# Money Slide & Judge Talking Points
*Agent A — for Klarity hackathon submission*

---

## 1. The Money Slide

**Mental health drop-off is the largest preventable revenue leak in behavioral health practice management.** Across Klarity's network of ~3,000 practices and ~40K visits/month (~13 visits/practice/month), roughly half of patients drop after Session 1 and ~70% are gone by Session 3. Outpatient behavioral health LTV runs $4K–$15K per patient per industry benchmarks; the brief uses a conservative $500–$2K. Even at the floor, the addressable leak is **~$50M/yr** for Klarity's network. A 20% recapture is **~$10M/yr** of new ARR-equivalent revenue back to the practices Klarity serves — the strongest possible wedge for an AI layer Klarity ships.

| Metric | Value | Source |
|---|---|---|
| Klarity-network drop-off cost | **~$50M/yr** ($14M revenue + $36M LTV; conservative) | Brief + benchmarks below |
| 20% recapture upside | **~$10M/yr** back to practice network | Modeled |
| Per-practice opportunity | **~$3.3K/yr** additional retained revenue per practice (at conservative LTV); **~$10K+/yr** at industry-mean BH LTV | 3K practices ÷ $10M; sensitivity from BSPKN/Foundry CRO |

> *Numbers verified against the brief; LTV range flagged as conservative — true upside is materially higher than $50M if you use $4K–$15K outpatient BH LTV.*

---

## 2. Research-Backed Citations

1. **Drop-off after first session ~20–57%; ~50% by Session 3.** Olfson et al., National Comorbidity Survey Replication — 22.4% of adults dropped before their provider wanted them to; first two visits are the critical window. [PMC: Early Withdrawal from Mental Health Treatment](https://pmc.ncbi.nlm.nih.gov/articles/PMC2762228/) · [APA Monitor — Are your clients leaving too soon?](https://www.apa.org/monitor/2015/04/clients)
2. **Premature termination prevalence 40–60% in U.S. outpatient settings.** Swift & Greenberg meta-analysis (146 studies) finds mean dropout 34.8%, U.S. studies 37.9%. [PMC: Premature Dropout From Psychotherapy](https://pmc.ncbi.nlm.nih.gov/articles/PMC9667417/)
3. **Behavioral health no-show rates 25–42% (community MH); up to ~50% in outpatient.** [JAMA Network Open 2023 — Telehealth and Missed Appointments in BH](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2807436) · [AJMC — "No-Shows": Failure to follow up on initial BH appointments](https://www.ajmc.com/view/feb09-3915p105-112)
4. **Patient acquisition cost in behavioral health: $1,000–$2,500 — highest of any healthcare specialty.** PAC:LTV ratios 5x–25x retention vs. acquisition. [BSPKN: Patient Acquisition Cost 2026 Healthcare Benchmarks](https://www.bspkn.co/insights/patient-acquisition-cost-2026-healthcare-marketing/) · [Behavioral Health Business — Curbing CAC](https://bhbusiness.com/2022/09/14/what-traditional-behavioral-health-operators-can-teach-startups-about-curbing-customer-acquisition-costs/)
5. **Outpatient BH LTV: $4K–$15K per patient.** [Foundry CRO — Healthcare Marketing Benchmarks 2026](https://foundrycro.com/blog/healthcare-marketing-benchmarks-by-specialty/)
6. **Therapist burnout: 61% emotional fatigue, 77% mental fatigue (highest of any specialty after EM); documentation cited as #1 driver.** [Medscape Physician Mental Health & Well-Being Report 2025](https://www.medscape.com/sites/public/mental-health/2025) · [AMA — National Physician Burnout Survey](https://www.ama-assn.org/practice-management/physician-health/national-physician-burnout-survey)
7. **Engagement lift from AI session intelligence (RCT).** Eleos Scribe RCT: clients of providers using AI documentation had **2x engagement** and **3–4x better symptom improvement** vs. treatment as usual. [Eleos Health Press](https://eleos.health/press-releases/strongeleos-advances-behavioral-health-ai-with-breakthrough-offering-for-field-providers-strong/) — *establishes a published causal link between AI continuity tooling and retention; we extend the same mechanism to the patient side.*

---

## 3. Three Sharp Judge Talking Points

**Innovation (vs. existing AI scribes).** Every player in this space — Abridge, Eleos, Blueprint, Freed, JotPsych — points the AI at the *therapist's note*. We point it at the *patient's continuity*. The novel primitive is reflecting the **patient's own language** back to them between sessions ("I'm allowed to celebrate my wins" — not a clinical paraphrase), plus a **Pattern Agent** that detects when a patient is circling on the same topic across 4–5 sessions. No competitor surfaces patient-side anchors or clinician-facing circle-back alerts. This is a new product category, not a feature.

**Impact (the patient-language insight + circling-back detection).** Drop-off happens because patients do invisible cognitive labor — re-telling their story, re-anchoring takeaways, deciding whether the work is "working." Reflecting their words verbatim gets ~2x engagement (Eleos RCT analog). Surfacing circling earlier converts a silent drop-off signal into a clinical decision point. Conservative model: a 20% recapture across Klarity's network is **~$10M/yr** of retained revenue with zero new patient acquisition spend — vs. a $1K–$2.5K CAC to replace each lost patient.

**Strategic fit for Klarity (buy/build, not compete).** Klarity already owns scheduling, intake, documentation, and billing — the entire ops surface of the practice. The one thing it does *not* own is the **continuity layer between sessions**. That's the missing AI primitive. Anyone else who builds this becomes a wedge competitor sitting on top of Klarity's data. Klarity should ship this — the patient-owned story + dual-layer architecture (patient curates story, therapist authors record) is defensible because portability is the moat: patient-controlled data is the only continuity that survives therapist switches, insurance changes, and practice migrations. That's also what makes it Klarity-network-native: every practice on Klarity gets retention lift; switching off Klarity costs the practice that lift.

---

## 4. Competitive Landscape

| Player | What they do | What they DON'T do that we do |
|---|---|---|
| **Abridge** | Enterprise ambient AI scribe inside Epic; therapist-facing note generation | No patient-facing layer; no between-session reinforcement; not BH-specific |
| **Eleos Health** | BH-exclusive scribe + supervisor "Replay" + care intelligence | Therapist/supervisor-side only; no patient anchor cards; no circling-back detection surfaced to clinician |
| **Blueprint Health** | Measurement-based care (PHQ-9, GAD-7) — assessments and dashboards | Not a continuity product; doesn't capture patient language; questionnaire-driven, not narrative |
| **Freed / JotPsych** | Independent-clinician AI scribe for psychiatry/therapy | Note generation only; no patient app; no cross-session pattern detection |
| **Headway / Alma / Grow Therapy** | Therapist marketplace + practice ops | No AI continuity layer; competes with Klarity on ops, not on retention |
| **Talkspace / BetterHelp** | DTC therapy delivery | Owns the relationship, not an AI layer practices can adopt; not a fit for Klarity's 3K independent practices |
| **Woebot / Wysa** | AI chatbots that act *as* the therapist | Replaces the clinician — opposite of our thesis ("never pretends to be the therapist") |

**The white space:** patient-owned, between-session continuity that augments the therapist instead of replacing them, surfaced as alerts a human approves. Nobody is here yet.

---

## 5. The 10-Second Pitch (≤25 words)

> **Klarity owns the practice. We give Klarity the patient-continuity layer that recovers $10M/yr of mental health drop-off — without replacing the therapist.**

*(23 words.)*
