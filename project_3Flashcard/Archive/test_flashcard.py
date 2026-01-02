"""Madison Nitti"""
import unittest

from flashcard import Flashcard


class TestFlashcard(unittest.TestCase):
    """Unit test for flashcard class."""

    def test_init(self):
        """Make sure flashcard initializes prompt/response correctly."""
        card= Flashcard("What is the current ranking "
        "of the Virginia Tech Football team in the ACC?",
        "10")
        self.assertEqual(card.prompt, "What is the current"
        " ranking of the Virginia Tech Football team in"
        " the ACC?")
        self.assertEqual(card.response, "10")

    def test_str(self):
        """Make sure str method returns correct string formatted."""
        card= Flashcard("Answer", "response")
        self.assertEqual(str(card), "Answer: response")

    def test_check_answer_true_cases(self):
        """Test that check_answer returns T for correct answers."""
        card=Flashcard("What is my name?", "Madison")
        self.assertTrue(card.check_answer("madison"))
        self.assertTrue(card.check_answer("MADISON"))

    def test_check_answer_false_cases(self):
        """Test that check_answer returns F for wrong answer."""
        card= Flashcard("What is my name?", "Madison")
        self.assertFalse(card.check_answer("Taylor"))

    def test_display(self):
        """Make sure display prints correct question."""
        card= Flashcard("What is the VT mascot?", "Hokie")
        card.display()

    def test_get_options(self):
        """Make sure get_options returns expected list"""
        card=Flashcard("How are you?", "Good")
        self.assertEqual(card.get_options(), ["Fill "
        "in the blank"])

if __name__ == "__main__":
    unittest.main()
