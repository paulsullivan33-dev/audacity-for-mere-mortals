# Limits

What Audacity cannot do, stated
plainly.

## It edits audio; it does not make music

There is no MIDI sequencing worth
planning around, no software
instruments, no notation. Audacity can
record a performed instrument and edit
the recording — that is its whole
musical scope. Composition belongs to
the neighbours (chapter 13).

## An export cannot be un-mixed

Everything a project held separately —
tracks, clips, labels, envelopes — is
one stream of samples in the export.
Tools elsewhere promise to separate a
mixed file back into stems; treat the
promises as weather forecasts. The
practical defence is this guide's
boring one: keep the project
(chapter 11).

## Undo is one session deep

History ends when the project closes,
and applied effects (chapter 7) are
rewrites. Between Save Copy and the
trash, there is no third place to
stand. A workflow that needs revision
after delivery — a client who changes
their mind next month — needs Save
Copies kept like versions, because
Audacity will not reconstruct them.

## Noise reduction is not resurrection

Chapter 8's measured optimism has
edges:

- It works on *steady* noise against a
  *learned profile*. Unsteady noise —
  traffic, crowds, weather — yields
  unsteady results.
- It trims the wanted sound along with
  the unwanted: the lab's own table
  shows the tone's passage losing a
  third of its level while the noise-
  only passage lost half.
- It cannot fix echo, distance, or
  clipping. Those are recording
  problems wearing clean-up clothes.

## The stack and the sample

The live effect stack (chapter 7)
processes per track, in order, and its
plugins are third-party citizens:
a stack that names an effect your
collaborator's machine lacks renders
differently there. Applied effects do
not have this problem — they also do
not have an undo. Pick per project
which risk you prefer.

## One machine, one pair of hands

Audacity is a single-user desktop
program. There is no shared project
editing, no server form, no headless
mode: the lab drove it through a
virtual display and its scripting pipe
precisely because the program insists
on being a window (chapter 3,
`criteria.md`). Automation rides on
the pipe and macros, within the
boundary chapter 10 measured — macros
cannot even be started from the pipe
in this version.

## What this guide could not test

Restated from `criteria.md`, because a
limits chapter is where it belongs:
the lab had no microphone, no speakers
and no display, so recording (chapter
5) is documented only; by-ear judgements
— how a compressor setting *sounds* —
are described from the documentation
and standard practice, not from lab
listening; and running a macro from the
window (chapter 10) is documented for
the same reason macros could not be
run at all from the lab's pipe. What
was run for real — install, GUI,
import, normalize (twice, measured),
noise reduction (measured), WAV and
MP3 export, project save/inspect/
reopen — is the load-bearing core, and
your machine, which almost certainly
has ears' worth of hardware, allows
all of the blocked list.
