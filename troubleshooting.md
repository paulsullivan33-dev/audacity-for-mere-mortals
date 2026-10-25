# Troubleshooting

Symptom → likely cause → the fix.
Where a trap is this guide's own lab
story, it says so.

## "Error opening sound device"

Audacity cannot open the playback or
recording device it is set to use.

- **The device vanished**: unplugged,
  or another program holds the
  microphone exclusively. Transport >
  Rescan Audio Devices, then re-check
  Audio Setup.
- **The rate disagrees**: device at
  48,000 Hz, project at 44,100 (chapter
  5). Match them.
- **There is no device**: a machine
  with no sound hardware offers nothing
  to open — the lab's bench behaved
  exactly like this until it was given
  a software null device (chapter 3).
  On a real machine, this message
  usually means drivers, not destiny.

## The recording is a flat, silent line

- **Wrong input**: the laptop's
  built-in mic (or worse, a muted
  channel) is selected while you speak
  into the real one. Audio Setup >
  Recording Device; watch the meter
  while you tap each candidate.
- **The mic is muted upstream**: in the
  operating system's sound settings, or
  by a physical switch on the headset
  cable.
- **Monitoring confusion**: you are
  hearing the track, not the input.
  Chapter 5's meter is the witness.

## The recording is loud and distorted

Clipping: peaks hit 0 dB and shear off.
Lower the level *at the source* —
mic gain, distance, the recording
slider, in that order — and re-record.
Clip Fix (chapter 8) can cosmetically
mend seconds of it; it cannot mend a
take. Undo does not apply to the real
world.

## Exports come out wrong

- **Too quiet / too loud overall**:
  you exported without the final
  levelling step, or the stack's live
  effects didn't include the normalize
  you applied to a *different* track.
  Measure the export (below) rather
  than re-listening hopefully.
- **Only part of the song**: Export
  Audio uses the whole project;
  Export Selected Audio uses the
  selection. A selection left over from
  an edit is the usual culprit.
- **An MP3 at the wrong rate/size**:
  check the export dialog's format
  options before blaming the file —
  bitrate and channel mode are set
  there, per export.
- **The metadata is stale**: it is
  edited in the export dialog and kept
  from your last export. Skim it every
  time.

Measure an export from the command
line:

```bash
sox export.wav -n stat   # peak and RMS
ffprobe export.mp3       # format claims
```

## The effect "did nothing"

- **The selection wasn't the audio**:
  nothing selected, or the wrong track
  had focus. Effects act on selections
  (chapter 2). Select deliberately and
  re-run.
- **It previewed but never applied**:
  the effect dialog's Preview is a
  tasting spoon, not the meal. OK
  applies.
- **Via the pipe, it applied defaults**:
  this lab's story (transcript t03) —
  a scripted effect with misspelled
  parameter names runs anyway, on
  defaults, and reports success. The
  cure is to verify outputs by
  measurement and to read parameter
  names from the program itself:
  `GetInfo: Type=Commands` inside the
  pipe, or a macro's parameter table
  (chapter 10).

## The scripting pipe isn't there

- **The module is off**: mod-script-pipe
  must be enabled — Preferences >
  Modules, and the program restarted.
- **Two config lines, one winner**: the
  lab's trap (transcript t02) — an old
  `mod-script-pipe=4` ("new, not
  enabled") lower in `audacity.cfg`
  silently outvotes your `=1` above it.
  One module, one line; search the
  file for the module's name and leave
  exactly one entry.
- **The pipes have moved with the
  user**: they are per-user
  (`/tmp/audacity_script_pipe.to.<uid>`)
  and exist only while the program
  runs.

## A modal dialog ate my script

A scripted command whose parameters
fail to parse can raise a dialog
("Could not load settings below.
Default settings will be used") — the
lab met it — and a dialog is modal:
the pipe stops answering until a human
(or a synthetic Return) dismisses it.
Scripts that drive the GUI's program
must expect the GUI to occasionally
insist on being one.

## The project file is locked / busy

An open project holds its `.aup3`
database locked, with a `-wal` file
beside it (chapter 11). That is the
format working, not corruption: close
the project (or the program) before
copying, backing up, or opening the
file with database tools. A leftover
`-wal` after a crash is the recovery
system mid-sentence — launch Audacity
and accept the recovery offer rather
than deleting files by hand.
