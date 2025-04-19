import random
from character import *

MAX_TEAM_SIZE = 4


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
        weapon_addition = input(f"Congrats on winning the battle! Please "
                f"choose one weapon to add to your character's weapons from "
                f"this list: {Character.add_ability} ")
        armour_addition = input(f"Now please choose one armour to add to "
                                f"your character's armour from this list:"
                                f"{Character.add_ability} ")
        weapons.append(weapon_addition)
        armour.append(armour_addition)
    elif battle_outcome == "Lost":
        print(f"Unfortunately, you lost your battle and are not able to "
                f"upgrade your weapons and armour. Your weapons are: "
                f"{weapons} and your armour is: {armour}. Better "
                f"luck next time!")
    else:
        print(f"A battle was not played. Your weapons are: {weapons} "
                f"and your armour is: {armour}.")
        

def ComputerTurn(human_party, monster_party):
    """Decides how the monsters in the enemy party will attack our player's
        party own characters: Written by Nathan Castelo.
        
    Args:
        human_party (list of Characters): The characters in the Player's party
        monster_party (list of Characters): The characters in the Computer's 
            party
        
    Side effects:
        Reduces the HP of a targeted character
        Prints out the result of an attack
        Prints out if a player's character has died if their HP is reduced
        to 0 or less
    """
    human_party_max_hp = [character.max_hp for character in human_party]
    selected_target = None
    for monster in monster_party:
        for character in human_party:
            # A character will always be targeted if they are below an HP
            # threshhold which is less than or equal to 10% of their HP
            if character.hp <= character.hp * 0.10:
                selected_target = character
            if character.max_hp == max(human_party_max_hp):
                probability = random.randint(1, 100)
                if probability <= 65:
                    selected_target = character
            elif character.max_hp == min(human_party_max_hp):
                probability = random.randint(1,100)
                if probability <= 25:
                    selected_target = character
            else:
                selected_target = character
                
        monster.attack(selected_target)
        print(f"{monster.name} has attacked {selected_target.name}! "
              f"{selected_target.name} now has "
              f"{selected_target.hp} remaining HP!")
        if selected_target.hp <= 0:
            print(f"{selected_target.name} has died!")
            human_party.remove(selected_target)
    print(f"Party HP: {human_party}")

def print_character_options(characters):
    for character in characters:
        print(f"{character.char_id}. {character.name} | {character.hp}HP | "
              f"{character.role}")
        
def print_characters(characters):
    for character in characters:
        print(f"{character.name} | {character.hp}HP | {character.role}")


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
    print("Assemble your team!")
    # The below line should probably be moved out of this function and into 
    # start() when it is implemented.
    print_character_options(characters)
    team = []
    chosen_numbers = []
    while len(team) != MAX_TEAM_SIZE:
        choice = int(input("Enter the number of the character you would like on"
                       f" your team. You may only have "
                       f"one of each character. "))
        # There's probably a more legible way to document the fact that the 
        # choice needs to be within the valid 1 - 6 range
        if (choice in range(1,7) and choice not in chosen_numbers):
                chosen_numbers.append(choice)
                team.append(characters[choice - 1])
                print(f"Your team: ")
                print_characters(team)
        else:
            print(f"Invalid Entry. Please Enter the number of the character "
                  f"you would like on your team. You may only have one of "
                  f"each character. ")
            
    return team
        
def start():
    """Starts the gameplay loop.
    """
    raise NotImplementedError;  