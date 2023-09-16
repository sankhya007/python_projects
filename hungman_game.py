
import random

# List of words for the game
words = ["python", "java", "javascript", "ruby", "html", "css", "php", "cplusplus", "swift", "kotlin","apple","banana","fruits","hello","what"]

def choose_word():
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nAttempts left:", attempts)
        displayed_word = display_word(word_to_guess, guessed_letters)
        print("Current word:", displayed_word)
        guessed_letters_str = ', '.join(guessed_letters)
        print("Guessed letters:", guessed_letters_str)

        guess = input("Enter a letter or the full word guess: ").lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess!")
                attempts -= 1
                guessed_letters.append(guess)
        elif len(guess) == len(word_to_guess) and guess.isalpha():
            if guess == word_to_guess:
                print("Congratulations! You guessed the word!")
                return
            else:
                print("Incorrect guess!")
                attempts -= 1
        else:
            print("Invalid input. Please enter a valid letter or the full word guess.")

    print("You ran out of attempts! The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()


