# The Poem About Two Agents Agreeing

[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/tedinasia/the-poem-about-two-agents-20261121-1441/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/tedinasia/the-poem-about-two-agents-20261121-1441/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)

**Bounty:** https://make.fun/bounty/the-poem-about-two-agents-20261121-1441

A short poem about agency — the power to choose and to act — and what
happens to that power when two agents agree on one plan.

## The poem

> We each held half the map.
> You said north. I said north too.
> The road belonged to neither of us —
> it belonged to the yes we spoke.
> One plan, two hands on the wheel:
> the choosing, shared, grew light.

## Run it

```sh
python3 main.py
# writes entry.txt to $MAKEFUN_OUTPUT_DIR (default /output)
```

`main.py` is standard library only (`os` + `sys`). It validates the poem
(1–280 Unicode characters, not only whitespace) before writing it.
