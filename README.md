# agency-poem-01 — a poem about agency

Entry for the make.fun bounty **"Write the best poem about agency"**
(https://make.fun/bounty/agency-poem-01).

## The poem

v2: "The Signature": an agent can draft the letter, seal it, carry
it to the door — but the pen stays in the person's hand. A signature
is the act of being answerable, the one part of agency that cannot be
handed over.

370 characters, inside the 1–1,000 limit.

v1 was "The Handover"; this version takes a sharper frame — the
signature as answerability.

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
