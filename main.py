"""Six Words, One Story — make.fun program entry.

Writes one complete six-word story to entry.txt in the output
directory. The story: a whole working life in one breath — the
Friday farewell party, then the Monday silence. Nobody calls.
The turn is the gap between the two days: valued one day,
forgotten the next, and everything unsaid in between.
"""

import os

STORY = "Retired Friday. Monday, nobody called back."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY + "\n")

if __name__ == "__main__":
    main()
