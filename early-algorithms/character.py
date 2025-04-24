import equipment
import random
import weapon_and_armor_test as et

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
    
    def __init__(self, name: str, char_id: int, hp: int, weapon: et.Weapon = None, 
                 armor: et.Armor = None, abilities: dict = dict()):
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
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f"Not valid type for name: {type(name)}")
        
        if isinstance(char_id, int):
            self.char_id = char_id
        else: 
            raise TypeError(f"Not valid type for char id: {type(char_id)}")
        
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
        
        if isinstance(abilities, dict):
            self.abilities = abilities
        else:
            raise TypeError(f"Not valid type for abilities: {type(abilities)}")
        
        self.attack = self.weapon.damage
        self.defense = self.armor.defense
        
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
    
    def __repr__(self):
        return f"{self.name}: {self.hp}"

# Ideally these classes will eventually be shrank down to just Tank(), Damage(), Support()
# and predefined characters will inherit from the respective class which 
# inherits from the Character class
class Tank_1(Character):
    # TODO: Verify that the empty abilities list is inherited without me 
    # explicitly saying so
    def __init__(self, name, hp):
        super().__init__(name, 1, hp) # char id of 1
    role = "Tank"

class Tank_2(Character):
    def __init__(self, name, hp):
        super().__init__(name, 2, hp)
    
    role = "Tank"

class Dmg_1(Character):
    def __init__(self, name, hp):
        super().__init__(name, 3, hp)
        
    role = "Damage"

class Dmg_2(Character):
    def __init__(self, name, hp):
        super().__init__(name, 4, hp)
        
    role = "Damage"

class Supp_1(Character):
    def __init__(self, name, hp):
        super().__init__(name, 5, hp)
        
    role = "Support"

class Supp_2(Character):
    def __init__(self, name, hp):
        super().__init__(name, 6, hp)
        
    role = "Support"




