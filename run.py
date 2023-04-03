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

puzzleRoomPieces = ['coffin', 'candle', 'river']
playerPuzzleInvt = []
riddlePartOne = False
riddlePartTwo = False
riddlePartThree = False
items = ['crystal', 'Sword', 'key']
playerInventory = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def gameOver():
    print('GAMEOVER')


print("******* Goblin Crypt ********")
print("******* Enter S to start the game ********")

while True:
    start_choice = input()
    if start_choice.lower() == 's':
        clear_screen()
        break
    else:
        print("Invalid choice. Please press 's' to start the game.")

while True:
    player_name = input('Adventurer, what is your name? (5 - 12 characters): ')
    if len(player_name) <= 4 or len(player_name) >= 13:
        print('Invalid name length, please try again.')
        if (player_name) == '':
            print('You must have a name? Please try again.')
    else:
        break

while True:
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")  
    player_class = input(f"Well then, {player_name} what kind "
                         "of adventurer are you?")
    
    if player_class == '1':
        print('Ah, a mighty warrior')
        clear_screen()
        break
        
    elif player_class == '2':
        print('Ah, a wise mage')
        break
        
    elif player_class == '3':
        print('Ah, a cunning burglar')
        break
        
    else:
        print('Invalid answer, please try again')
        break

while True:
    enter_dungeon = input("You step out of the dark woods " 
                          "and into a clearing. " 
                          "Your eyes take a moment " 
                          "to adjust to the sudden brightness, " 
                          "and you inhale deeply, filling your " 
                          "lungs with the crisp, fresh air. " 
                          "Ahead of you looms the entrance to "
                          "a dungeon, the stone walls slick " 
                          "with moisture and the musty scent of decay " 
                          "hanging heavy in the air. " 
                          "You can hear the faint sound of dripping water and "
                          "the echo of footsteps coming from within. " 
                          "Will you be brave enough to venture " 
                          "into the depths of the dungeon, " 
                          "or will you turn back and seek refuge " 
                          "in the safety of the woods?")
    if enter_dungeon.lower() == "y":
        print("You descend the dungeon stairs, to the depths below.")
        break
    elif enter_dungeon.lower() == "n":
        print("You return home and live a very long and boring life.")
        break
    else:
        print("Invalid choice, please try again.")

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
                               "your path carefully.")
    if mainChamber_choice == "1":
        print("You make your way down the first stairs. " 
              "You feel one of the steps sink " 
              "lower than the others, " 
              "as a poison dart is released " 
              "from a nearby wall.")
        break
    elif mainChamber_choice == "2":
        print("You cautously move down the second stairs. " 
              "Your steps echo against the damp stone walls." 
              "Bending down through an archway, you are met " 
              "with a large altar with 3 texts carved into its stone. " 
              "Each .")
        break
    elif mainChamber_choice == "3":
        print("You make your way down the first stairs. " 
              "You feel one of the steps sink " 
              "lower than the others, " 
              "as a poison dart is released " 
              "from a nearby wall.")
        break
    else:
        print("Invalid answer, please try again.")

while True:
    if mainChamber_choice == "2":
        print('3 small tablets are laid out in front of you.')
        print('Each has an engraving carved into it.')
        print('You see a river, a candle and a coffin')
        print('Below each riddle is a plate for each tablet.')
        print('Solve each riddle and place the tablets correctly.\n\n')
        print("Riddle 1: I have a bed but don't sleep, a bank but no money.")
    break

while True:
    riddleOne = input('Which tablet do you place here?')
    if riddleOne == 'river':
        print('The tablet weighs down the plate with a crisp click')
        riddlePartOne = True
        break
    elif riddleOne == 'coffin' or riddleOne == 'candle':
        print('You hear a loud crunch from above your head')
        print('The ceiling begins to move towards you')
        print('The light begins to fade...')
        break
    else:
        print('Invalid input, please try again.')      

while True:
    if riddlePartOne is True:
        riddleTwo = input('I look taller when I am young. '
                          'As I grow old I become shorter.')
        if riddleTwo == 'candle':  
            print('The tablet weighs down the plate with a crisp click')
            riddlePartTwo = True
            break
        elif riddleTwo == 'coffin' or 'river':
            print('You hear a loud crunch from above your head')
            print('The ceiling begins to move towards you')
            print('The light begins to fade...')
            break
        else:
            print('Incorrect answer, please try again')

while True:
    if riddlePartOne is True:
        riddleTwo = input('Who makes it, has no need of it. '
                          'Who buys it, has no use for it.')
        if riddleTwo == 'coffin':  
            print('The tablet weighs down the plate with a crisp click')
            riddlePartThree = True
            break
        elif riddleTwo == 'candle' or 'river':
            print('You hear a loud crunch from above your head')
            print('The ceiling begins to move towards you')
            print('The light begins to fade...')
            break
        else:
            print('Incorrect answer, please try again')

while True:
    if riddlePartThree is True:
        print('A large stone door reveals a tunnel with a red glow')
        print('You proceed onwards.')
        break
    
                            

