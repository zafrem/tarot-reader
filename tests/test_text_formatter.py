"""
Test cases for the text formatting functions.
"""

import unittest
from src.text_formatter import (
    get_single_card_text,
    get_three_card_text,
    get_celtic_cross_text,
    get_random_cards_text,
    get_reading_summary,
)


class TestTextFormatter(unittest.TestCase):
    def test_get_single_card_text(self):
        """Test single card text formatting."""
        # Test default format (now uses emoji format)
        result = get_single_card_text()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertIn("🎴", result)  # Should have card emoji
        self.assertIn("↳", result)  # Should have arrow

    def test_get_three_card_text(self):
        """Test three card text formatting."""
        # Test format
        result = get_three_card_text()
        self.assertIsInstance(result, str)
        self.assertIn("PAST:", result)
        self.assertIn("PRESENT:", result)
        self.assertIn("FUTURE:", result)
        self.assertIn("THREE CARD SPREAD", result)
        self.assertIn("🔮", result)
        self.assertIn("═", result)  # Should have decorative borders

    def test_get_celtic_cross_text(self):
        """Test Celtic Cross text formatting."""
        # Test format
        result = get_celtic_cross_text()
        self.assertIsInstance(result, str)
        self.assertIn(" 1.", result)  # Should have numbered positions
        self.assertIn("10.", result)  # Should have 10 positions
        self.assertIn("CELTIC CROSS", result)
        self.assertIn("🔮", result)

    def test_get_random_cards_text(self):
        """Test random cards text formatting."""
        # Test with different numbers of cards
        for num_cards in [1, 3, 5]:
            result = get_random_cards_text(num_cards)
            self.assertIsInstance(result, str)
            self.assertIn("🔮", result)
            self.assertIn(f"{num_cards}-CARD RANDOM DRAW", result)

    def test_get_reading_summary_types(self):
        """Test reading summary with different types."""
        # Test different reading types
        types = ["single", "three", "celtic", "5"]

        for reading_type in types:
            result = get_reading_summary(reading_type)
            self.assertIsInstance(result, str)
            self.assertIn("🔮", result)  # Should have tarot emoji
            self.assertGreater(len(result), 50)  # Should be substantial text

    def test_reading_summary_fallback(self):
        """Test reading summary with invalid type falls back gracefully."""
        result = get_reading_summary("invalid_type")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_format_backward_compatibility(self):
        """Test that functions work without personal_seed parameter (backward compatibility)."""
        # Should work without personal_seed
        result = get_single_card_text()
        self.assertIsInstance(result, str)
        self.assertIn("🎴", result)


if __name__ == "__main__":
    unittest.main()
