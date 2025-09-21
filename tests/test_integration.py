"""
Integration tests for the tarot_reader package.
"""

import unittest
import json
from tarot_reader import draw_single, draw_three, celtic_cross


class TestIntegration(unittest.TestCase):
    def test_package_imports(self):
        """Test that the package imports work correctly."""
        # Test that all main functions are importable
        from tarot_reader import draw_single, draw_three, celtic_cross

        # Test that functions are callable
        self.assertTrue(callable(draw_single))
        self.assertTrue(callable(draw_three))
        self.assertTrue(callable(celtic_cross))

    def test_json_serializable_output(self):
        """Test that all reading outputs are JSON serializable (FR-5)."""
        # Test single card
        card = draw_single()
        json_str = json.dumps(card)
        self.assertIsInstance(json_str, str)

        # Test three card spread
        reading = draw_three()
        json_str = json.dumps(reading)
        self.assertIsInstance(json_str, str)

        # Test Celtic Cross
        reading = celtic_cross()
        json_str = json.dumps(reading)
        self.assertIsInstance(json_str, str)

    def test_example_usage_single_draw(self):
        """Test the example usage from SRS for single draw."""
        card = draw_single()

        # Should be able to access name and meaning as shown in example
        name_and_orientation = f"{card['name']} ({card['orientation']})" if card['orientation'] == 'Reversed' else card['name']
        meaning = card['meaning']

        self.assertIsInstance(name_and_orientation, str)
        self.assertIsInstance(meaning, str)
        self.assertGreater(len(name_and_orientation), 0)
        self.assertGreater(len(meaning), 0)

    def test_example_usage_three_card(self):
        """Test the example usage from SRS for three-card spread."""
        reading = draw_three()

        # Should be able to iterate as shown in example
        for pos, card in reading.items():
            position_info = f"{pos}: {card['name']} - {card['meaning']}"
            self.assertIsInstance(position_info, str)
            self.assertIn(pos, ["Past", "Present", "Future"])

    def test_example_usage_celtic_cross(self):
        """Test the example usage from SRS for Celtic Cross."""
        reading = celtic_cross()

        # Should be able to iterate as shown in example
        position_count = 0
        for pos, card in reading.items():
            position_count += 1
            position_info = f"{pos}: {card['name']} - {card['meaning']}"
            self.assertIsInstance(position_info, str)

        self.assertEqual(position_count, 10)

    def test_no_external_dependencies(self):
        """Test that the package works without external dependencies."""
        # This test passes if the imports and function calls work
        # since we've designed the package to use only standard library
        try:
            card = draw_single()
            reading = draw_three()
            celtic = celtic_cross()
            self.assertTrue(True)  # If we get here, no external deps were needed
        except ImportError as e:
            self.fail(f"Package requires external dependency: {e}")

    def test_entertainment_disclaimer_data(self):
        """Test that the package includes entertainment disclaimer."""
        import tarot_reader
        docstring = tarot_reader.__doc__

        # Check that the docstring mentions entertainment
        self.assertIsNotNone(docstring)
        self.assertIn("entertainment", docstring.lower())

    def test_consistent_card_structure(self):
        """Test that all readings return cards with consistent structure."""
        # Get cards from all reading types
        single_card = draw_single()
        three_cards = list(draw_three().values())
        celtic_cards = list(celtic_cross().values())

        all_cards = [single_card] + three_cards + celtic_cards

        for card in all_cards:
            # All cards should have these required fields
            self.assertIn("name", card)
            self.assertIn("orientation", card)
            self.assertIn("meaning", card)

            # All values should be strings
            self.assertIsInstance(card["name"], str)
            self.assertIsInstance(card["orientation"], str)
            self.assertIsInstance(card["meaning"], str)

            # Values should not be empty
            self.assertGreater(len(card["name"]), 0)
            self.assertGreater(len(card["orientation"]), 0)
            self.assertGreater(len(card["meaning"]), 0)

            # Orientation should be valid
            self.assertIn(card["orientation"], ["Upright", "Reversed"])


if __name__ == "__main__":
    unittest.main()