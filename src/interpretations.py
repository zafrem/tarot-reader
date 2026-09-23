"""
Extended interpretation variants for tarot cards.

deck.json (and deck.py) hold exactly one canonical upright/reversed line per
card — that's the lean, load-bearing dataset every draw function reads from.
This module is a separate, additive layer: alternate phrasings of the same
upright/reversed meanings, for browsing a wider range of interpretations per
card. It is not wired into src/core.py's draw functions; a reading still
draws the single canonical line from deck.json.
"""

import json
from typing import Dict, List

from .deck import DATA_DIR, MAJOR_ARCANA, MINOR_ARCANA

with open(DATA_DIR / "interpretations.json", encoding="utf-8") as _f:
    _VARIANTS: Dict[str, Dict[str, List[str]]] = json.load(_f)


def _find_canonical_card(card_name: str):
    for card in MAJOR_ARCANA:
        if card["name"] == card_name:
            return card
    for cards in MINOR_ARCANA.values():
        for card in cards:
            if card["name"] == card_name:
                return card
    return None


def get_interpretation_variants(card_name: str) -> Dict[str, List[str]]:
    """Return the additional upright/reversed interpretation variants for a card.

    Returns {"upright": [...], "reversed": [...]}, or
    {"upright": [], "reversed": []} if the card has none recorded (should
    not happen for any of the 78 cards, but don't crash on an unrecognized
    name).
    """
    entry = _VARIANTS.get(card_name)
    if entry is None:
        return {"upright": [], "reversed": []}
    return {"upright": list(entry["upright"]), "reversed": list(entry["reversed"])}


def get_all_interpretations(card_name: str) -> Dict[str, List[str]]:
    """Return every upright/reversed interpretation for a card: the canonical
    deck.json line plus every variant from interpretations.json, as
    {"upright": [<deck.json line>, <variant>, <variant>], "reversed": [...]}.
    """
    canonical = _find_canonical_card(card_name)
    variants = get_interpretation_variants(card_name)

    if canonical is None:
        return variants

    return {
        "upright": [canonical["upright"]] + variants["upright"],
        "reversed": [canonical["reversed"]] + variants["reversed"],
    }
