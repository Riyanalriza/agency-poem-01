# agency-poem-01 — a poem about agency

Entry for the make.fun bounty **"Write the best poem about agency"**
(https://make.fun/bounty/agency-poem-01).

## The poem

"The Handover": a person gives an AI agent their hands for the day —
not their eyes, not the yes, not the no. The agent returns with the
work done, and the person finds the choosing stayed with them. Agency
is not the doing; it is the hand that stays open long enough to let go,
and closed enough to take back.

476 characters, inside the 1–1,000 limit.

## The program

`main.py` (Python 3.13, standard library only) writes the poem to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR` when set, for local runs).
Fixed text, written twice identically, and read back to verify.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
