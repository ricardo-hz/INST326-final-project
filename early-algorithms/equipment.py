#from ability_test import *

class Weapon:
    """Representation of a Weapon.
    
    Attributes:
        name (str): name of weapon
        damage (int): damage of weapon
    """
    def __init__(self, name, damage):
        # name of weapon, str
        if isinstance(name, str):
            self.name: str = name
        else:
            raise TypeError(f"Not valid type for name: {type(name)}")
        
        # weapon damage. an integer value
        if isinstance(damage, int):
            self.damage = damage
        else:
            raise TypeError(f"Not valid type for dmg: {type(damage)}")

# Name, dmg, allowed characters?
WEAPONS = [Weapon("Generic Weapon 1", 20),
           Weapon("Generic Weapon 2", 25),
           Weapon("Generic Weapon 3", 15),
           Weapon("Generic Weapon 4", 35),
        ]


class Armor:
    """Representation of armor.
    
    Attributes:
        name (str): name of armor
        defense (float): damage reduction as a float 0 - 1
    """
    def __init__(self, name, defense):
        # armor defense. an integer value
        if isinstance(defense, float):
            self.defense = defense
        else:
            raise TypeError(f"Not valid type for defn: {type(defense)}")
        
        # name of weapon, str
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f"Not valid type for name: {type(name)}")
        
ARMOR = [Armor("Generic Armor 1", 0.20),
           Armor("Generic Armor 2", 0.25),
           Armor("Generic Armor 3", 0.15),
           Armor("Generic Armor 4", 0.35),
        ]



ABILITIES = {
    "Generic Ability 1" : [100, 0, 2],
    "Generic Ability 2" : [85, 0, 3],
    "Generic Ability 3" : [0, 100, 1],
    "Generic Ability 4" : [10, 63, 2]
}

class Ability():
    def __init__(self, name, damage = 0, heal = 0, cooldown = 0):
        """Initializes an ability object.
        
        """

        # Set the other ability elements
        self.name = name
        self.damage, self.heal, self.maximum_cooldown = [*ABILITIES[name]]
        #self.damage = damage
        #self.heal = heal
        #self.maximum_cooldown = cooldown
        self.cooldown = cooldown
    
    def use(self, other_character):
        """Casts an ability object onto a character.
        
        """
        other_character.hp += self.heal
        other_character.hp -= self.damage
        # Reset cooldown to maximum according to dictionary
        self.cooldown = self.maximum_cooldown
        print("ability used!")
        
    def __str__(self):
        return(f"Name: {self.name} "
               f"Damage: {self.damage} "
               f"Healing: {self.heal} "
               f"Maximum cooldown: {self.maximum_cooldown} "
               f"Current cooldown: {self.cooldown} "
               )
# Abilities dictionary with all possible abilities?
# Name : dmg, heal, cooldown
# Maybe damage can be a percentage of the enemies health to make this more
# interesting

ABILITIES_LIST = [Ability(key, *value) for key,value in ABILITIES.items()]