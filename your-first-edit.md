# Your First Edit

Five moves — import, play, select, cut,
undo — are 90% of Audacity. This chapter
does them once, slowly, on a harmless
file. Make the file first, so nothing
real is at risk:

```bash
sox -n -r 44100 -c 1 tone.wav \
  synth 10 sine 440 sine 880 gain -12
```

(Ten seconds of two quiet tones. No
sox? Any short recording you own will
do; the moves are the same.)

## Move 1: import

File > Import > Audio… and choose
`tone.wav` — or drag the file onto the
window. A track appears, named for the
file, with its facts under the name
("Mono, 44100 Hz, 32-bit float" in the
lab's case).

**The rule that protects you:**
importing *copies* the sound into the
project. The file on disk is never
edited, whatever you do next. Audacity
may ask, the first time, whether to copy
files into the project or read them in
place — choose **copy**. Reading in
place is faster and is how projects end
up depending on files that later move.

**Check:** the project title bar says
"Untitled" (or your save name) — not the
file's name. You are editing a project
that *contains* the sound, not the file.

## Move 2: play

Spacebar, or the green play button.
Playback starts at the cursor; the
playing head sweeps the waveform and
the playback meter moves. Spacebar
again stops. Two habits worth forming
now:

- **Shift+Space** loops the selection —
  the way to listen to one syllable
  twenty times.
- The **zoom** keys (Ctrl+1 in,
  Ctrl+3 out, Ctrl+2 normal — on macOS,
  Cmd) — editing happens zoomed in;
  finding things happens zoomed out.

## Move 3: select

Drag across the waveform: a stretch
highlights. Refine it with the numbers
in the Selection toolbar at the bottom
(type exact seconds), or hold Shift and
click to extend. Select > All (Ctrl+A)
takes everything. Everything in
Audacity happens to the selection —
when in doubt about an edit, doubt the
selection first.

**Check:** select seconds 3 to 5 and
press Space. Only that stretch plays,
and the Selection toolbar shows
00 h 00 m 03.000 s → 00 h 00 m 05.000 s.

## Move 4: cut, trim, silence — three different verbs

With seconds 3–5 selected:

- **Delete** (Del, or Edit > Delete):
  the sound is gone and the gap closes
  — everything after slides earlier.
  The recording is now 8 seconds.
- Undo (Ctrl+Z). Then **Edit > Trim
  Audio** (Ctrl+T): the *opposite* —
  everything *except* the selection is
  removed. The recording is now the
  2 selected seconds.
- Undo. Then the **Silence Audio**
  button (or Ctrl+L): the selection
  becomes flat silence but *keeps its
  length*. The recording is still 10
  seconds, with a quiet hole.

Confusing Delete and Silence is the
classic beginner's timing bug: a podcast
that slowly drifts out of sync with its
music bed was usually silenced where it
should have been cut, or cut where it
should have been silenced.

## Move 5: undo, and its limits

Ctrl+Z walks backwards through every
edit this session; Ctrl+Y (Ctrl+Shift+Z
on some systems) walks forward again.
Edit > History… shows the list with
names — the map of everything you've
done, and the quick way back to "before
the effect".

Undo is a session luxury: **closing the
project throws the history away.** A
saved project reopens at its final
state. That is why chapter 11 exists,
and why the recipes (chapter 12) say
"Save Copy before this step" at the
scary parts.

## Save, briefly

File > Save Project > Save Project… and
name it `first-edit.aup3`. You now hold
both of chapter 1's artefacts: the
project on the workbench, and outside
it the untouched `tone.wav`. Chapter 9
turns the project into a finished file
someone else can play.
