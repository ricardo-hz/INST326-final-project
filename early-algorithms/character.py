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
        
    def character_equipment(self, weapons, armour, battle):
        for an_ability in self.abilities:
            if isinstance(an_ability, Weapon):
                self.weapons.append(an_ability)
            else:
                self.armour.append(an_ability)
        print(f"It is now {self.name}'s turn. The weapons that {self.name} " 
              f"currrently has are {self.weapons} and their current armour "
              f"is {self.armour}.")
        input(f"The battle you are fighting is: {self.battle}. Please choose "
              f"one weapon from the lists given ")
        if self.battle == "Won":
            weapon_addition = input("Congrats on winning the battle! Please "
                  "choose one weapon to add to your character's abilities ")
            armour_addition = input("Now please choose one weapon to add to "
                                    "your character's abilities ")
            self.weapons.append(weapon_addition)
            self.armour.append(armour_addition)
        elif self.battle == "Lost":
            print(f"Unfortunately, you lost your battle and are not able to "
                  f"upgrade your weapons and armour. Your weapons are: "
                  f"{self.weapons} and your armour is: {self.armour}. Better "
                  f"luck next time!")
        else:
            print(f"A battle was not played. Your weapons are: {self.weapons} "
                  f"and your armour is: {self.armour}.")

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
