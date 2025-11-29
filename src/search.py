"""
Card search functionality.
"""

from .deck import get_all_cards

def search_cards(query: str):
    """
    Search for cards by name, number, or alias.

    Args:
        query: The search query (e.g., "The Fool", "1", "s1").

    Returns:
        A list of matching cards.
    """
    query = query.lower().strip()
    if not query:
        return []
    all_cards = get_all_cards()
    results = []

    # Create a mapping for aliases
    suit_aliases = {
        "w": "wands",
        "c": "cups",
        "s": "swords",
        "p": "pentacles",
    }
    court_aliases = {
        "p": "page",
        "kn": "knight",
        "q": "queen",
        "k": "king",
        "a": "ace",
    }

    for card in all_cards:
        card_name_lower = card["name"].lower()
        
        # Search by full name
        if query in card_name_lower:
            results.append(card)
            continue

        # Search by number (Major Arcana)
        if "number" in card and str(card["number"]) == query:
            results.append(card)
            continue

        # Search by alias (e.g., s1, w10, ck)
        # s1 -> swords 1 -> ace of swords
        # wk -> wands king -> king of wands
        if len(query) >= 2:
            suit_char = query[0]
            rank_char = query[1:]

            if suit_char in suit_aliases:
                suit = suit_aliases[suit_char]
                
                # court cards
                if rank_char in court_aliases:
                    rank = court_aliases[rank_char]
                    if f"{rank} of {suit}" in card_name_lower:
                        results.append(card)
                        continue
                
                # numbered cards
                if rank_char.isdigit():
                    rank_num = int(rank_char)
                    if rank_num == 1:
                        if f"ace of {suit}" in card_name_lower:
                             results.append(card)
                             continue
                    elif 1 < rank_num <= 10:
                        # e.g. two of wands
                        number_map = {
                            2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
                            7: "seven", 8: "eight", 9: "nine", 10: "ten"
                        }
                        if f"{number_map[rank_num]} of {suit}" in card_name_lower:
                            results.append(card)
                            continue
    
    # Remove duplicates
    unique_results = []
    seen_names = set()
    for card in results:
        if card["name"] not in seen_names:
            unique_results.append(card)
            seen_names.add(card["name"])

    return unique_results
