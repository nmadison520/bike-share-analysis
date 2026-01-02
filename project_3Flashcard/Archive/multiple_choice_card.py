"""Madison Nitti"""
from flashcard import Flashcard


class MultipleChoiceCard(Flashcard):
    """Flashcard representing multiple choice question."""

    def __init__(self, question: str, answer: str, choices: dict):
        """Initialize a MultipleChoiceCard.

        Arguments: question(str), question text, answer(str), choices(dict)
        """
        super().__init__(question, answer)
        self.choices = choices
#__str__ is already inherited
#check_answer() is already inherited
#no need to rewrite these due to inheritance
    def display(self):
        """Display question and all mc options."""
        super().display()
        for label, choice in self.choices.items():
            print(f"{label}: {choice}")
    def get_options(self):
        """Return list of possible answer labels.

        Returns: list of option keys a-d.
        """
        return list(self.choices.keys())
