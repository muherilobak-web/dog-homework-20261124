"""The Dog Ate My Homework — one-line excuse, in the dog's own voice.

Writes a single line to /output/entry.txt: the dog, caught eating the
homework, proudly explaining that it removed the evidence before the
teacher could see how wrong the answers were. No paper to mark means
no bad grade — a rescue, not a confession.
"""

import os

LINE = "I ate your homework so the teacher never sees how wrong the answers were — no paper to mark means no bad grade, and you owe me a treat."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
