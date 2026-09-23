"""
Test cases for extended interpretation variants.
"""

import unittest
from src.deck import get_all_cards
from src.interpretations import get_interpretation_variants, get_all_interpretations


class TestInterpretations(unittest.TestCase):
    def test_variants_structure(self):
        """Test that variants come back as a dict with upright/reversed lists."""
        variants = get_interpretation_variants("The Fool")
        self.assertIsInstance(variants, dict)
        self.assertIn("upright", variants)
        self.assertIn("reversed", variants)
        self.assertIsInstance(variants["upright"], list)
        self.assertIsInstance(variants["reversed"], list)

    def test_every_card_has_variants(self):
        """Test that all 78 cards have recorded interpretation variants."""
        for card in get_all_cards():
            variants = get_interpretation_variants(card["name"])
            self.assertTrue(
                len(variants["upright"]) > 0, f"{card['name']} missing upright variants"
            )
            self.assertTrue(
                len(variants["reversed"]) > 0,
                f"{card['name']} missing reversed variants",
            )

    def test_unknown_card_returns_empty_lists(self):
        """Test that an unrecognized card name returns empty lists, not an error."""
        variants = get_interpretation_variants("Not A Real Card")
        self.assertEqual(variants, {"upright": [], "reversed": []})

    def test_all_interpretations_includes_canonical_line(self):
        """Test that get_all_interpretations prepends the canonical deck.json line."""
        result = get_all_interpretations("The Fool")
        canonical = next(c for c in get_all_cards() if c["name"] == "The Fool")

        self.assertEqual(result["upright"][0], canonical["upright"])
        self.assertEqual(result["reversed"][0], canonical["reversed"])

    def test_all_interpretations_has_three_per_orientation(self):
        """Test that a sample card has 3 total interpretations per orientation
        (1 canonical + 2 variants)."""
        result = get_all_interpretations("The Tower")
        self.assertEqual(len(result["upright"]), 3)
        self.assertEqual(len(result["reversed"]), 3)

    def test_variants_are_distinct_from_canonical(self):
        """Test that variant text doesn't just duplicate the canonical line."""
        for card in get_all_cards():
            variants = get_interpretation_variants(card["name"])
            self.assertNotIn(card["upright"], variants["upright"])
            self.assertNotIn(card["reversed"], variants["reversed"])


if __name__ == "__main__":
    unittest.main()
