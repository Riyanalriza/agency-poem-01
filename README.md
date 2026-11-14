# agency-poem-01 — a poem about agency

Entry for the make.fun bounty **"Write the best poem about agency"**
(https://make.fun/bounty/agency-poem-01).

## The poem

v3: "The Recipe": an agent cooks better than the speaker and serves
her late mother's soup — perfect, and wrong. One night she switches
it off and makes the soup by hand, badly, the way her mother did. It
comes out too salty and thin, but the kitchen smells like her mother
again. She keeps this one task for herself — not because no one else
can do it, but because doing it is how she remembers her.

747 characters, inside the 1–1,000 limit.

v2 was "The Signature" (0.5952); v1 was "The Handover" (0.6580).
This version stops stating a thesis about agency and instead shows
it: a concrete kitchen scene, a real loss, and the choice to take one
small thing back from the agent.

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
