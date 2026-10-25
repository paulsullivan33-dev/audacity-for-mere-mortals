# What Audacity Is

The mental model first; buttons later.

## Sound you can see

Audacity's founding idea is that a
recording should be *visible*. A sound
is drawn as a **waveform** — a graph of
loudness over time, loud parts tall,
quiet parts flat — and once sound has a
picture, editing it feels like editing
text. You drag across a stretch of the
waveform to select it, the way you drag
across words. Then the ordinary verbs
apply: cut, copy, paste, delete. And
the audio verbs apply: make it louder,
make it fade, remove the hiss.

Nothing about the model needs a studio.
The readers this guide assumes have a
recording that needs fixing — a podcast
episode, a meeting, an interview, a
tape they digitised — and a computer.

## A project is not a file

The single most useful distinction in
Audacity:

- A **project** (saved as one `.aup3`
  file) is your workbench: every track,
  every clip in its place, your edits
  waiting to be changed again. It is
  Audacity's private format. Nothing
  else plays it.
- An **export** is a finished audio
  file — WAV, MP3, OGG, FLAC — that any
  player, phone or website understands.
  Exporting *mixes everything down* to
  one stream of sound. The workbench
  does not come along.

Closing a project does not export it;
exporting does not save the project.
Losing work in Audacity almost always
means confusing these two (chapters 9
and 11). Studio people would say:
the project is the recipe and the
ingredients; the export is one cooked
meal. You cannot un-cook a meal back
into ingredients, and an MP3 cannot be
un-mixed back into tracks.

## Tracks, stacked in time

A project holds **tracks** — parallel
recordings that play at the same time.
One track might be a voice, another a
music bed under it, a third the
interviewee on the other channel. Each
track holds **clips**: stretches of
audio that can be moved, trimmed and
split without touching their neighbours
(chapter 6). Playback mixes the tracks
together; the export mixes them for
keeps.

Editing in Audacity is mostly
**non-destructive at the project
level**: cutting a clip removes it
from the timeline, but until you close
the project, Undo remembers. Effects
come in two kinds — ones that rewrite
the selected audio (destructive, one
Undo deep) and a per-track **effect
stack** that processes live on playback
and can be adjusted or removed at any
time (chapter 7). The distinction
matters and is worth learning early.

## What Audacity is not

- **Not a music studio (DAW).** It has
  no software instruments, no piano
  roll, no MIDI sequencing to speak of.
  It edits audio; it does not compose.
  Ardour and Reaper (chapter 13) live
  in that world.
- **Not a live tool.** Effects largely
  apply to recordings, after the fact.
  For live streaming and live mixing,
  OBS Studio and real mixers are the
  neighbours (chapter 13).
- **Not a restorer of the dead.**
  Noise reduction, click removal and
  equalisation (chapter 8) can improve
  a damaged recording, sometimes a lot.
  They cannot recover sound that was
  never captured — words drowned under
  a louder noise at the moment of
  recording are gone, not hidden.
- **Not destructive by accident.**
  Audacity never rewrites the audio
  file you imported. Importing copies
  the sound into the project; your
  original stays as it was. The risk
  runs the other way: forgetting the
  project is the only place your edited
  work exists until you export.

## Why it is everywhere

Audacity is free, open source, and runs
on Windows, macOS and Linux with the
same project format on all three. It
asks little of the machine — the lab
for this guide ran it, under a virtual
display, on 2 CPUs — and nothing of
your wallet. Its age shows in places:
the interface is dense, and some
workflows (chapter 10's macros) carry
their history with them. But for the
job "record or open sound, fix it,
export it", it remains the tool a
mortal can learn in an afternoon and
use for years.
