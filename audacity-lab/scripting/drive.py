#!/usr/bin/env python3
"""Drive Audacity 3.4.2 through mod-script-pipe (lab driver, v2).

Reads with os.read on the raw fd and collects until the pipe goes
quiet: this build frames responses loosely, so we gather everything
rather than trusting blank-line terminators."""
import os, select, sys, time

TO = "/tmp/audacity_script_pipe.to.0"
FROM = "/tmp/audacity_script_pipe.from.0"

to_fd = os.open(TO, os.O_WRONLY)
from_fd = os.open(FROM, os.O_RDONLY)

def send(cmd, timeout=60, quiet=1.5):
    print(f">>> {cmd}", flush=True)
    os.write(to_fd, (cmd + "\n").encode())
    data = b""
    deadline = time.time() + timeout
    last = time.time()
    while time.time() < deadline:
        r, _, _ = select.select([from_fd], [], [], 0.25)
        if r:
            chunk = os.read(from_fd, 65536)
            if not chunk:
                break
            data += chunk
            last = time.time()
        elif data and time.time() - last > quiet:
            break
    text = data.decode(errors="replace")
    print(text, end="", flush=True)
    if text and not text.endswith("\n"):
        print(flush=True)
    print("<<< end", flush=True)
    return text

if __name__ == "__main__":
    for cmd in sys.argv[1:]:
        send(cmd)
