class Weapon:
    def __init__(self, name: str, damage: int, abilMod: list | None = None, \
        hitMod: int = 0):
        
        # weapon damage. an integer value
        if isinstance(damage, int):
            self.damage: int = damage
        else:
            raise TypeError(f"Not valid type for dmg: {type(damage)}")
        
        # name of weapon, str
        if isinstance(name, str):
            self.name: str = name
        else:
            raise TypeError(f"Not valid type for name: {type(name)}")
        
        # ability that is modified by weapon, has orig abil and new abil
        self.abilMod: list | None = abilMod
        # abilMod is list of two strings containing name of orig ability, name
        # of enhanced ability with weapon


WEAPONS = [Weapon("Generic Weapon 1", 20, []),
           Weapon("Generic Weapon 2", 25, []),
           Weapon("Generic Weapon 3", 15, []),
           Weapon("Generic Weapon 4", 35, []),
        ]
class Armor:
    def __init__(self, name: str, defense:int, abilMod: list | None = None):
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
        self.abilMod: list | None = abilMod