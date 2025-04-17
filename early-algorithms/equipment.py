# Idk if we'll actually need all or any of these classes, I'm just putting them 
# here as a foundation of sorts

class Weapon():
    pass

class Armor():
    pass

# Abilities dictionary with all possible abilities?
ABILITIES = {
    "SUPER SMASH" : [0, 0, 0]
}

class Ability():
    def __init__(self, damage = 0, heal = 0, cooldown = 0):
        """Initializes an ability object.
        
        """
        pass
    
    def use(self, other_character):
        """Casts an ability object onto a character.
        
        """
        print("ability used!")
        pass