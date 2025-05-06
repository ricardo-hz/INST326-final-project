import equipment
from weaponarmor_btest import *
import random

class Character():
    """Represents a character.
    
    This class is only being used for demonstration purposes and early algorithm
    testing.
    
    Attributes:
        something (type) : 
        
    Methods:
        attack (self, other_character) : 
        add_weapon (self, weapon) : 
        remove_weapon (self, weapon) : 
        add_ability (self, ability) : Adds an ability object to a character's 
            abilities list.
    """
    
    def __init__(self, name, hp, weapon = None, 
                 armor = None, abilities = []):
        """Initializes a new character object.
        
        Args:
            name (str) : The character's name
            hp (float) : The character's starting health points.
            weapon (Weapon) : The character's starting weapon. None if omitted.
            armor (Armor) : The character's starting armor. None if omited.
            abilities (list of Ability) : The character's starting abilities.
                Empty list if ommitted. 
        
        TODO:
            - Should weapon be a list of weapon objects? or will characters 
            have one weapon only?
        """
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.weapon = weapon
        self.armor = armor
        self.abilities = abilities
        
    def attack(self, other_character):
        other_character.hp -= 20
    
    def add_weapon(self, weapon):
        raise NotImplementedError;  
    
    def remove_weapon(self, weapon):
        raise NotImplementedError;  
    
    def add_ability(self, ability):
        """Adds an ability object to a character's abilities list.
        
        Args:
            ability (Ability) : The ability to add. This ability and information
                pertaining to it's use should be present in the ABILITIES
                dictionary of equipment.py.
        """
        if ability.name.upper() not in self.abilities:
            self.abilities.append(equipment.Ability(ability.name.upper())) 
    
    def __repr__(self):
        return f"{self.name}: {self.hp}"

CHARACTER_DICT = {
    "Char1" : [100, WEAPONS[0], "Generic Armor 1", []],
    "Char2" : [150, WEAPONS[1], "Generic Armor 2", []],
    "Char3" : [200, WEAPONS[2], "Generic Armor 3", []],
    "Char4" : [250, WEAPONS[3], "Generic Armor 4", []]
}

CHARACTER_LIST = [Character(key, *value) for key,value in CHARACTER_DICT.items()]

def print_character(character):
    """Prints detailed information about a character.
    """
    print(f"Name: {character}")
    print(f"HP: {CHARACTER_DICT[character][0]}")
    print(f"Weapon: {CHARACTER_DICT[character][1].name} - {CHARACTER_DICT[character][1].damage} DMG")
    print(f"Armor: {CHARACTER_DICT[character][2]}")
    print(f"Abilities: {CHARACTER_DICT[character][3]}")

        
def print_characters(characters):
    """Prints basic information about a list or dict of characters.
    
    Args:
        characters (list or dict) : The characters to be printed.
    """
    # Convert passed dicts to list of characters
    if isinstance(characters, dict):
        characters = CHARACTER_LIST
        
    for character in characters:
        print(f"{character.name} | {character.hp}HP")