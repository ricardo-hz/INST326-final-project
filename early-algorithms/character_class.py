from equipment import *
import random
from ability_test import *

class Character:
    """Representation of a character.
    
    Attributes:
        name (str): The character's name
        character_id (int): The numeric, unique id of the character
        current_hp (int): current health of character
        max_hp (int): maximum health of character
        weapon (Weapon): weapon character wields
        armor (Armor): armor character wields
        character_abilities (AbilityList): abilities character has access to
        attack_base (int): base attack stat character has. based off of weapon
        attack_stat (int): attack stat used in calculations, incl. modifications
        defense_base (int): base defense stat character has, based off of armor
        defense_stat (int): defense stat used in calculations, incl. modifications
        agility_base (int): base agility stat character has
        agility_stat (int): agility stat used in party order
        player_character (bool): whether or not character is controlled by player.
        false unless chosen in character select
        conscious (bool): whether or not character can act
    
    """
    
    def __init__(self, name: str, hp: int, agility: int, weapon: Weapon, 
            armor: Armor, character_abilities: AbilityList):
        """Initializes a new character object.
        
        Args:
            name (str) : The character's name
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
        
        if isinstance(hp, int):
            self.current_hp = hp
            self.max_hp = hp
        else:
            raise TypeError(f"Not valid type for hp: {type(hp)}")
        
        if isinstance(weapon, Weapon):
            self.weapon: Weapon = weapon
            self.attack_base: int = self.weapon.damage
            self.attack_stat: int = self.attack_base
        elif weapon is None:
            self.weapon = None
            self.attack_base: int = 0
            self.attack_stat: int = 0
        else:
            raise TypeError(f"Not valid type for weapon: {type(weapon)}")
        
        if isinstance(armor, Armor):
            self.armor: Armor = armor
            self.defense_base: int = self.armor.defense
            self.defense_stat: int = self.defense_base
        elif armor is None:
            self.armor = None
            self.defense_base: int = 0
            self.defense_stat: int = 0
        else:
            raise TypeError(f"Not valid type for armor: {type(armor)}")
        
        if isinstance(character_abilities, AbilityList):
            self.character_abilities = character_abilities
        else:
            raise TypeError(f"Not valid type for character_abilities: \
            {type(character_abilities)}")
        
        self.agility_base: int = agility
        self.agility_stat: int = self.agility_base
        
        self.character_abilities: AbilityList = character_abilities
        self.player_character: bool = False
        self.conscious: bool = True
    
    def swap_weapon(self, new_weapon) -> None:
        self.weapon: Weapon = new_weapon
        self.attack_base: int = self.weapon.damage
        self.attack_stat: int = self.attack_base
    
    def swap_armor(self, new_armor) -> None:
        self.armor: Armor = new_armor
        self.defense_base: int = self.armor.defense
        self.defense_stat: int = self.defense_base
        
    def damageSelf(self, damage: int) -> None:
        self.hp -= damage
        
    
    def add_ability(self, ability: Ability) -> None:
        """Adds an ability object to a character's abilities list.
        
        Args:
            ability (Ability) : The ability to add. This ability and information
                pertaining to it's use should be present in the ABILITIES
                dictionary of equipment.py.
        """
        self.character_abilities.addTo(Ability)
    
    def __str__(self) -> str:
        """Prints detailed information about a character.
        """
        return f"Name: {self.name}\n" + \
        f"HP: {self.current_hp} (Base: {self.max_hp})\n" + \
        f"Weapon: {self.weapon.name} - {self.attack_stat} (Base: {self.attack_base}) ATK\n" + \
        f"Armor: {self.armor.name} - {self.defense_stat} (Base: {self.defense_base}) DEF\n" + \
        f"Abilities: {self.character_abilities}\n"
        
    def __lt__(self, other) -> bool:
        return self.agility_stat < other.agility_stat
    
    def __rt__(self, other) -> bool:
        return self.agility_stat > other.agility_stat

# I know constants are traditionally placed at top, this
# line won't work due to Character not being defined if it's placed there

class Party():
    def __init__(self, party_list: list):
        self.party_list = party_list
        
    def __str__(self) -> str:
        listofcharacteramongus = str()
        for c in self.party_list:
            listofcharacteramongus = listofcharacteramongus + f"Name: {c.name} | HP: {c.current_hp} ({c.max_hp})\n"
        return listofcharacteramongus
        
class Player_Party(Party):
    def __init__(self, party_list: list):
        for p in party_list:
            p.player_character = True
        self.party_list = party_list

    def __getitem__(self, index) -> Character:
        return self.party_list[index]
    
    def __len__(self) -> int:
        return len(self.party_list)