from ability_test import *

# Abilities dictionary with all possible abilities?
# Name : dmg, heal, cooldown
ABILITIES = {
    "ABILITY NOT FOUND" : [3.14, 3.14, 9999], # Special ability reserved for debugging
    "SUPER SMASH" : [10, 0, 0],
    "Strike": Ability("Strike", "Damage", 1),
    "Mend Injury": Ability("Mend Injury", "Heal", 1.5),
    "Water Bottle": Ability("Water Bottle", "Damage", 20)
}

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
         
WEAPONS = {
        "Weapon 1": Weapon("Generic Weapon 1", 20),
        "Weapon 2": Weapon("Generic Weapon 2", 25),
        "Weapon 3": Weapon("Generic Weapon 3", 15),
        "Weapon 4": Weapon("Generic Weapon 4", 35),
}

ARMOR = {
        "Armor 1": Armor("Armor 1", 5),
        "Armor 2": Armor("Armor 2", 15),
        "Armor 3": Armor("Armor 3", 10),
        "Armor 4": Armor("Armor 4", 15)
}