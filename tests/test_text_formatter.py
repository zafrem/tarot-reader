"""
Test cases for the text formatting functions.
"""

import unittest
from tarot_reader.text_formatter import (
    get_single_card_text,
    get_three_card_text,
    get_celtic_cross_text,
    get_random_cards_text,
    get_reading_summary
)


class TestTextFormatter(unittest.TestCase):
    def test_get_single_card_text(self):
        """Test single card text formatting."""
        # Test LLM format
        result_llm = get_single_card_text("llm")
        self.assertIsInstance(result_llm, str)
        self.assertGreater(len(result_llm), 0)
        self.assertIn(" - ", result_llm)  # Should have card name - meaning format

        # Test CUI format
        result_cui = get_single_card_text("cui")
        self.assertIsInstance(result_cui, str)
        self.assertIn("🎴", result_cui)  # Should have card emoji
        self.assertIn("↳", result_cui)  # Should have arrow

    def test_get_three_card_text(self):
        """Test three card text formatting."""
        # Test LLM format
        result_llm = get_three_card_text("llm")
        self.assertIsInstance(result_llm, str)
        self.assertIn("Past:", result_llm)
        self.assertIn("Present:", result_llm)
        self.assertIn("Future:", result_llm)

        # Test CUI format
        result_cui = get_three_card_text("cui")
        self.assertIsInstance(result_cui, str)
        self.assertIn("THREE CARD SPREAD", result_cui)
        self.assertIn("🔮", result_cui)
        self.assertIn("═", result_cui)  # Should have decorative borders

    def test_get_celtic_cross_text(self):
        """Test Celtic Cross text formatting."""
        # Test LLM format
        result_llm = get_celtic_cross_text("llm")
        self.assertIsInstance(result_llm, str)
        self.assertIn("1.", result_llm)  # Should have numbered positions
        self.assertIn("10.", result_llm)  # Should have 10 positions

        # Test CUI format
        result_cui = get_celtic_cross_text("cui")
        self.assertIsInstance(result_cui, str)
        self.assertIn("CELTIC CROSS", result_cui)
        self.assertIn("🔮", result_cui)

    def test_get_random_cards_text(self):
        """Test random cards text formatting."""
        # Test with different numbers of cards and formats
        for num_cards in [1, 3, 5]:
            # Test LLM format
            result_llm = get_random_cards_text(num_cards, "llm")
            self.assertIsInstance(result_llm, str)
            lines_llm = result_llm.split("\n")
            self.assertEqual(len(lines_llm), num_cards)

            # Test CUI format
            result_cui = get_random_cards_text(num_cards, "cui")
            self.assertIsInstance(result_cui, str)
            self.assertIn("🔮", result_cui)

    def test_get_reading_summary_types(self):
        """Test reading summary with different types and formats."""
        # Test different reading types
        types = ["single", "three", "celtic", "5"]

        for reading_type in types:
            # Test LLM format
            result_llm = get_reading_summary(reading_type, "llm")
            self.assertIsInstance(result_llm, str)
            self.assertIn("🔮", result_llm)  # Should have tarot emoji
            self.assertGreater(len(result_llm), 50)  # Should be substantial text

            # Test CUI format
            result_cui = get_reading_summary(reading_type, "cui")
            self.assertIsInstance(result_cui, str)
            self.assertIn("🔮", result_cui)
            self.assertGreater(len(result_cui), 50)

    def test_reading_summary_fallback(self):
        """Test reading summary with invalid type falls back gracefully."""
        result_llm = get_reading_summary("invalid_type", "llm")
        self.assertIsInstance(result_llm, str)
        self.assertGreater(len(result_llm), 0)

        result_cui = get_reading_summary("invalid_type", "cui")
        self.assertIsInstance(result_cui, str)
        self.assertGreater(len(result_cui), 0)

    def test_format_backward_compatibility(self):
        """Test that functions work without format parameter (backward compatibility)."""
        # Should default to LLM format
        result = get_single_card_text()
        self.assertIsInstance(result, str)
        self.assertIn(" - ", result)


if __name__ == "__main__":
    unittest.main()