import random
from colorama import init

def main():
    init()  # Initialize colorama for terminal colors
    print("\033[1;37mWelcome to \033[1;4m\033[1;31mHangman\033[0m\033[1;37m!")
    print("Guess the word letter by letter before you run out of attempts.")
    print("Correct guesses don't use attempts. \033[1;33m\033[1mGood luck!\033[0m")

    # Word list
    words = [
        "hangman", "random", "intern", "codealpha", "clothing",
        "computer", "python", "program", "glasses", "programming",
        "science", "internship", "friends", "coding", "biology",
        "algebra", "university", "guesses", "attempts"
    ]
    chosen_word = random.choice(words).lower()
    guessed_letters = []  # Track guessed letters
    word_guessed = ["-" for _ in chosen_word]  # Masked word representation
    attempts = 2  # Only two chances to guess the word

    # Game loop
    while attempts > 0 and "-" in word_guessed:
        print(f"\033[1;31m\nAttempts Remaining: {attempts}")
        print("\033[1;34mWord: " + "".join(word_guessed))

        player_guess = input("\033[1;37m\nType in a letter: ").lower()

        # Validate input
        if not player_guess.isalpha():
            print("Please enter a valid letter.")
            continue
        elif len(player_guess) != 1:
            print("Please enter only one letter.")
            continue
        elif player_guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(player_guess)

        # Check for correct guesses
        if player_guess in chosen_word:
            for idx, letter in enumerate(chosen_word):
                if letter == player_guess:
                    word_guessed[idx] = player_guess
        else:
            attempts -= 1  # Decrease attempts only on incorrect guesses

    # End of game results
    if "-" not in word_guessed:
        print(f"\n\033[1;4m\033[1;32mCongratulations\033[0m\033[1;37m! You guessed the word: {chosen_word}")
    else:
        print(f"\n\033[1;4m\033[1;31mYou lose\033[0m\033[1;37m! The word was: {chosen_word}")

    print("\033[1;33mThanks for playing Hangman! Goodbye!\033[0m")

if __name__ == "__main__":
    main()
