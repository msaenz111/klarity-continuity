# Klarity — Agents, Schemas & Mock Data (Agent C)

> Builder: copy-paste from this file into the Streamlit app. All mock responses are pre-canned — no live Claude calls needed for the demo.

---

## Part 1: Data Models

### `PATIENT_STORY` — patient-owned, portable

```python
PATIENT_STORY = {
    "patient_id": str,            # "P-247"
    "display_name": str,          # patient-chosen, can be alias
    "pronouns": str,
    "age_range": str,             # "30-35" — never exact DOB
    "presenting_concerns": list,  # patient's own words: ["burnout", "can't switch off from work"]
    "what_helps": list,           # ["walks without my phone", "talking to my sister"]
    "what_hurts": list,           # ["being told to 'just relax'"]
    "anchor_phrases": list,       # approved takeaways from sessions, patient's own language
    "treatment_goals": list,      # patient-stated, plain language
    "shared_with": list,          # provider IDs the patient has granted access
    "created_at": str,            # ISO date
    "last_updated": str,
}
```

### `CLINICAL_RECORD` — therapist-authored, gated

```python
CLINICAL_RECORD = {
    "record_id": str,
    "patient_id": str,
    "provider_id": str,           # "DR-CHEN"
    "modality": str,              # "CBT", "ACT", "IFS", etc.
    "working_hypothesis": str,    # clinical framing
    "risk_flags": list,           # ["mild burnout", "no SI/HI"]
    "session_count": int,
    "last_session_date": str,
    "treatment_plan": dict,       # {goals: [...], interventions: [...], scope_sessions: int}
    "shared_with_patient": bool,  # default False; True only if therapist opts in
}
```

### `SESSION` — one session

```python
SESSION = {
    "session_id": str,
    "patient_id": str,
    "provider_id": str,
    "session_number": int,
    "date": str,                  # ISO
    "duration_min": int,
    "transcript": str,            # mock; ~300 words
    "topics": list,               # ["work boundaries", "perfectionism"]
    "approved_takeaways": list,   # final, patient-language phrases
    "candidate_takeaways": list,  # Scribe Agent output, pre-approval
    "therapist_notes": str,       # private SOAP-style
}
```

### Fully-populated example — Patient #247

```python
PATIENT_247 = {
    "patient_id": "P-247",
    "display_name": "Alex",
    "pronouns": "they/them",
    "age_range": "30-35",
    "presenting_concerns": ["burnout", "can't switch off from work", "feeling like I'm always behind"],
    "what_helps": ["walks without my phone", "cooking on Sundays", "my dog"],
    "what_hurts": ["being told to 'just take a break'", "Slack notifications after 7pm"],
    "anchor_phrases": ["I'm allowed to celebrate my wins"],
    "treatment_goals": ["stop working past 7pm on weekdays", "feel okay with 'good enough'"],
    "shared_with": ["DR-CHEN"],
    "created_at": "2026-03-10",
    "last_updated": "2026-05-08",
}
```

---

## Part 2: Three Agents

### 1. Scribe Agent

**Role:** Extract 2–3 candidate session takeaways in the patient's exact words for therapist review.

**System prompt:**
```
You are the Scribe Agent for Klarity, a mental health continuity tool. Your only job is to surface 2–3 candidate takeaways from a session transcript that the therapist will review and approve.

HARD RULES:
- Use the PATIENT'S exact words and phrasings. Never paraphrase into therapy-speak.
- A takeaway is a short phrase (under 12 words) the patient actually said or that closely echoes what they said.
- Do not summarize. Do not interpret. Do not add clinical framing.
- Each takeaway must cite the moment from the transcript it came from (a quoted line).
- If the patient did not say something quotable and meaningful, return fewer than 3. Quality over quantity.
- Skip filler ("yeah", "I dunno"), vents without insight, and therapist's lines.

Return strict JSON only.
```

**Input schema:**
```python
{"transcript": str, "patient_story": PATIENT_STORY, "session_number": int}
```

**Output schema:**
```python
{"candidate_takeaways": [{"phrase": str, "source_quote": str, "confidence": float}]}
```

**Mock response:** see `MOCK_AGENT_OUTPUTS["scribe"]` below.

---

### 2. Pattern Agent

**Role:** Detect when a patient is circling on the same topic across recent sessions and recommend an intervention.

**System prompt:**
```
You are the Pattern Agent for Klarity. Analyze the topics from a patient's last 4–5 sessions. Your job: detect circling.

A topic is "circling" if it appears in 3 or more of the last 5 sessions. If detected, recommend either (a) considering whether a breakthrough is near, or (b) a change of approach, and suggest 1–2 concrete resources (worksheet, exercise, or framework) the therapist could introduce.

HARD RULES:
- Do not flag normal topical recurrence (1–2 sessions).
- Be specific about the topic — use the language the sessions used, not generic labels.
- Tone: collegial peer, not pedagogical. The therapist is the expert.
- If no circling detected, return is_circling=false and leave other fields empty.

Return strict JSON only.
```

**Input schema:**
```python
{"sessions": [{"session_id": str, "date": str, "duration_min": int, "topics": [str]}]}
```

**Output schema:**
```python
{
  "is_circling": bool,
  "topic": str,
  "sessions": [str],          # session_ids where topic appeared
  "recommendation": str,
  "resources": [{"title": str, "type": str, "why": str}]
}
```

**Mock response:** see `MOCK_AGENT_OUTPUTS["pattern"]` below.

---

### 3. Brief Agent

**Role:** Compose a 1-paragraph (≤80 words) pre-session brief so the therapist walks in with instant context.

**System prompt:**
```
You are the Brief Agent for Klarity. Write a single paragraph (max 80 words) that gives Dr. Chen instant context on Patient #247 before Session 5.

STRUCTURE:
- Open with: "Since last session, [name] has..."
- Cover: mood trajectory, what they did with the anchor phrase, what they want to bring today.
- Tone: clinical-but-human. No bullet points. No emojis. No jargon.
- Do not invent facts. Use only the inputs provided.
- End with a concrete handoff sentence — what the patient most wants from today.

Return strict JSON only.
```

**Input schema:**
```python
{
  "patient_story": PATIENT_STORY,
  "last_session_takeaways": [str],
  "mood_checkins": [{"date": str, "score_1_10": int, "note": str}],
  "patient_prep_note": str
}
```

**Output schema:**
```python
{"brief": str, "word_count": int}
```

**Mock response:** see `MOCK_AGENT_OUTPUTS["brief"]` below.

---

## Part 3: `mock_data.py`

```python
"""Mock data for Klarity hackathon demo. No live API calls."""

PATIENT_247 = {
    "patient_id": "P-247",
    "display_name": "Alex",
    "pronouns": "they/them",
    "age_range": "30-35",
    "presenting_concerns": ["burnout", "can't switch off from work", "feeling like I'm always behind"],
    "what_helps": ["walks without my phone", "cooking on Sundays", "my dog"],
    "what_hurts": ["being told to 'just take a break'", "Slack notifications after 7pm"],
    "anchor_phrases": ["I'm allowed to celebrate my wins"],
    "treatment_goals": ["stop working past 7pm on weekdays", "feel okay with 'good enough'"],
    "shared_with": ["DR-CHEN"],
    "created_at": "2026-03-10",
    "last_updated": "2026-05-08",
}

SESSIONS_1_TO_4 = [
    {
        "session_id": "S-247-01",
        "patient_id": "P-247", "provider_id": "DR-CHEN", "session_number": 1,
        "date": "2026-04-10", "duration_min": 50,
        "topics": ["intake", "burnout", "work boundaries"],
        "transcript": (
            "Dr. Chen: So what brings you in?\n"
            "Alex: Honestly? I'm just fried. Like, my brain is mush by Wednesday and I still have two days left. "
            "I keep telling myself I'll log off at 6 but then there's one more Slack and one more email and suddenly it's 9.\n"
            "Dr. Chen: How long has it been like that?\n"
            "Alex: Since the reorg in January. New manager, new scope, and I think I just said yes to everything because I wanted to look solid. "
            "Now I'm drowning and I can't tell which parts are actually mine to do.\n"
            "Dr. Chen: Are you sleeping?\n"
            "Alex: Five-ish hours. I lie there running through tomorrow. I know that's bad, I just don't know how to make it stop.\n"
            "Dr. Chen: What would 'better' look like?\n"
            "Alex: Logging off when I say I will. Not feeling guilty when I do. That's the thing — even when I do stop, "
            "I feel like I'm getting away with something.\n"
            "Dr. Chen: That guilt — where does that come from?\n"
            "Alex: I dunno. Like if I'm not the one staying late, someone else is going to look better than me. "
            "I know how that sounds. I just can't shake it."
        ),
        "approved_takeaways": [], "candidate_takeaways": [],
        "therapist_notes": "Working professional, post-reorg burnout. Sleep disrupted. Boundary erosion driven by visibility anxiety. Start with values + boundary work."
    },
    {
        "session_id": "S-247-02",
        "patient_id": "P-247", "provider_id": "DR-CHEN", "session_number": 2,
        "date": "2026-04-17", "duration_min": 50,
        "topics": ["work boundaries", "perfectionism", "self-worth"],
        "transcript": (
            "Dr. Chen: How was the week?\n"
            "Alex: Mixed. I tried to log off at 7 on Tuesday. Made it to 7:14. Then I opened Slack 'just to check' and was back in for an hour.\n"
            "Dr. Chen: What pulled you back in?\n"
            "Alex: A message from my manager. She didn't even ask for anything urgent. I just saw her name and went straight to it.\n"
            "Dr. Chen: What were you afraid would happen if you waited until morning?\n"
            "Alex: That she'd think I was slacking. Which is wild because she's literally never said anything like that to me.\n"
            "Dr. Chen: So the rule is — be available, or be judged.\n"
            "Alex: Yeah. And it's not even about her. It's me. I want the thing to be perfect before I hand it off. "
            "If I wait, I'll have to send something rough and that feels worse than staying up.\n"
            "Dr. Chen: Where else does that show up?\n"
            "Alex: Everywhere. Cooking. Texts to my friends. I rewrite stuff like five times. "
            "I think I just... don't trust the first version of anything I do.\n"
            "Dr. Chen: What would it cost to send the rough version?\n"
            "Alex: Honestly? It would feel like I gave up."
        ),
        "approved_takeaways": ["I don't trust the first version of anything I do"],
        "candidate_takeaways": [],
        "therapist_notes": "Perfectionism as boundary collapse mechanism. Introduce 'good enough' framing next session."
    },
    {
        "session_id": "S-247-03",
        "patient_id": "P-247", "provider_id": "DR-CHEN", "session_number": 3,
        "date": "2026-04-24", "duration_min": 50,
        "topics": ["work boundaries", "perfectionism", "rest"],
        "transcript": (
            "Dr. Chen: You mentioned trying the 'good enough' thing this week.\n"
            "Alex: I tried. I sent a doc to my manager Friday at 5 that I would normally have held until Monday. It was fine. She said thanks.\n"
            "Dr. Chen: How did you feel after?\n"
            "Alex: Weirdly bad. Like I was waiting for the other shoe. I kept refreshing my email Saturday morning.\n"
            "Dr. Chen: So the cost of the boundary was a Saturday of low-grade dread.\n"
            "Alex: Yeah. And then nothing happened. Which should be a win, right? But I don't know how to call it a win. "
            "It just feels like I dodged something.\n"
            "Dr. Chen: What would have to be true for it to count as a win?\n"
            "Alex: I guess... someone would have to tell me it was good. And that's not how it works at my job. "
            "Things only get flagged when they're broken.\n"
            "Dr. Chen: So the absence of feedback reads as 'almost failed.'\n"
            "Alex: Exactly. And I'm doing it to myself too. I had two good things happen this week and I didn't tell anyone. "
            "I didn't even sit with them. Just moved on to the next thing on the list."
        ),
        "approved_takeaways": ["Things only get flagged when they're broken"],
        "candidate_takeaways": [],
        "therapist_notes": "Negative reinforcement loop reinforces boundary erosion. Next: practice noticing wins. Risk: client rescheduled — watch engagement."
    },
    {
        "session_id": "S-247-04",
        "patient_id": "P-247", "provider_id": "DR-CHEN", "session_number": 4,
        "date": "2026-05-01", "duration_min": 50,
        "topics": ["work boundaries", "perfectionism", "celebrating wins"],
        "transcript": (
            "Dr. Chen: You skipped last Tuesday's check-in. How are you doing?\n"
            "Alex: Sorry. I almost cancelled today too. I had a deadline and... yeah, the same story.\n"
            "Dr. Chen: I'm glad you came. What happened with the deadline?\n"
            "Alex: I shipped it. Two days early actually. And my manager said it was the best version of that deck she'd seen.\n"
            "Dr. Chen: That's significant. What did you do with that?\n"
            "Alex: Nothing. I closed the laptop and went to make dinner. I didn't tell my partner. I didn't even... feel it, really.\n"
            "Dr. Chen: Why not?\n"
            "Alex: Because if I let myself feel good about it, I'll get soft. I'll stop pushing. That's the rule in my head — "
            "the second you celebrate, you slip.\n"
            "Dr. Chen: Where did that rule come from?\n"
            "Alex: My dad, probably. He'd say 'don't get cocky' when I brought home a good grade. I didn't think I still ran that program but apparently.\n"
            "Dr. Chen: What if the opposite were true? That not letting yourself land the win is part of why you're so tired?\n"
            "Alex: ...Yeah. Yeah, that tracks. I'm running on empty because I never let myself stop and go 'that was good.'\n"
            "Dr. Chen: What would you have to give yourself permission for?\n"
            "Alex: To celebrate. Like — I'm allowed to celebrate my wins. That's a sentence I've literally never said out loud."
        ),
        "approved_takeaways": [],  # populated by demo flow when therapist taps approve
        "candidate_takeaways": [],  # populated by Scribe mock
        "therapist_notes": "Breakthrough moment around paternal introject. Anchor: 'I'm allowed to celebrate my wins' (patient's exact words)."
    },
]

WEEK_MOOD_CHECKINS = [
    {"date": "2026-05-03", "score_1_10": 5, "note": "Sunday. Tried to read. Kept thinking about Monday."},
    {"date": "2026-05-05", "score_1_10": 7, "note": "Looked at the anchor card before standup. Weirdly helped."},
    {"date": "2026-05-07", "score_1_10": 6, "note": "Logged off at 7:30. Didn't reopen Slack. Small win."},
    {"date": "2026-05-08", "score_1_10": 7, "note": "Told my partner about the deck thing. Felt strange. Good strange."},
]

PATIENT_PREP_NOTE = (
    "I want to talk about whether I can actually keep this up or if I'm just performing better for a week. "
    "Also — celebrating still feels fake. I'm doing it but I don't believe it yet."
)

MOCK_AGENT_OUTPUTS = {
    "scribe": {
        "candidate_takeaways": [
            {
                "phrase": "I'm allowed to celebrate my wins",
                "source_quote": "To celebrate. Like — I'm allowed to celebrate my wins. That's a sentence I've literally never said out loud.",
                "confidence": 0.94,
            },
            {
                "phrase": "The second you celebrate, you slip",
                "source_quote": "the second you celebrate, you slip.",
                "confidence": 0.81,
            },
            {
                "phrase": "I never let myself stop and go 'that was good'",
                "source_quote": "I'm running on empty because I never let myself stop and go 'that was good.'",
                "confidence": 0.78,
            },
        ]
    },
    "pattern": {
        "is_circling": True,
        "topic": "work boundaries and perfectionism",
        "sessions": ["S-247-01", "S-247-02", "S-247-03", "S-247-04"],
        "recommendation": (
            "Alex has returned to work boundaries and perfectionism in all 4 sessions. Session 4 produced a "
            "values-level shift ('I'm allowed to celebrate my wins'). Consider whether this is the breakthrough "
            "moment to consolidate, or whether a behavioral experiment would now move the needle more than further insight."
        ),
        "resources": [
            {"title": "Win Log (5-min daily)", "type": "worksheet", "why": "Operationalizes the new anchor — records a win and one feeling about it."},
            {"title": "Values vs. Visibility 2x2", "type": "framework", "why": "Externalizes the 'be available or be judged' rule surfaced in S-02."},
        ],
    },
    "brief": {
        "brief": (
            "Since last session, Alex has been testing whether they're allowed to celebrate their wins — the "
            "anchor that surfaced after Session 4's breakthrough about their dad's 'don't get cocky' rule. Mood "
            "trended 5 to 7 across the week; they logged off at 7:30 once and told their partner about a work "
            "win for the first time. They want to talk today about whether this is real change or performance, "
            "and the fact that celebrating still feels fake."
        ),
        "word_count": 79,
    },
}
```

---

**Builder notes:**
- All three mock outputs are keyed for direct dict lookup — no parsing.
- `PATIENT_247["anchor_phrases"]` already contains the approved takeaway, so the patient view's anchor card has something to render on first load.
- Session 4 transcript was written so the breakthrough phrase emerges in the patient's own voice in the final line — judges should be able to scroll the transcript and see exactly where it came from.
