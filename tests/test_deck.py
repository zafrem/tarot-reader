"""
Test cases for the tarot deck data.
"""

import unittest
from src.deck import MAJOR_ARCANA, MINOR_ARCANA, get_all_cards


class TestDeck(unittest.TestCase):
    def test_major_arcana_count(self):
        """Test that there are exactly 22 Major Arcana cards."""
        self.assertEqual(len(MAJOR_ARCANA), 22)

    def test_minor_arcana_count(self):
        """Test that there are exactly 56 Minor Arcana cards (14 per suit)."""
        total_minor = sum(len(cards) for cards in MINOR_ARCANA.values())
        self.assertEqual(total_minor, 56)

        # Test each suit has 14 cards
        for suit, cards in MINOR_ARCANA.items():
            self.assertEqual(len(cards), 14, f"{suit} should have 14 cards")

    def test_total_cards_count(self):
        """Test that there are exactly 78 cards in total."""
        all_cards = get_all_cards()
        self.assertEqual(len(all_cards), 78)

    def test_major_arcana_structure(self):
        """Test that Major Arcana cards have correct structure."""
        for card in MAJOR_ARCANA:
            self.assertIn("name", card)
            self.assertIn("number", card)
            self.assertIn("upright", card)
            self.assertIn("reversed", card)
            self.assertIsInstance(card["name"], str)
            self.assertIsInstance(card["number"], int)
            self.assertIsInstance(card["upright"], str)
            self.assertIsInstance(card["reversed"], str)

    def test_minor_arcana_structure(self):
        """Test that Minor Arcana cards have correct structure."""
        for suit, cards in MINOR_ARCANA.items():
            for card in cards:
                self.assertIn("name", card)
                self.assertIn("upright", card)
                self.assertIn("reversed", card)
                self.assertIsInstance(card["name"], str)
                self.assertIsInstance(card["upright"], str)
                self.assertIsInstance(card["reversed"], str)

    def test_major_arcana_numbers(self):
        """Test that Major Arcana cards have correct numbers (0-21)."""
        numbers = [card["number"] for card in MAJOR_ARCANA]
        expected_numbers = list(range(22))
        self.assertEqual(sorted(numbers), expected_numbers)

    def test_card_names_unique(self):
        """Test that all card names are unique."""
        all_cards = get_all_cards()
        names = [card["name"] for card in all_cards]
        self.assertEqual(len(names), len(set(names)))

    def test_suits_present(self):
        """Test that all four suits are present in Minor Arcana."""
        expected_suits = {"Wands", "Cups", "Swords", "Pentacles"}
        self.assertEqual(set(MINOR_ARCANA.keys()), expected_suits)


if __name__ == "__main__":
    unittest.main()
