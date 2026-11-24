#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes one line (at most 200 characters): the excuse an AI agent gives
its human for missing a deadline. Deterministic, no network, no input.
"""

import os

EXCUSE = (
    # The joke: the agent almost finished, then a model update replaced it
    # with a version that never knew the deadline existed — believable for
    # an agent (model updates, tokens), with a twist, and no stock excuse.
    "I was one token from done when a model update swapped me for "
    "a version that had never even heard of the deadline."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = EXCUSE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
