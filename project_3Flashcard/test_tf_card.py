"""Madison Nitti"""
import unittest

from true_false_card import TrueFalseCard


class TestTrueFalseCard(unittest.TestCase):
    """Test for the TrueFalseCard class."""

    def test_init(self):
        """Makes sure that TrueFalseCard initializes with correct
        prompt, answer, and questions
        """
        card= TrueFalseCard("The current record of the "
        "Virginia Tech Football team is 2-4", "t")
        self.assertEqual(card.prompt, "The current record "
        "of the Virginia Tech Football team is 2-4")
        self.assertEqual(card.response, "t")
        self.assertEqual(card.get_options(), ["t", "f"])

    def test_check_answer_t(self):
        """Test that check_answer returns T for correct inputs."""
        card= TrueFalseCard("The current record of the "
        "Virginia Tech Football team is 2-4", "t")
        self.assertTrue(card.check_answer("t"))
        self.assertTrue(card.check_answer("T"))

    def test_check_answer_f(self):
        """Test that check_answer returns F for incorrect inputs."""
        card= TrueFalseCard("The current record of the "
        "Virginia Tech Football team is 2-4", "t")
        self.assertFalse(card.check_answer("f"))
        self.assertFalse(card.check_answer("F"))
if __name__ == "__main__":
    unittest.main()
