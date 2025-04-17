# Idk if we'll actually need all or any of these classes, I'm just putting them 
# here as a foundation of sorts

class Weapon():
    pass

class Armor():
    pass

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