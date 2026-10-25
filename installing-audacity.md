# Installing Audacity

## The ordinary ways

Audacity is a free download from
audacityteam.org, and the shape of the
install depends on your system:

- **Windows** — an installer (`.exe`),
  and also a portable `.zip` build that
  runs from a folder without installing;
  the portable build keeps its settings
  in a "Portable Settings" folder beside
  the program.
- **macOS** — a `.dmg` with the app to
  drag into Applications. First launch
  of an app from the internet gets the
  usual Gatekeeper question.
- **Linux** — your distribution's
  package (`audacity` in Debian/Ubuntu
  and most others), or the official
  AppImage. Packaged versions can lag
  the newest release; the guide's lab
  used Ubuntu 24.04's package, Audacity
  3.4.2, and says so wherever a version
  could matter.

Whichever route: Audacity 3 needs no
extra encoder for MP3. Older generations
famously sent Windows and Mac users off
to install LAME separately; the current
program has MP3 encoding built in, and
this guide's lab exported an MP3 from
the stock package to prove it
(transcript t03).

**Check:** start the program. You
should land on an empty project window
(chapter 2's tour), possibly after the
dialog below.

## The first-run dialog

The first launch shows a "How to get
help" dialog listing the manual and
forums (transcript t01). It is not an
error and collects nothing. Tick
"Don't show this again at start up" and
press OK — and actually tick it: the
lab dismissed the dialog without the
tick and met it again on a later launch.

## Sound devices

Audacity talks to whatever sound
devices your operating system offers:

- **Playback device** and **recording
  device** are chosen in the Audio
  Setup button on the toolbar (or
  Preferences > Audio Settings).
- If the lists are empty or the program
  complains on startup, the machine is
  offering Audacity nothing — a machine
  with no sound hardware at all does
  exactly this. On Linux, a machine
  with a sound server but no hardware
  may still show a "default" device
  that leads nowhere.
- Sample rates must agree: a device
  that runs at 48,000 Hz recording into
  a 44,100 Hz project makes Audacity
  resample live, which usually works
  and occasionally crackles. Chapter 5
  returns to this.

**Check:** play the tone file from
chapter 4 once you have it. The
playback meter should move and, if your
device is real, you should hear it.

## Where your settings live

Per user, not per project:

- Linux: `~/.config/audacity/
  audacity.cfg`, with data (macros,
  plug-ins) under
  `~/.local/share/audacity/`.
- Windows: `%APPDATA%\audacity\`.
- macOS: `~/Library/Application
  Support/audacity/`.

The `.cfg` is plain text and editable —
chapter 10 enables the scripting module
by adding one line to it, and
transcript t02 tells the small cautionary
tale of the duplicate line that silently
outvoted it.

## The lab's install, declared

The bench was a sandbox: no display, no
sound hardware, 2 CPUs, and a cousin
guide's builders also working in it.
The install was the plain apt one,
`audacity` 3.4.2+dfsg-1build4, 20
packages configured (transcript t00).
To give the program a world to run in,
the lab cheated honestly:

- a **virtual display** (Xvfb), so the
  GUI ran for real, just unseen except
  through screenshots;
- an ALSA **"null" device** as the
  default sound device — a device that
  accepts audio and plays silence, so
  Audacity had something to open. It
  proves the program's device handling
  works; it proves nothing about how
  any real microphone sounds;
- a **scratch HOME**, so the lab's
  settings never touched a real user's.

Your machine has a screen and speakers,
so none of this is your install — it is
declared so that the verification notes
in `criteria.md` can be read honestly:
everything the lab claims was done in
that declared world.
