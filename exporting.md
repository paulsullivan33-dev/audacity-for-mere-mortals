# Exporting

## The export is the finished file

File > Export > Export as … mixes the
project — every track, every envelope,
every live effect in each track's
stack — into one audio file. The
project is unchanged by exporting; you
can export again at another format, or
after further edits, forever.

The lab's export evidence
(transcript t03) is a single line with
consequences: the 3-second tone
imported, normalized, and exported as
WAV and MP3. The WAV's peak measured
0.891418 (−1 dB, as ordered); the MP3
came back from ffprobe as `format_name
= mp3, duration = 3.000000` — a real
compressed file, not a renamed
pretender.

## Which format

| Format | When to use it |
|---|---|
| **WAV** | Working masters, archives, anything you will edit again. Uncompressed; large (about 10 MB per minute at CD quality) |
| **FLAC** | Archives with size in mind. Lossless — every bit returns — at roughly half WAV's size |
| **MP3** | Publishing: podcasts, websites, players. Small; throws away detail you mostly cannot hear |
| **OGG Vorbis / Opus** | Publishing where the platform prefers them; Opus excels at speech at low bitrates |
| **AIFF** | WAV's twin from the Mac world; same sound, different wrapper |

Bitrate is the MP3 dial: 128 kbps is
fine for speech, 192–256 for music,
320 for the archivable-ish. Mono
halves the file and is the right choice
for a single voice. Sample rate follows
the project (44,100 Hz for CD-era
compatibility, 48,000 for video) —
exporting does not invent quality the
recording never had.

## Export pieces, not just wholes

- **Export Audio** — the whole project,
  mixed, from the first sample to the
  last.
- **Export Selected Audio** — only the
  current selection (and its tracks).
  The quick way to pull one quote out
  of an interview.
- **Export Multiple** — one file per
  label (chapter 6): split a long
  recording into chapters, named after
  the labels, in one pass. Label tracks
  are the entire mechanism; if a label
  is missing, its piece merges into a
  neighbour, so check the labels first.
- **Export Range** — a stretch defined
  by numbers, for automation (chapter
  10).

## The metadata step

The export dialog asks for metadata —
artist, title, album, year, comments.
For a podcast this is the episode
title and show name that players
display; for an archive it is the
provenance. It rides inside the file
and survives copying. Fill it in at
export time; editing it later means a
second tool.

## The two mistakes

1. **Exporting the project to itself.**
   There is no such thing: the export
   and the project are different
   artefacts (chapter 1). An MP3 saved
   over your only copy of the recording
   is a one-way trip: reopening it and
   editing means editing a compressed
   file's approximation.
2. **Exporting at a higher sample rate
   than the source.** Upsampling makes
   bigger files, not better sound.
   Record at the rate you intend to
   publish (chapter 5), and export at
   the same.
