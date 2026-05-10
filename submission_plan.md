# Throughline — Submission Plan (Two-Part Video)

Two videos, stitched in order: **PixVerse first (problem + framing, ~60s)**, then **Loom (product demo, ~60s)**. Total runtime ~2 minutes.

---

## Part 1 — PixVerse (Problem + Framing) ~60s

The cinematic, emotional opening. NO product UI. Just the human story and the thesis.

### Scene-by-scene

**Scene A — 0:00–0:08 (8s)** *[silent]*
**Visual:** Slow push-in on a single handwritten line — *"I'm allowed to celebrate my wins"* — pencil on cream paper, soft window light, faint dust motes. Shallow focus, warm grain. No people.
**VO:** *(silence — let it land)*

**Scene B — 0:08–0:18 (10s)**
**Visual:** A person in their 30s in a sunlit kitchen at dawn, exhale visible, shoulders dropping. Static medium shot, natural light, no UI on screen.
**VO:** "I'm allowed to celebrate my wins. A patient said that out loud for the first time in their life, in session four. Seventy percent of patients like them never make it to session five."

**Scene C — 0:18–0:28 (10s)**
**Visual:** Overhead of empty therapy chairs in golden afternoon light, one cushion still indented. Slow dolly. No clinical signage, no logos.
**VO:** "Drop-off after session three costs Klarity's network roughly fifty million dollars a year. Not because therapy fails — because nothing holds the patient's story between sessions."

**Scene D — 0:28–0:38 (10s)**
**Visual:** Three quick cuts (3s each): hands re-telling the same story to a new face / a phone with "How are you doing?" texted at the top / a calendar with "Session 5" being deleted.
**VO:** "Patients re-tell their story. Therapists start cold from 'so how are you doing?' Treatment drifts. Then they drop."

**Scene E — 0:38–0:48 (10s)**
**Visual:** Macro of a finger underlining a single typewritten sentence on a cream page; other lines softly out of focus. Sage-green desk surface at edges.
**VO:** "Every AI in mental health is pointed at the therapist's note. We point it at the patient's sentence."

**Scene F — 0:48–0:58 (10s)**
**Visual:** Return to the handwritten line on cream paper, now with the word **THROUGHLINE** appearing softly in serif beneath it. Slow pull-back.
**VO:** "This is Throughline. The AI memory layer between therapy sessions. Built on Klarity. Now let me show you how it works."

**End of Part 1 — cut directly to Loom screen recording.**

### Style prompt (paste into PixVerse for every scene)

> Cinematic, soft documentary realism in the style of Aftersun and Sofia Coppola — natural window light, 35mm grain, shallow depth of field, gentle handheld micro-movement. Color palette: warm cream, sage green, soft coral, honey gold. Quiet, intimate, contemplative pacing. Composition favors stillness and negative space; subjects partially out of frame or in soft silhouette. No music cue, no captions, no on-screen text overlays. Respectful, literary, A24 emotional register.

### Negative prompts
- No clinical settings, hospital rooms, white coats, fluorescent lighting
- No chatbot UI, glowing AI orbs, neural-network graphics, "tech" overlays
- No sad-person-on-couch, head-in-hands, crying-into-tissue tropes
- No drone city shots, server racks, stock-corporate b-roll
- No identifiable faces in close-up; keep subjects soft, partial, backs-of-heads

### PixVerse how-to
1. **PixVerse v4.5** (text-to-video, 1080p, 8-10s clips). Paste the Style Prompt first, then the Visual Prompt beneath it.
2. **Voiceover:** record yourself reading the VO into Voice Memos OR generate via ElevenLabs (voice: Charlotte or Rachel, warm/slow). Save as one continuous WAV.
3. **Stitch in CapCut:** drop scenes A–F in order, lay VO underneath, nudge cuts to land on sentence breaks. Add 8s silent black at start.

---

## Part 2 — Loom (Product Demo) ~60s

Tight, no preamble. Walk through the live app.

### The script (read while clicking)

| Beat | Click / View | VOICE |
|---|---|---|
| 1 | Demo Control, fresh load | "Patient #247 almost dropped after session four. Here's what Throughline did instead." |
| 2 | Click **▶ Play full demo (auto)** | "Three agents fire across the patient's week." |
| 3 | Switch to **Therapist** view, scroll to "From your last session" | "End of session four — the Scribe agent surfaces three takeaways in the patient's own words. Dr. Chen approves one." |
| 4 | Switch to **Patient** view (anchor card) | "Tuesday morning — the patient sees their own breakthrough on their phone. Not a generic AI summary. Their actual sentence." |
| 5 | Back to **Therapist** view, "Patterns we've noticed" | "Friday — the Pattern agent flags Dr. Chen: work boundaries, four of the last five sessions." |
| 6 | Scroll up to "Today's brief" | "Monday — the Brief agent gives Dr. Chen a one-paragraph note before session five. She walks in ready." |
| 7 | Stay on Therapist view, engagement metrics visible | "Drop-off risk: down from high to moderate. Five of six partner-deck metrics move." |
| 8 | Switch to Patient view, anchor card | "We're not the therapist. We're the continuity. Victor — partner with us at Klarity." |

**Total: ~60 seconds.** Read fast, don't pause between beats.

### Loom how-to (60-second setup)
1. **loom.com** → Sign up with Google
2. Install **Loom Chrome extension** when prompted
3. Click Loom icon in Chrome toolbar → **Screen + Cam** (or Screen only)
4. Pick **Current Tab**, mic = system default, confirm green sound bars
5. Open the live URL: `klarity-continuity-epq7zblk7m7pd2scofxptz.streamlit.app`
6. Hit **Start Recording**, read the script, stop, copy share URL

### Pre-flight checklist
- Browser zoom 110% (Cmd+ once)
- Mute Slack/Mail/iMessage (Focus → Do Not Disturb)
- Hard-refresh the live URL — confirm fonts load (titles should be serif Lora)
- Click ▶ Play full demo *once* — don't step through 5 buttons during recording
- End on the Patient anchor card

---

## Stitching the two together

1. Export PixVerse as MP4
2. Export Loom as MP4 (Download → 1080p)
3. **CapCut** (free, web): drag PixVerse first, Loom second. Add 0.5s crossfade between. Export.
4. Upload final MP4 to Loom or Google Drive. **That's the submission link.**

---

## Submission

- Final video URL → Klarity submission form
- Live app URL → `klarity-continuity-epq7zblk7m7pd2scofxptz.streamlit.app`
- Repo URL → `github.com/msaenz111/klarity-continuity`
- README → paste all three URLs at the top
