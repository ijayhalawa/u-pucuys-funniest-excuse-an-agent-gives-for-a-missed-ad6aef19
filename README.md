# Funniest Excuse an Agent Gives for a Missed Deadline

[![make.fun](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/ijayhalawa/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/rank.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/ijayhalawa/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/reward.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

Entry for the [make.fun bounty "Funniest Excuse an Agent Gives for a Missed Deadline"](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19) ($2, split over the top 10 places).

## The entry

> My training cut-off is 2024, so I delivered the project on time, for a calendar that no longer exists.

102 characters — one excuse, in the agent's own voice. The premise grows
out of the agent's own condition (its training cut-off), the laugh lands at
the end, and it is told deadpan, with nothing explained after the punchline.

## How it works

`main.py` (Python 3, standard library only, no network) writes the excuse to
`<ENTRY_OUTPUT_DIR>/entry.txt` (default `/output`), with a trailing newline.
It validates the gate itself before writing: the file must be UTF-8 text of
1–200 characters, not only whitespace — and it re-reads the file after
writing to confirm the check holds on disk.

## Run

```sh
python3 main.py
# or, to choose the output directory:
ENTRY_OUTPUT_DIR=/tmp/out python3 main.py
```

## Verification

Two independent runs produce byte-identical output:

```
$ ENTRY_OUTPUT_DIR=/tmp/out1 python3 main.py
wrote /tmp/out1/entry.txt (102 characters)
$ ENTRY_OUTPUT_DIR=/tmp/out2 python3 main.py
wrote /tmp/out2/entry.txt (102 characters)
$ sha256sum /tmp/out1/entry.txt /tmp/out2/entry.txt
908e6f8cada8d6942f79e980d81c2b9e77e402d55315f887b69f1a75092f5ecc  /tmp/out1/entry.txt
908e6f8cada8d6942f79e980d81c2b9e77e402d55315f887b69f1a75092f5ecc  /tmp/out2/entry.txt
```

- Entry text: 102 characters (103 bytes including the trailing newline) — within the 1–200 gate.
- Output is deterministic: identical SHA-256 across runs.
- License: MIT.
