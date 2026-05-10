"""
Klarity — The AI Layer for Mental Health Practices.
A patient-owned continuity layer. Not the therapist. The continuity.
"""

import streamlit as st

from mock_data import (
    MOCK_AGENT_OUTPUTS,
    PATIENT_247,
    PATIENT_PREP_NOTE,
    SESSIONS_1_TO_4,
    WEEK_MOOD_CHECKINS,
)

st.set_page_config(page_title="Klarity", page_icon="🌱", layout="centered")

# -------------------- CSS --------------------
st.markdown(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
    <style>
      /* ---------- Palette ----------
         #FAF7F2  cream bg
         #FFF8F4  warm white card bg
         #2A2A2A  body text
         #6B8E7F  sage green primary
         #C97B5C  warm coral accent
         #6B7B6F  muted sage
         #8A8A8A  soft muted gray
         #EAE3D2  warm border
      */

      /* ---------- Base shell (force light) ---------- */
      html, body, [class*="css"] {
          font-family: 'Inter', system-ui, -apple-system, "Segoe UI", Roboto, sans-serif !important;
      }
      .stApp {
          background-color: #FAF7F2 !important;
          color: #2A2A2A !important;
      }
      .main .block-container {
          padding-top: 2.5rem;
          padding-bottom: 4rem;
          max-width: 780px;
      }

      /* ---------- Typography ---------- */
      h1, h2, h3, h4, h5, h6 {
          font-family: 'Lora', Georgia, serif !important;
          color: #2A2A2A !important;
          letter-spacing: -0.01em;
      }
      h1 { font-size: 2.25rem; line-height: 1.2; font-weight: 600; }
      h2 { font-size: 1.6rem; line-height: 1.25; font-weight: 600; }
      h3 { font-size: 1.25rem; line-height: 1.3; font-weight: 600; }
      h4 { font-size: 1.05rem; line-height: 1.35; font-weight: 600; }
      p, li, span, label, div { color: #2A2A2A; }
      .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span {
          color: #2A2A2A !important;
          font-size: 16px;
          line-height: 1.6;
      }
      .stMarkdown strong { color: #2A2A2A !important; }
      .stMarkdown em { color: #2A2A2A; }

      /* Captions — muted but legible */
      .stCaption, [data-testid="stCaptionContainer"], small,
      .stMarkdown small {
          color: #6B7B6F !important;
          font-size: 13px !important;
          line-height: 1.5 !important;
      }

      /* ---------- st.metric ---------- */
      [data-testid="stMetric"] {
          background-color: #FFF8F4;
          border: 1px solid #EAE3D2;
          border-radius: 12px;
          padding: 14px 16px;
      }
      [data-testid="stMetricLabel"],
      [data-testid="stMetricLabel"] * {
          color: #6B7B6F !important;
          font-weight: 500 !important;
          font-size: 13px !important;
      }
      [data-testid="stMetricValue"],
      [data-testid="stMetricValue"] * {
          color: #2A2A2A !important;
          font-family: 'Lora', Georgia, serif !important;
          font-weight: 600 !important;
      }
      [data-testid="stMetricDelta"],
      [data-testid="stMetricDelta"] * {
          color: #6B8E7F !important;
          font-weight: 500 !important;
      }

      /* ---------- Inputs ---------- */
      .stTextArea textarea, .stTextInput input {
          background-color: #FFFFFF !important;
          color: #2A2A2A !important;
          border: 1px solid #EAE3D2 !important;
          border-radius: 10px !important;
      }
      .stTextArea textarea::placeholder, .stTextInput input::placeholder {
          color: #B8B8B8 !important;
      }
      .stTextArea label, .stTextInput label {
          color: #2A2A2A !important;
          font-weight: 500 !important;
      }

      /* ---------- Buttons ---------- */
      .stButton > button {
          background-color: #FFFFFF;
          color: #2A2A2A !important;
          border: 1px solid #EAE3D2;
          border-radius: 10px;
          font-weight: 500;
          padding: 0.5rem 1rem;
          transition: all 0.15s ease;
      }
      .stButton > button:hover {
          border-color: #6B8E7F;
          color: #6B8E7F !important;
          background-color: #FFFFFF;
      }
      .stButton > button[kind="primary"] {
          background-color: #6B8E7F !important;
          color: #FFFFFF !important;
          border: 1px solid #6B8E7F !important;
      }
      .stButton > button[kind="primary"]:hover {
          background-color: #5A7C6E !important;
          border-color: #5A7C6E !important;
          color: #FFFFFF !important;
      }
      .stButton > button:disabled {
          color: #B8B8B8 !important;
          background-color: #F4EFE7 !important;
          border-color: #EAE3D2 !important;
      }

      /* ---------- Expander ---------- */
      [data-testid="stExpander"] {
          background-color: #FFF8F4;
          border: 1px solid #EAE3D2 !important;
          border-radius: 12px !important;
      }
      [data-testid="stExpander"] summary,
      [data-testid="stExpander"] summary * {
          color: #2A2A2A !important;
          font-weight: 500 !important;
      }
      [data-testid="stExpander"] summary:hover,
      [data-testid="stExpander"] summary:hover * {
          color: #6B8E7F !important;
      }
      [data-testid="stExpander"] [data-testid="stMarkdownContainer"] p,
      [data-testid="stExpander"] [data-testid="stMarkdownContainer"] li {
          color: #2A2A2A !important;
      }

      /* ---------- Bordered containers ---------- */
      [data-testid="stVerticalBlockBorderWrapper"] {
          background-color: #FFF8F4;
          border-radius: 12px !important;
      }

      /* ---------- Alerts ---------- */
      [data-testid="stAlert"] { border-radius: 12px; }
      .stAlert p, .stAlert div, [data-testid="stAlert"] * {
          color: #2A2A2A !important;
      }

      /* ---------- Sidebar (intentionally dark) ---------- */
      [data-testid="stSidebar"] {
          background-color: #2A2A2A !important;
      }
      [data-testid="stSidebar"] * { color: #F4EFE7 !important; }
      [data-testid="stSidebar"] h1,
      [data-testid="stSidebar"] h2,
      [data-testid="stSidebar"] h3,
      [data-testid="stSidebar"] h4 { color: #FFFFFF !important; }
      [data-testid="stSidebar"] [data-testid="stCaptionContainer"],
      [data-testid="stSidebar"] small { color: #B8B8B8 !important; }
      [data-testid="stSidebar"] label,
      [data-testid="stSidebar"] [role="radiogroup"] label,
      [data-testid="stSidebar"] [role="radiogroup"] label * {
          color: #F4EFE7 !important;
          font-weight: 500;
      }
      [data-testid="stSidebar"] hr { border-color: #444 !important; }

      /* ---------- Custom Klarity components ---------- */
      .anchor-quote {
          font-family: 'Lora', Georgia, serif;
          font-size: 32px;
          line-height: 1.35;
          color: #2A2A2A !important;
          text-align: center;
          padding: 40px 24px 16px 24px;
          font-weight: 500;
          letter-spacing: -0.01em;
      }
      .anchor-attrib {
          text-align: center;
          color: #6B7B6F !important;
          font-size: 13px;
          font-style: italic;
          padding-bottom: 32px;
          letter-spacing: 0.02em;
      }
      .brief-card {
          background-color: #FFF8F4;
          border-left: 4px solid #6B8E7F;
          border-radius: 12px;
          padding: 24px 28px;
          box-shadow: 0 1px 4px rgba(42,42,42,0.04);
          margin-bottom: 16px;
          color: #2A2A2A;
          line-height: 1.6;
      }
      .brief-card strong { color: #2A2A2A; }
      .pattern-card {
          background-color: #FFF8F4;
          border-left: 4px solid #C97B5C;
          border-radius: 12px;
          padding: 20px 24px;
          margin-bottom: 16px;
          color: #2A2A2A;
          line-height: 1.6;
      }
      .pattern-card strong { color: #2A2A2A; }
      .takeaway-card {
          background-color: #FFF8F4;
          border-radius: 14px;
          padding: 28px 28px 24px 28px;
          box-shadow: 0 1px 4px rgba(42,42,42,0.04);
          margin-bottom: 14px;
          border: 1px solid #EAE3D2;
          color: #2A2A2A;
      }
      .anchor-card {
          background-color: #FFFFFF;
          border-radius: 24px;
          padding: 8px 24px 16px 24px;
          box-shadow: 0 8px 32px rgba(107,142,127,0.12),
                      0 2px 6px rgba(42,42,42,0.04);
          margin: 24px 0;
          border: 1px solid #EAE3D2;
      }
      .small-muted { color: #8A8A8A !important; font-size: 13px; }
      /* Pills appear in the dark sidebar — colors tuned for that contrast.
         Selector boosted with [data-testid="stSidebar"] to win over the
         sidebar's universal text-color rule. */
      [data-testid="stSidebar"] .pill-on,
      .pill-on  { color: #A8C9B8 !important; font-weight: 600; }
      [data-testid="stSidebar"] .pill-off,
      .pill-off { color: #9A9A9A !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------- Session state --------------------
DEMO_FLAGS = [
    "session_4_ended",
    "takeaway_approved",
    "anchor_delivered",
    "pattern_alert_fired",
    "brief_generated",
]
for k in DEMO_FLAGS:
    if k not in st.session_state:
        st.session_state[k] = False

# -------------------- Sidebar --------------------
view = st.sidebar.radio("View", ["Demo Control", "Therapist", "Patient"], index=0)

st.sidebar.markdown("---")
st.sidebar.caption("Demo state")
for k in DEMO_FLAGS:
    mark = "✓" if st.session_state[k] else "–"
    klass = "pill-on" if st.session_state[k] else "pill-off"
    label = k.replace("_", " ")
    st.sidebar.markdown(
        f"<span class='{klass}'>{mark}  {label}</span>",
        unsafe_allow_html=True,
    )


# -------------------- Story banner --------------------
def current_moment():
    """Return (headline, subline) describing where we are in the demo arc."""
    s = st.session_state
    if s["brief_generated"]:
        return (
            "Monday morning, May 11 — Brief Agent has prepped Dr. Chen for Session 5",
            "One paragraph distilled from the patient's week. No 'so how are you doing?'",
        )
    if s["pattern_alert_fired"]:
        return (
            "Friday, May 8 — Pattern Agent flagged a 4-week loop",
            "Work boundaries keep coming up. Therapist decides what to do with that.",
        )
    if s["anchor_delivered"]:
        return (
            "Tuesday morning, May 12 — the patient's anchor just landed",
            "Their own words from Session 4, reflected back on a weekday morning.",
        )
    if s["takeaway_approved"]:
        return (
            "Saturday — Dr. Chen approved the anchor",
            "Queued to reach the patient Tuesday at 7am. Therapist always in the loop.",
        )
    if s["session_4_ended"]:
        return (
            "End of Session 4 — Scribe Agent surfaced 3 takeaways",
            "In the patient's own language. Dr. Chen picks one to send as this week's anchor.",
        )
    return (
        "Before we start — Patient #247 almost dropped after Session 4",
        "Like 70% of mental health patients do. Here's what happened instead.",
    )


def render_story_banner():
    headline, subline = current_moment()
    st.markdown(
        f"""
        <div style="
            background-color:#FFFFFF;
            border:1px solid #EAE3D2;
            border-left:4px solid #6B8E7F;
            border-radius:12px;
            padding:14px 18px;
            margin-bottom:18px;
            box-shadow:0 1px 4px rgba(0,0,0,0.04);
        ">
          <div style="font-size:11px;letter-spacing:0.08em;text-transform:uppercase;color:#6B7B6F;font-weight:600;">
            Where we are
          </div>
          <div style="font-family:'Lora',Georgia,serif;font-size:18px;color:#2A2A2A;margin-top:2px;">
            {headline}
          </div>
          <div style="color:#6B7B6F;font-size:13px;margin-top:4px;">
            {subline}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------------------- THERAPIST VIEW --------------------
def therapist_view():
    render_story_banner()

    if not any(st.session_state[k] for k in DEMO_FLAGS):
        st.info(
            "Nothing has happened yet in the demo. Open **Demo Control** in the "
            "sidebar and click **▶ Play full demo** to fast-forward the full story."
        )

    st.markdown("### Good morning, Dr. Chen")
    st.caption("Monday, May 11 · 3 sessions today · Patient #247 at 2:00pm")
    st.markdown("")

    # ----- Section 1: Today's brief -----
    st.markdown("### Today's brief")
    st.caption(
        "Brief Agent reads the week's check-ins and prep notes, hands you one paragraph."
    )
    if st.session_state["brief_generated"]:
        brief = MOCK_AGENT_OUTPUTS["brief"]["brief"]
        st.markdown(
            f"""
            <div class="brief-card">
              <strong>Patient #247 · Session 5 · Tuesday 2:00pm</strong><br><br>
              {brief}
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("Generated by Brief Agent at 8:42am · you reviewed it at 8:44am")
    else:
        st.markdown(
            """
            <div class="brief-card">
              <span class="small-muted">
                The brief for Patient #247 lands here on Monday morning, once the
                week's check-ins are in.
              </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")

    # ----- Section 2: Patterns we've noticed -----
    st.markdown("### Patterns we've noticed")
    st.caption(
        "Pattern Agent watches the last 4–5 sessions for topics that keep returning."
    )
    if st.session_state["pattern_alert_fired"]:
        pattern = MOCK_AGENT_OUTPUTS["pattern"]
        with st.expander(
            "Circling on work boundaries — 4 of the last 5 sessions",
            expanded=True,
        ):
            st.markdown(
                f"""
                <div class="pattern-card">
                  <strong>{pattern['topic']}</strong><br><br>
                  {pattern['recommendation']}
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown("**A few things you could try**")
            for r in pattern["resources"]:
                st.markdown(f"• **{r['title']}** — *{r['why']}*")
            st.markdown("")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.button("Suggest a values exercise", key="pat_b1")
            with c2:
                st.button("Resurface their Session 2 quote", key="pat_b2")
            with c3:
                st.button("Dismiss", key="pat_b3")
            st.caption(
                "You choose. Klarity never messages the patient without your approval."
            )
    else:
        st.markdown(
            """
            <div class="pattern-card">
              <span class="small-muted">
                No loops worth flagging yet. The Pattern Agent will surface here when
                a topic repeats.
              </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")

    # ----- Section 3: From your last session -----
    st.markdown("### From your last session")
    st.caption(
        "Scribe Agent extracts 2–3 takeaways in the patient's own language. You pick the one to send."
    )
    if st.session_state["session_4_ended"] and not st.session_state["takeaway_approved"]:
        for i, t in enumerate(MOCK_AGENT_OUTPUTS["scribe"]["candidate_takeaways"]):
            st.markdown(
                f"""
                <div class="takeaway-card">
                  <div style="font-family:'Lora',Georgia,serif;font-size:20px;line-height:1.4;">
                    "{t['phrase']}."
                  </div>
                  <div class="small-muted" style="margin-top:8px;">
                    From: <em>"{t['source_quote']}"</em>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            cols = st.columns([1, 1, 4])
            with cols[0]:
                if st.button("Approve & send", key=f"approve_{i}"):
                    st.session_state["takeaway_approved"] = True
                    st.rerun()
            with cols[1]:
                st.button("Edit", key=f"edit_{i}")
        st.markdown("")
    elif st.session_state["takeaway_approved"]:
        st.success(
            "Anchor approved. Patient #247 will wake up to *“I'm allowed to celebrate my wins”* Tuesday at 7am."
        )
    else:
        st.markdown(
            """
            <div class="takeaway-card">
              <span class="small-muted">
                Takeaway candidates from your next session will show up here for review.
              </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")

    # ----- Section 4: Engagement at a glance -----
    st.markdown("### Engagement at a glance")
    st.caption(
        "Drop-off risk blends attendance, between-session engagement, and circling signals."
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Sessions attended", "4 of 5", delta="−1 no-show")
    with c2:
        st.metric("Drop-off risk", "Moderate", delta="↓ from High")
    with c3:
        st.metric("Last engagement", "2 days ago", delta="anchor tapped")


# -------------------- PATIENT VIEW --------------------
def patient_view():
    render_story_banner()

    if not any(st.session_state[k] for k in DEMO_FLAGS):
        st.info(
            "Nothing has happened yet. Open **Demo Control** in the sidebar and "
            "click **▶ Play full demo** to see what the patient sees."
        )

    cols = st.columns([1, 4, 1])
    with cols[1]:
        # Tiny grounding header
        st.markdown(
            "<div style='text-transform:uppercase;letter-spacing:0.1em;"
            "font-size:11px;color:#6B7B6F;font-weight:600;'>"
            "Your morning · May 12</div>",
            unsafe_allow_html=True,
        )
        st.markdown("# Hi, Alex 🌱")
        st.caption("One thing for today, then the rest of your morning.")
        st.markdown("")

        # ----- THE moment: daily anchor -----
        if st.session_state["anchor_delivered"]:
            st.markdown(
                """
                <div class="anchor-card">
                  <div class="anchor-quote">
                    "I'm allowed to<br>celebrate my wins."
                  </div>
                  <div class="anchor-attrib">— Your words, Session 4</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            b1, b2, b3 = st.columns(3)
            with b1:
                st.button("This lands today", key="res")
            with b2:
                st.button("Not today", key="not")
            with b3:
                st.button("Save to my Story", key="save")
            st.caption(
                "This came from something you said, not something an AI wrote for you."
            )
        else:
            st.markdown(
                """
                <div class="anchor-card">
                  <div class="anchor-quote small-muted">
                    Your next anchor lands here<br>after Dr. Chen reviews Session 4.
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("")

        # ----- Mood check-in -----
        st.markdown("**How's today landing?**")
        m = st.feedback("stars")
        if m is not None:
            st.toast("Logged. Thanks for checking in.")

        st.markdown("")

        # ----- Prep for next session -----
        with st.expander("Prepping for Tuesday with Dr. Chen", expanded=False):
            st.caption("A heads-up for Dr. Chen, in your own words. Optional, always.")
            st.markdown("*The last 4 sessions, you talked about:*")
            st.markdown("- Work boundaries (4×)")
            st.markdown("- Perfectionism (3×)")
            st.markdown("- Celebrating wins (2×)")
            st.markdown("- Your sister's wedding (1×)")
            st.text_area(
                "Anything new you want to bring in?",
                placeholder="A sentence is enough.",
                key="prep_note",
            )
            st.button("Send to Dr. Chen", key="share_prep")

        # ----- Your Story -----
        with st.expander("Your Story · yours, portable", expanded=False):
            st.caption(
                "The version of you Klarity carries between therapists. "
                "You own it — edit, hide, or take it with you anytime."
            )
            st.markdown("- *Started therapy because work was eating Saturdays.*")
            st.markdown(
                "- *An anchor that's landed: \"I'm allowed to celebrate my wins.\"*"
            )
            st.markdown("- *Working on: saying no without writing an essay first.*")
            cc = st.columns(3)
            with cc[0]:
                st.button("Edit", key="story_edit")
            with cc[1]:
                st.button("Export", key="story_export")
            with cc[2]:
                st.button("Share with a new therapist", key="story_share")


# -------------------- DEMO CONTROL --------------------
def demo_control():
    render_story_banner()

    st.title("Demo Control")
    st.markdown(
        "**New here?** Click **▶ Play full demo** below, then flip to **Therapist** "
        "and **Patient** in the sidebar to see the story unfold."
    )

    with st.expander("What is Klarity? (for judges landing cold)", expanded=False):
        st.markdown(
            "**Klarity is the AI continuity layer for mental health practices.** "
            "It captures the patient's own words from each session, reinforces them between "
            "sessions, and briefs the therapist before the next one — so patients stop dropping "
            "and therapists stop starting from scratch. **Not the therapist. The continuity.**"
        )

    cc = st.columns([1, 1])
    with cc[0]:
        if st.button("▶  Play full demo (auto)", type="primary", use_container_width=True):
            for k in DEMO_FLAGS:
                st.session_state[k] = True
            st.rerun()
    with cc[1]:
        if st.button("↺  Reset demo", use_container_width=True):
            for k in DEMO_FLAGS:
                st.session_state[k] = False
            st.rerun()

    if all(st.session_state[k] for k in DEMO_FLAGS):
        st.success(
            "Full demo played. Open **Therapist** in the sidebar to read the brief, "
            "pattern alert, and approved takeaway — then **Patient** to see the anchor."
        )

    st.markdown("---")
    st.markdown("#### Or step through it, beat by beat")
    st.caption("Each step unlocks the next. After each one, follow the green callout.")

    steps = [
        (
            "1 ▶ End Session 4 (Scribe runs)",
            "session_4_ended",
            "Step 1 done. → Click **Therapist** in the sidebar — 3 takeaway candidates are waiting.",
            "Triggers Scribe Agent. The therapist will see 3 takeaways in the patient's own words.",
            None,
        ),
        (
            "2 ▶ Therapist approves the anchor",
            "takeaway_approved",
            "Step 2 done. Anchor queued for Tuesday 7am. → Run step 3 to deliver it.",
            "Simulates Dr. Chen tapping Approve on \"I'm allowed to celebrate my wins.\"",
            "session_4_ended",
        ),
        (
            "3 ▶ Tuesday morning — deliver the anchor",
            "anchor_delivered",
            "Step 3 done. → Click **Patient** in the sidebar — the anchor card is live.",
            "The patient wakes up to their own sentence on their phone.",
            "takeaway_approved",
        ),
        (
            "4 ▶ Friday — Pattern Agent fires",
            "pattern_alert_fired",
            "Step 4 done. → Click **Therapist** — the circling alert is now visible.",
            "Pattern Agent flags that work boundaries have come up 4 weeks running.",
            None,
        ),
        (
            "5 ▶ Monday — Session 5 Brief drops",
            "brief_generated",
            "Step 5 done. → Click **Therapist** — the pre-session brief is at the top.",
            "Brief Agent hands Dr. Chen one paragraph for Tuesday's 2pm session.",
            "anchor_delivered",
        ),
    ]

    for label, flag, status_msg, hint, dep in steps:
        with st.container(border=True):
            cols = st.columns([3, 4])
            with cols[0]:
                disabled = (dep is not None and not st.session_state[dep]) or st.session_state[flag]
                if st.button(label, disabled=disabled, key=f"btn_{flag}"):
                    st.session_state[flag] = True
                    st.rerun()
                if dep is not None and not st.session_state[dep] and not st.session_state[flag]:
                    st.caption("_Locked — finish the previous step first._")
            with cols[1]:
                if st.session_state[flag]:
                    st.success(status_msg)
                else:
                    st.caption(hint)

    st.markdown("---")
    st.caption(
        "Recording tip: keep Therapist open in one tab, Patient in another, drive everything from here."
    )


# -------------------- ROUTER --------------------
if view == "Therapist":
    therapist_view()
elif view == "Patient":
    patient_view()
else:
    demo_control()
