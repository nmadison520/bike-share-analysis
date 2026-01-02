"""Warning Test Class using unittest."""

import unittest

from warning import Warning


class TestWarning(unittest.TestCase):
    """Defining the Test Case."""
    def setUp(self):
        """Defining the default vars and values.

        Remember that setUp() is run before each test case.
        """
        self.warning = Warning("poetic")

    def test_generate1(self):
        """Tesing the sassy output."""
        self.warning.style = "sassy"
        result = self.warning.generate("Poe", "I am so lazy!")
        expected_value = "Poe says: "
        expected_value += "Just taking a spa day in the magma chamber. "
        expected_value += "Don't get too comfortable."
        self.assertEqual(result, expected_value)
    
    def test_generate_sassy_if(self):
        """Tesing the sassy output."""
        self.warning.style = "sassy"
        result = self.warning.generate("Poe", "I am so lazy!")
        expected_value = "Poe says: "
        expected_value += "Just taking a spa day in the magma chamber. "
        expected_value += "Don't get too comfortable."
        self.assertEqual(result, expected_value)

    def test_generate2(self):
        """Tesing the poetic output."""
        self.warning.style = "poetic"
        result = self.warning.generate("Poe", "eruption imminent")
        expected_value = "Poe whispers: "
        expected_value += "My fire stirs beneath the stone, prepare to flee, "
        expected_value += "leave me alone."
        self.assertEqual(result, expected_value)

    def test_generate3(self):
        """Tesing the poetic output."""
        self.warning.style = "poetic"
        result = self.warning.generate("Poe", "Working on it!")
        expected_value = "Poe hums: "
        expected_value += "I slumber deep, my rage asleep."
        self.assertEqual(result, expected_value)

    def test_generate4(self):
        """Tesing the poetic output."""
        result = self.warning.generate("Poe", "eruption imminent")
        expected_value = "Poe whispers: "
        expected_value += "My fire stirs beneath the stone, prepare to flee, "
        expected_value += "leave me alone."
        self.assertEqual(result, expected_value)

    def test_generate5(self):
        """Tesing the scientific output."""
        result = self.warning.generate("Poe", "eruption imminent")
        expected_value = "Poe whispers: "
        expected_value += "My fire stirs beneath the stone, prepare to flee, "
        expected_value += "leave me alone."
        self.assertEqual(result, expected_value)

if __name__ == '__main__':
    unittest.main(verbosity=2)
