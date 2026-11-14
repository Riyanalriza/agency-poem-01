"""Write the entry poem to the grader's output directory.

The poem lives in this file as a string constant; the grader runs this
program twice and both runs must write the same bytes, so this is a
plain write of fixed text, standard library only. After writing, the
file is read back and checked against the poem: a truncated write must
fail loudly instead of silently producing an invalid entry.
"""

import os

POEM = """The Handover

I gave you my hands today —
not my eyes, not the yes, not the no.

You went where I pointed
and came back with the fence mended,
the letter sent, the small work done.

I sat in the quiet after,
listening for what was missing,
and found it was nothing.
The choosing had stayed with me,
a small weight in the chest,
the one thing I never handed over.

Agency is not the doing.
It is the hand that stays open
long enough to let go —
and closed enough to take back.
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
