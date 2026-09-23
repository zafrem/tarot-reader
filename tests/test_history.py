"""
Test cases for local Daily Tarot history persistence.
"""

import json
import tempfile
import unittest
from pathlib import Path

from src.history import record_daily_reading, get_daily_history
from src.core import daily_reading


class TestHistory(unittest.TestCase):
    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        self.history_path = Path(self._tmpdir.name) / "history.json"

    def tearDown(self):
        self._tmpdir.cleanup()

    def test_record_creates_file(self):
        """Test that recording a reading creates the history file."""
        self.assertFalse(self.history_path.exists())
        record_daily_reading(path=self.history_path)
        self.assertTrue(self.history_path.exists())

    def test_record_returns_the_saved_reading(self):
        """Test that record_daily_reading returns the reading it saved."""
        reading = record_daily_reading(path=self.history_path)
        self.assertIn("date", reading)
        self.assertIn("name", reading)

    def test_recorded_reading_matches_pure_computation(self):
        """Test that the saved reading matches what daily_reading() computes."""
        reading = record_daily_reading(path=self.history_path)
        expected = daily_reading(date=reading["date"])
        self.assertEqual(reading, expected)

    def test_same_day_overwrites_not_duplicates(self):
        """Test that calling twice the same day results in one history entry."""
        record_daily_reading(path=self.history_path)
        record_daily_reading(path=self.history_path)

        with open(self.history_path) as f:
            raw = json.load(f)
        self.assertEqual(len(raw), 1)

    def test_get_daily_history_empty_when_no_file(self):
        """Test that reading history from a nonexistent file returns empty list."""
        missing_path = Path(self._tmpdir.name) / "does-not-exist.json"
        self.assertEqual(get_daily_history(path=missing_path), [])

    def test_get_daily_history_sorted_by_date(self):
        """Test that get_daily_history returns entries sorted oldest to newest."""
        history = {
            "2026-03-01": daily_reading(date="2026-03-01"),
            "2026-01-15": daily_reading(date="2026-01-15"),
            "2026-02-10": daily_reading(date="2026-02-10"),
        }
        with open(self.history_path, "w") as f:
            json.dump(history, f)

        result = get_daily_history(path=self.history_path)
        dates = [r["date"] for r in result]
        self.assertEqual(dates, sorted(dates))

    def test_personal_seed_is_recorded(self):
        """Test that a personal seed produces a saved, personalized reading."""
        reading = record_daily_reading(personal_seed="INFP", path=self.history_path)
        expected = daily_reading(personal_seed="INFP", date=reading["date"])
        self.assertEqual(reading, expected)


if __name__ == "__main__":
    unittest.main()
