# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Goblin Crypt

# Code for google api (For player score sheet)

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

print("******* Goblin Crypt ********")
print("******* Enter S to start the game ********")

while True:
    start_choice = input()
    if start_choice.lower() == 's':
        break
    else:
        print("Invalid choice. Please press 's' to start the game.")

while True:
    player_name = input('Adventurer, what is your name? (5 - 12 characters): ')
    if len(player_name) <= 4 or len(player_name) >= 13:
        print('Invalid name length, please try again.')
    else:
        break

while True:    
    player_class = input(f"Well then, {player_name} what kind of adventurer "
                         "are you?")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    if player_class == '1':
        print('Ah, a mighty warrior')
        break
        
    if player_class == '2':
        print('Ah, a wise mage')
        break
        
    if player_class == '3':
        print('Ah, a cunning burglar')
        break
    else:
        print('Invalid answer, please try again')

while True:
    enter_dungeon = input("You step out of the dark woods and into a clearing. " 
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
    break                      
                
while True:                       
    if enter_dungeon == "y":
        print("You decend the dungeon stairs, "
              "to the depths below.")
    if enter_dungeon == "n":
        print("You return home and live a " 
              "very long and boring life.")
    else:
        print("Invalid choice, please try again.")
        break      