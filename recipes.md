# Recipes

Whole jobs, start to finish. Each
assumes the chapters it cites; each
ends with something exportable. The
people and programmes are invented;
the steps are the point.

## A podcast episode, cleaned

*One voice, recorded at home, an
introduction clip, a music bed.*

1. Import the episode recording
   (chapter 4, copy it in). Save the
   project as `episode.aup3` before
   touching anything (chapter 11).
2. Trim head and tail: select the dead
   air at each end, Delete.
3. Cut the long pauses that add
   nothing (listen, don't automate this
   part — judgment lives here), and use
   Truncate Silence (chapter 8) only
   for the mechanical tightening.
4. Noise Reduction's two steps
   (chapter 8), profiled on the room
   tone before the first word. If the
   room is steady, the voice comes
   forward immediately.
5. High-pass at 80 Hz (chapter 7) to
   lift table thumps and rumble; a
   gentle Compressor pass if the
   speaker wanders in volume.
6. Add the intro clip on its own track;
   align; put the music bed on a third
   track, low (−20 dB is a starting
   guess), with an envelope dip under
   the first spoken line (chapter 6).
7. **Loudness Normalization** to the
   platform's target (podcast speech is
   commonly aimed near −16 LUFS stereo,
   −19 LUFS mono — check your host's
   current guidance; targets move).
8. Save Copy as `episode-clean.aup3`.
   Export MP3, 128 kbps mono for one
   voice, metadata filled in
   (chapter 9).

## A meeting recording, made listenable

*One laptop microphone, six speakers,
a fan.*

The honest expectation first: this will
be *clearer*, not *good*. The laptop
microphone spent the meeting far from
most mouths (chapter 5's trap), and no
chain fixes distance.

1. Noise Reduction, profiled on the
   fan-only stretches between items.
2. Normalize to −1 dB peak so quieter
   speakers at least reach the same
   ceiling; accept the raised noise —
   steps 1 and 3 fence it.
3. Envelope down (chapter 6) the two
   loudest passages — the chair's laugh,
   the laptop being moved — rather
   than compressing everyone equally.
4. Labels at each agenda item
   (chapter 6); Export Multiple to one
   MP3 per item (chapter 9). Listeners
   forgive thin audio faster than they
   forgive 90 unindexed minutes.

## A long recording split into chapters

*An oral-history interview, three
hours, one track.*

1. Listen through at 1.5× (Change
   Tempo on a *copy*, or just scrub)
   and drop a label at each topic
   change, named as the file should be:
   `01-childhood`, `02-the-move`, …
2. Check every label twice — Export
   Multiple (chapter 9) is mechanical
   and will faithfully misname a
   chapter whose label you mistyped.
3. Export WAV or FLAC per label to a
   folder with the same names; keep the
   project untouched as the master.

## A backlog, normalized alike

*Twenty voice memos, all different
volumes, one folder of MP3s wanted.*

1. Build the chain once as a macro
   (chapter 10): SelectAll → Normalize
   (peak −1 dB) → Export as MP3 to a
   fixed folder. In the Macro Manager,
   test it on **one** file and measure
   the export (chapter 10's sox habit):
   peak lands where the macro promised.
2. Run the macro across the file list
   from the Manager's Files view.
3. Spot-check three outputs — the
   first, the middle, the last — by
   measurement, not by opening all
   twenty.

The macro runs from the window; that
is this version's boundary (chapter
10). The same chain through the pipe,
with a script choosing files and
verifying each export's peak, is the
programmatic alternative — and the
lab's transcripts t03–t04 are its
worked example.
