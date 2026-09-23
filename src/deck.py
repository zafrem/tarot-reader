"""
Tarot deck data containing all 78 cards with upright and reversed meanings.

Card content and images are loaded from data/deck.json, a portable,
Python-independent dataset. Any native client (mobile, Obsidian plugin,
Notion import script, etc.) can read that JSON and its accompanying
data/images/ directory directly without depending on this module.
"""

import json
from pathlib import Path
from typing import Any, Dict, List

DATA_DIR = Path(__file__).parent / "data"
IMAGES_DIR = DATA_DIR / "images"

with open(DATA_DIR / "deck.json", encoding="utf-8") as _f:
    _RAW_CARDS = json.load(_f)

MAJOR_ARCANA = [
    {
        "name": c["name"],
        "number": c["number"],
        "upright": c["upright"],
        "reversed": c["reversed"],
        "images": c["images"],
    }
    for c in _RAW_CARDS
    if c["arcana"] == "major"
]

MINOR_ARCANA: Dict[str, List[Dict[str, Any]]] = {}
for _c in _RAW_CARDS:
    if _c["arcana"] == "minor":
        MINOR_ARCANA.setdefault(_c["suit"], []).append(
            {
                "name": _c["name"],
                "upright": _c["upright"],
                "reversed": _c["reversed"],
                "images": _c["images"],
            }
        )


def get_all_cards():
    """Return a list of all 78 tarot cards."""
    all_cards = []

    # Add Major Arcana
    all_cards.extend(MAJOR_ARCANA)

    # Add Minor Arcana
    for suit, cards in MINOR_ARCANA.items():
        all_cards.extend(cards)

    return all_cards


def get_card_image_path(card, image_type: str = "default"):
    """Return the absolute filesystem path to a card's image.

    Args:
        card: A card dict (as returned by get_all_cards()), an "images"
              dict directly, or an image path string (e.g.
              "images/the_fool.jpg") to resolve as-is.
        image_type: Which entry of the card's "images" dict to resolve
                    (default: "default").
    """
    if isinstance(card, dict):
        images = card["images"] if "images" in card else card
        image = images[image_type]
    else:
        image = card
    return DATA_DIR / image
