"""Madison Nitti"""
import unittest

from multiple_choice_card import MultipleChoiceCard


class TestMultipleChoiceCard(unittest.TestCase):
    """Test for MultipleChoiceCard class."""

    def setUp(self):
        """Initialize a MultipleChoiceCard instance for use in classes."""
        self.choices= {"a": "Caleb Woodson", "b": "Darius Taylor",
        "c": "Kyron Drones", "d": "Kaleb Spencer"}
        self.card= MultipleChoiceCard("What is the name of the "
        "current Virginia Tech quarterback?", "c", self.choices)

    def test_init(self):
        """Ensure MultipleChoiceCard initializes with correct attributes."""
        self.assertEqual(self.card.prompt, "What is the name of the "
        "current Virginia Tech quarterback?")
        self.assertEqual(self.card.response, "c")
        self.assertEqual(self.card.get_options(), ["a", "b",
                                                   "c", "d"])
    def test_check_answer_true_case(self):
        """Test that check_answer returns T for right answers."""
        self.assertTrue(self.card.check_answer("c"))
        self.assertTrue(self.card.check_answer("C"))

    def test_check_answer_false_case(self):
        """Test that check_answer returns F for wrong answers."""
        self.assertFalse(self.card.check_answer("d"))
        self.assertFalse(self.card.check_answer("no"))

if __name__ == "__main__":
    unittest.main()
