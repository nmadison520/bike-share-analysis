"""Madison Nitti"""
import unittest
from deck import Deck
from flashcard import Flashcard


class TestDeck(unittest.TestCase):
    """Test for Deck class."""

    def test_add_cards(self):
        """Test that cards have been added to deck correctly."""
        deck= Deck()
        card_1= Flashcard("Q1", "A1")
        card_2= Flashcard("Q2", "A2")
        deck.add_cards([card_1, card_2])
        self.assertEqual(len(deck.cards), 2)
        self.assertEqual(deck.cards[0], card_1)
        self.assertEqual(deck.cards[1], card_2)
    def test_str(self):
        """Test that deck's string is in correct format."""
        deck= Deck()
        deck.add_cards([Flashcard("Q1", "A1"), Flashcard("Q2", "A2")])
        expected_output= "1. Q1\n2. Q2"
        self.assertEqual(str(deck), expected_output)
if __name__ == "__main__":
    unittest.main()
