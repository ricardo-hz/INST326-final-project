class Weapon:
    """Representation of a Weapon.
    
    Attributes:
        name (str): name of weapon
        damage (int): damage of weapon
        abilMod (None/list): ability upgrades granted by weapon, a list with
        two ability names: original abilities, and new ability name
        by default None THIS SHOULD  BE CHANGED OR REMOVED PROLLY REMOVED 
        hitMod (int): amount of additional hits this weapon adds to abilities.
        by default, 0
    """
    def __init__(self, name: str, damage: int, abilMod: list | None = None, \
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
        self.abilMod: list | None = abilMod
        # abilMod is list of two strings containing name of orig ability, name
        # of enhanced ability with weapon
        
        hitMod: int = hitMod
class Armor:
    """Representation of armor.
    
    Attributes:
        name (str): name of weapon
        damage (int): damage of weapon
        abilMod (None/list): ability upgrades granted by weapon, a list with
        two ability names: original abilities, and new ability name
        by default None THIS SHOULD  BE CHANGED OR REMOVED PROLLY REMOVED 
    """
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