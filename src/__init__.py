"""
Tarot Reader - A lightweight, text-based tarot reading package for Python.

This package provides functions for tarot card readings including:
- Single card draws
- 3-card spreads (Past/Present/Future)
- Celtic Cross spreads (10 cards)

For entertainment purposes only.
"""

from .core import draw_single, draw_three, celtic_cross, random_drop
from .search import search_cards
from .text_formatter import (
    get_single_card_text,
    get_three_card_text,
    get_celtic_cross_text,
    get_random_cards_text,
    get_reading_summary,
)

__version__ = "0.0.5"
__author__ = "Tarot Reader"

__all__ = [
    "draw_single",
    "draw_three",
    "celtic_cross",
    "random_drop",
    "search_cards",
    "get_single_card_text",
    "get_three_card_text",
    "get_celtic_cross_text",
    "get_random_cards_text",
    "get_reading_summary",
]
