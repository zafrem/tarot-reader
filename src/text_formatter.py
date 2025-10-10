"""
Text formatting utilities for tarot readings - designed for terminal display.
These functions return formatted text strings for command-line interface display.
"""

from .core import draw_single, draw_three, celtic_cross


def _format_card_for_display(card):
    """
    Format a single card for terminal display.

    Args:
        card: Card dictionary with name, orientation, meaning

    Returns:
        Formatted string for the card
    """
    orientation_text = (
        f" ({card['orientation']})" if card["orientation"] == "Reversed" else ""
    )
    return f"🎴 {card['name']}{orientation_text}\n   ↳ {card['meaning']}"


def get_single_card_text(personal_seed=None) -> str:
    """
    Get a single card reading as formatted text string.

    Args:
        personal_seed: Optional personal information to seed the shuffle

    Returns:
        String containing the card name, orientation, and meaning
    """
    card = draw_single(personal_seed)
    return _format_card_for_display(card)


def get_three_card_text(personal_seed=None) -> str:
    """
    Get a 3-card spread reading as formatted text string.

    Args:
        personal_seed: Optional personal information to seed the shuffle

    Returns:
        String containing Past, Present, Future cards with meanings
    """
    reading = draw_three(personal_seed)
    lines = []

    lines.append("═" * 50)
    lines.append("🔮 THREE CARD SPREAD (Past • Present • Future)")
    if personal_seed:
        lines.append(f"🎯 Personal Seed: {personal_seed}")
    lines.append("═" * 50)

    for position, card in reading.items():
        lines.append(f"\n📅 {position.upper()}:")
        lines.append(_format_card_for_display(card))

    return "\n".join(lines)


def get_celtic_cross_text(personal_seed=None) -> str:
    """
    Get a Celtic Cross spread reading as formatted text string.

    Args:
        personal_seed: Optional personal information to seed the shuffle

    Returns:
        String containing all 10 positions with card names and meanings
    """
    reading = celtic_cross(personal_seed)
    lines = []

    lines.append("═" * 60)
    lines.append("🔮 CELTIC CROSS SPREAD")
    if personal_seed:
        lines.append(f"🎯 Personal Seed: {personal_seed}")
    lines.append("═" * 60)

    for i, (position, card) in enumerate(reading.items(), 1):
        lines.append(f"\n{i:2d}. {position.upper()}:")
        lines.append(_format_card_for_display(card))

    return "\n".join(lines)


def get_random_cards_text(num_cards: int, personal_seed=None) -> str:
    """
    Get a custom number of random cards as formatted text string.

    Args:
        num_cards: Number of cards to draw (1-78)
        personal_seed: Optional personal information to seed the shuffle

    Returns:
        String containing the drawn cards with meanings
    """
    from .core import _draw_cards

    cards = _draw_cards(num_cards, personal_seed)
    lines = []

    lines.append("═" * 50)
    lines.append(f"🔮 {num_cards}-CARD RANDOM DRAW")
    if personal_seed:
        lines.append(f"🎯 Personal Seed: {personal_seed}")
    lines.append("═" * 50)

    for i, card in enumerate(cards, 1):
        lines.append(f"\n{i:2d}.")
        lines.append(_format_card_for_display(card))

    return "\n".join(lines)


def get_reading_summary(reading_type: str = "single", personal_seed=None) -> str:
    """
    Get a complete tarot reading with context for terminal display.

    Args:
        reading_type: Type of reading ("single", "three", "celtic", or number as string)
        personal_seed: Optional personal information to seed the shuffle

    Returns:
        String containing the full reading with context
    """
    if reading_type == "single":
        card_text = get_single_card_text(personal_seed)
        header = "╔══════════════════════════════════════════════════╗\n║              🔮 DAILY CARD READING               ║\n"
        if personal_seed:
            header += f"║           🎯 Seed: {personal_seed[:30]:<30} ║\n"
        header += "╚══════════════════════════════════════════════════╝"
        return f"{header}\n\n{card_text}\n\n💫 This card represents your current energy and guidance for today."

    elif reading_type == "three":
        cards_text = get_three_card_text(personal_seed)
        return f"{cards_text}\n\n💫 This spread shows the flow of time and how past influences\n   shape your present and future path."

    elif reading_type == "celtic":
        cards_text = get_celtic_cross_text(personal_seed)
        return f"{cards_text}\n\n💫 This comprehensive spread provides deep insight into your\n   situation, challenges, and potential outcomes."

    else:
        try:
            num_cards = int(reading_type)
            cards_text = get_random_cards_text(num_cards, personal_seed)
            return f"{cards_text}\n\n💫 These cards offer guidance and insight for your current journey."
        except ValueError:
            return get_single_card_text(personal_seed)
