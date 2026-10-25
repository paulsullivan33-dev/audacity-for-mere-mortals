# Writing Criteria

Every guide in this repo is written to the same
standard. If you're adding or editing a guide —
human or AI — hold it to these.

1. **Plain words, real ideas.** Simple language,
   never dumbed-down concepts. Explain jargon on
   first use; collect terms in the glossary.
2. **No hype.** No marketing adjectives, no
   "revolutionary," no promises about what
   something will do for the reader.
3. **Honest about limits.** Say what the thing
   *can't* do. State uncertainty instead of
   smoothing it over. Validation notes include
   what remains unverified.
4. **No invented numbers.** Benchmarks, defaults,
   and specs are either measured or qualified with
   "depends on your setup." If it wasn't tested,
   say so.
5. **Checkable.** Commands are meant to be run,
   with "Check:" blocks showing what success looks
   like. Sources are linked, not asserted.
6. **Respect the reader's setup.** Call out
   Windows/Mac/Linux differences. Don't assume a
   GPU, a budget, or prior experience.
7. **Safety isn't skipped.** Real risks get
   stated plainly, not buried.
8. **Scoped.** Each guide says what it covers and
   points elsewhere for the rest. No guide
   pretends to be the whole subject.
9. **Structure over prose.** Tables, before/after
   examples, symptom → fix. Scannable beats essay.

## Verification notes for this guide

Built and verified 2026-10-24/25 against
**Audacity 3.4.2** (Ubuntu package
3.4.2+dfsg-1build4), on a 2-CPU,
7.9 GB sandbox machine running
Ubuntu 24.04.

**The ceiling, stated plainly:** the
bench had no microphone, no speakers
and no display. Audacity ran on a
virtual display (Xvfb) with a software
"null" device as its sound device.
Everything the program exposes without
ears — install, the window itself,
import, effects, exports, the project
file, the scripting pipe — was executed
and measured for real. What needs
ears or real hardware — recording, and
every judgement of the form "this
sounds better" — could not be, and is
documented only, as labelled below.
The transcripts are the evidence:
`audacity-lab/transcripts/`, t00–t06.

**Primary sources read, not
remembered** — and used against
memory twice: the build's own command
catalogue, obtained from the running
program (`GetInfo: Type=Commands`,
transcript t02), gave the scripting
command list and the true parameter
names for Normalize, Noise Reduction,
Export2 and Save Project2. A first
scripted normalize used parameter
names from memory, was silently run on
defaults by the program, and was
repeated with the catalogue's names
(transcript t03). The Audacity manual
(Documentation for 3.4) backs the
chapters on recording, macros and
export formats.

**Ran for real:**

- t00 — `apt install audacity`
  (exit 0); version 3.4.2+dfsg-1build4
  from the package and from the
  program's own first-run dialog
  (`audacity --version` in this build
  initialises and exits silently; no
  claim rests on its output). Test
  audio generated with sox and
  measured: a 440 Hz tone, 3 s, peak
  0.100002 / RMS 0.070711; a 5 s file
  of 1.5 s white noise + 3.5 s of
  tone-with-noise, peak 0.255067 /
  RMS 0.075139.
- t01 — full GUI launch under Xvfb:
  the first-run "How to get help"
  dialog (dismissed by synthetic
  keypress), then the complete main
  window, screenshotted; chapter 2's
  anatomy is that window.
- t02 — mod-script-pipe enabled via
  `audacity.cfg`. First attempt
  failed: a stale `mod-script-pipe=4`
  line later in the same section
  outvoted the added `=1`, and no
  pipes appeared. With exactly one
  line, both pipes opened
  (`/tmp/audacity_script_pipe.to.0`,
  `.from.0`) and answered. The
  catalogue query returned **93
  commands** with parameters and
  defaults; Noise Reduction has no
  parameters at all.
- t03 — through the pipe: Import2 of
  the tone, SelectAll, Normalize,
  Export2 to WAV and to MP3. WAV peak
  measured 0.100002 → **0.891418**
  (−1 dB); MP3 confirmed by ffprobe
  (format mp3, 3.000 s). Repeated
  normalize with the catalogue's
  parameter names at PeakLevel −3 dB:
  peak **0.708069** against 0.707946
  expected.
- t04 — noise reduction's two steps
  through the pipe: NoiseReduction on
  the noise-only selection (profile),
  SelectAll, NoiseReduction again
  (apply), Export2. Measured before/
  after: noise-only RMS **0.021443 →
  0.010758**; tone+noise RMS
  **0.088704 → 0.061805**.
- t05 — a macro file written to the
  real Macros folder
  (`~/.local/share/audacity/Macros/
  LabPrep.txt`, kept in
  `audacity-lab/macros/`). Running it
  through the pipe failed:
  `ApplyMacro` is "not recognized",
  and the 93-command catalogue
  contains no macro command. Macros
  in 3.4.2 start from the window.
- t06 — SaveProject2 through the pipe
  wrote `lab-project.aup3`; read back
  with SQLite (on a copy; the live
  project locks its database): tables
  `autosave`, `project` (one row,
  1,608-byte document), `sampleblocks`
  (5 rows). On quit the file compacted
  3,604,480 → 557,056 bytes.
  Relaunched, reopened via
  OpenProject2, and `GetInfo:
  Type=Tracks` returned the track by
  name ("quiet-tone", wave, 0–3 s,
  1 channel).

**Errors hit and diagnosed for real,**
written up in chapter 15: the duplicate
config key that disabled the scripting
module; the scripted effect that
accepted wrong parameter names and ran
on defaults (found by measurement,
not by the program); and the modal
dialog raised by a malformed scripted
command, which blocks the pipe until
dismissed.

**Documented only, and labelled as
such in the chapters:** recording in
full (chapter 5 — no microphone, and
the null device cannot stand in for
one); sound quality by ear — every
clean-up claim in chapter 8 rests on
the t04 measurements and on documented
behaviour, not on listening; running a
macro from the window and batch
processing with it (chapter 10 — the
file and its placement are verified;
the run is the GUI's, and the pipe
proved it cannot be started from a
script in this version); mouse-driven
clip editing as a *demonstrated* act
(chapter 6 — the tools are real, the
lab's hands were keystrokes and pipe
commands); third-party plug-ins and
the effect stack in use; Windows- and
macOS-specific installation details
(chapter 3), described from the
project's documentation.

**Fixtures:** every sound in the lab
was generated — two sine tones and
white noise, composed with sox, chosen
so results could be measured to four
decimal places. The people in the
recipes (a podcaster, a meeting chair,
an oral-history interviewer) are
invented for the guide. Nothing in
the lab is modelled on any real
person, organisation or event.
