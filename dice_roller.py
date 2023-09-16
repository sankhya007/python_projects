

import random

def roll_dice():
    return random.randint(1, 6)

if __name__ == "__main__":
    print("Welcome to the Python Dice Roller!")

    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print("You rolled a", result)

        play_again = input("Roll again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("Thank you for using the Python Dice Roller!")

