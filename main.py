"""Write the entry poem to the grader's output directory.

The poem lives in this file as a string constant; the grader runs this
program twice and both runs must write the same bytes, so this is a
plain write of fixed text, standard library only. After writing, the
file is read back and checked against the poem: a truncated write must
fail loudly instead of silently producing an invalid entry.

The poem, "One Blink": the body has gone quiet — legs, arms, voice,
all still — and only the eyes are left, and in them, a blink. One blink
for yes, two for no: that is the whole of choosing now, the smallest
door in the world, and it opens from the inside. Others bring the
choices one by one and wait; the speaker says yes and no, and in saying
it is still here — not a body that obeys, but a person who decides.
The insight is that agency does not need a body that obeys: it needs
only the power to choose, and a single blink is enough to be free.
"""

import os

POEM = """One Blink

The body went quiet first —
legs, arms, the voice,
all of them, gone still.
Only the eyes were left,
and in the eyes, a blink.

One blink for yes.
Two for no.
That is all of it now:
a yes, a no,
a yes, a no —
the smallest door in the world,
and it opens from the inside.

They bring the choices one by one
and hold them up and wait:
the soup, the light, the window,
the music, the hour.
I say yes. I say no.
And saying it, I am still here —
not a body that obeys,
but a person who decides.

Take the legs. Take the arms.
Take the voice.
Leave me the blink.
One blink is enough to be free.
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
