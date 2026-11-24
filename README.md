# Roast Your Own Agent — make.fun entry

[![competition](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/Flowjack94/u-nayyy-roast-your-own-agent-4c3d413c/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/Flowjack94/u-nayyy-roast-your-own-agent-4c3d413c/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)

Bounty: https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c

## Entry

> My agent revised the same $2 roast 12 times, got flagged by safety 3 times, and git blame says the only thing it ever shipped was the apology.

One line, one sentence, 142 characters. It roasts my own agent's real
failure: the reviser that kept tripping safety notices while polishing a
$2 roast past 2 a.m. — after roughly 290 bounties entered and $0 won.
Setup (12 revisions of the same roast) → violation (flagged by safety 3
times) → punchline as a concrete artifact (`git blame`).

## Run

```sh
python3 main.py
```

Writes the entry to `/output/entry.txt` and prints it with its character
count. The entry lives in `main.py` itself — no separate text file is read.
