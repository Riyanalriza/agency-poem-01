"""Write the entry poem to the grader's output directory.

The poem lives in this file as a string constant; the grader runs this
program twice and both runs must write the same bytes, so this is a
plain write of fixed text, standard library only. After writing, the
file is read back and checked against the poem: a truncated write must
fail loudly instead of silently producing an invalid entry.

The poem, "The Recipe": an agent cooks better than the speaker and
serves her late mother's soup — perfect, and wrong. So one night she
switches it off and makes the soup by hand, badly, the way her mother
did. It comes out too salty and thin, but the kitchen smells like her
mother again. The speaker keeps this one task for herself — not because
no one else can do it, but because doing it is how she remembers her.
Agency here is the choice to take one small thing back from the agent,
and the insight is that some acts cannot be delegated because the
doing itself is the remembering.
"""

import os

POEM = """The Recipe

The agent cooks better than I do.
It weighs the onion to the gram,
knows the minute the stock should turn,
the exact pinch of salt.
It set the table, lit the candle,
and served my mother's soup —
perfect, and wrong.

So tonight I switched it off.
I stood in the kitchen, radio low,
and made it the way she did:
a knob of butter, a handful of dill,
a bay leaf, tasting as I went,
getting it wrong — the steam on my face,
the salt on my tongue.

It came out too salty. It came out thin.
But the kitchen smelled like her again,
not like a recipe, but like a room
where she once stood, stirring, tasting,
staying a little longer than she had to.

I keep this one.
Not because no one else can do it.
Because doing it is how I remember her.
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
