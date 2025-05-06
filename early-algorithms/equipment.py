from ability_test import *

class Weapon:
    """Representation of a Weapon.
    
    Attributes:
        name (str): name of weapon
        damage (int): damage of weapon
        ability_included (None/list): ability given by weapon
        hitMod (int): amount of additional hits this weapon adds to abilities.
        by default, 0
    """
    def __init__(self, name: str, damage: int, ability_included: Ability = None, \
        hitMod: int = 0):
        # name of weapon, str
        if isinstance(name, str):
            self.name: str = name
        else:
            raise TypeError(f"Not valid type for name: {type(name)}")
        
        # weapon damage. an integer value
        if isinstance(damage, int):
            self.damage: int = damage
        else:
            raise TypeError(f"Not valid type for dmg: {type(damage)}")
        
        
        # ability that is modified by weapon, has orig abil and new abil
        self.ability_included: Ability = ability_included
        # abilMod is list of two strings containing name of orig ability, name
        # of enhanced ability with weapon
        
        hitMod: int = hitMod
class Armor:
    """Representation of armor.
    
    Attributes:
        name (str): name of weapon
        damage (int): damage of weapon
        ability_included (None/list): ability given by armor
    """
    def __init__(self, name: str, defense:int, \
        ability_included: Ability = None):
        # weapon damage. an integer value
        if isinstance(defense, int):
            self.defense: int = defense
        else:
            raise TypeError(f"Not valid type for defn: {type(defense)}")
        
        # name of weapon, str
        if isinstance(name, str):
            self.name: str = name
        else:
            raise TypeError(f"Not valid type for name: {type(name)}")
        
        # ability that is modified by weapon, has orig abil and new abil
        self.ability_included: Ability = ability_included
        
WEAPONS = [Weapon("Generic Weapon 1", 20, []),
           Weapon("Generic Weapon 2", 25, []),
           Weapon("Generic Weapon 3", 15, []),
           Weapon("Generic Weapon 4", 35, []),
        ]

# Abilities dictionary with all possible abilities?
# Name : dmg, heal, cooldown
ABILITIES = {
    "ABILITY NOT FOUND" : [3.14, 3.14, 9999], # Special ability reserved for debugging
    "SUPER SMASH" : [10, 0, 0]
}

class Ability():
    def __init__(self, name, damage = 0, heal = 0, cooldown = 0):
        """Initializes an ability object.
        
        """
        # Ensure ability is in ability dictionary
        if name.upper() in ABILITIES:
            self.name = name.upper()
        else:
            raise NameError(f"{name} is not a valid ability.")
        
        # Set the other ability elements
        self.damage = ABILITIES[self.name][0]
        self.heal = ABILITIES[self.name][1]
        self.cooldown = ABILITIES[self.name][2]
    
    def use(self, other_character):
        """Casts an ability object onto a character.
        
        """
        other_character.hp += self.heal
        other_character.hp -= self.damage
        # Reset cooldown to maximum according to dictionary
        self.cooldown = ABILITIES[self.name][2]
        print("ability used!")