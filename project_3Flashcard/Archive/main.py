"""Madison Nitti"""

from deck import Deck
from flashcard import Flashcard
from multiple_choice_card import MultipleChoiceCard
from study_session import StudySession
from true_false_card import TrueFalseCard


def main():
    """Run the flashcard study session."""
    #This creates three example cards with questions
    #It uses code from flashcard.py, multiple_choice_card
    #.py, and true_false_card.py to test each program,
    #and generate a response based on these cards
    card_1= TrueFalseCard(
        "The current record of the Virginia Tech Football team "
        "is 2-4",
        "t"
    #card_1 used the TrueFalseCard import, and asked
    #a question, where the user will either choose true
    #or false. The code will provide an output as to whether
    #they are correct
    )
    card_2= MultipleChoiceCard(
        "What is the name of the current Virginia Tech "
        "quarterback?",
        "c",
        {"a": "Caleb Woodson", "b": "Darius Taylor",
        "c": "Kyron Drones", "d": "Kaleb Spencer"}
    )
    #card_2 used the MultipleChoiceCard, where
    #the computer will ask a question, and the user
    #will enter a reponse based on the options provided.
    #The code will provide feedback as to whether the
    #answer listed is correct.
    card_3= Flashcard(
        "What is the current ranking of the Virginia Tech "
        "Football team in the ACC?",
        "10"
    )
    #card_3 used the FlashCard import, and the computer
    #will ask for a response from the user, and then
    #feedback will be provided for correctness.

    #this constructs a deck, and the cards that will
    #be used in the deck
    deck = Deck()
    deck.add_cards([card_1, card_2, card_3])

    #this begins a study session using the
    #study session imported program
    session= StudySession(deck)
    session.start()

    #this displays the overview of the code
    #that was run
    print("\nThis is an overview of the Study Session: ")
    print(session)

if __name__ == "__main__":
    main()
