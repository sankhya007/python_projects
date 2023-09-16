


# import time

# def print_slow(str):
#     for letter in str:
#         print(letter, end='', flush=True)
#         time.sleep(0.03)
#     print()

# def intro():
#     print_slow("Welcome to the Adventure RPG!")
#     print_slow("You find yourself in a mysterious forest.")
#     print_slow("You need to find your way out and reach the safety of the village.")
#     print_slow("Good luck!")

# def forest():
#     print_slow("You are in the forest.")
#     print_slow("You see three paths: left, right, and straight ahead.")
#     print_slow("Which path do you choose? (left/right/straight)")

#     choice = input().lower()

#     if choice == 'left':
#         print_slow("You encounter a friendly squirrel.")
#         print_slow("It guides you to a river.")
#         river()
#     elif choice == 'right':
#         print_slow("You find a hidden cave.")
#         print_slow("You enter the cave.")
#         cave()
#     elif choice == 'straight':
#         print_slow("You decide to forge ahead.")
#         print_slow("After walking for a while, you come across an abandoned campsite.")
#         print_slow("Do you want to investigate the campsite? (yes/no)")

#         choice = input().lower()
#         if choice == 'yes':
#             print_slow("You find a map that helps you navigate through the forest.")
#             print_slow("You continue on your journey.")
#             forest()
#         elif choice == 'no':
#             print_slow("You ignore the campsite and continue walking.")
#             print_slow("You encounter a group of wild animals, but manage to scare them away.")
#             print_slow("You continue on your journey.")
#             village()
#         else:
#             print_slow("Invalid choice. Please try again.")
#             forest()
#     else:
#         print_slow("Invalid choice. Please try again.")
#         forest()

# def river():
#     print_slow("You arrive at the river.")
#     print_slow("You can either swim across or look for a bridge.")
#     print_slow("What would you like to do? (swim/bridge)")

#     choice = input().lower()

#     if choice == 'swim':
#         print_slow("You attempt to swim across.")
#         print_slow("Oh no! The current is too strong and you are swept away.")
#         print_slow("Game over.")
#     elif choice == 'bridge':
#         print_slow("You find a sturdy bridge and safely cross the river.")
#         print_slow("You continue on your journey.")
#         village()
#     else:
#         print_slow("Invalid choice. Please try again.")
#         river()

# def cave():
#     print_slow("You enter the dark cave.")
#     print_slow("It's very dark and you can't see much.")
#     print_slow("You can either use a torch or go back.")

#     choice = input().lower()

#     if choice == 'torch':
#         print_slow("You light your torch and explore the cave.")
#         print_slow("You find a secret passage that leads you outside of the cave.")
#         print_slow("You continue on your journey.")
#         village()
#     elif choice == 'go back':
#         print_slow("You decide to go back to the forest.")
#         forest()
#     else:
#         print_slow("Invalid choice. Please try again.")
#         cave()

# def village():
#     print_slow("You arrive at the village.")
#     print_slow("Congratulations! You have successfully reached safety.")
#     print_slow("Thanks for playing!")

# # Start the game
# intro()
# forest()














#pokemon story 


import time

def print_slow(str):
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(0.03)
    print()

def intro():
    print_slow("Welcome to the Pokemon Adventure RPG!")
    print_slow("You are a Pokemon Trainer on a quest to capture the legendary Celestial Dragonite.")
    print_slow("Rumors suggest that it resides deep within the mystical Evershadow Forest.")
    print_slow("May your Pokeballs be true and your journey victorious!")

def forest():
    print_slow("You enter the heart of Evershadow Forest, a realm of mystery and wonder.")
    print_slow("You see three paths: 'The Leafy Trail', 'The Dark Cave', and 'The Enchanted Glade'.")
    print_slow("Which path do you choose? (trail/cave/glade)")

    choice = input().lower()

    if choice == 'trail':
        print_slow("You take The Leafy Trail, where Pokemon chatter fills the air.")
        leafy_trail()
    elif choice == 'cave':
        print_slow("You venture into The Dark Cave, a place where rare Pokemon are said to hide.")
        dark_cave()
    elif choice == 'glade':
        print_slow("You step into The Enchanted Glade, where a serene aura surrounds you.")
        enchanted_glade()
    else:
        print_slow("Invalid choice. Please try again.")
        forest()

def leafy_trail():
    print_slow("The Leafy Trail is alive with rustling leaves and the calls of wild Pokemon.")
    print_slow("You encounter a Pikachu playing in the leaves and a path leading to a waterfall.")
    print_slow("Which path would you like to take? (pikachu/waterfall)")

    choice = input().lower()

    if choice == 'pikachu':
        print_slow("You approach the Pikachu and try to befriend it.")
        pikachu_encounter()
    elif choice == 'waterfall':
        print_slow("You follow the path to the waterfall, seeking adventure.")
        waterfall_adventure()
    else:
        print_slow("Invalid choice. Please try again.")
        leafy_trail()

def dark_cave():
    print_slow("The Dark Cave is dimly lit, and the echoes of mysterious cries reverberate.")
    print_slow("You come across a branching path: 'The Abyssal Depths' and 'The Luminous Crystals'.")
    print_slow("Which way would you like to go? (depths/crystals)")

    choice = input().lower()

    if choice == 'depths':
        print_slow("You venture into The Abyssal Depths, braving the darkness.")
        abyssal_depths()
    elif choice == 'crystals':
        print_slow("You explore The Luminous Crystals, captivated by their glow.")
        luminous_crystals()
    else:
        print_slow("Invalid choice. Please try again.")
        dark_cave()

def enchanted_glade():
    print_slow("The Enchanted Glade is a place of peace and beauty.")
    print_slow("You notice a Celebi flying gracefully and a path leading to a mysterious shrine.")
    print_slow("Which feature would you like to explore? (celebi/shrine)")

    choice = input().lower()

    if choice == 'celebi':
        print_slow("You follow Celebi in awe, hoping for a glimpse of the legendary Pokemon.")
        celebi_encounter()
    elif choice == 'shrine':
        print_slow("You visit the mysterious shrine, intrigued by its ancient design.")
        shrine_mystery()
    else:
        print_slow("Invalid choice. Please try again.")
        enchanted_glade()

# ... Implement other steps and encounters

# Implement additional steps and encounters based on the chosen paths.

def pikachu_encounter():
    # Implement the story for encountering Pikachu
    pass

def waterfall_adventure():
    # Implement the story for the waterfall adventure
    pass

def abyssal_depths():
    # Implement the story for venturing into the abyssal depths
    pass

def luminous_crystals():
    # Implement the story for exploring the luminous crystals
    pass

def celebi_encounter():
    # Implement the story for encountering Celebi
    pass

def shrine_mystery():
    # Implement the story for the mysterious shrine
    pass

# Start the game
intro()
forest()
