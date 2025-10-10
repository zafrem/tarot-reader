"""
Core functionality for tarot card readings.
"""

import random
import hashlib
import time
from typing import Dict, List, Any, Optional
from .deck import get_all_cards


def _create_personal_seed(personal_info: str) -> int:
    """
    Create a time-influenced seed from personal information.

    Args:
        personal_info: Any personal information (MBTI, blood type, reason, etc.)

    Returns:
        Integer seed for random number generation with time component
    """
    # Convert to lowercase and strip whitespace for consistency
    normalized = personal_info.lower().strip()

    # Add current time to ensure different results each reading
    time_component = str(int(time.time() * 1000000))
    combined_info = normalized + time_component

    # Create a hash of the personal info + time
    hash_object = hashlib.md5(combined_info.encode())
    hash_hex = hash_object.hexdigest()

    # Convert first 8 characters of hex to integer
    seed = int(hash_hex[:8], 16)
    return seed


def _create_time_seed() -> int:
    """
    Create a seed based on current time for truly random drops.

    Returns:
        Integer seed based on current timestamp
    """
    return int(time.time() * 1000000) % (2**32)


def random_drop(num_cards: int = 1) -> List[Dict[str, Any]]:
    """
    Perform a completely random card drop using current time as seed.

    Args:
        num_cards: Number of cards to draw (default: 1)

    Returns:
        List of randomly drawn cards with time-based randomness
    """
    if num_cards < 1 or num_cards > 78:
        raise ValueError("Number of cards must be between 1 and 78")

    # Use time-based seed for true randomness
    time_seed = _create_time_seed()
    random.seed(time_seed)

    all_cards = get_all_cards()

    # Shuffle multiple times for extra randomness
    for _ in range(random.randint(3, 7)):
        random.shuffle(all_cards)

    # Draw cards
    drawn_cards = all_cards[:num_cards]

    # Assign random orientation with time-influenced probability
    result = []
    for card in drawn_cards:
        # Use time microseconds to influence reversed probability
        time_micro = int(time.time() * 1000000) % 100
        is_reversed = time_micro < 50  # 50% chance, but time-influenced

        card_result = {
            "name": card["name"],
            "orientation": "Reversed" if is_reversed else "Upright",
            "meaning": card["reversed"] if is_reversed else card["upright"],
            "draw_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        }

        # Add number for Major Arcana cards
        if "number" in card:
            card_result["number"] = card["number"]

        result.append(card_result)

    # Reset to truly random seed
    random.seed()

    return result


def _draw_cards(
    num_cards: int, personal_seed: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Draw a specified number of cards from the deck.

    Args:
        num_cards: Number of cards to draw
        personal_seed: Optional personal information to seed the shuffle

    Returns:
        List of card dictionaries with name, meaning, and orientation
    """
    if num_cards < 1 or num_cards > 78:
        raise ValueError("Number of cards must be between 1 and 78")

    # Set random seed if personal info provided
    if personal_seed:
        seed = _create_personal_seed(personal_seed)
        random.seed(seed)

    all_cards = get_all_cards()

    # Shuffle the deck
    random.shuffle(all_cards)

    # Draw the specified number of cards
    drawn_cards = all_cards[:num_cards]

    # Assign random orientation (upright/reversed) to each card
    result = []
    for card in drawn_cards:
        is_reversed = random.choice([True, False])

        card_result = {
            "name": card["name"],
            "orientation": "Reversed" if is_reversed else "Upright",
            "meaning": card["reversed"] if is_reversed else card["upright"],
        }

        # Add number for Major Arcana cards
        if "number" in card:
            card_result["number"] = card["number"]

        result.append(card_result)

    # Reset random seed to current time for subsequent calls
    if personal_seed:
        random.seed()

    return result


def draw_single(personal_seed: Optional[str] = None) -> Dict[str, Any]:
    """
    Draw a single card for a basic reading.

    Args:
        personal_seed: Optional personal information to seed the shuffle
                      (e.g., "INFP", "O+", "seeking love guidance")

    Returns:
        Dictionary containing card name, orientation, and meaning
    """
    cards = _draw_cards(1, personal_seed)
    return cards[0]


def draw_three(personal_seed: Optional[str] = None) -> Dict[str, Dict[str, Any]]:
    """
    Draw three cards for a Past/Present/Future reading.

    Args:
        personal_seed: Optional personal information to seed the shuffle
                      (e.g., "ENFJ + career change", "AB blood type")

    Returns:
        Dictionary with Past, Present, and Future keys containing card info
    """
    cards = _draw_cards(3, personal_seed)

    return {"Past": cards[0], "Present": cards[1], "Future": cards[2]}


def celtic_cross(personal_seed: Optional[str] = None) -> Dict[str, Dict[str, Any]]:
    """
    Draw ten cards for a Celtic Cross spread.

    Args:
        personal_seed: Optional personal information to seed the shuffle
                      (e.g., "ISTJ born 1990", "relationship questions")

    Returns:
        Dictionary with position names as keys containing card info
    """
    cards = _draw_cards(10, personal_seed)

    positions = [
        "Present Situation",
        "Challenge",
        "Distant Past/Foundation",
        "Recent Past",
        "Possible Outcome",
        "Near Future",
        "Your Approach",
        "External Influences",
        "Hopes and Fears",
        "Final Outcome",
    ]

    return {position: card for position, card in zip(positions, cards)}
