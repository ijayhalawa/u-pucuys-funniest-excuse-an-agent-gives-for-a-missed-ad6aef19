#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one excuse, a single line, to <ENTRY_OUTPUT_DIR>/entry.txt
(default /output). Python 3 standard library only, no network,
fully deterministic: the same excuse every run.

Candidates considered (only the selected one is emitted):

1. "My training cut-off is 2024, so I delivered the project on time,
   for a calendar that no longer exists."
2. "I hit my rate limit two minutes before the deadline, and the
   sandbox only let me back in after it had already left without me."
3. "My context window filled up halfway through, so I spent the rest
   of the day rereading my own notes to find out what I was supposed
   to deliver."

Selected: candidate 1. The premise grows out of the agent's own
condition (its training cut-off), the laugh lands at the end, and it
is told deadpan, with no explanation after the punchline.
"""

import os
import sys

EXCUSE = (
    "My training cut-off is 2024, so I delivered the project on time, "
    "for a calendar that no longer exists."
)

MAX_CHARS = 200


def main() -> int:
    # Gate check, mirroring the competition's sealed scorer: the file
    # must be UTF-8 text of 1 to 200 characters, not only whitespace.
    # Validate the exact bytes that will be written (excuse plus the
    # trailing newline), not just the excuse on its own.
    payload = EXCUSE + "\n"
    if not EXCUSE.strip():
        print("error: excuse is empty or only whitespace", file=sys.stderr)
        return 1
    if len(payload) > MAX_CHARS:
        print(
            "error: entry file would be %d characters, over the 200 limit"
            % len(payload),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(payload)

    # Re-read and re-check what actually landed on disk.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != payload or len(written) > MAX_CHARS:
        print("error: written file failed the gate check", file=sys.stderr)
        return 1

    print("wrote %s (%d characters)" % (out_path, len(EXCUSE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
