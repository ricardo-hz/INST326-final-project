import equipment
import random
import weaponarmor_btest as et
import ability_test as at

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
    
    """
    
    def __init__(self, name: str, character_id: int, hp: int, agility: int, weapon: et.Weapon, 
                 armor: et.Armor, characterAbilities: at.AbilityList):
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
        
        TODO:
            - Should weapon be a list of weapon objects? or will characters 
            have one weapon only?
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
        
        if isinstance(characterAbilities, dict):
            self.abilities = characterAbilities
        else:
            raise TypeError(f"Not valid type for abilities: {type(characterAbilities)}")
        
        self.attack_base = self.weapon.damage
        self.attack_stat = self.attack_base
        self.defense_base = self.armor.defense
        self.defense_stat = self.defense_base
        self.agility_base = agility
        self.agility_stat = self.agility_base
        
        self.characterAbilities = characterAbilities
        
    def attack(self, other_character):
        other_character.hp -= 20
    
    def add_weapon(self, weapon):
        raise NotImplementedError;  
    
    def remove_weapon(self, weapon):
        raise NotImplementedError;  
    
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
    
    def __str__(self) -> str:
        return f"{self.name}: {self.hp}"
    
    def __lt__(self, other) -> bool:
        return self.agility < other.agility

class Party():
    def __init__(self, partyList: list):
        self.partyList = sorted(partyList)
        