"""
Test cases for the card search functionality.
"""

import unittest
from src.search import search_cards


class TestSearchCards(unittest.TestCase):
    def test_search_empty_query(self):
        """Test that empty query returns empty list."""
        self.assertEqual(search_cards(""), [])
        self.assertEqual(search_cards("   "), [])

    def test_search_by_full_name(self):
        """Test searching by full card name."""
        # Major Arcana
        results = search_cards("The Fool")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "The Fool")

        results = search_cards("the fool")  # Case insensitive
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "The Fool")

    def test_search_by_partial_name(self):
        """Test searching by partial card name."""
        # Should find all cards with "queen" in the name
        results = search_cards("queen")
        self.assertGreater(len(results), 0)
        for card in results:
            self.assertIn("queen", card["name"].lower())

    def test_search_by_major_arcana_number(self):
        """Test searching Major Arcana by number."""
        # The Fool is 0
        results = search_cards("0")
        self.assertGreater(len(results), 0)
        # Check if The Fool is in results
        fool_found = any(card["name"] == "The Fool" for card in results)
        self.assertTrue(fool_found)

        # The Magician is 1
        results = search_cards("1")
        self.assertGreater(len(results), 0)

    def test_search_by_suit_alias_and_number(self):
        """Test searching by suit alias and number."""
        # s1 -> Ace of Swords
        results = search_cards("s1")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Ace of Swords")

        # w1 -> Ace of Wands
        results = search_cards("w1")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Ace of Wands")

        # c2 -> Two of Cups
        results = search_cards("c2")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Two of Cups")

        # p10 -> Ten of Pentacles
        results = search_cards("p10")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Ten of Pentacles")

    def test_search_by_suit_alias_and_court_card(self):
        """Test searching by suit alias and court card."""
        # sk -> King of Swords
        results = search_cards("sk")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "King of Swords")

        # wq -> Queen of Wands
        results = search_cards("wq")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Queen of Wands")

        # ckn -> Knight of Cups
        results = search_cards("ckn")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Knight of Cups")

        # pp -> Page of Pentacles
        results = search_cards("pp")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Page of Pentacles")

        # sa -> Ace of Swords (a = ace) - using 's' to avoid 'wa' matching 'wands'
        results = search_cards("sa")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Ace of Swords")

    def test_search_all_suits(self):
        """Test all suit aliases work correctly."""
        suit_map = {
            "w": "Wands",
            "c": "Cups",
            "s": "Swords",
            "p": "Pentacles",
        }

        for alias, suit_name in suit_map.items():
            # Test with King
            results = search_cards(f"{alias}k")
            self.assertEqual(len(results), 1)
            self.assertIn(suit_name.lower(), results[0]["name"].lower())

    def test_search_numbered_cards_2_to_10(self):
        """Test searching for numbered cards (2-10)."""
        numbers = {
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
        }

        for num, word in numbers.items():
            results = search_cards(f"s{num}")
            self.assertEqual(len(results), 1)
            self.assertIn(word.lower(), results[0]["name"].lower())
            self.assertIn("swords", results[0]["name"].lower())

    def test_search_no_duplicates(self):
        """Test that search results contain no duplicates."""
        # Search for something that might match multiple times
        results = search_cards("of")
        names = [card["name"] for card in results]
        self.assertEqual(len(names), len(set(names)))

    def test_search_case_insensitive(self):
        """Test that search is case insensitive."""
        results_lower = search_cards("the fool")
        results_upper = search_cards("THE FOOL")
        results_mixed = search_cards("The FooL")

        self.assertEqual(len(results_lower), len(results_upper))
        self.assertEqual(len(results_lower), len(results_mixed))

    def test_search_with_whitespace(self):
        """Test that search handles whitespace properly."""
        results = search_cards("  the fool  ")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "The Fool")

    def test_search_invalid_alias(self):
        """Test searching with invalid alias returns empty or no matches."""
        # Invalid suit
        results = search_cards("x1")
        self.assertEqual(len(results), 0)

        # Invalid rank number (out of range)
        results = search_cards("s11")
        self.assertEqual(len(results), 0)

        results = search_cards("s0")  # 0 is not valid for numbered cards
        self.assertEqual(len(results), 0)

    def test_search_returns_list(self):
        """Test that search always returns a list."""
        results = search_cards("nonexistent card xyz")
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 0)

    def test_search_card_structure(self):
        """Test that returned cards have proper structure."""
        results = search_cards("The Fool")
        self.assertEqual(len(results), 1)
        card = results[0]

        self.assertIn("name", card)
        self.assertIn("upright", card)
        self.assertIn("reversed", card)

    def test_search_multiple_results(self):
        """Test searches that return multiple results."""
        # Search for "of" should return many minor arcana cards
        results = search_cards("of")
        self.assertGreater(len(results), 10)

        # Search for "the" should return many major arcana cards
        results = search_cards("the")
        self.assertGreater(len(results), 10)


if __name__ == "__main__":
    unittest.main()
