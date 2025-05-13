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

def information(filename):
    """Reads in text file of lore/instructional information (declutters code)
        and prints it out
    
    Args:
        filename (str): the file of the according text file
    """
    try:
        with open(filename, 'r', encoding = "utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Error: {filename} not found!")

def title_screen():
    """Title screen for the game, user selects which 'screen' to see
    
    Side effects:
        Prints to screen of gameplay information or lore
    """
    while True:
        print("=== Welcome to the Tournament of Water Bottle ===")
        print()
        print("1. Play Game")
        print("2. How-to-Play")
        print("3. Lore")
        
        choice = input(f"Enter the corresponding number depending on "
                       f"which section to enter: ").strip()
        print()
        
        if choice == "1":
            break
        elif choice == "2":
            information("how_to_play.txt")
            print()
            input("Press enter or any key to continue...")
            print()
        elif choice == "3":
            information("lore.txt")
            print()
        else:
            print("Invalid Input!")
            
# Ricardo's function
def assemble_team(characters):
    """Assembles a team using user prompts at a menu.
    
    Args:
        characters (list of Characters) : The characters which a player can
            choose from.
    
    Side effects:
        Prints to the screen.
    
    Returns:
        The player's team as a list of Character objects.
    """
    team = []
    i=1
    for character in characters:
        print(f"{i}. {character.name} | {character.current_hp} "
              f"({character.max_hp}) HP")
        i += 1

    numbers_chosen = []
    while len(team) != MAX_TEAM_SIZE:
        choice = input("Enter the number of the character you would like on"
                f" your team. You may only have "
                f"one of each character. Type --v after a number to learn more"
                f"about a character. ").split("--")
        choice = [c.strip() for c in choice]
        
        numeric_choice = choice[0]
        try:
            numeric_choice = int(choice[0])
        except:
            pass
        if choice[0] == "waterbottle":
            return [characters[c] for c in characters]
        # One branch for info
        if len(choice) == 2:
            if (numeric_choice < 1) and (numeric_choice >= len(team)):
                print("Character doesn't exist")
            elif choice[1] != 'v':
                print("Invalid flag.")
            else:
                print(characters[numeric_choice - 1])
                
        # One branch for adding
        elif len(choice) == 1:
            print(f"{numbers_chosen}")
            # First verify that what was entered is even a character
            if (numeric_choice < 1) and (numeric_choice >= len(team)):
                print("Character doesn't exist")
            # Then check if the character is already on their team
            elif numeric_choice in numbers_chosen:
                print("Character already on team")
            else:
                chosen_char = characters[numeric_choice - 1]
                print(f"{chosen_char.name}: {chosen_char.selection_message}")
                team.append(chosen_char)
                numbers_chosen.append(numeric_choice)

        else:
            print("Invalid argument.")
    
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