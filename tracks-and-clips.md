# Tracks and Clips

Chapter 4 edited inside one clip. Real
projects are carpentry between clips:
moving pieces in time, joining them,
shaping their edges. This chapter is
that carpentry.

## Splitting and joining

- **Split** (Ctrl+I): the clip divides
  at the cursor, or at both edges of
  the selection. Nothing moves; you now
  own the pieces separately.
- **Split Delete**: the selection is
  removed but the gap *stays* — the
  neighbours do not slide. (Plain
  Delete slides them; chapter 4's
  distinction again, at clip scale.)
- **Join** (Ctrl+J): selected adjacent
  clips become one again. Joining does
  not heal edits inside the audio; it
  only removes the seam.

The common pattern — isolate a phrase,
nudge it, treat it differently — is:
split, split, work on the middle piece,
join only if you're sure.

## Moving things in time

- The **Time Shift tool** (the ↔ toolbar
  icon, F5) drags a whole clip left or
  right along its track, and — in
  Audacity 3 — a clip can be dragged to
  another track of the same kind.
- Select a stretch and **Cut/Paste** to
  move audio between tracks or projects
  (two project windows can be open; the
  clipboard carries real audio).
- **Tracks > Align Tracks** lines clips
  up: by start, by end, or end-to-end —
  the interview whose answers must sit
  exactly under their questions.

Tracks themselves reorder by dragging
their panels, duplicate (Ctrl+D makes a
copy of the selected track's selection,
ready for an effect A/B), and mix:
**Tracks > Mix > Mix and Render** bakes
selected tracks into one — permanent,
so Save Copy first (chapter 11).

## Edges: fades and crossfades

Raw clip edges click: a waveform cut
mid-cycle starts at a non-zero value and
the speaker snaps. The fixes are tiny
and non-negotiable:

- **Fade In / Fade Out** (Effect menu):
  a straight-line ramp over the
  selection. Two or three milliseconds
  at every edit point is inaudible and
  removes the click; whole seconds make
  the classic podcast swell.
- **Crossfade** (Effect > Crossfade
  Clips / Crossfade Tracks): one clip
  fades out as the next fades in — the
  join between two takes of the same
  sentence.
- **Studio Fade Out** and **Adjustable
  Fade** are the shaped variants, for
  music beds and endings.

## The envelope: volume as a drawn line

The **Envelope tool** (the icon like a
line with dots, F6) puts a volume line
on each clip. Click to add a point, drag
it down, and the clip quiets *there* —
dip the music under the first word,
tame one explosive laugh, lower the
sentence where the truck passed. The
audio samples are untouched; the line
rides along when the clip moves, and
exports honour it. Most "editing" of
speech at mortal scale is envelopes,
not effects.

## Labels: naming time

A **label track** (Tracks > Add New >
Label Track) holds markers: click in it
at a position and type. Labels name
points ("question 3") or stretches
(select, then Ctrl+B, and the label
takes the selection's span).

Labels are cheap; their uses are not:

- **Navigation** in a two-hour
  recording: labels survive saving, and
  the label list is a table of
  contents.
- **Chapter exports**: chapter 9
  exports one file per label.
- **Analysis anchors**: chapter 8's
  noise work is easier when "the noisy
  part" is a labelled fact, not a
  memory.

## Grouping, gently

Clips on different tracks that must move
together (voice and its music dip) can
be **synced** by selecting across tracks
before moving, or simply by aligning
their starts and using Align Tracks
after any slip. Audacity's grouping is
lightweight next to a DAW's; for the
speech-scale work this guide covers,
alignment plus care is the whole story.
