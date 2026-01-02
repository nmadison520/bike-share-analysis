"""Madison Nitti"""
from multiple_choice_card import MultipleChoiceCard


class TrueFalseCard(MultipleChoiceCard):
    """Initialize class of flashcards for T/F questions."""

    def __init__(self, question: str, answer: str):
        """Initialize a T/F card with a question and answer(correct)

        Arguments: question(str)- T/F question, answer(str)-correct answer("t" or "f")
        """
        choices= {"t": "true", "f": "false"}
        super().__init__(question, answer, choices)


