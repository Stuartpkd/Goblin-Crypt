# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Goblin Crypt

# Code for google api (For player score sheet)

import os
import gspread
import time
import random
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


def upload_data(player_title, player_class_upload, death_reason):
    row = [player_title, player_class_upload, death_reason]
    player_death = SHEET.worksheet('credits')
    player_death.append_row(row)


def show_tombstone():
    clear_screen()
    player_death = SHEET.worksheet('credits')
    adventurer_name = player_death.col_values(1)
    adventurer_class = player_death.col_values(2)
    adventurer_death = player_death.col_values(3)
    
    print(f"""{"Adventurer":<20} {"Class":<20} {"Cause of death":<20}""")

    # Print data
    for name, adv_class, death in zip(adventurer_name, 
                                      adventurer_class, adventurer_death):
        print(f"""{name:<20} {adv_class:<20} {death:<20}""")
    while True:
        escape = input('Enter x to return to main menu.')
        escape = escape.lower().strip()
        if escape == 'x':
            main()
            break
        else:
            invalid_input()
            continue
    

def invalid_input():
    """
    Function for printing invalid choice
    """
    print("Invalid choice, please try again\n\n")


def no_choice():
    """
    Function printing empty input
    """
    print('You did not enter anything, please try again.\n')


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
    print('GAMEOVER'
          'Would you like to play again? (y or n)\n')
    play_again = input()
    play_again = play_again.lower().strip()
    while True:
        if play_again == 'y':
            main()
            break
        elif play_again == 'n':
            print_with_delay('Farewell Adventurer!')
            exit()
        else:
            invalid_input()
            continue


def main():
    # Classes
    PLAYER_CLASS = ''

    # Rooms
    TABLET_ROOM = False
    CRYSTAL_ROOM = False
    CHEST_ROOM = False
    GOBLIN_ROOM = False
    BOSS_ROOM = False
    LOCKED_DOOR = False
    GOBLIN_CRYPT = False
    OUTRO = False

    # Goblin Language
    GOBLIN_LANGUAGE = False

    # Items
    PLAYER_SWORD = ''
    GOBLIN_KEY = False
    # Actions
    SEARCH_GOBLIN = False
    TAKE_KEY = False
    OPEN_LOCKED_DOOR = False
    CROWN_RIDDLE = False

    def start_game():
        """
        Function that shows player start game choice.
        Validates input and then starts game.
        """
        clear_screen()
        print("     ******* Goblin - Crypt ********")
        print("******* Enter S to start the game ********")
        print("******* Enter T to show past adventures ********")
        while True:
            start_choice = input()
            if start_choice.lower().strip() == 's':
                clear_screen()
                break
            elif start_choice.lower().strip() == 't':
                show_tombstone()
                continue
            else:
                print("Invalid choice. Please enter 's' to start the game.\n\n"
                      "Or enter 't' to view past adventurers.")
                continue

    start_game()

    # User inputs their name
    while True:
        player_name = input('Adventurer, what is your '
                            'name? (5 - 12 characters):\n')
        if (len(player_name) <= 4 or
           len(player_name) >= 13 or player_name == ''):
            print('Invalid name length, please try again.\n')
        else:
            clear_screen()
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
            clear_screen()
            break
        
        elif player_class_choice == '2':
            PLAYER_CLASS = 'mage'
            clear_screen()
            break

        elif player_class_choice == '3':
            PLAYER_CLASS = 'rogue'
            clear_screen()
            break

        elif player_class_choice == '':
            no_choice()
            continue    
        else:
            invalid_input()
            continue

    # Introduction to dungeon
    while True:
        if PLAYER_CLASS == 'warrior':
            print("Ah, a mighty warrior.\n")
        elif PLAYER_CLASS == 'mage':
            print("Ah, a wise mage.\n")
        elif PLAYER_CLASS == 'rogue':
            print('Ah, a cunning rogue.\n')
        else:
            break
        enter_dungeon = input("You step out of the dark woods "
                              "and into a clearing.\n"
                              "Your eyes take a moment "
                              "to adjust to the sudden brightness.\n"
                              "You inhale deeply, filling your "
                              "lungs with the crisp air.\n"
                              "Ahead of you looms the entrance to "
                              "a dungeon, the stone walls slick\n"
                              "with moisture and the scent of decay.\n\n"
                              "Will you be brave enough to venture "
                              "into the depths of the dungeon?\n"
                              "Or will you turn back "
                              "and seek refuge (y or n)\n")
        if enter_dungeon.lower().strip() == "y":
            clear_screen()
            print("You descend the dungeon stairs, to the depths below.\n")
            break
        elif enter_dungeon.lower().strip() == "n":
            clear_screen()
            print("You return home and live a very long and boring life.\n")
            exit()
        elif enter_dungeon == '':
            no_choice()
            continue
        else:
            invalid_input()
            continue

    # Main chamber choices (Tunnels 1 - 3)
    while True:
        mainChamber_choice = input("You enter the first "
                                   "chamber of the dungeon.\n"
                                   "Ahead of you are three identical "
                                   "stairways leading down.\n"
                                   "The light from torches mounted on the "
                                   "walls flickers,\ncasting an eerie "
                                   "glow on the stairs.\n\n"
                                   "The heat emanating from the "
                                   "torches is palpable,\n"
                                   "making the air thick and heavy.\n\nChoose "
                                   "your path carefully: (1, 2, or 3)\n")
        mainChamber_choice = mainChamber_choice.lower().strip()
        if mainChamber_choice == "1":
            clear_screen()
            print("You make your way down the first stairs. "
                  "You feel\none of the steps sink "
                  "lower than the others,\n"
                  "as a poison dart is released "
                  "from a nearby wall.\n")
            player_title = player_name
            player_class_upload = PLAYER_CLASS
            death_reason = 'Poison dart to the neck.'
            upload_data(player_title, player_class_upload, death_reason)
            game_over()
            break

        elif mainChamber_choice == "2":
            clear_screen()
            print("You cautously move down the second stairs.\n"
                  "Your steps echo against the damp stone walls.\n"
                  "Bending down through an archway, you are met\n"
                  "with a large altar with 3 texts carved into it's stone.\n"
                  "Each text is a riddle to be solved.\n")
            TABLET_ROOM = True
            break
        elif mainChamber_choice == "3":
            clear_screen()
            print("The stairs lead down to a dusty room "
                  "The air is cold and dank.\n"
                  "You see a chest in the middle of the room,\n"
                  "decomposed skeletons are littered around it.\n")
            CHEST_ROOM = True
            break
        elif mainChamber_choice == '':
            no_choice()
            continue
        else:
            invalid_input()
            continue

    # Riddle room choices

    if TABLET_ROOM is True and CHEST_ROOM is False:
        print('3 small tablets are laid out in front of you.')
        print('Each has an engraving carved into it.')
        print('You see a river, a candle and a coffin.')
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
            player_title = player_name
            player_class_upload = PLAYER_CLASS
            death_reason = 'Crushed like a pancake.'
            upload_data(player_title, player_class_upload, death_reason)
            game_over()

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
            else:
                invalid_input()
                continue
        if riddleTwo == 'candle':
            RIDDLE_TWO = True
        elif riddleTwo == 'coffin' or 'river':
            print('You hear a loud crunch from above your head')
            print('The ceiling begins to move towards you')
            print('The light begins to fade...')
            player_title = player_name
            player_class_upload = PLAYER_CLASS
            death_reason = 'Crushed like a pancake.'
            upload_data(player_title, player_class_upload, death_reason)
            game_over()
            
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
            else:
                invalid_input()
                continue
        if riddleThree == 'coffin':
            print('The tablet weighs down the plate with a crisp click\n')
            RIDDLE_THREE = True
        elif riddleThree == 'candle' or 'river':
            print('You hear a loud crunch from above your head')
            print('The ceiling begins to move towards you')
            print('The light begins to fade...')
            player_title = player_name
            player_class_upload = PLAYER_CLASS
            death_reason = 'Crushed like a pancake.'
            upload_data(player_title, player_class_upload, death_reason)
            game_over()
            
    RIDDLE_THREE = True
    if RIDDLE_THREE is True and CHEST_ROOM is False:
        while True:
            clear_screen()
            TABLET_ROOM = False
            CRYSTAL_ROOM = True
            print('A large stone door reveals a tunnel with a red glow\n')
            print('You proceed onwards.\n')
            break
        
# Chest room choices

    if CHEST_ROOM is True and TABLET_ROOM is False:
        while True:
            chestChoice = input('Do you open the chest? (y or n)\n')
            chestChoice = chestChoice.lower().strip()
            if chestChoice == 'y':
                clear_screen()
                print('You are greeted with a gleaming '
                      'sword wrapped in cloth.\n')
                print('You place it onto your belt.\n')
                PLAYER_SWORD = 'held'
                GOBLIN_ROOM = True
                break
            elif chestChoice == 'n':
                clear_screen()
                print('You think it is probably best to leave it be.\n')
                print('You continue onwards into the dungeon.\n')
                GOBLIN_ROOM = True
                break
            elif chestChoice == '':
                no_choice()
                continue
            else:
                print('Invalid input, please try again.')
                continue

    # Crystal room choices
    if CRYSTAL_ROOM is True and CHEST_ROOM is False:
        while True:
            crystalChoice = input('After following the tunnel you come '
                                  'to a large\naltar with a red crystal '
                                  'hovering above it.\n'
                                  'You feel yourself drawn towards it...\n\n'
                                  'Do you take the crystal? (y or n)\n')
            crystalChoice = crystalChoice.lower().strip()
            if crystalChoice == 'y' and PLAYER_CLASS == 'mage':
                clear_screen()
                print('You clasp your hand around the crystal.\n'
                      'A powerful surge rockets through your body!\n'
                      'The knowledge and history of the goblins '
                      'begins rushing\nthrough your mind.\n'
                      'Their culture and language is clear to you now.\n')
                GOBLIN_LANGUAGE = True
                GOBLIN_ROOM = True
                break
            elif (crystalChoice == 'y' and
                  (PLAYER_CLASS == 'warrior' or PLAYER_CLASS == 'rogue')):
                clear_screen()
                print('You clasp your hand around the crystal.\n'
                      'A powerful surge rockets through your body!\n'
                      'Thousands of voices begin to pierce your mind,\n'
                      'unintelligable images and symbols '
                      'burn into your eyes.\n'
                      'Your vision fails you and you fall to the floor.\n')
                player_title = player_name
                player_class_upload = PLAYER_CLASS
                death_reason = 'Mind filled with cosmic horrors.'
                upload_data(player_title, player_class_upload, death_reason)
                game_over()
            elif crystalChoice == 'n':
                clear_screen()
                print('Mother always said not to touch glowing crystals,\n'
                      'Best to move on.\n')
                GOBLIN_ROOM = True
                break
            elif crystalChoice == '':
                no_choice()
                continue
            else:
                invalid_input()
                continue

    # Goblin room
    if GOBLIN_ROOM is True:
        while True:
            print('As you approach the next room, you hear\n'
                  'strange voices ahead.\n\n'
                  'Pearing around the small doorway to the room,\n'
                  'you see a group of goblins.\nThey are gathered '
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
                clear_screen()
                print_with_delay('You dispatch the goblins with ease.\n'
                                 'They are no match for your '
                                 'fighting prowess.\n\n'
                                 'With a flurry of blows and cuts they are '
                                 'left lifeless on the ground.')
                SEARCH_GOBLIN = True
                break
            elif goblinChoice == '1':
                clear_screen()
                print_with_delay('You are quickly overwhelmed '
                                 'by the goblins.\n'
                                 'They scratch and tear at you until you lose '
                                 'balance and hit the floor.\n\n'
                                 'The last thing you see is '
                                 'them looting your bag.\n')
                player_title = player_name
                player_class_upload = PLAYER_CLASS
                death_reason = 'Terrible at sword-fighting.'
                upload_data(player_title, player_class_upload, death_reason)
                game_over()
                break
            elif goblinChoice == '2' and PLAYER_CLASS == 'rogue':
                clear_screen()
                print_with_delay('Clinging to the edges of the room, '
                                 'you make your\nway through the shadows. '
                                 'The goblins continue to '
                                 'bicker over their gold.\n'
                                 'You manage to reach the '
                                 'end of the room unseen.\n\n'
                                 'Sneaking through the doorway, you '
                                 'continue on through the dungeon.\n')
                LOCKED_DOOR = True
                break
            elif goblinChoice == '2':
                clear_screen()
                print_with_delay('Clinging to the edges of the room, '
                                 'you make your\nway through the shadows. '
                                 'Your cloak gets snagged '
                                 'on an\nexposed nail and '
                                 'brings down a shelf of loot and trinkets.\n'
                                 'The group of goblins turn to you '
                                 'with a gleeful look in their eye.\n\n'
                                 'There is no escape...\n')
                player_title = player_name
                player_class_upload = PLAYER_CLASS
                death_reason = 'Caught sneaking by goblins.'
                upload_data(player_title, player_class_upload, death_reason)
                game_over()
                break
            elif goblinChoice == '3':
                random_choice = random.randint(1, 10)
                if random_choice == 8:
                    clear_screen()
                    print_with_delay('You throw a nearby '
                                     'chalice over the heads '
                                     'of the goblins.\n'
                                     'It crashes into a structurally '
                                     'unstable pile of loot.\n'
                                     'This seems to send the '
                                     'goblins into hysterics.\n'
                                     'Leaving you time to make your '
                                     'way out of the room.\n')
                    LOCKED_DOOR = True
                    break
                elif random_choice != 8:
                    clear_screen()
                    print_with_delay('Your pathetic attempt at '
                                     'throwing a nearby '
                                     'chalice\nresults in striking one of the '
                                     'goblins in the head.\n'
                                     'In your final moments, '
                                     'you feel quite foolish.\n')
                    player_title = player_name
                    player_class_upload = PLAYER_CLASS
                    death_reason = 'Throws like a sloth.'
                    upload_data(player_title, player_class_upload, 
                                death_reason)
                    game_over()
                    break
            elif (goblinChoice == '4' and 
                  (GOBLIN_LANGUAGE is True and PLAYER_CLASS == 'mage')):
                clear_screen()
                print_with_delay('With your new found '
                                 'understanding of goblin tongue,\n'
                                 'you are able to make out what '
                                 'the goblins are saying.\n\n'
                                 'They are upset over how much '
                                 'they have to pay to their goblin leader.\n'
                                 'You greet them in your best goblin accent.\n'
                                 'They are very impressed with your handle '
                                 'of the language.\n\n'
                                 'After exchanging pleasantries '
                                 'you tell them about '
                                 'the wonders of tax fraud.\n'
                                 'A simple way for them to keep '
                                 'their hard earned gold.\n\n'
                                 'The goblins are ecstatic with their new '
                                 'found financial powers\n'
                                 'and let you go onwards '
                                 'through the dungeon. '
                                 'They even give you some '
                                 'gold for the tip.\n')
                LOCKED_DOOR = True
                break
            elif goblinChoice == '4':
                clear_screen()
                print_with_delay('For some strange reason you felt it '
                                 'correct\nto try and reason '
                                 'with the goblins.\n'
                                 'You quickly find out you do not speak their '
                                 'language and\nhave made a grave mistake.\n')
                player_title = player_name
                player_class_upload = PLAYER_CLASS
                death_reason = 'Tried to reason with goblins.'
                upload_data(player_title, player_class_upload, death_reason)
                game_over()
                break
            elif goblinChoice == '':
                no_choice()
                continue
            else:
                invalid_input()
                continue

    if (PLAYER_CLASS == 'warrior' and SEARCH_GOBLIN is True or
       (PLAYER_SWORD == 'held' and SEARCH_GOBLIN is True)):
        while True:
            print_with_delay('The goblins lay still before you.\n\n'
                             'Do you search their bodies? (y or n)\n')
            goblin_search = input()
            goblin_search = goblin_search.lower().strip()
            if goblin_search == 'y':
                clear_screen()
                print_with_delay('The goblins seem interested in collecting '
                                 'snails and dirt.\n'
                                 'However on the last goblin you find a large '
                                 'brass key.\n')
                TAKE_KEY = True
                break
            elif goblin_search == 'n':
                clear_screen()
                print_with_delay('Your head is swimming after the fight with '
                                 'the goblin group.\n'
                                 'Perhaps it is best to keep moving.\n\n'
                                 'You continue down a stone stairway, '
                                 'the air begins to smell foul...\n')
                BOSS_ROOM = True
                break
            else:
                invalid_input()
                continue

    if TAKE_KEY is True:
        while True:
            print_with_delay('Do you take the key? (y or n)')
            take_goblin_key = input()
            take_goblin_key = take_goblin_key.lower().strip()
            if take_goblin_key == 'y':
                clear_screen()
                print_with_delay('You tie the key to your belt and '
                                 'make your way onwards.\n')
                LOCKED_DOOR = True
                GOBLIN_KEY = True
                break
            elif take_goblin_key == 'n':
                clear_screen()
                print_with_delay("You're feeling quite remorseful about "
                                 "barging into their home and killing them.\n"
                                 "Perhaps looting them "
                                 "might be over-doing it.\n")
                LOCKED_DOOR = True
                break
            else:
                invalid_input()
                continue

    if LOCKED_DOOR is True:
        while True:
            print_with_delay('As you make your way '
                             'along a eerily quiet hallway,\n'
                             'you spot a door covered in goblin skulls.\n\n'
                             'Do you try open it? (y or n)\n')
            try_locked_door = input()
            try_locked_door = try_locked_door.lower().strip()
            if try_locked_door == 'y':
                clear_screen()
                print_with_delay('You try the handle and '
                                 'realise it is locked.\n')
                OPEN_LOCKED_DOOR = True
                break
            elif try_locked_door == 'n':
                clear_screen()
                print_with_delay('The fact it is covered '
                                 'in goblin skulls makes '
                                 'you\nfeel that you are not '
                                 'supposed to be in there.\n')
                BOSS_ROOM = True
                break
            else:
                invalid_input()
                continue

    if OPEN_LOCKED_DOOR is True:
        while True:
            print_with_delay('Probably for good reason...\n')
            if GOBLIN_KEY is True:
                print_with_delay('You remember the key you '
                                 'got off the goblins!\n'
                                 'You try it in the door '
                                 'and it makes a\nsatisfying '
                                 'click when turned.\n')
                GOBLIN_CRYPT = True
                break
            elif GOBLIN_KEY is False:
                print_with_delay('You have no way of '
                                 'getting through this door.\n'
                                 'It is best to move on, time to '
                                 'get out of this dungeon.\n')
                BOSS_ROOM = True
                break

    if GOBLIN_CRYPT is True:
        print_with_delay('You descend down the damp and musty '
                         'stairs into the goblin crypt.\nThe '
                         'flicker of your torch casts eerie '
                         'shadows on the moss-covered walls.\n\nThe stale '
                         'air is thick with the smell of decay and\n'
                         'the sound of dripping water '
                         'echoes in the distance.\n\n'
                         'In front of you, you see three wooden '
                         'coffins,\neach one ornately decorated '
                         'with carvings of twisted vines and skulls.\n\n')
        while True:
            print_with_delay('Perhaps one of the coffins '
                             'contains a way out.\n\n'
                             'Which coffin do you search? (1, 2 or 3)\n')
            coffin_choice = input()
            coffin_choice = coffin_choice.lower().strip()
            if coffin_choice == '1':
                clear_screen()
                print_with_delay('You slide the coffin lid off, it '
                                 'falls to the ground and\nshatters in a mist '
                                 'of splinters and dust.\n\n'
                                 'Gazing back into the coffin you see a nest '
                                 'of venomous vipers staring back at you.\n\n'
                                 'They lunge towards you, you do your best to '
                                 'get them off you but its too late...\n')
                player_title = player_name
                player_class_upload = PLAYER_CLASS
                death_reason = 'Why did it have to be snakes?'
                upload_data(player_title, player_class_upload, death_reason)
                game_over()
                break
            elif coffin_choice == '2':
                clear_screen()
                print_with_delay('The coffin lid reveals the skeleton of '
                                 'a past goblin king.\n'
                                 'He is buried with stolen jewelry and '
                                 'trinkets.\n'
                                 'Placed on top of his skull is a crown '
                                 'plastered with precious '
                                 'gems and metals.\n')
                CROWN_RIDDLE = True
                break
            elif coffin_choice == '3':
                clear_screen()
                print_with_delay('As you begin to push the lid from the '
                                 'coffin,\na boney and decomposing hand grabs '
                                 'your wrist.\n\n'
                                 'You are dragged into the '
                                 'coffin and the lid is '
                                 'placed back on top.\n'
                                 'Sealing you in the coffin, '
                                 'you are a part of the '
                                 'dungeon forever now...\n')
                player_title = player_name
                player_class_upload = PLAYER_CLASS
                death_reason = 'Entombed in a coffin forever.'
                upload_data(player_title, player_class_upload, death_reason)
                game_over()
                break

    if CROWN_RIDDLE is True:
        wrong_answer_count = 0
        while True:
            print_with_delay('Engraved in the band of the crown you see '
                             'the words:\n\n'
                             'It cannot be seen, cannot be felt, '
                             'cannot be heard,\ncannot be smelt. '
                             'It lies behind stars and under hills,\n'
                             'And empty holes it fills. '
                             'It comes out first and follows after,\n'
                             'ends life, kills laughter.\n\n'
                             'What word will you speak?\n')
            crown_riddle_answer = input()
            crown_riddle_answer = crown_riddle_answer.lower().strip()
            if crown_riddle_answer == 'dark':
                clear_screen()
                print_with_delay('You utter the words dark, all of the gem '
                                 'begin to glow and vibrate.\n'
                                 'The wall behind lights up with glyphs '
                                 'and symbols similar to the crown.\n'
                                 'A hidden door is revealed as the stone '
                                 'grinds and scrapes open.\n'
                                 'Fresh air pours into the crypt.\n')
                OUTRO = True
                break
            elif crown_riddle_answer == '':
                no_choice()
                continue
            elif wrong_answer_count == 5:
                print_with_delay('The crown begins to shake and tremble.\n'
                                 'The crypts ceilings begin to crack and '
                                 'crumble.\n'
                                 'You are buried alive within the tomb.')
                player_title = player_name
                player_class_upload = PLAYER_CLASS
                death_reason = 'Buried alive.'
                upload_data(player_title, player_class_upload, death_reason)
                game_over()
                break
            else:
                print_with_delay('Nothing seems to happen...\n\n')
                wrong_answer_count += 1
                continue

    if BOSS_ROOM is True:
        PLAYER_HEALTH = 100
        BOSS_HEALTH = 100
        print_with_delay('You enter a large hall with a '
                         'skull encrusted throne.\n'
                         'Sitting a top the throne is a large goblin,\nmuch '
                         'larger then the others you have seen.\n\n'
                         'It is adorned in human bones and skulls. '
                         'His bulbous belly protrudes\nfrom '
                         'beneath a tattered red robe,\nand his skin is a '
                         'sickly green hue.\n\n'
                         "The king's maw hangs open, revealing a "
                         "mouth full of sharp, rotting teeth.\n"
                         "He grips a rusted battle axe in one "
                         "meaty hand,\nready to defend "
                         "his throne at all costs.\n\n"
                         "He lunges off his throne to attack.\n")
        while True:
            print_with_delay('How do you attack? (slash, parry or thrust)\n')
            choices = ['slash', 'parry', 'thrust']
            player_fight_choice = input()
            player_fight_choice = player_fight_choice.lower().strip()
            boss_choice = random.choice(choices)
            # Slash beats parry
            if player_fight_choice == 'parry' and boss_choice == 'slash':
                # Player loses
                clear_screen()
                PLAYER_HEALTH -= 10
                print('You took a hit!\n\n')
                print('Player Health:', PLAYER_HEALTH)
                print('Goblin King Health:', BOSS_HEALTH)
                continue
            elif player_fight_choice == 'slash' and boss_choice == 'parry':
                # Player wins
                clear_screen()
                BOSS_HEALTH -= 10
                print('You landed a hit!\n\n')
                print('Player Health:', PLAYER_HEALTH)
                print('Goblin King Health:', BOSS_HEALTH)
                continue
            # Parry beats thrust
            elif player_fight_choice == 'thrust' and boss_choice == 'parry':
                # Player loses
                clear_screen()
                PLAYER_HEALTH -= 10
                print('You took a hit!\n\n')
                print('Player Health:', PLAYER_HEALTH)
                print('Goblin King Health:', BOSS_HEALTH)
                continue
            elif player_fight_choice == 'parry' and boss_choice == 'thrust':
                # Player wins
                BOSS_HEALTH -= 10
                clear_screen()
                print('You landed a hit!\n\n')
                print('Player Health:', PLAYER_HEALTH)
                print('Goblin King Health:', BOSS_HEALTH)
                continue
            # Thrust beats slash
            elif player_fight_choice == 'slash' and boss_choice == 'thrust':
                # Player loses
                PLAYER_HEALTH -= 10
                clear_screen()
                print('You took a hit!\n\n')
                print('Player Health:', PLAYER_HEALTH)
                print('Goblin King Health:', BOSS_HEALTH)
                continue
            elif player_fight_choice == 'thrust' and boss_choice == 'slash':
                # Player wins
                BOSS_HEALTH -= 10
                clear_screen()
                print('You landed a hit!\n\n')
                print('Player Health:', PLAYER_HEALTH)
                print('Goblin King Health:', BOSS_HEALTH)
                continue
            elif player_fight_choice == boss_choice:
                # draw
                clear_screen()
                print('Your attacks bounce off eachother.\n\n')
                print('Player Health:', PLAYER_HEALTH)
                print('Goblin King Health:', BOSS_HEALTH)
            elif player_fight_choice == '':
                no_choice()
                continue
            else:
                invalid_input()
                continue
            if PLAYER_HEALTH == 0:
                clear_screen()
                print_with_delay('You have been defeated!')
                player_title = player_name
                player_class_upload = PLAYER_CLASS
                death_reason = 'Cut in half.'
                upload_data(player_title, player_class_upload, death_reason)
                game_over()
                break
            elif BOSS_HEALTH == 0:
                clear_screen()
                print_with_delay('You have won!')
                OUTRO = True
                break

    if OUTRO is True:
        while True:
            print_with_delay('You win the game!')
            break


main()
