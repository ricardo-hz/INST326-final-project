import random
from character_class import *
from combat import party_info

MAX_TEAM_SIZE = 3


#Aviva's function
def character_equipment(name, weapons, armour, battle_outcome):
    """Updates the weapons and armour of players.
    
    Args:
        name (str): the player's name
        weapons (list): a list of weapons that a player has at a given time
        armour (list): a list of armour that a player has at a given time
        battle_outcome (str): the outcome of the battle just played, either
            'Won' or 'Lost'
            
    Returns:
        rand_weapon (str): a randomly chosen weapon for the battle
        rand_armour (str): a randomly chosen armour for the battle
            
    Side effects:
        Prints messages and input statements to the console/user.
        Modifies the weapons and armour lists.
    """
    
    print(f"It is now {name}'s turn. The weapons that {name} " 
            f"currrently has are: {weapons} and their current armour "
            f"is: {armour}.")
    weapon_input = input(f"Please choose one weapon from the list given or let " 
                         f"the game pick at random. If random, input "
                         f"'random'. ")
    if weapon_input == "random":
        for rand_weapon in weapons:
            rand_weapon = weapons[random.randint(len(weapons))]
            return rand_weapon
    else:
        return weapon_input
    armour_input = input(f"Please choose one piece of armour from the list "
                         f"given or let the game pick at random. If random, "
                         f"input 'random'. ")
    if armour_input == "random":
        for rand_armour in armour:
            rand_armour = weapons[random.randint(len(weapons))]
            return rand_armour
    else:
        return armour_input
    if battle_outcome == "Won":
        weapon_upgrade = input("Congrats on winning the battle! Please "
                "choose one weapon to upgrade from your list of weapons. ")
        armour_upgrade = input("Now please choose one armor to upgrade from "
                               "your list of armor. ")
        weapons.append(weapon_upgrade)
        armour.append(armour_upgrade)
    elif battle_outcome == "Lost":
        print(f"Unfortunately, you lost your battle and are not able to "
                f"upgrade your weapons and armour. Your weapons are: "
                f"{weapons} and your armour is: {armour}. Better "
                f"luck next time!")
    else:
        print(f"A battle was not played. Your weapons are: {weapons} "
                f"and your armour is: {armour}.")
        
def title_screen():
    """Title screen for the game, user selects which 'screen' to see
    
    Side effects:
        Prints to screen of gameplay information or lore
    """
    while True:
        print(f"=== Welcome to the Tournament of Water Bottle ===\n")
        print()
        print(f"1. Play Game\n"
              f"2. How-to-Play\n"
              f"3. Lore\n")
        
        choice = input(f"Enter the corresponding number depending on "
                       f"which section to enter: ")
        print()
        
        if choice == "1":
            break
        elif choice == "2":
            print("=== HOW-TO-PLAY THIS GAME ===\n")
            print(f"The game is your classic turn-based RPG game\n")
            print(f"1. Select your team from a given pool of characters"
                  f" to be in your party, max of three characters\n"
                  f"2. Enter combat! A turn-order will be shown to see which"
                  f" which characters or enemies will go first. If it's a"
                  f" character turn, you will be given the option to choose"
                  f" what abilities your character will target. Enemies will"
                  f" attack your characters and turns will repeat until either"
                  f" team falls in combat.\n"
                  f"3. Between combats you will be able to enter a 'shop' where"
                  f" Each character's weapon or armor will be upgraded!\n"
                  f"4. Steps 2 and 3 will repeat until the 6th combat, where"
                  f" you will face a boss in combat and will see if humanity"
                  f" will fall or triumph against the monsters of the tournament")
            print()
            input("Press enter or any key to continue...")
            print()
        elif choice == "3":
            print("=== LORE BEHIND THE GAME ===\n")
            print("Humanity is on the brink of extinction because of the 'Water Bottle Wars'...")
            print("A tournament is created by the gods as a last chance effort for humanity to survive...")
            print("Three heroes must rise up to take the challenge of protecting humanity...")
            print("Will they fail or will they triumph over evil forces...")
            print()
            input("Press enter or any key to continue...")
            print()
        else:
            print("Invalid Input!")
            

# Ricardo's function
def assemble_team(characters):
    """Assembles a team using user prompts at a menu.
    
    Args:
        characters (dict of Characters) : The characters which a player can
            choose from.
    
    Side effects:
        Prints to the screen.
    
    Returns:
        The player's team as a list of Character objects.
    """
    party_info()
    team = []
    while len(team) != MAX_TEAM_SIZE:
        choice = input("Enter the name of the character you would like on"
                f" your team. You may only have "
                f"one of each character. ").split("--")
        choice = [c.strip() for c in choice]
        
        if choice[0] == "waterbottle":
            return [characters[c] for c in characters]
        # One branch for info
        if len(choice) == 2:
            if choice[0] not in [characters[c].name for c in characters]:
                print("Character doesn't exist")
            elif choice[1] != 'v':
                print("Invalid flag.")
            else:
                print(characters[choice[0]])
                
        # One branch for adding
        elif len(choice) == 1:
            # First verify that what was entered is even a character
            if choice[0] not in [characters[c].name for c in characters]:
                print("Character doesn't exist")
            # Then check if the character is already on their team
            elif choice[0] in [character.name for character in team]:
                print("Character already on team")
            else:
                print(f"Welcome, {choice[0]}!")
                team.append(characters[choice[0]])
        else:
            print("Too many arguments entered.")
    
    return team


        
        
        
        
"""   
    while len(team) != MAX_TEAM_SIZE:
        choice = input("Enter the name of the character you would like on"
                       f" your team. You may only have "
                       f"one of each character. ")
        # There's probably a more legible way to document the fact that the 
        # choice needs to be within the valid 1 - 6 range
        if (choice not in):
                team.append(choice)
                team.append(characters[choice - 1])
                print(f"Your team: ")
                print_characters(team)
        else:
            print(f"Invalid Entry. Please Enter the number of the character "
                  f"you would like on your team. You may only have one of "
                  f"each character. ")
            
    return team
"""   
def start():
    """Starts the gameplay loop.
    """
    raise NotImplementedError;  