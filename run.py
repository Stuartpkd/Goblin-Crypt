# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Goblin Crypt

# Code for google api (For player score sheet)

import os
import gspread
import time
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

TABLET_ROOM = False
CRYSTAL_ROOM = False
CHEST_ROOM = False
GOBLIN_ROOM = False

# Goblin Language
GOBLIN_LANGUAGE = False

# Items
PLAYER_SWORD = ''
PLAYER_CRYSTAL = ''
PLAYER_KEY = ''


def print_with_delay(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


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
        if start_choice.lower().strip() == 's':
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
    player_class_choice = player_class_choice.lower().strip()
    
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
    if enter_dungeon.lower().strip() == "y":
        clear_screen()
        print("You descend the dungeon stairs, to the depths below.\n")
        break
    elif enter_dungeon.lower().strip() == "n":
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
    mainChamber_choice = mainChamber_choice.lower().strip()
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
        continue

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
        riddleOne = riddleOne.lower().strip()
        if riddleOne in ['candle', 'coffin', 'river']:
            break
        else:
            invalid_input()
            continue
    if riddleOne == 'river':
        RIDDLE_ONE = True   
    elif riddleOne == 'coffin' or riddleOne == 'candle':
        print('You hear a loud crunch from above your head')
        print('The ceiling begins to move towards you')
        print('The light begins to fade...\n')
        exit()

RIDDLE_ONE = True
if RIDDLE_ONE is True and CHEST_ROOM is False:
    clear_screen()
    print('The tablet weighs down the plate with a crisp click\n')
    print('You look to the next riddle:\n')
    while True:
        riddleTwo = input('I look taller when I am young. '
                          'As I grow old I become shorter. '
                          '(coffin, candle or river)\n')
        riddleTwo = riddleTwo.lower().strip()
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
            continue

RIDDLE_TWO = True
if RIDDLE_TWO is True and CHEST_ROOM is False:
    clear_screen()
    print('The tablet weighs down the plate with a crisp click\n')
    print('You look to the next riddle:\n')
    while True:
        riddleThree = input('Who makes it, has no need of it. '
                            'Who buys it, has no use for it. ' 
                            '(coffin, candle or river)\n')
        riddleThree = riddleThree.lower().strip()
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
            continue

RIDDLE_THREE = True
if RIDDLE_THREE is True and CHEST_ROOM is False:
    while True:
        TABLET_ROOM = False
        CRYSTAL_ROOM = True
        print('A large stone door reveals a tunnel with a red glow')
        print('You proceed onwards.')
        break
    

# Chest room choices

if CHEST_ROOM is True and TABLET_ROOM is False:
    while True:
        chestChoice = input('Do you open the chest? (y or n)\n')
        chestChoice = chestChoice.lower().strip()
        if chestChoice == 'y':
            print('You are greeted with a gleaming sword wrapped in cloth.\n')
            print('You place it onto your belt.\n')
            PLAYER_SWORD = 'held'
            GOBLIN_ROOM = True
            break
        elif chestChoice == 'n':
            print('You think it is probably best to leave it be')
            print('You continue onwards into the dungeon.\n')
            GOBLIN_ROOM = True
            break
        else:
            print('Invalid input, please try again.')
            continue

# Crystal room choices
if CRYSTAL_ROOM is True and CHEST_ROOM is False:
    while True:
        clear_screen()
        crystalChoice = input('After following the tunnel you come ' 
                              'to a large altar with a red crystal '
                              'hovering above it.\n '
                              'You feel yourself drawn towards it...\n'
                              'Do you take the crystal? (y or n)\n')
        crystalChoice = crystalChoice.lower().strip()
        if crystalChoice == 'y' and PLAYER_CLASS == 'mage':
            print('You clasp your hand around the crystal.\n '
                  'A powerful surge rockets through your body! '
                  'The knowledge and history of the goblins '
                  'begins rushing through your mind '
                  'Their culture and language is clear to you now.')
            GOBLIN_LANGUAGE = True
            GOBLIN_ROOM = True
            break
        elif (crystalChoice == 'y' and
              (PLAYER_CLASS == 'warrior' or PLAYER_CLASS == 'rogue')):
            print('You clasp your hand around the crystal.\n '
                  'A powerful surge rockets through your body! '
                  'Thousands of voices begin to pierce your mind,\n '
                  'unintelligable images and symbols burn into your eyes. '
                  'Your vision fails you and you fall to the floor.\n')
            exit()
        elif crystalChoice == 'n':
            print('Mother always said not to touch glowing crystals,\n'
                  'Best to move on.')
            GOBLIN_ROOM = True
            break
        else:
            invalid_input()
            continue

# Goblin room
if GOBLIN_ROOM is True:
    while True:
        print('As you approach the next room, you hear\n '
              'strange voices ahead.\n'
              'Pearing around the small doorway to the room,'
              'you see a group of goblins. They are gathered '
              'around a pile of gold.\n\n'
              'The room is covered in various trinkets and objects.\n'
              'These goblins clearly have a hoarding issue...\n\n'
              'You remain hidden in the doorway.')
        print('What shall you do? (1, 2, 3 or 4)\n\n'
              '1. Fight them?\n'
              '2. Sneak by them?\n'
              '3. Distract them?\n'
              '4. Speak to them?\n')
        goblinChoice = input()
        goblinChoice = goblinChoice.lower().strip()
        if (goblinChoice == '1' and 
           (PLAYER_CLASS == 'warrior' or PLAYER_SWORD == 'held')):
            print_with_delay('You dispatch the goblins with ease.\n'
                             'They are no match for your '
                             'fighting prowess.\n\n'
                             'With a flurry of blows and cuts they are '
                             'left lifeless on the ground.')
            break
        elif goblinChoice == '1':
            print_with_delay('You are quickly overwhelmed by the goblins.\n'
                             'They scratch and tear at you until you lose '
                             'balance and hit the floor.\n\n'
                             'The last thing you see is '
                             'them looting your bag.')
            break
        elif goblinChoice == '2' and PLAYER_CLASS == 'rogue':
            print_with_delay('Clinging to the edges of the room,'
                             'you make your way through the shadows.'
                             'The goblins continue to bicker over their gold.'
                             'You manage to reach the end of the room unseen.'
                             'Sneaking through the doorway, you '
                             'continue on through the dungeon.\n')
        else:
            invalid_input()
            continue

             
        

