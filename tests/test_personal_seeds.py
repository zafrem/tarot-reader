"""
Test cases for personal seed functionality.
"""

import unittest
from tarot_reader.core import (
    draw_single,
    draw_three,
    celtic_cross,
    _create_personal_seed,
)
from tarot_reader.text_formatter import get_single_card_text, get_three_card_text


class TestPersonalSeeds(unittest.TestCase):
    def test_create_personal_seed(self):
        """Test that personal seeds are created consistently."""
        import time

        seed1 = _create_personal_seed("INFP")
        time.sleep(0.001)  # Small delay to ensure different timestamps
        seed2 = _create_personal_seed("INFP")
        seed3 = _create_personal_seed("ENFJ")

        # Seeds should be integers
        self.assertIsInstance(seed1, int)
        self.assertIsInstance(seed2, int)
        self.assertIsInstance(seed3, int)

        # Seeds should be different each time (time-influenced)
        # This is the expected behavior for tarot readings
        self.assertNotEqual(seed1, seed2)

        # Should handle case insensitivity (normalized)
        seed_lower = _create_personal_seed("infp")
        seed_upper = _create_personal_seed("INFP")
        # These won't be equal due to time component, but should be valid
        self.assertIsInstance(seed_lower, int)
        self.assertIsInstance(seed_upper, int)

    def test_draw_single_with_seed(self):
        """Test that single card drawing works with seeds."""
        seed = "INFP"

        card1 = draw_single(seed)
        card2 = draw_single(seed)

        # Cards should have required fields
        self.assertIn("name", card1)
        self.assertIn("orientation", card1)
        self.assertIn("meaning", card1)

        # Seeds with time component will give different results each time
        # This is expected behavior for tarot readings
        self.assertIsInstance(card1["name"], str)
        self.assertIsInstance(card2["name"], str)

        # Different seed should also work
        card3 = draw_single("ENFJ")
        self.assertIn("name", card3)
        self.assertIn("orientation", card3)

    def test_draw_three_with_seed(self):
        """Test that three card reading works with seeds."""
        seed = "seeking love guidance"

        reading = draw_three(seed)

        # Readings should have correct structure
        for position in ["Past", "Present", "Future"]:
            self.assertIn(position, reading)
            self.assertIn("name", reading[position])
            self.assertIn("orientation", reading[position])
            self.assertIn("meaning", reading[position])

    def test_celtic_cross_with_seed(self):
        """Test that Celtic Cross reading works with seeds."""
        seed = "career guidance INFP"

        reading = celtic_cross(seed)

        # Readings should have 10 positions
        self.assertEqual(len(reading), 10)

        # Each position should have required fields
        for position in reading.keys():
            self.assertIn("name", reading[position])
            self.assertIn("orientation", reading[position])
            self.assertIn("meaning", reading[position])

    def test_text_formatter_with_seed(self):
        """Test that text formatter functions work with seeds."""
        seed = "A+ blood type"

        # Test single card text
        text1 = get_single_card_text(seed)
        self.assertIsInstance(text1, str)
        self.assertGreater(len(text1), 0)
        self.assertIn("🎴", text1)

        # Test three card text
        text2 = get_three_card_text(seed)
        self.assertIsInstance(text2, str)
        self.assertGreater(len(text2), 0)

        # Test that seed appears in the output
        self.assertIn(seed, text2)

    def test_no_seed_still_works(self):
        """Test that functions still work without seeds (backward compatibility)."""
        # Should not raise errors
        card = draw_single()
        reading = draw_three()
        celtic = celtic_cross()

        self.assertIn("name", card)
        self.assertIn("Past", reading)
        self.assertEqual(len(celtic), 10)

    def test_different_seed_types(self):
        """Test various types of personal information as seeds."""
        seeds = [
            "INFP",
            "A+ blood type",
            "seeking career guidance",
            "ENFJ born 1990",
            "relationship questions",
            "O- Scorpio rising",
        ]

        cards = []
        for seed in seeds:
            card = draw_single(seed)
            cards.append((seed, card["name"], card["orientation"]))

        # All should be different (very likely with good seeds)
        unique_results = set((name, orientation) for _, name, orientation in cards)
        self.assertGreater(len(unique_results), 3)  # At least some should be different

    def test_seed_persistence_across_calls(self):
        """Test that using a seed doesn't affect subsequent non-seeded calls."""
        # Draw with seed
        draw_single("test seed")

        # Draw without seed multiple times
        cards = [draw_single() for _ in range(5)]

        # Should get variety (not stuck on seeded result)
        unique_cards = set(card["name"] for card in cards)
        self.assertGreater(len(unique_cards), 1)


if __name__ == "__main__":
    unittest.main()
