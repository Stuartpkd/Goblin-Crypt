# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Goblin Crypt

# Code for google api (For player score sheet)

import os
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


PORT = 8000
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('goblin-crypt')

# Classes
PLAYER_CLASS = ''

# Rooms
global TABLET_ROOM
TABLET_ROOM = False

CHEST_ROOM = False

# Riddles
global RIDDLE_ONE
RIDDLE_ONE = False
global RIDDLE_TWO
RIDDLE_TWO = False
global RIDDLE_THREE
RIDDLE_THREE = False

# Items
PLAYER_SWORD = ''
PLAYER_CRYSTAL = ''
PLAYER_KEY = ''


def clear_screen():
    """
    Clears the terminal screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def game_over():
    """
    Prints game over to the player
    Resets values and then starts game if yes
    Ends program if no.
    """
    print('GAMEOVER')
    play_again = input('Would you like to try again? (y/n)')
    if play_again == 'y':
        start_game()
    elif play_again == 'n':
        exit()
    else:
        print('Invalid input, please try again') 


def start_game():
    """
    Function that shows player start game choice.
    Validates input and then starts game.
    """
    print("******* Goblin - Crypt ********")
    print("******* Enter S to start the game ********")
    while True:
        start_choice = input()
        if start_choice.lower() == 's':
            clear_screen()
            break
        else:
            print("Invalid choice. Please enter 's' to start the game.")


def invalid_input():
    """
    Function for printing invalid choice
    """
    print("Invalid choice, please try again")
    

def no_choice():
    """
    Function printing empty input
    """
    print('You did not enter anything, please try again.')
      

start_game()

# User inputs their name
while True:
    player_name = input('Adventurer, what is your name? (5 - 12 characters): ')
    if len(player_name) <= 4 or len(player_name) >= 13 or player_name == '':
        clear_screen()
        print('Invalid name length, please try again.')
    else:
        break

# Class choice for player
while True:
    print("1. Warrior\n")
    print("2. Mage\n")
    print("3. Rogue\n")  
    player_class_choice = input(f"Well then, {player_name} what kind "
                                "of adventurer are you? (1, 2 or 3)\n\n")
    
    if player_class_choice == '1':
        PLAYER_CLASS = 'warrior'
        break
       
    elif player_class_choice == '2':
        PLAYER_CLASS = 'mage'
        break
        
    elif player_class_choice == '3':
        PLAYER_CLASS = 'rogue'
        break
        
    else:
        invalid_input()

# Introduction to dungeon
while True:
    clear_screen()
    if PLAYER_CLASS == 'warrior':
        print("Ah, a mighty warrior.\n")
    elif PLAYER_CLASS == 'mage':
        print("Ah, a wise mage.\n")
    elif PLAYER_CLASS == 'rogue':
        print('Ah, a cunning rogue.\n')
    else:
        break
    enter_dungeon = input("You step out of the dark woods "
                          "and into a clearing.\n "
                          "Your eyes take a moment "
                          "to adjust to the sudden brightness, "
                          "and you inhale deeply, filling your "
                          "lungs with the crisp, fresh air.\n "
                          "Ahead of you looms the entrance to "
                          "a dungeon, the stone walls slick "
                          "with moisture and the musty scent of decay.\n "
                          "Will you be brave enough to venture "
                          "into the depths of the dungeon, "
                          "or will you turn back and seek refuge "
                          "in the safety of the woods? (y or n)\n")
    if enter_dungeon.lower() == "y":
        clear_screen()
        print("You descend the dungeon stairs, to the depths below.\n")
        break
    elif enter_dungeon.lower() == "n":
        clear_screen()
        print("You return home and live a very long and boring life.\n")
        exit()   
    else:
        print("Invalid choice, please try again.")

# Main chamber choices (Tunnels 1 - 3)
while True:
    clear_screen()
    mainChamber_choice = input("You enter the first chamber of the dungeon. " 
                               "Ahead of you are three identical " 
                               "stairways leading down. " 
                               "The light from torches mounted on the " 
                               "walls flickers, casting an eerie "
                               "glow on the stairs. " 
                               "The heat emanating from the " 
                               "torches is palpable, " 
                               "making the air thick and heavy. Choose "
                               "your path carefully. (1, 2, or 3)\n")
    if mainChamber_choice == "1":
        print("You make your way down the first stairs. " 
              "You feel one of the steps sink " 
              "lower than the others, " 
              "as a poison dart is released " 
              "from a nearby wall.\n")
        exit()
        
    elif mainChamber_choice == "2":
        print("You cautously move down the second stairs. " 
              "Your steps echo against the damp stone walls." 
              "Bending down through an archway, you are met " 
              "with a large altar with 3 texts carved into its stone. " 
              "Each.\n")
        TABLET_ROOM = True
        break
    elif mainChamber_choice == "3":
        print("The stairs lead down to a dusty room " 
              "The air is cold and dank. " 
              "You see a chest in the middle of the room, " 
              "decomposed skeletons are littered around it. " 
              "from a nearby wall.")
        CHEST_ROOM = True
        break
    else:
        print("Invalid answer, please try again.")

# Riddle room choices

if TABLET_ROOM is True and CHEST_ROOM is False:
    print('3 small tablets are laid out in front of you.')
    print('Each has an engraving carved into it.')
    print('You see a river, a candle and a coffin')
    print('Below each riddle is a plate for each tablet.')
    print('Solve each riddle and place the tablets correctly.\n')
    print("Riddle 1: I have a bed but don't sleep, a bank but no money.\n")
    

if TABLET_ROOM is True and CHEST_ROOM is False:
    while True:
        riddleOne = input('Which tablet do you place here? ' 
                          '(coffin, candle or river)\n')
        riddleOne = riddleOne.lower()
        if riddleOne in ['candle', 'coffin', 'river']:
            break
        else:
            invalid_input()
    if riddleOne == 'river':
        RIDDLE_ONE = True   
    elif riddleOne == 'coffin' or riddleOne == 'candle':
        print('You hear a loud crunch from above your head')
        print('The ceiling begins to move towards you')
        print('The light begins to fade...\n')
        exit()

if RIDDLE_ONE is True and CHEST_ROOM is False:
    clear_screen()
    print('The tablet weighs down the plate with a crisp click\n')
    print('You look to the next riddle:\n')
    while True:
        riddleTwo = input('I look taller when I am young. '
                          'As I grow old I become shorter. '
                          '(coffin, candle or river)\n')
        riddleTwo = riddleTwo.lower()
        if riddleTwo in ['candle', 'coffin', 'river']:
            break
        elif riddleTwo == 'candle':
            RIDDLE_TWO = True
        elif riddleTwo == 'coffin' or 'river':
            print('You hear a loud crunch from above your head')
            print('The ceiling begins to move towards you')
            print('The light begins to fade...')
            exit()
        else:
            invalid_input()

RIDDLE_TWO = True
if RIDDLE_TWO is True and CHEST_ROOM is False:
    clear_screen()
    print('The tablet weighs down the plate with a crisp click\n')
    print('You look to the next riddle:\n')
    while True:
        riddleThree = input('Who makes it, has no need of it. '
                            'Who buys it, has no use for it. ' 
                            '(coffin, candle or river)\n')
        riddleThree = riddleThree.lower()
        if riddleThree in ['candle', 'coffin', 'river']:
            break
        elif riddleThree == 'coffin':
            print('The tablet weighs down the plate with a crisp click')
            RIDDLE_THREE = True
            break
        elif riddleThree == 'candle' or 'river':
            print('You hear a loud crunch from above your head')
            print('The ceiling begins to move towards you')
            print('The light begins to fade...')
            exit()
        else:
            invalid_input()

RIDDLE_THREE = True
if RIDDLE_THREE is True and CHEST_ROOM is False:
    while True:
        TABLET_ROOM = False
        print('A large stone door reveals a tunnel with a red glow')
        print('You proceed onwards.')
        break
    

# Chest room choices

if CHEST_ROOM is True and TABLET_ROOM is False:
    while True:
        clear_screen()
        chestChoice = input('Do you open the chest? (y or n)\n')
        chestChoice = chestChoice.lower()
    if chestChoice == 'y':
        print('You are greeted with a gleaming sword wrapped in cloth.\n')
        print('You place it onto your belt.\n')
        PLAYER_SWORD = 'held'
    elif chestChoice == 'n':
        print('You think it is probably best to leave it be')
        print('You continue onwards into the dungeon.\n')
    else:
        print('Invalid input, please try again.')

