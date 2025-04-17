import equipment

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
    
    def __init__(self, hp, weapon = None, armor = None, abilities = []):
        """Initializes a new character object.
        
        Args:
            hp (float) : The character's starting health points.
            weapon (Weapon) : The character's starting weapon. None if omitted.
            armor (Armor) : The character's starting armor. None if omited.
            abilities (list of Ability) : The character's starting abilities.
                Empty list if ommitted. 
        
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
        """Adds an ability object to a character's abilities list.
        
        Args:
            ability (Ability) : The ability to add. This ability and information
                pertaining to it's use should be present in the ABILITIES
                dictionary of equipment.py.
        """
        if ability.name.upper() not in self.abilities:
            self.abilities.append(equipment.Ability(ability.name.upper())) 
    
    # Methods needed for group members:
        # Some sort of method needed for abilities for Ricardo
        # Attack method for Nathan
        # Aviva is doing something with equipment (weapon and armor)

#################################
# The below code is for testing #
#################################
c = Character(250)
p = Character(200)
c.add_ability(equipment.Ability("Super Smash"))
# Is there a better way to make it apparent that we're calling a specific 
# ability than abilities[index]?

# I think there might not be because of the menu based nature of the game when 
# it's complete
print(f"health: {p.hp}")
c.abilities[0].use(p)
print(f"health: {p.hp}")
