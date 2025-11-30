"""
Test cases for the CLI functionality.
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
from io import StringIO


class TestCLI(unittest.TestCase):
    def test_main_default_single_reading(self):
        """Test CLI with default arguments (single reading)."""
        with patch("sys.argv", ["tarot-reader"]):
            with patch("builtins.print") as mock_print:
                from src.__main__ import main

                main()
                mock_print.assert_called_once()
                output = mock_print.call_args[0][0]
                self.assertIsInstance(output, str)
                self.assertGreater(len(output), 0)

    def test_main_single_reading_explicit(self):
        """Test CLI with explicit single reading type."""
        with patch("sys.argv", ["tarot-reader", "--type", "single"]):
            with patch("builtins.print") as mock_print:
                from src.__main__ import main

                main()
                mock_print.assert_called_once()
                output = mock_print.call_args[0][0]
                self.assertIsInstance(output, str)

    def test_main_three_card_reading(self):
        """Test CLI with three-card reading type."""
        with patch("sys.argv", ["tarot-reader", "--type", "three"]):
            with patch("builtins.print") as mock_print:
                from src.__main__ import main

                main()
                mock_print.assert_called_once()
                output = mock_print.call_args[0][0]
                self.assertIsInstance(output, str)
                # Should contain Past, Present, Future
                self.assertIn("Past", output)
                self.assertIn("Present", output)
                self.assertIn("Future", output)

    def test_main_celtic_cross_reading(self):
        """Test CLI with Celtic Cross reading type."""
        with patch("sys.argv", ["tarot-reader", "--type", "celtic"]):
            with patch("builtins.print") as mock_print:
                from src.__main__ import main

                main()
                mock_print.assert_called_once()
                output = mock_print.call_args[0][0]
                self.assertIsInstance(output, str)

    def test_main_with_seed(self):
        """Test CLI with personal seed."""
        with patch("sys.argv", ["tarot-reader", "--seed", "INFP"]):
            with patch("builtins.print") as mock_print:
                from src.__main__ import main

                main()
                mock_print.assert_called_once()
                output = mock_print.call_args[0][0]
                self.assertIsInstance(output, str)

    def test_main_three_card_with_seed(self):
        """Test CLI with three-card reading and seed."""
        with patch("sys.argv", ["tarot-reader", "-t", "three", "-s", "ENFJ"]):
            with patch("builtins.print") as mock_print:
                from src.__main__ import main

                main()
                mock_print.assert_called_once()
                output = mock_print.call_args[0][0]
                self.assertIsInstance(output, str)

    def test_main_celtic_with_seed(self):
        """Test CLI with Celtic Cross and seed."""
        with patch("sys.argv", ["tarot-reader", "-t", "celtic", "-s", "O+"]):
            with patch("builtins.print") as mock_print:
                from src.__main__ import main

                main()
                mock_print.assert_called_once()
                output = mock_print.call_args[0][0]
                self.assertIsInstance(output, str)

    def test_main_version_flag(self):
        """Test CLI with version flag."""
        with patch("sys.argv", ["tarot-reader", "--version"]):
            with self.assertRaises(SystemExit) as cm:
                from src.__main__ import main

                main()
            self.assertEqual(cm.exception.code, 0)

    def test_main_short_options(self):
        """Test CLI with short option flags."""
        with patch("sys.argv", ["tarot-reader", "-t", "single", "-s", "test"]):
            with patch("builtins.print") as mock_print:
                from src.__main__ import main

                main()
                mock_print.assert_called_once()

    def test_main_invalid_type(self):
        """Test CLI with invalid reading type."""
        with patch("sys.argv", ["tarot-reader", "--type", "invalid"]):
            with self.assertRaises(SystemExit):
                from src.__main__ import main

                main()

    def test_seed_different_readings_over_time(self):
        """Test that seed produces different readings over time (time-influenced)."""
        import time

        # First reading
        with patch("sys.argv", ["tarot-reader", "-t", "single", "-s", "test123"]):
            with patch("builtins.print") as mock_print:
                # Need to reload the module to reset any caching
                import importlib
                import src.__main__

                importlib.reload(src.__main__)
                src.__main__.main()
                output1 = mock_print.call_args[0][0]

        # Small delay to ensure different timestamp
        time.sleep(0.01)

        # Second reading with same seed but different time
        with patch("sys.argv", ["tarot-reader", "-t", "single", "-s", "test123"]):
            with patch("builtins.print") as mock_print:
                import importlib
                import src.__main__

                importlib.reload(src.__main__)
                src.__main__.main()
                output2 = mock_print.call_args[0][0]

        # Due to time component, readings should be different
        # This is the expected behavior per the design
        self.assertNotEqual(output1, output2)


if __name__ == "__main__":
    unittest.main()
