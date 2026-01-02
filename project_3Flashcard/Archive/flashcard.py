"""Madison Nitti"""
class Flashcard:
    """A class showing a flashcard containing q&a."""

    def __init__(self, question: str, answer: str):
        """Initialize a flashcard object with a question and answer.

        Arguments: question(str): The prompt on the flashcard
        answer(str): The correct response for the flashcard
        """
        self.prompt = question
        self.response = answer
    def __str__(self) -> str:
        """Return a string representation of the flashcard and answer."""
        return f"Answer: {self.response}"
    def check_answer(self, user_input: str):
        """Check whether the user's input matches the flashcard.

        Arguments: user_input(str): The answer given by the user.
        Returns: Boolean True if the user's answer is correct,
        otherwise false.
        """
        if (user_input or "").lower()== (self.response or "").lower():
            return True
        else:
            return False
    def display(self):
        """Display the question for the flashcard."""
        print(f"Question: {self.prompt}")
    def get_options(self):
        """Return the answer options for the flashcard.

        Returns: list[str]: a list containing ["Fill in the blank"].
        """
        return["Fill in the blank"]
