import equipment

class Character():
    """Represents a character.
    
    This class is only being used for demonstration purposes and early algorithm
    testing.
    
    Attributes:
        something (type) : 
        
    Methods:
        something (self, arg, arg) : 
    """
    
    def __init__(self, hp, weapon = None, armor = None, abilities = []):
        """Initializes a new character object.
        
        Args:
            hp (float) : The character's starting health points.
            weapon (Weapon) : The character's starting weapon. None if omitted.
            armor (Armor) : The character's starting armor. None if omited.
            abilities (list of Ability) : The character's starting abilities.
                None if ommitted. 
        
        TODO:
            - Should weapon be a list of weapon objects? or will characters 
            have one weapon only?
        """
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
        self.abilities = abilities
        
    def attack(self, other_character):
        pass
    
    def add_weapon(self, weapon):
        pass
    
    def remove_weapon(self, weapon):
        pass
    
    def add_ability(self, ability):
        if ability not in self.abilities:
            self.abilities.append(ability) 
    
    # Methods needed for group members:
        # Some sort of method needed for abilities for Ricardo
        # Attack method for Nathan
        # Aviva is doing something with equipment (weapon and armor)
        
c = Character(250)
c.add_ability("Super Smash")
print(c.abilities)