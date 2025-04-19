import equipment
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
    
    def __init__(self, name, char_id, hp, weapon = None, 
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
        self.char_id = char_id
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

# Ideally these classes will eventually be shrank down to just Tank() and 
# predefined characters will inherit from the Tank class which inherits from
# the Character class
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




