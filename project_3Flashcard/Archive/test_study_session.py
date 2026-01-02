"""Madison Nitti"""

import unittest
from io import StringIO
from unittest.mock import patch

from deck import Deck
from flashcard import Flashcard
from multiple_choice_card import MultipleChoiceCard
from study_session import StudySession
from true_false_card import TrueFalseCard


class TestStudySession(unittest.TestCase):
    """Test for study session, including input and output."""

    def setUp(self):
        """Build small card deck and StudySession."""
        self.deck= Deck()
        m_c= MultipleChoiceCard("What is the name of the current Virginia Tech "
        "quarterback?",
        "c",
        {"a": "Caleb Woodson", "b": "Darius Taylor",
        "c": "Kyron Drones", "d": "Kaleb Spencer"})
        t_f= TrueFalseCard("The current record of t1he Virginia Tech Football team "
        "is 2-4", "t")
        f_c= Flashcard("What is the current ranking of the Virginia Tech "
        "Football team in the ACC?", "10")
        self.deck.add_cards([m_c, t_f, f_c])
        self.session= StudySession(self.deck)

    def test_str_before(self):
        """__str__ should not start before session has begun."""
        self.assertEqual(str(self.session), "Study Session not started")
    @patch('builtins.input', side_effect=["a", "c",
            "t",
            "0", "0"])
    def test_start(self, mock_input):
        """For MCs, if wrong then correct, still counts.
        If TF correct once, counts as correct. If FC wrong twice,
        counts as incorrect. Then stores info and prints total q's
        asked, total q's correctly guessed, and percentage correct.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.session.start()
        output = fake_out.getvalue()
        self.assertIn("Correct: 2", output)
        self.assertIn("Questions: 3", output)
        self.assertIn("Percent: 67%", output)

        self.assertIn("Answer Options", output)
        self.assertEqual(str(self.session), "67%")
    @patch('builtins.input', side_effect=["c", "t", "10"])
    def test_correct_answers_100_(self, mock_input):
        """Answer guessed on first try get 100 percent."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.session.start()
            output=fake_out.getvalue()

        self.assertIn("Correct: 3", output)
        self.assertIn("Questions: 3", output)
        self.assertIn("Percent: 100%", output)
        self.assertIn(str(self.session), "100%")
if __name__ == "__main__":
    unittest.main()
