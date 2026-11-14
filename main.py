"""Write the entry poem to the grader's output directory.

The poem lives in this file as a string constant; the grader runs this
program twice and both runs must write the same bytes, so this is a
plain write of fixed text, standard library only. After writing, the
file is read back and checked against the poem: a truncated write must
fail loudly instead of silently producing an invalid entry.

The poem, "The Signature": an agent can draft, seal and carry the
letter — but the pen stays in the person's hand. A signature is the
act of being answerable, the one part of agency that cannot be handed
over.
"""

import os

POEM = """The Signature

You may draft the letter,
seal it, carry it to the door —
but the pen stays in my hand.

Everything else I can give away:
the errands, the hours, the heavy lifting.
Only this I keep:
the small black line
where my name becomes a promise.

An agent can do anything
except be answerable.
That is what a signature is —
the place where I stand behind my name.
"""

HERE = os.path.dirname(os.path.abspath(__file__))
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")

os.makedirs(os.path.dirname(DST), exist_ok=True)
with open(DST, "w", encoding="utf-8") as f:
    f.write(POEM)

with open(DST, "r", encoding="utf-8") as f:
    written = f.read()
if written != POEM:
    raise SystemExit("entry.txt differs from the poem")
