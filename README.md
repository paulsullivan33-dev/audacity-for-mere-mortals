# Audacity for Mere Mortals

Sound, once recorded, used to be
physical: tape you cut with a razor,
discs you could not un-press.
**Audacity** is the free program that
made sound ordinary to edit on an
ordinary computer. You see the sound as
a picture — a waveform — you select
parts of it the way you select words in
a document, and you cut, copy, quieten,
clean and rearrange it. Underneath, it
is a multitrack editor: several
recordings can sit on parallel tracks,
play together, and be mixed down to one
finished file. It runs on Windows,
macOS and Linux, it costs nothing, and
it has been the default answer to "how
do I fix this recording?" for over two
decades.

This guide explains how Audacity thinks
— projects, tracks, clips, selections,
effects — then walks the work people
actually do with it: a first edit,
recording, cleaning up a noisy or
hissy recording, effects, exporting a
finished file, saving projects safely,
and automating the repetitive parts
with macros and scripting. The limits
are stated plainly, including the ones
the lab ran into.

The lab behind this guide ran the real
thing: **Audacity 3.4.2**, Ubuntu
24.04's packaged build, installed with
apt onto a small Linux machine with no
sound hardware and no display. The
program was given a virtual display and
a silent "null" sound device, and then
driven two ways: at its window, and
through its own scripting pipe — a
channel that lets another program type
commands into it. Along that pipe went
real work: audio files the lab
generated (pure tones and noise, made
with SoX, so every result could be
measured exactly), an import, a
normalize whose output peak was then
measured — 0.100 in, 0.891 out, which
is −1 dB as ordered — a noise reduction
that halved the level of a noise-only
passage while touching the tone
carrying it far less, exports to WAV
and MP3, and a project saved, taken
apart (an `.aup3` is a SQLite database;
the lab listed its tables) and
reopened. The measurements are in the
transcripts and quoted in the chapters.

What the lab could not do, it did not
fake. There was no microphone and no
real sound device, so **recording** is
taught from the documentation and
labelled as such. **Macros** turned
out to be a hard boundary: their files
are plain text and the lab wrote one,
but this build's scripting catalogue
contains no command that runs one —
macros start from the window. And
point-at-it editing — dragging clips
with a mouse, riding faders by ear —
is described, not demonstrated, because
the lab's hands were a keyboard and a
pipe. `criteria.md` keeps the full
ledger of what was run and what was
only read.

## What this guide covers

- [**What Audacity is**](what-audacity-is.md) —
  the mental model: sound as something
  you can see and select, projects
  versus finished files, and what
  Audacity is not (a music studio, a
  live broadcast desk)
- [**The moving parts**](the-moving-parts.md) —
  tracks, clips, the timeline, the
  selection, effects and the effect
  stack, envelopes and labels: what
  each holds, and what breaks when
  each is misunderstood
- [**Installing Audacity**](installing-audacity.md) —
  the official installers and the
  package install, the first-run
  dialog, sound devices, and the
  sandbox the lab actually used, told
  in full
- [**Your first edit**](your-first-edit.md) —
  import a file, play it, select,
  cut, trim, undo: the five moves
  every other chapter assumes
- [**Recording**](recording.md) —
  choosing a microphone, setting
  levels, monitoring, overdubs —
  documented only in this guide, and
  labelled where it matters
- [**Tracks and clips**](tracks-and-clips.md) —
  splitting and joining, moving clips,
  fades, the envelope tool, and labels
  for chapters and sections
- [**Effects and the effect
  stack**](effects-and-the-effect-stack.md) —
  the two ways effects apply (for real,
  on a copy of the sound — or live, in
  the stack), and a tour of the
  built-ins that matter
- [**Cleaning up
  audio**](cleaning-up-audio.md) —
  noise reduction's two steps, the
  noise gate, click removal, trimming
  silence, and loudness: with the
  lab's measured numbers
- [**Exporting**](exporting.md) —
  WAV, MP3 and friends; exporting a
  mix versus exporting pieces by
  label; and why the export is not
  the project
- [**Macros and
  scripting**](macros-and-scripting.md) —
  chains of effects you can re-run,
  the scripting pipe the lab drove,
  and Nyquist, the built-in language
  for new effects
- [**Projects and
  backup**](projects-and-backup.md) —
  the `.aup3` file taken apart,
  autosave and recovery, Save Copy,
  and moving a project between
  machines
- [**Recipes**](recipes.md) — a podcast
  episode cleaned start to finish, a
  meeting recording made listenable, a
  long recording split into chapters,
  and a batch of files normalized the
  same way
- [**The neighbours**](the-neighbours.md) —
  OBS Studio, Ardour, Reaper, Tenacity,
  Ocenaudio, and the SoX/ffmpeg
  command line: what each one trades
- [**Limits**](limits.md) — no MIDI
  composition, no second chances in a
  flattened file, noise reduction's
  real limits, stated plainly
- [**Troubleshooting**](troubleshooting.md) —
  "error opening sound device", the
  flat silent line, exports that come
  out wrong, and the scripting trap
  this guide's lab fell into so you
  don't have to
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Making music. Audacity records and
edits audio that already exists; it
has no instruments, no MIDI sequencing
worth the name, and no score. Studios
that do those things are chapter 13's
neighbours, and they are different
books. Live streaming and live sound
reinforcement are likewise pointed at,
not taught — Audacity's effects are
mostly applied to finished recordings,
and it is not a broadcast desk.
Forensic audio work (authenticating
recordings, enhancing speech for
evidence) gets a warning about
expectations, not a tutorial.

## How to use this guide

Read chapter 1 for the model and
chapter 2 before opening the program —
knowing the difference between a
project and a file, and between a
track and a clip, turns later
confusion into a named problem.
Chapter 4 is the hands-on start: the
five moves. Chapter 8 (cleaning up) is
the one most people came for; it
assumes chapter 4. Chapter 11 is the
other one not to skip — save and back
up a project while it is small enough
that a rehearsal costs minutes. The
lab's transcripts live in
`audacity-lab/transcripts/`; its notes
are `examples/lab-notes.txt`.
