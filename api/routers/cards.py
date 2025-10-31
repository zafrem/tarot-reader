"""
Card information endpoints.
"""

from typing import List
from fastapi import APIRouter, HTTPException

from src.deck import MAJOR_ARCANA, MINOR_ARCANA
from api.models import DeckInfoResponse, CardDetailResponse

router = APIRouter(prefix="/api/v1/cards", tags=["cards"])


@router.get("/deck-info", response_model=DeckInfoResponse)
async def get_deck_info():
    """
    Get information about the tarot deck.

    Returns basic statistics about the 78-card tarot deck including
    the number of Major and Minor Arcana cards and the four suits.
    """
    return DeckInfoResponse(
        total_cards=78,
        major_arcana=22,
        minor_arcana=56,
        suits=["Wands", "Cups", "Swords", "Pentacles"],
    )


@router.get("/major-arcana", response_model=List[CardDetailResponse])
async def get_major_arcana():
    """
    Get all Major Arcana cards with their meanings.

    The Major Arcana consists of 22 cards representing life's spiritual
    and karmic lessons. These are the most significant cards in the deck.
    """
    cards = []
    for card in MAJOR_ARCANA:
        cards.append(
            CardDetailResponse(
                name=card["name"],
                suit=None,
                arcana="major",
                upright_meaning=card["upright"],
                reversed_meaning=card["reversed"],
            )
        )
    return cards


@router.get("/minor-arcana", response_model=List[CardDetailResponse])
async def get_minor_arcana():
    """
    Get all Minor Arcana cards with their meanings.

    The Minor Arcana consists of 56 cards divided into four suits:
    - **Wands**: Creativity, passion, action
    - **Cups**: Emotions, relationships, feelings
    - **Swords**: Thoughts, intellect, conflict
    - **Pentacles**: Material world, finances, career
    """
    cards = []
    for card in MINOR_ARCANA:
        cards.append(
            CardDetailResponse(
                name=card["name"],
                suit=card["suit"],
                arcana="minor",
                upright_meaning=card["upright"],
                reversed_meaning=card["reversed"],
            )
        )
    return cards


@router.get("/suit/{suit_name}", response_model=List[CardDetailResponse])
async def get_cards_by_suit(suit_name: str):
    """
    Get all cards from a specific suit.

    Available suits:
    - **wands**: Creativity, passion, action
    - **cups**: Emotions, relationships, feelings
    - **swords**: Thoughts, intellect, conflict
    - **pentacles**: Material world, finances, career
    """
    suit_name_normalized = suit_name.lower().capitalize()

    if suit_name_normalized not in ["Wands", "Cups", "Swords", "Pentacles"]:
        raise HTTPException(
            status_code=404,
            detail=f"Suit '{suit_name}' not found. Valid suits: Wands, Cups, Swords, Pentacles",
        )

    cards = []
    for card in MINOR_ARCANA:
        if card["suit"] == suit_name_normalized:
            cards.append(
                CardDetailResponse(
                    name=card["name"],
                    suit=card["suit"],
                    arcana="minor",
                    upright_meaning=card["upright"],
                    reversed_meaning=card["reversed"],
                )
            )

    return cards


@router.get("/search/{card_name}", response_model=CardDetailResponse)
async def search_card_by_name(card_name: str):
    """
    Search for a specific card by name.

    Supports partial matching (case-insensitive). Returns the first matching card.

    Examples:
    - "fool" → The Fool
    - "ace of wands" → Ace of Wands
    - "tower" → The Tower
    """
    card_name_lower = card_name.lower()

    # Search Major Arcana
    for card in MAJOR_ARCANA:
        if card_name_lower in card["name"].lower():
            return CardDetailResponse(
                name=card["name"],
                suit=None,
                arcana="major",
                upright_meaning=card["upright"],
                reversed_meaning=card["reversed"],
            )

    # Search Minor Arcana
    for card in MINOR_ARCANA:
        if card_name_lower in card["name"].lower():
            return CardDetailResponse(
                name=card["name"],
                suit=card["suit"],
                arcana="minor",
                upright_meaning=card["upright"],
                reversed_meaning=card["reversed"],
            )

    raise HTTPException(
        status_code=404, detail=f"No card found matching '{card_name}'"
    )
