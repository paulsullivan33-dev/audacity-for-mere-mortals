# The Moving Parts

What each piece of Audacity holds, and
what breaks when it is misunderstood.
Names here are used everywhere later.

## The project window

One window holds one project. Its
landscape, top to bottom (measured off
the lab's first launch, transcript
t01):

- **Menus** — File, Edit, Select, View,
  Transport, Tracks, Generate, Effect,
  Analyze, Tools, Help. Nearly
  everything lives here, including
  things with no button.
- **Transport toolbar** — pause, play,
  stop, skip to start/end, record. The
  buttons a tape recorder would have.
- **Meters** — two bar graphs, playback
  and recording levels, drawn in
  decibels from −48 up to 0. They are
  how you know whether sound is too
  quiet or clipping (chapter 5).
- **The timeline ruler** — seconds
  across the top; click to place the
  cursor, drag to select.
- **Tracks** — the stacked rows below,
  each with its own control panel.
- **Selection toolbar** — the selection
  start and end as numbers, for when a
  mouse is too coarse. Chapter 10's
  scripting selects this precisely.

## Tracks and their controls

Each track's panel (left edge) holds:

- The track **name** and a menu (rename,
  move the track up/down, change how
  its waveform is drawn).
- **Mute** and **Solo** — silence this
  track, or hear only this one. The
  fastest way to find which track a
  noise lives on.
- **Gain** (left/right sliders in the
  panel: overall loudness of the track)
  and **Pan** (where it sits between
  left and right speakers).
- Under the name: the facts — "Mono,
  44100 Hz, 32-bit float", as the lab's
  imported track announced itself. The
  **sample rate** (how many snapshots
  of the sound per second) and **sample
  format** (how exact each snapshot is)
  are set per track; the project's rate
  (bottom corner) governs exports.

## Clips

A **clip** is one continuous stretch of
audio on a track. Import a file: one
clip. Record twice on the same track:
two clips. Cut a piece out of the
middle: the clip becomes two. Clips can
be dragged in time, trimmed at their
edges by dragging the edge, split at
the cursor, and joined back. Silence
between clips is real silence, not
missing data.

The waveform inside a clip can be drawn
two ways: the ordinary **waveform**
(loudness over time) and the
**spectrogram** (frequencies over time,
pitch drawn as height, loudness as
brightness). The spectrogram is the
clean-up chapter's best friend: hiss,
hum and room ring all have visible
shapes (chapter 8).

## The selection

Most commands act on **the selection**
— a stretch of time, on one or more
tracks. No selection usually means "the
clip under the cursor" or nothing at
all, and an effect that "did nothing"
usually means the selection wasn't
where you thought. Chapter 10's lab
work starts every effect with an
explicit SelectTime or SelectAll for
exactly this reason.

Three relatives of the selection:

- The **cursor** — a position with no
  length; where playback starts and
  where splits happen.
- **Labels** — named markers attached
  to a point or a stretch, on their own
  label track. They survive exports as
  a plan: chapter 9 exports one file
  per label.
- **Envelopes** — a line drawn on a
  clip that bends its volume up and
  down over time: fade a laugh under a
  sentence without cutting anything
  (chapter 6).

## Effects, two ways

- **Applied effects** (the Effect
  menu): pick a selection, run the
  effect, the audio itself is
  rewritten. Undo can take it back; a
  saved-and-closed project cannot.
  Normalize, Noise Reduction and most
  of the classics live here.
- **The effect stack** (the "Effects"
  button on a track's panel): effects
  that run live during playback, in
  order, adjustable and removable at
  any time, applied to the whole track.
  Reverb and EQ while you experiment
  belong here; the final export still
  bakes them in.

Under the hood both kinds are the same
effect code; what differs is when it
runs and whether the original samples
survive.

## Files Audacity reads and writes

| Thing | What it is |
|---|---|
| `.aup3` | The project. One SQLite database: project document + audio in blocks (chapter 11, transcript t06) |
| WAV, AIFF | Uncompressed audio. The safe working and archive formats |
| MP3, OGG, Opus | Compressed exports for publishing; small, lossy |
| FLAC | Compressed but lossless; half the size of WAV, every bit kept |
| `.au` folders | The pre-3.0 project shape (a small file plus a data folder). Audacity 3 opens and converts them |
| Macro `.txt` | Plain-text command chains in the Macros folder (chapter 10) |

Importing is generous — dozens of
formats, including video files (their
soundtrack is taken, via ffmpeg when
installed) — but a project is the only
thing that keeps tracks separate.

## The parts that aren't the window

- **Preferences** — one dialog of
  settings; stored per user in
  `audacity.cfg` (chapter 3 shows the
  file earning its keep).
- **Modules** — optional pieces loaded
  at startup, listed in Preferences >
  Modules. Most are file-format
  handlers. One of them, mod-script-pipe,
  is chapter 10's door into the program.
- **Nyquist** — a programming language
  for audio, built in: many bundled
  effects are written in it, and you can
  write your own (chapter 10).
- **The temp folder** — where an unsaved
  project's audio lives while you work.
  Chapter 11's recovery story starts
  here.
