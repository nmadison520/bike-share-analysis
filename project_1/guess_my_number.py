"""Guess my number game.

The purpose of this game is to allow the user to guess a pseudo-random
number between 1 and 99, consisting of 2 guesses by the player and a
randomly drawn action card from a deck of 52 cards.  The cycle will repeat
until the correct number is guessed.  The card itself may provide hints,
change the target number, or potentially reveal the answer.

Author: Madison Nitti.
"""
import random


def game_intro():
    """Displays the game rules and instructions to the player."""
    print("""This is a console-based guessing game where the player tries to " \
    "guess a psuedo-randomly generated number between 1 and 99." \
    "This game will be structured in rounds, each consisting of " \
    "Two guesses by the player, and a randomly drawn action card from a " \
    "deck of 52 cards. This card may provide hints, change the target" \
    "number, or even reveal the answer. The cycle repeats until the " \
    "player correctly guesses the number""")
    print("Input a number between the values of 1 and 99, including 99. ")
    print("Be sure to entire only whole numbers, without decimals.")

def computer_number():
    #creates a list of cards- numbers as the number on each card
    """Generates a pseudo-random integer from 1 to 99 for the player to guess."""
    #creates a random list of cards from 1-99
    return random.randint(1,99)

def player_number():
    """Prompts the player to enter a guess and returns their number as an integer."""
    return int(input("Enter your guess from 1-99: "))

def number_feedback(guess, winNum):
    """This compares the player's guessing number to the target number.

    It offers advice of what's wrong if incorrect.
    """
    if guess > winNum:
        print("Too High")
    elif guess < winNum:
        print("Too Low")
    #else- instructions say to do nothing, so no code needed

def card_feedback(d_cards, num):
    """This function will offer feedback and output cards based on 6 various tests.

    'New number' will print the name, the pseudo-randomly generated number, and the new
    value.
    'Starts with' will print the name, the pseudo-random integer, and the new value that
    it starts with.
    'Sum of digits' will print the name, and the sum of the digits.
    'I love python' will print the name with no change to the code itself.
    'Divisible by 3' will print the name, and whether the target number is divisible by
    3.
    'Winner!' will show the number.
    """
     # this will make every input string lowercase to fix case-sensitive issues.
    card= random.choice(d_cards)
    lc = card.lower()

    if "new number" in lc:
        print("New Number")
        num = random.randint(1, 99)
    elif "starts with" in lc:
        print(f"Starts With {str(num)[0]}")
    elif "sum of digits" in lc:
        print(f"Sum of digits {sum(int(d) for d in str(num))}")
    elif "divisible by 3" in lc:
        if num % 3 == 0:
            print("Divisible by 3: Yes")
        else:
            print("Divisible by 3: No")
    elif "i love python" in lc:
        print("I Love Python")
    elif "winner" in lc:
        print("Winner!")
        print(num)
    else:
        print(card)

    return int(num)


def main():
    """Controls the overall game flow.

    Initialization, guessing loop, card drawing, and win condition.
    """
    # Step 1: Ouput the instructions to the player
    game_intro()
    # create list for the cards
    cards= ['New Number', 'Starts With', 'Sum of Digits', 'Divisible by 3',
            'I Love Python']
    deck = random.choices(cards, [.2, .2, .15, .25, .3], k=51)
    deck.append('Winner!')

    target= computer_number()

    while True:
        for _ in range(2):
            #this ensures that 2 guesses will occur per round rather than just only one.
            guess = player_number()
            if guess == target:
                print("Correct!")
                return
            number_feedback(guess, target)
            #gives feedback based on the guess and draws a card following 2 wrong.
        target = card_feedback(deck, target)

# Do not change or add anything below
if '__main__' == __name__:
    main()
