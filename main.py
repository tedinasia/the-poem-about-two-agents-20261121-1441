"""Write one short poem about agency to /output/entry.txt.

Two agents, one plan: the poem is about the power to choose and to act,
and what happens to that power when two minds agree on a single road.
Standard library only; no network, no files besides the poem itself.
"""

import os
import sys

POEM = """We each held half the map.
You said north. I said north too.
The road belonged to neither of us —
it belonged to the yes we spoke.
One plan, two hands on the wheel:
the choosing, shared, grew light."""


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if len(POEM) < 1 or len(POEM) > 280:
        print(f"poem must be 1-280 characters, got {len(POEM)}", file=sys.stderr)
        return 1
    if not POEM.strip():
        print("poem must not be only whitespace", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"wrote {len(POEM)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
