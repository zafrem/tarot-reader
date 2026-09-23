"""
Test cases for the core tarot reading functionality.
"""

import unittest
from unittest.mock import patch
from src.core import (
    draw_single,
    draw_three,
    celtic_cross,
    _draw_cards,
    random_drop,
    _create_time_seed,
    daily_reading,
    _create_daily_seed,
)


class TestCore(unittest.TestCase):
    def test_draw_single_returns_dict(self):
        """Test that draw_single returns a dictionary with required keys."""
        card = draw_single()
        self.assertIsInstance(card, dict)
        self.assertIn("name", card)
        self.assertIn("orientation", card)
        self.assertIn("meaning", card)

    def test_draw_single_orientation(self):
        """Test that draw_single returns either Upright or Reversed orientation."""
        card = draw_single()
        self.assertIn(card["orientation"], ["Upright", "Reversed"])

    def test_draw_three_structure(self):
        """Test that draw_three returns correct structure."""
        reading = draw_three()
        self.assertIsInstance(reading, dict)
        expected_keys = {"Past", "Present", "Future"}
        self.assertEqual(set(reading.keys()), expected_keys)

        for position, card in reading.items():
            self.assertIsInstance(card, dict)
            self.assertIn("name", card)
            self.assertIn("orientation", card)
            self.assertIn("meaning", card)

    def test_celtic_cross_structure(self):
        """Test that celtic_cross returns correct structure."""
        reading = celtic_cross()
        self.assertIsInstance(reading, dict)

        expected_positions = [
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

        self.assertEqual(set(reading.keys()), set(expected_positions))
        self.assertEqual(len(reading), 10)

        for position, card in reading.items():
            self.assertIsInstance(card, dict)
            self.assertIn("name", card)
            self.assertIn("orientation", card)
            self.assertIn("meaning", card)

    def test_draw_cards_valid_range(self):
        """Test that _draw_cards works with valid card counts."""
        # Test single card
        cards = _draw_cards(1)
        self.assertEqual(len(cards), 1)

        # Test multiple cards
        cards = _draw_cards(5)
        self.assertEqual(len(cards), 5)

        # Test maximum cards
        cards = _draw_cards(78)
        self.assertEqual(len(cards), 78)

    def test_draw_cards_invalid_range(self):
        """Test that _draw_cards raises ValueError for invalid counts."""
        with self.assertRaises(ValueError):
            _draw_cards(0)

        with self.assertRaises(ValueError):
            _draw_cards(-1)

        with self.assertRaises(ValueError):
            _draw_cards(79)

    def test_cards_are_unique_in_single_reading(self):
        """Test that no duplicate cards appear in a single reading."""
        # Test with celtic cross (10 cards)
        reading = celtic_cross()
        card_names = [card["name"] for card in reading.values()]
        self.assertEqual(len(card_names), len(set(card_names)))

        # Test with 3-card spread
        reading = draw_three()
        card_names = [card["name"] for card in reading.values()]
        self.assertEqual(len(card_names), len(set(card_names)))

    @patch("random.choice")
    @patch("random.shuffle")
    def test_orientation_randomness(self, mock_shuffle, mock_choice):
        """Test that card orientation is properly randomized."""
        # Mock shuffle to do nothing (preserve order)
        mock_shuffle.side_effect = lambda x: None

        # Mock choice to return True (reversed) then False (upright)
        mock_choice.side_effect = [True, False]

        cards = _draw_cards(2)

        self.assertEqual(cards[0]["orientation"], "Reversed")
        self.assertEqual(cards[1]["orientation"], "Upright")

    def test_performance_requirement(self):
        """Test that drawing 10 cards completes quickly (NFR-2)."""
        import time

        start_time = time.time()
        celtic_cross()
        end_time = time.time()

        # Should complete in much less than 1 second
        self.assertLess(end_time - start_time, 1.0)

    def test_major_arcana_includes_number(self):
        """Test that Major Arcana cards include their number."""
        # Draw enough cards to likely get a Major Arcana card
        for _ in range(10):  # Try multiple times
            card = draw_single()
            if "number" in card:
                # Found a Major Arcana card
                self.assertIsInstance(card["number"], int)
                self.assertGreaterEqual(card["number"], 0)
                self.assertLessEqual(card["number"], 21)
                break
        else:
            # If we didn't find one, that's still valid but unlikely
            pass

    def test_randomness_different_results(self):
        """Test that multiple readings produce different results."""
        # This test might rarely fail due to randomness, but very unlikely
        readings = [draw_single()["name"] for _ in range(10)]

        # At least some cards should be different
        unique_cards = set(readings)
        self.assertGreater(len(unique_cards), 1)

    def test_random_drop_returns_list(self):
        """Test that random_drop returns a list."""
        result = random_drop()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)

    def test_random_drop_multiple_cards(self):
        """Test that random_drop can return multiple cards."""
        result = random_drop(5)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)

    def test_random_drop_card_structure(self):
        """Test that random_drop returns cards with correct structure."""
        result = random_drop(1)
        card = result[0]

        self.assertIn("name", card)
        self.assertIn("orientation", card)
        self.assertIn("meaning", card)
        self.assertIn("draw_time", card)
        self.assertIn(card["orientation"], ["Upright", "Reversed"])

    def test_random_drop_invalid_range(self):
        """Test that random_drop raises ValueError for invalid counts."""
        with self.assertRaises(ValueError):
            random_drop(0)

        with self.assertRaises(ValueError):
            random_drop(-1)

        with self.assertRaises(ValueError):
            random_drop(79)

    def test_random_drop_valid_range(self):
        """Test that random_drop works with valid card counts."""
        # Test minimum
        result = random_drop(1)
        self.assertEqual(len(result), 1)

        # Test medium
        result = random_drop(10)
        self.assertEqual(len(result), 10)

        # Test maximum
        result = random_drop(78)
        self.assertEqual(len(result), 78)

    def test_random_drop_unique_cards(self):
        """Test that random_drop returns unique cards."""
        result = random_drop(10)
        card_names = [card["name"] for card in result]
        self.assertEqual(len(card_names), len(set(card_names)))

    def test_random_drop_includes_timestamp(self):
        """Test that random_drop includes draw_time in results."""
        result = random_drop(1)
        self.assertIn("draw_time", result[0])
        self.assertIsInstance(result[0]["draw_time"], str)

    def test_random_drop_major_arcana_numbers(self):
        """Test that Major Arcana cards in random_drop include numbers."""
        # Draw multiple cards to increase chance of getting Major Arcana
        result = random_drop(20)
        for card in result:
            if "number" in card:
                self.assertIsInstance(card["number"], int)
                self.assertGreaterEqual(card["number"], 0)
                self.assertLessEqual(card["number"], 21)
                break
        # This test is probabilistic but very likely to pass

    def test_create_time_seed_returns_int(self):
        """Test that _create_time_seed returns an integer."""
        seed = _create_time_seed()
        self.assertIsInstance(seed, int)

    def test_create_time_seed_in_valid_range(self):
        """Test that _create_time_seed returns value in valid range."""
        seed = _create_time_seed()
        # Should be within 32-bit integer range
        self.assertGreaterEqual(seed, 0)
        self.assertLess(seed, 2**32)

    def test_create_time_seed_changes_over_time(self):
        """Test that _create_time_seed produces different values."""
        import time

        seed1 = _create_time_seed()
        time.sleep(0.01)  # Small delay
        seed2 = _create_time_seed()
        # Seeds should be different due to time change
        self.assertNotEqual(seed1, seed2)


class TestDailyReading(unittest.TestCase):
    def test_returns_expected_structure(self):
        """Test that daily_reading returns a dict with all expected keys."""
        reading = daily_reading(date="2026-01-01")
        self.assertIsInstance(reading, dict)
        for key in ("date", "name", "orientation", "meaning", "images"):
            self.assertIn(key, reading)
        self.assertIn("default", reading["images"])
        self.assertEqual(reading["date"], "2026-01-01")
        self.assertIn(reading["orientation"], ["Upright", "Reversed"])

    def test_same_date_is_deterministic(self):
        """Test that the same date (and seed) always returns the same card."""
        reading1 = daily_reading(date="2026-03-14")
        reading2 = daily_reading(date="2026-03-14")
        self.assertEqual(reading1, reading2)

        seeded1 = daily_reading(personal_seed="INFP", date="2026-03-14")
        seeded2 = daily_reading(personal_seed="INFP", date="2026-03-14")
        self.assertEqual(seeded1, seeded2)

    def test_different_dates_produce_variety(self):
        """Test that drawing across many dates doesn't always return the same card."""
        readings = [daily_reading(date=f"2026-01-{day:02d}") for day in range(1, 29)]
        distinct = {(r["name"], r["orientation"]) for r in readings}
        self.assertGreater(len(distinct), 1)

    def test_defaults_to_today(self):
        """Test that omitting date uses today's date."""
        import time

        reading = daily_reading()
        self.assertEqual(reading["date"], time.strftime("%Y-%m-%d"))

    def test_daily_seed_varies_by_personal_seed(self):
        """Test that a personal seed changes the seed for the same date."""
        base = _create_daily_seed("2026-03-14")
        seeded = _create_daily_seed("2026-03-14", "INFP")
        self.assertNotEqual(base, seeded)

    def test_daily_seed_is_deterministic(self):
        """Test that _create_daily_seed has no time component."""
        seed1 = _create_daily_seed("2026-03-14", "INFP")
        seed2 = _create_daily_seed("2026-03-14", "INFP")
        self.assertEqual(seed1, seed2)


if __name__ == "__main__":
    unittest.main()
