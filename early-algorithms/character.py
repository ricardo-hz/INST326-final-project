import equipment
import random
from equipment import *
from ability_test import *

CHARACTER_DICT = {
    "Char1" : [100, WEAPONS[0], "Generic Armor 1", []],
    "Char2" : [150, WEAPONS[1], "Generic Armor 2", []],
    "Char3" : [200, WEAPONS[2], "Generic Armor 3", []],
    "Char4" : [250, WEAPONS[3], "Generic Armor 4", []]
}

class Character():
    """Representation of a character.
    
    Attributes:
        name (str): The character's name
        character_id (int): The numeric, unique id of the character
        hp (int): current health of character
        max_hp (int): maximum health of character
        weapon (Weapon): weapon character wields
        armor (Armor): armor character wields
        abilities (dict): abilities character has access to
        attack_base (int): base attack stat character has. based off of weapon
        attack_stat (int): attack stat used in calculations, incl. modifications
        defense_base (int): base defense stat character has, based off of armor
        defense_stat (int): defense stat used in calculations, incl. modifications
        agility_base (int): base agility stat character has
        agility_stat (int): agility stat used in party order
        player_character (bool): whether or not character is controlled by player.
        false unless chosen in character select
    
    """
    
    def __init__(self, name: str, character_id: int, hp: int, agility: int, weapon: et.Weapon, 
                 armor: et.Armor, character_abilities: AbilityList):
        """Initializes a new character object.
        
        Args:
            name (str) : The character's name
            character_id (int): The numeric, unique id of the character
            hp (int): The character's starting health points.
            agility (int): The character's agility
            weapon (Weapon) : The character's starting weapon.
            armor (Armor) : The character's starting armor.
            abilities (AbilityList) : The character's starting abilities.
                Empty list if ommitted. 
        
        Side effects:
            Initalizes character object
        """
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f"Not valid type for name: {type(name)}")
        
        if isinstance(character_id, int):
            self.character_id = character_id
        else: 
            raise TypeError(f"Not valid type for char id: {type(character_id)}")
        
        if isinstance(hp, int):
            self.hp = hp
            self.max_hp = hp
        else:
            raise TypeError(f"Not valid type for hp: {type(hp)}")
        
        if isinstance(weapon, et.Weapon) or weapon is None:
            self.weapon = weapon
        else:
            raise TypeError(f"Not valid type for weapon: {type(weapon)}")
        
        if isinstance(armor, et.Armor) or armor is None:
            self.armor = armor
        else:
            raise TypeError(f"Not valid type for armor: {type(armor)}")
        
        if isinstance(character_abilities, dict):
            self.abilities = character_abilities
        else:
            raise TypeError(f"Not valid type for character_abilities: \
            {type(character_abilities)}")
        
        self.attack_base: int = self.weapon.damage
        self.attack_stat: int = self.attack_base
        self.defense_base: int = self.armor.defense
        self.defense_stat: int = self.defense_base
        self.agility_base: int = agility
        self.agility_stat: int = self.agility_base
        
        self.character_abilities = character_abilities
        self.player_character = False
        
    def attack(self, other_character):
        other_character.hp -= 20
    
    def swap_weapon(self, new_weapon) -> None:
        raise NotImplementedError("help")
    
    def damageSelf(self, damage: int) -> None:
        self.hp -= damage
        
    
    def add_ability(self, ability):
        """Adds an ability object to a character's abilities list.
        
        Args:
            ability (Ability) : The ability to add. This ability and information
                pertaining to it's use should be present in the ABILITIES
                dictionary of equipment.py.
        """
        if ability.name.upper() not in self.abilities:
            self.abilities.append(equipment.Ability(ability.name.upper()))
    
    
    def add_weapon(self, weapon):
        raise NotImplementedError;  
    
    def remove_weapon(self, weapon):
        raise NotImplementedError;  
    
    def __str__(self) -> str:
        """Prints detailed information about a character.
        """
        print(f"Name: {self.name}")
        print(f"HP: {self.hp} ({self.max_hp})")
        print(f"Weapon: {self.weapon.name} - {self.attack_stat} ({self.attack_base})")
        print(f"Armor: {self.armor.name} - {self.defense_stat} ({self.defense_base})")
        print(f"Abilities: {self.character_abilities}")
        
    def __lt__(self, other) -> bool:
        return self.agility < other.agility
    
    def __rt__(self ,other) -> bool:
        return self.agility_base > other.agility

# I know constants are traditionally placed at top, this
# line won't work due to Character not being defined if it's placed there
CHARACTER_LIST = [Character(key, *value) for key,value in CHARACTER_DICT.items()]

class Party():
    def __init__(self, party_list: list):
        self.party_list = party_list
        
    def __str__(self) -> str:
        listofcharacteramongus = str()
        for c in self.party_list:
            listofcharacteramongus = listofcharacteramongus + f"Name: {c.name} | HP: {c.hp} ({c.max_hp})"
        return listofcharacteramongus
        
class Player_Party(Party):
    def __init__(self, party_list: list):
        for p in party_list:
            p.player_character = True
        self.party_list = party_list
            
class Enemy_Party(Party):
    def __init__(self, party_list: list, enemy_behaviors: dict = None, intro_message: str = None):
        # i should really really really be banned from programming for this
        self.party_list = party_list
        
        # dict should be of form like i dunno {"enemyName": damageTargetting}
        # but there's objectively a better way to go about this surely
        # feel free to not use this if so i should probably just explode tbh
        self.enemy_behaviors = enemy_behaviors
        
        #gotta give the enemy party a bit of a hype-up of course
        self.intro_message = intro_message

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