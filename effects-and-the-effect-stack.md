# Effects and the Effect Stack

Effects are where Audacity stops being
scissors and starts being a workshop.
This chapter is about the two ways an
effect can act on your audio, then a
tour of the ones that matter. Chapter 8
applies the cleaning crew in earnest.

## Two ways to apply

**Applied (destructive) effects** — the
Effect menu. Select audio, choose the
effect, set its numbers, OK: the samples
are rewritten. Consequences:

- The result can be measured, exported,
  and relied on — it *is* the audio now.
- Undo is the only way back, and Undo
  ends when the project closes.
- Chains are order-sensitive: normalize
  after noise reduction is a different
  result from normalize before.

**The effect stack** — the Effects
button on a track's panel. A list of
effects that process the track *live*,
top to bottom, every playback and at
export, without touching samples:

- Adjust, reorder, bypass or remove at
  any time — the tool for experiments.
- The track's whole length, not a
  selection. (For one phrase, split it
  onto its own track, or apply instead.)
- Exports bake the stack in. If you
  send the *project* to someone, the
  stack travels with it; if you send
  the export, it is simply heard.

Generators (Generate menu — tones,
noise, silence, chirps) and analyzers
(Analyze menu — measure RMS, find
clipping, label sounds, plot spectrum)
are the menu's other two families: one
makes audio, the other reports on it
without changing a sample. Chapter 10's
measurements leaned on the reporting
idea from outside the program; the
built-ins do the same kind of reporting
from inside.

## The tour

**Volume and shape**

- **Amplify** — multiply by a factor
  (given in dB): the plain volume knob,
  with an "allow clipping" warning you
  should leave unticked.
- **Normalize** — set the loudest peak
  to a chosen level (−1 dB is the usual
  choice) and remove any DC offset.
  The lab's measured demonstration is
  transcript t03: peak 0.100 → 0.891.
- **Loudness Normalization** — normalize
  by perceived loudness (LUFS or RMS)
  instead of peak; what podcast and
  broadcast targets are written in.
- **Fade In/Out**, **Adjustable Fade**,
  **Studio Fade Out** — chapter 6's
  edge tools, living here.
- **Compressor** and **Limiter** — tame
  a recording whose loud parts shout
  and quiet parts whisper: the
  compressor squeezes the range
  automatically, the limiter is its
  hard ceiling. Powerful and easy to
  overdo; chapter 12 uses both gently.

**Repairs** — chapter 8's whole story:
Noise Reduction, Noise Gate, Click
Removal, Clip Fix, Repair (for single
glitches a few hundred samples long).

**Equalisation**

- **Filter Curve EQ** and **Graphic EQ**
  — boost or cut frequency bands: cut
  the rumble below 80 Hz, soften a
  harsh "ess". EQ is the surgery knife;
  small cuts beat big boosts.
- **High-Pass / Low-Pass filters** —
  remove everything below/above a
  frequency: rumble and hiss's outer
  fences, respectively.
- **Bass and Treble** — the two-knob
  version, for quick tonal fixes.
- **Notch Filter** — removes one narrow
  frequency: mains hum (50/60 Hz and
  its harmonics) is the classic target.

**Time and pitch**

- **Change Tempo** — faster or slower,
  pitch held; **Change Speed and
  Pitch** — the tape-machine way, both
  together; **Change Pitch** — the
  reverse. Podcast at 1.2× without the
  chipmunk is Change Tempo's party
  trick; long stretches expose its
  artefacts, so test on the worst
  passage, not the best.
- **Echo**, **Reverb**, **Delay**,
  **Phaser**, **Wahwah** — the colour
  box. On speech, reverb is seasoning,
  not sauce.

**The undoing kind**: Invert, Reverse,
(Stereo to Mono lives in the Tracks
menu) — utilities more than effects.

## A rule for chains

Apply in this order, when several are
needed: **repairs first** (chapter 8),
**EQ second**, **level last**
(normalize or loudness at the very
end). Levelling early just gives the
later steps a louder mess to work on,
and measuring between steps (chapter
10 shows how) tells you which step
earned its keep.
