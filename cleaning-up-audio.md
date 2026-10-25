# Cleaning Up Audio

The chapter most people came for. The
lab's numbers first, the general
guidance after, because "it sounds
better" is not a measurement and this
chapter has one (transcript t04).

## Noise Reduction: two steps, no shortcuts

Noise Reduction is the strongest
general clean-up, and it only works as
a pair:

**Step 1 — teach it the noise.** Find a
stretch containing *only* the noise —
the half-second before the speaker
starts, the pause between sentences —
select it and run Effect > Noise
Reduction, choosing "Get Noise
Profile". Audacity studies that
stretch's frequency picture and
remembers it.

**Step 2 — apply it.** Select the audio
to clean (usually everything) and run
the effect again, this time with the
numbers: how many decibels to reduce,
sensitivity, frequency smoothing.
Higher reduction removes more noise
and more of the voice with it — 12 dB
is the usual default for a reason.

The lab's measured version, driven
through the scripting pipe on a file
built for the purpose: 1.5 seconds of
white noise alone, then 3.5 seconds of
tone mixed with the same noise. The
noise-only passage, measured before and
after the two steps:

| Passage | RMS before | RMS after |
|---|---|---|
| Noise only | 0.021443 | 0.010758 |
| Tone + noise | 0.088704 | 0.061805 |

The noise-only part halved; the tone's
part fell by roughly a third. That is
the shape of a working reduction — and
its honest limit, in the same table:
the tool cannot fully tell voice from
noise, so it trims both. Pushing
reduction higher flattens the noise
further and starts to make the voice
sound underwater, an artefact listeners
notice before they can name it.

Conditions for success, in descending
order of importance:

1. **The noise is steady.** Fan hum,
   hiss, room tone — yes. A passing
   truck, a dog, a door — no.
2. **The profile stretch is noise
   alone.** One syllable in the profile
   teaches the effect that syllables
   are noise.
3. **The profile matches the whole
   track.** Noise that changes midway
   (a fan that spins up) needs a second
   profile and a second pass on that
   passage.

## Noise Gate: silence below a level

The **Noise Gate** lets sound through
above a threshold and quiets everything
below it. For a recording with long
pauses — a narrator who thinks between
sentences — it turns breath and room
tone into silence without touching
speech. The controls are the threshold
itself, how fast it opens (attack) and
closes (decay), and how deep the cut
is. Set the threshold *between* your
quietest speech and your noise floor;
if the gate chops the starts of words,
the threshold is too high or the attack
too slow.

Gate vs Noise Reduction, in one line:
the gate judges by loudness alone and
works between words; noise reduction
judges by frequency picture and works
*inside* words. They combine well, in
that order.

## The smaller repairs

- **Click Removal** — finds and mends
  short clicks (a mouth click, a vinyl
  pop's bigger cousins). Two numbers:
  how sensitive, how wide a click to
  suspect. Too eager, and it eats the
  attack of consonants.
- **Clip Fix** — rebuilds clipped peaks
  by guessing the shape above the flat
  top, at a percentage of strength.
  Useful on a few seconds; futile on a
  whole recording that clipped. The
  only real fix for clipping is chapter
  5's level, before recording.
- **Repair** — for glitches under
  about 128 samples: select the glitch
  and it is interpolated away.
- **Truncate Silence** — compresses
  pauses longer than a threshold to a
  chosen length: a 45-minute lecture
  with 2-second gaps becomes a tighter
  one. Set the floor low enough that
  natural breaths survive.

## Hum and rumble

Constant low tones have targeted
cures, usually better than noise
reduction:

- **Notch Filter** at the mains
  frequency (50 Hz in most of the
  world, 60 Hz in North America) plus
  its harmonics (100/120, 150/180,
  200/240) — each notch narrow, each
  measured by ear.
- **High-Pass Filter** at 60–80 Hz for
  voices: removes room rumble and
  handling noise with no audible cost
  to speech.

## The spectrogram, briefly

View > Spectrogram (per track) draws
pitch as height and loudness as
brightness. In it, a fan is a set of
flat lines, a click is a vertical
streak, a truck is a smear that rises
and falls. When you cannot name the
problem by ear, look at it — the shape
tells you which of this chapter's
tools applies, and whether a steady
profile stretch exists at all.

## What cleaning up cannot do

It cannot remove a louder sound
layered over speech (the television in
the next room), cannot restore clipped
audio, cannot fix echo in a room (echo
is the room; only the room fixes that),
and cannot make a distant phone
recording sound studio-made. A
recording that needs heroic clean-up
probably needs re-recording — and
chapter 5's level rule is cheaper than
any chapter in this book.
