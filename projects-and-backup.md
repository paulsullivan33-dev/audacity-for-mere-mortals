# Projects and Backup

## The `.aup3` file, taken apart

Since Audacity 3, a project is **one
file**, and the file is a database.
The lab opened a copy of its own
project with SQLite and read the table
list (transcript t06):

| Table | Holds |
|---|---|
| `project` | One row: the project document — tracks, clips, envelope points, settings — as an XML document stored in binary form (1,608 bytes in the lab's three-second project) |
| `sampleblocks` | The audio itself, block by block (5 blocks for the lab's single clip) |
| `autosave` | The recovery copy when the project has unsaved changes; empty rows when it doesn't |
| `sqlite_sequence` | SQLite's own bookkeeping |

Consequences of the shape:

- **Moving a project means moving one
  file.** No more hunting for the
  `_data` folder that pre-3.0 projects
  kept beside their `.aup` file (if you
  meet one of those pairs in the wild,
  they must travel together; Audacity 3
  converts them on open).
- **Size grows honestly.** A project
  holds its audio *plus* its undo
  ability while open — the lab's file
  was 3,604,480 bytes with the session
  live and 557,056 bytes after the
  program closed and compacted it.
  Long projects with heavy editing
  histories are large for the same
  reason.
- **A locked project is normal.** While
  a project is open, its database is
  locked and wears a `-wal` sidecar
  file. Copy the project *before* the
  program quits and tools may refuse
  the copy or read it mid-thought.
  Chapter 15 has the symptom.

## Autosave and recovery

While you work, Audacity keeps an
autosave of the project in its temp
area (chapter 2). If the program or
the machine dies, the next launch
offers **Recover Projects** — take the
offer, save immediately under a new
name, *then* decide whether the
recovery is trustworthy. Recovery is a
second chance at the working state,
not a guarantee about the audio near
the crash.

The genuinely safe habit stands one
level up: **Save Project early and
often** (Ctrl+S works mid-thought),
and treat "Untitled" in the title bar
as a small emergency.

## Save Copy: the time machine

File > Save Project > **Save Copy…**
writes the whole project — audio
included — as a *separate* `.aup3` and
keeps you working in the current one.
Its uses:

- **Before heroic edits**: before Mix
  and Render, before the aggressive
  noise reduction, before handing the
  project to an effect chain you
  haven't tried (chapters 7, 8, 12 lean
  on this).
- **Milestones**: `episode-12-rough`,
  `episode-12-clean`, `episode-12-final`
  — cheap, complete, restorable.

Save As… alone (which switches you
into the new file) does half this job;
Save Copy is the one that leaves
today's file exactly as it was.

## Backup properly

- Back up the `.aup3` **and the
  original recordings**. The project
  contains copies of imported audio —
  if you chose "copy" at import
  (chapter 4) — but the originals are
  your source of truth when a project
  corrupts.
- Back up **exports of finished work**
  too: the export is the thing
  listeners hear; the project is the
  thing you can rebuild it from. Lose
  either and the other still serves.
- A project copied to another machine
  works whole — same format on Windows,
  macOS and Linux — *except* that
  plug-ins (third-party effects in the
  stack, Nyquist files) live outside
  the project and must travel by name
  and version, not by file.

## The discipline, in one paragraph

Import with copy. Save the project
before you record, edit, or clean.
Save Copy before each irreversible
step. Export the finished piece, and
back up all three kinds of artefact —
originals, projects, exports — like
they were different things, because
they are.
