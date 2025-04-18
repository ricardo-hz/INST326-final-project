import equipment
import random

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
    
    def __init__(self, name, hp, weapon = None, armor = None, abilities 
                 = []):
        """Initializes a new character object.
        
        Args:
            name (str) : The character's name
            hp (float) : The character's starting health points.
            weapon (Weapon) : The character's starting weapon. None if omitted.
            armor (Armor) : The character's starting armor. None if omited.
            abilities (list of Ability) : The character's starting abilities.
                Empty list if ommitted. 
        
        TODO:
            - Should weapon be a list of weapon objects? or will characters 
            have one weapon only?
        """
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.weapon = weapon
        self.armor = armor
        self.abilities = abilities
        
    def attack(self, other_character):
        other_character.hp -= 20
    
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
    
    def __repr__(self):
        return f"{self.name}: {self.hp}"
    # Methods needed for group members:
        # Some sort of method needed for abilities for Ricardo
        # Attack method for Nathan
        # Aviva is doing something with equipment (weapon and armor)
        
def character_equipment(name, weapons, armour, battle_outcome):
    for an_ability in Character.add_ability:
        if isinstance(an_ability, equipment.Weapon()):
            weapons.append(an_ability)
        else:
            armour.append(an_ability)
    print(f"It is now {name}'s turn. The weapons that {name} " 
            f"currrently has are: {weapons} and their current armour "
            f"is: {armour}.")
    input(f"Please choose one weapon from the list given. ")
    input(f"Please choose one piece of armour from the list given. ")
    if battle_outcome == "Won":
        weapon_addition = input("Congrats on winning the battle! Please "
                "choose one weapon to add to your character's abilities ")
        armour_addition = input("Now please choose one weapon to add to "
                                "your character's abilities ")
        weapons.append(weapon_addition)
        armour.append(armour_addition)
    elif battle_outcome == "Lost":
        print(f"Unfortunately, you lost your battle and are not able to "
                f"upgrade your weapons and armour. Your weapons are: "
                f"{weapons} and your armour is: {armour}. Better "
                f"luck next time!")
    else:
        print(f"A battle was not played. Your weapons are: {weapons} "
                f"and your armour is: {armour}.")

def ComputerTurn(human_party, monster_party):
    """Decides how the monsters in the enemy party will attack our player's
        party own characters: Written by Nathan Castelo.
        
    Args:
        human_party (list of Characters): The characters in the Player's party
        monster_party (list of Characters): The characters in the Computer's 
            party
        
    Side effects:
        Reduces the HP of a targeted character
        Prints out the result of an attack
        Prints out if a player's character has died if their HP is reduced
        to 0 or less
    """
    human_party_max_hp = [character.max_hp for character in human_party]
    selected_target = None
    for monster in monster_party:
        for character in human_party:
            # A character will always be targeted if they are below an HP
            # threshhold which is less than or equal to 10% of their HP
            if character.hp <= character.hp * 0.10:
                selected_target = character
            if character.max_hp == max(human_party_max_hp):
                probability = random.randint(1, 100)
                if probability <= 65:
                    selected_target = character
            elif character.max_hp == min(human_party_max_hp):
                probability = random.randint(1,100)
                if probability <= 25:
                    selected_target = character
            else:
                selected_target = character
                
        monster.attack(selected_target)
        print(f"{monster.name} has attacked {selected_target.name}! "
              f"{selected_target.name} now has "
              f"{selected_target.hp} remaining HP!")
        if selected_target.hp <= 0:
            print(f"{selected_target.name} has died!")
            human_party.remove(selected_target)
    print(f"Party HP: {human_party}")
        

#################################
# The below code is for testing #
#################################
c = Character("Kal",250)
p = Character("Elvi",200)
e = Character("Natt", 300)
s = Character("Squishy", 150)

mon1 = Character("Yllive", 200)
mon2 = Character("Villye", 200)
mon3 = Character("Evilly", 200)
c.add_ability(equipment.Ability("Super Smash"))
# Is there a better way to make it apparent that we're calling a specific 
# ability than abilities[index]?


# I think there might not be because of the menu based nature of the game when 
# it's complete
print(f"health: {p.hp}")
c.abilities[0].use(p)
print(f"health: {p.hp}")

human_party = [c, e, s]
monster_party = [mon1, mon2, mon3]

for i in range(10):
    ComputerTurn(human_party, monster_party)



