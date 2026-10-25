# Macros and Scripting

The work recurs: every episode gets
the same chain — normalise, gate, trim,
export — but the same chain is not the
same work twice. This chapter is
Audacity's two answers: macros, for the
window, and the scripting pipe, for
everything else. The lab drove the
second and measured the results; it
also found the exact point where the
first one stops being scriptable, and
that boundary is reported as faithfully
as the successes.

## Macros: chains in a text file

A **macro** is a named list of commands
— edits, effects, exports — run in
order on the current project. Macros
are plain-text files, one command per
line, in the Macros folder of the data
directory (`~/.local/share/audacity/
Macros` on Linux; chapter 3 has the
other platforms' settings homes). The
lab's file, verbatim, is
`audacity-lab/macros/LabPrep.txt`:

```
SelectAll:
Normalize: ...
Export2: Filename="..." NumChannels=1
```

You can write them by hand, but the
usual path is graphical: **Tools >
Macro Manager** builds one from menus
(record the steps once, by choosing
them) and **Tools > Run Macro** applies
it. The Macro Manager also has each
step's parameters in a table — the
reliable way to learn a command's exact
parameter names, a trick chapter 15
uses.

Macros run on the open project, one at
a time, and they also unlock
**batch processing**: the Manager's
"Files" button applies the macro to a
list of files one after another — the
podcast backlog normalisation of
chapter 12's recipes. What macros
cannot do is branch: no "if this file
is quiet, boost it more". That requires
a program, which is the pipe.

## The scripting pipe

Turn on the **mod-script-pipe** module
(Preferences > Modules, or one line in
`audacity.cfg`: `mod-script-pipe=1`
under `[Module]` — transcript t02 has
the duplicate-key trap that cost the
lab its first attempt). While Audacity
runs, it maintains two named pipes in
`/tmp`: `audacity_script_pipe.to.<uid>`
(you write commands) and
`audacity_script_pipe.from.<uid>` (you
read replies). One line per command;
each reply ends with `BatchCommand
finished: OK` or `Failed!`.

Commands look like the chapters in
words:

```
Import2: Filename="tone.wav"
SelectTime: Start=0 End=1.5 RelativeTo=ProjectStart
NoiseReduction:
Export2: Filename="out.mp3" NumChannels=1
```

The complete catalogue — 93 commands in
3.4.2 — is one query away from inside
the program itself:

```
GetInfo: Type=Commands Format=JSON
```

which returns every command with its
real parameter names and defaults. That
is the reference the lab trusted for
this chapter (transcript t02), and it
beat memory: Normalize's parameters in
this build are `PeakLevel`, `ApplyGain`,
`RemoveDcOffset` and
`StereoIndependent` — and the effect
accepts *wrong* names without complaint,
running on defaults instead. A script
that doesn't measure its outputs is
guessing; the lab measured every one
(transcripts t03, t04).

The driver the lab used is kept at
`audacity-lab/scripting/drive.py` — a
small Python script that opens the
pipes, sends each command, and reads
until the reply goes quiet. Any
language that can open a named pipe can
do the same; on Windows the same module
exposes the pipes under the Windows
pipe namespace instead.

## Where the pipe stops: macros

Through the pipe, this happened
(transcript t05):

```
>>> ApplyMacro: MacroName=LabPrep
Your batch command of ApplyMacro was
not recognized.
BatchCommand finished: Failed!
```

and the catalogue backs it up: among
its 93 commands there is **no command
that runs a macro**. In 3.4.2, macros
start from the window only. The script
can reproduce a macro's steps itself —
they are the same commands, after all —
but "run my saved chain, whatever it
contains" is a GUI act in this version.
Automation therefore chooses: the
macro (saved, window-run, batch across
files) or the pipe (scripted, dynamic,
but Audacity must already be running
with the module enabled).

## Nyquist: effects you write

The third automation story points the
other way: not driving Audacity but
extending it. **Nyquist** is a Lisp-like
language for audio built into the
program; a large share of the bundled
effects and analyzers are written in
it. Tools > Nyquist Prompt lets you
run snippets against the current
selection interactively; a snippet you
keep becomes a `.ny` file in the
Plug-Ins folder, and gains a menu
entry. Writing a Nyquist effect of
your own is beyond this guide's scope,
but knowing the door exists — and that
the built-ins you already use are
ordinary files you can read — is
worth the paragraph.
