"""Madison Nitti"""
class Deck:
    """Class representing the card deck in study session."""

    def __init__(self):
        """Initialize deck object in empty list."""
        self.cards=[]
    def __str__(self):
        """Return a string listing all cards in deck.

        Cards shown with number and question.

        Returns: str(formatted string with cards and prompts)
        """
        result=[]
        for i, card in enumerate(self.cards, start=1):
            result.append(f"{i}. {card.prompt}")
        return "\n".join(result)
    def add_cards(self, cards):
        """Add flashcards to deck.

        Arguments: cards(list): list of flashcard objects to add.
        """
        self.cards.extend(cards)
