import random

def display_word(word, guesses):
    """
    Displays the current state of the word with guessed characters and blanks for unguessed characters.
    """
    return ' '.join(char if char in guesses else '_' for char in word)

def hangman():
    """
    Main function to play the Hangman game.
    """
    # Introduction
    name = input("What is your name? ")
    print(f"Good Luck, {name}!")

    # List of words
    words = [
        'rainbow', 'computer', 'science', 'programming',
        'python', 'mathematics', 'player', 'condition',
        'reverse', 'water', 'board', 'geeks'
    ]

    # Randomly select a word
    word = random.choice(words)

    # Initialize game variables
    guesses = set()
    turns = 12

    print("Guess the characters")

    while turns > 0:
        # Display current state of the word
        print(display_word(word, guesses))

        # Check if the user has won
        if '_' not in display_word(word, guesses):
            print("Congratulations, You Win!")
            print(f"The word was: {word}")
            break

        # Get user input
        guess = input("Guess a character: ").lower()

        # Validate input
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        # Update guesses
        if guess in guesses:
            print("You already guessed that letter.")
            continue

        guesses.add(guess)

        # Check if guess is correct
        if guess not in word:
            turns -= 1
            print(f"Wrong guess. You have {turns} more guesses.")
        else:
            print("Good guess!")

        # Check if the user has lost
        if turns == 0:
            print(f"Game Over. The word was: {word}")

if __name__ == "__main__":
    hangman()
