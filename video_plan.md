# Video Plan — Throughline 2-min Demo

## 1. The 2-minute script (final, locked)

| Time | VISUAL | VOICE |
|---|---|---|
| 0:00 | Patient anchor card fullscreen: *"I'm allowed to celebrate my wins."* — hold, silent, 3 beats | *(silence)* |
| 0:08 | Same card | "I'm allowed to celebrate my wins. A patient said that out loud for the first time in their life, in session four. Seventy percent of patients like them never make it to session five. This is the AI that changes that." |
| 0:25 | Demo Control screen, banner reading "Before we start — Patient #247 almost dropped after Session 4" | "Klarity runs three thousand mental health practices. Forty thousand visits a month. Drop-off after session three costs the network roughly fifty million a year. Not because therapy fails — because nobody holds the patient's story between sessions." |
| 0:42 | Click "▶ Play full demo (auto)" — banner advances | "Every AI in mental health is pointed at the therapist's note. We point it at the patient's sentence." |
| 0:50 | Switch sidebar to **Therapist** view — scroll to "From your last session" | "End of session four. The Scribe Agent pulls three takeaways in the patient's own words, not a generic summary. Dr. Chen reviewed them and approved this one." |
| 1:05 | Switch sidebar to **Patient** view — anchor card visible | "Tuesday morning. The patient opens the app. There's their own sentence, waiting for them. No sticky note. No phone wallpaper. The thing that mattered, reflected back." |
| 1:20 | Back to **Therapist** view — scroll to "Patterns we've noticed" expander | "Friday. The Pattern Agent flags Dr. Chen — work boundaries, four of the last five sessions. Time to consider a different approach." |
| 1:32 | Scroll up to "Today's brief" card | "Monday morning. One paragraph distilled from the patient's whole week. Dr. Chen walks into session five ready, instead of starting from 'so how are you doing?'" |
| 1:45 | Hold on Therapist view — engagement metrics visible (Drop-off risk: Moderate ↓ from High) | "Patients stay longer. Therapists walk in prepared. Five of your six partner-deck metrics move." |
| 1:54 | Cut back to anchor card | "We're not the therapist. We're the continuity. Victor — partner with us at Klarity." |
| 2:00 | End | |

## 2. The shot list

| # | App view | Demo state buttons | What's visible |
|---|---|---|---|
| 1 | Patient (pre-loaded with all flags ON) | — | Anchor card "I'm allowed to celebrate my wins" fullscreen-ish, centered |
| 2 | Demo Control (after reset) | None yet | Story banner "Patient #247 almost dropped after Session 4", title, Play button |
| 3 | Demo Control | Click **▶ Play full demo (auto)** | All 5 pills flip to ✓ in sidebar; success callout appears |
| 4 | Therapist | (all flags ON) | Scroll to "From your last session" — green success: anchor approved |
| 5 | Patient | (all flags ON) | Anchor card live, "Your morning · May 12", three response buttons |
| 6 | Therapist | (all flags ON) | "Patterns we've noticed" expander open — circling on work boundaries, 4 of 5 |
| 7 | Therapist | (all flags ON) | "Today's brief" card at top — one paragraph for Session 5 |
| 8 | Therapist | (all flags ON) | "Engagement at a glance" — Drop-off risk Moderate ↓ from High |
| 9 | Patient | (all flags ON) | Anchor card again, hold for closing line |

**Pre-flight:** open the deployed URL in two browser tabs — Tab A on Patient view (flags ON, for shot 1), Tab B on Demo Control (flags reset, for shots 2–3). Use Tab B's sidebar to switch views from shot 4 onward.

## 3. Recording setup

- **Loom** (free, browser-based): face cam ON in bottom corner, 1080p, MP4 export. Browser-tab capture only. Install the Chrome extension at loom.com.
- **Mac QuickTime** as backup — File → New Screen Recording, AirPods built-in mic selected.
- **Browser:** fresh Chrome window, no other tabs, 110% zoom (Cmd+ once), bookmarks bar hidden, only the Streamlit URL.
- **Mic:** AirPods built-in. Quiet room. Phone face-down, on Do Not Disturb.
- **One dry run** before recording — full pass start to finish, no stopping, even if you fumble. Then record for real.

## 4. Do-not-screw-this-up checklist

1. Tab A: Patient view, **all 5 demo flags already ON** (click ▶ Play full demo, then switch to Patient).
2. Tab B: Demo Control, **all flags RESET** — this is the tab you record from.
3. Sidebar wide enough that "View" radio + state pills are readable.
4. Mute Slack, Mail, Calendar, iMessage. macOS Focus → Do Not Disturb.
5. Browser zoom at 110% — anchor card should fill the centered column without scrolling.
6. Open the live URL `klarity-continuity-epq7zblk7m7pd2scofxptz.streamlit.app`, not localhost.
7. Confirm the app loaded the Lora + Inter fonts (titles should be serif). Hard-refresh if not.
8. First 8 seconds: hold silent on the anchor card. Resist the urge to start talking early.
9. Click **▶ Play full demo (auto)** *once* — don't step through the 5 numbered buttons during recording.
10. End on the anchor card, not on a metric — the wedge line lands on the patient's sentence.

## 5. Submission

- Loom URL → submit at the hackathon submission form (Klarity Health AI Challenge intake link from the kickoff email).
- Also paste the live app URL: `klarity-continuity-epq7zblk7m7pd2scofxptz.streamlit.app`
- **MP4 backup:** export from Loom (Download → MP4, 1080p), save to `~/Desktop/throughline-demo.mp4`. Drop in a Google Drive folder shared to Victor in case Loom is blocked.
