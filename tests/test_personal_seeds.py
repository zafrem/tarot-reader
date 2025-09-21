"""
Test cases for personal seed functionality.
"""

import unittest
from tarot_reader.core import draw_single, draw_three, celtic_cross, _create_personal_seed
from tarot_reader.text_formatter import get_single_card_text, get_three_card_text


class TestPersonalSeeds(unittest.TestCase):
    def test_create_personal_seed(self):
        """Test that personal seeds are created consistently."""
        seed1 = _create_personal_seed("INFP")
        seed2 = _create_personal_seed("INFP")
        seed3 = _create_personal_seed("ENFJ")

        # Same input should give same seed
        self.assertEqual(seed1, seed2)

        # Different input should give different seed
        self.assertNotEqual(seed1, seed3)

        # Should handle case insensitivity
        seed_lower = _create_personal_seed("infp")
        seed_upper = _create_personal_seed("INFP")
        self.assertEqual(seed_lower, seed_upper)

        # Should handle whitespace
        seed_space = _create_personal_seed("  INFP  ")
        self.assertEqual(seed1, seed_space)

    def test_draw_single_with_seed(self):
        """Test that single card drawing is consistent with same seed."""
        seed = "INFP"

        card1 = draw_single(seed)
        card2 = draw_single(seed)

        # Same seed should give same card
        self.assertEqual(card1["name"], card2["name"])
        self.assertEqual(card1["orientation"], card2["orientation"])
        self.assertEqual(card1["meaning"], card2["meaning"])

        # Different seed should give different result
        card3 = draw_single("ENFJ")
        self.assertTrue(
            card1["name"] != card3["name"] or
            card1["orientation"] != card3["orientation"]
        )

    def test_draw_three_with_seed(self):
        """Test that three card reading is consistent with same seed."""
        seed = "seeking love guidance"

        reading1 = draw_three(seed)
        reading2 = draw_three(seed)

        # Same seed should give same reading
        for position in ["Past", "Present", "Future"]:
            self.assertEqual(reading1[position]["name"], reading2[position]["name"])
            self.assertEqual(reading1[position]["orientation"], reading2[position]["orientation"])

    def test_celtic_cross_with_seed(self):
        """Test that Celtic Cross reading is consistent with same seed."""
        seed = "career guidance INFP"

        reading1 = celtic_cross(seed)
        reading2 = celtic_cross(seed)

        # Same seed should give same reading
        for position in reading1.keys():
            self.assertEqual(reading1[position]["name"], reading2[position]["name"])
            self.assertEqual(reading1[position]["orientation"], reading2[position]["orientation"])

    def test_text_formatter_with_seed(self):
        """Test that text formatter functions work with seeds."""
        seed = "A+ blood type"

        # Test single card text
        text1 = get_single_card_text("llm", seed)
        text2 = get_single_card_text("llm", seed)
        self.assertEqual(text1, text2)

        # Test three card text
        text3 = get_three_card_text("llm", seed)
        text4 = get_three_card_text("llm", seed)
        self.assertEqual(text3, text4)

        # Test that seed appears in CUI format
        cui_text = get_three_card_text("cui", seed)
        self.assertIn(seed, cui_text)

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
            "O- Scorpio rising"
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
        seeded_card = draw_single("test seed")

        # Draw without seed multiple times
        cards = [draw_single() for _ in range(5)]

        # Should get variety (not stuck on seeded result)
        unique_cards = set(card["name"] for card in cards)
        self.assertGreater(len(unique_cards), 1)


if __name__ == "__main__":
    unittest.main()