"""Madison Nitti"""
class StudySession:
    """Manages/runs a flashcard study session"""

    def __init__(self, deck):
        """Initialize a new study session

        Arguments: deck: Deck object has all flashcards within.
        """
        self.deck= deck
        self.correct= 0
        self.total= 0
    def __str__(self):
        """Return string of progress of study session

        Returns: str: formatted string with %correct and message otherwise
        """
        if self.total==0:
            return "Study Session not started"
        percent= int(self.correct*100/self.total+0.5)
        #0.5 ensures that it is always rounded to nearest whole number,
        #doesn't only take floor division into account but also
        #the nearest whole number given that floor division
        #only rounds down
        return f"{percent}%"
    def start(self):
        """Start study session asks user with each flashcard

        Method iterates over each card, displays question using display method,
        accepts user input, and takes note of total q's and correct answers.
        """
        for card in self.deck.cards:
            card.display()
            self.total +=1
            user = input("Enter a letter as your answer: ").strip()
            if user == str(card.response).lower():
                print("Correct!")
                self.correct +=1
            else:
                print("Incorrect. Please try again.")
                letters = ", ".join(card.get_options())
                print(f"Answer Options: {letters}")
                user = input("Enter a letter as your answer: ").strip().lower()
                if user == str(card.response).lower():
                    print("Correct!")
                    self.correct +=1
                else:
                    print(f"Incorrect.  The correct answer is {card.response}. ")
        print()
        print(f"Correct: {self.correct}")
        print(f"Questions: {self.total}")
        percent=int(self.correct*100/self.total+0.5)
        print(f"Percent: {percent}%")
