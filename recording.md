# Recording

> **Documented only in this guide.**
> The lab had no microphone and no real
> sound device — its "recording device"
> was a software null device that
> produces silence (chapter 3). The
> setup recorded below is Audacity's
> documented workflow and long-standing
> practice, described carefully, but no
> word of it was verified by recording
> in the lab. Levels and device
> behaviour vary by hardware; treat the
> numbers as starting points, not
> measurements.

## Choosing what records you

Audio Setup (toolbar) > Recording
Device lists what the operating system
offers: a USB microphone by name, a
headset, a line-in, sometimes a
"loopback" or "monitor" of the speakers
(the route to recording what the
computer itself is playing). Pick the
device you mean to use, and set
**Recording Channels** beside it — Mono
for one voice into one microphone,
Stereo for most interfaces and line
sources. Recording a mono source as
stereo doubles the file and adds an
empty channel you will delete later.

Two traps:

- **The wrong device is the default
  failure.** Laptops offer the built-in
  microphone first; if your recording
  sounds distant and full of room, you
  recorded the laptop, not the USB mic
  an inch from your mouth.
- **Sample rates must match.** If the
  device runs at 48,000 Hz, set the
  project rate (bottom-left) to 48,000
  too. A mismatch resamples live and is
  a common source of crackle and of
  slow pitch drift on long recordings.

## Levels: the one rule

Click the recording meter (or Transport
> Recording Meter) and speak at your
loudest expected volume. Aim for peaks
around **−12 to −6 dB**:

- Peaks hitting **0 dB** are *clipping*:
  the waveform is cut off flat, the
  sound is distorted, and no effect
  repairs it — chapter 8's clip fix is
  a cosmetic, not a cure. Too loud is
  the only unforgivable recording error.
- Peaks down at −30 dB are usable but
  thin: raising them later raises the
  room noise with them.

Set the level with the recording
slider, the microphone's own gain knob
if it has one, or distance — in that
order of convenience. Then leave it
alone; riding gain mid-recording is
audible.

## Monitoring and overdubs

- **Software playthrough** (Transport >
  Transport Options) echoes your input
  to your headphones with a delay. Fine
  for checking you are audible; the
  delay makes speaking through it
  miserable for most people.
- **Overdub** (same menu) plays the
  existing tracks while you record a
  new one — the podcast co-host recording
  late, the second harmony. Wear
  headphones: speakers playing the old
  tracks bleed into the new recording,
  and no clean-up fully removes them.
- **Punch-in**: select the stretch to
  replace, then record — with Transport
  Options set, recording starts a new
  clip over the selection on the same
  or a new track, depending on the
  "Record on a new track" option.

## The record button's relatives

- **Record** (R) starts at the cursor,
  appending to the selected track or
  starting a new one; Shift+R always
  starts a *new* track.
- **Pause** (P) halts recording but
  keeps the take open — coughs and door
  slams belong on pause, not in the
  edit.
- **Timer Record** (Transport menu)
  starts and stops unattended, for the
  scheduled broadcast or the long
  ambient capture.
- **Sound-activated recording** pauses
  itself below a level threshold. It
  also clips the soft beginnings of
  words; dictation tools do this
  better.

## After recording

Stop, then **Save Project before
anything else** (chapter 11) — an
unsaved recording lives in the temp
folder, and Audacity's crash recovery
is good but is not a filing system.
Then the work of chapters 6–8 begins:
trim the head and tail, cut the dead
air, clean the noise, set the level.
