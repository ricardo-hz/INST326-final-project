from character_class import Character
from equipment import WEAPONS, ARMOR
from ability_test import Ability, AbilityList

# Knight Abilities/Stuff
slash = Ability("Slash", "damage", 1)
knight_will = Ability("Knight's Will", "buff", 1.2, 4, 1, 3)
cross_slash = Ability("Cross Slash", "damage", 1.3, 3, 2)
knight_abilities = AbilityList([slash, knight_will, cross_slash])
knight = Character("Leo the Knight", 300, 30, WEAPONS["Knight"][0], None, 
                   knight_abilities)

# Priest Abilities/Stuff
light_ray = Ability("Light Ray", "damage", 1.15)
holy_blessing = Ability("Holy Blessing", "heal", 1.5, 3)
lichtgott_protection = Ability("Lichtgott's Protection", "buff", 1.3, 4, 1, 2)
priest_abilities = AbilityList([light_ray, holy_blessing, lichtgott_protection])
priest = Character("Aquarius the Priest", 200, 35, WEAPONS["Cleric"][0], None, 
                   priest_abilities)

# Thief Abilities/Stuff
stab = Ability("Stab", "damage", 1)
pocket_sand = Ability("Pocket Sand", "debuff", 1.3, 4, 1, 3)
triple_stab = Ability("Triple Stab", "damage", 1.25, 3, 3)
thief_abilities = AbilityList([stab, pocket_sand, triple_stab])
thief = Character("Gemini the Thief", 250, 80, WEAPONS["Thief"][0], None,
                  thief_abilities)

# Archer Abilities/Stuff
arrow_shot = Ability("Arrow Shot", "damage", 1)
double_shot = Ability("Double Shot", "damage", 1.25, 2, 2)
sniper_focus = Ability("Sniper's Focus", "damage", 1.75, 5)
archer_abilities = AbilityList([arrow_shot, double_shot, sniper_focus])
archer = Character("Sagitarrius the Archer", 250, 75, WEAPONS["Archer"][0], None,
                   archer_abilities)

# Mage Abilities/Stuff
blast = Ability("Elemental Blast", "damage", 1)
ice_pillars = Ability("Ice Pillars", "damage", 1.15, 3, 2)
fire_bolt = Ability("Fire Bolt", "damage", 1.5, 4)
mage_abilities = AbilityList([blast, ice_pillars, fire_bolt])
mage = Character("Pisces the Mage", 250, 35, WEAPONS["Mage"][0], None,
                 mage_abilities)

# Paladin Abilities/Stuff
bludgeon = Ability("Bludgeon", "damage", 1.15)
lichtgott_favor = Ability("Lichtgott's Favor", "heal", 1, 2)
hammer_throw = Ability("Hammer Throw", "damage", 1.25, 3)
paladin_abilites = AbilityList([bludgeon, lichtgott_favor, hammer_throw])
paladin = Character("Libra the Paladin", 350, 25, WEAPONS["Paladin"][0], None,
                    paladin_abilites)

# The Protagonist Abilities/Stuff (FOR TESTING/GRADING)
smack = Ability("SMACK!", "damage", 10, 1, 2)
throw = Ability("Water Bottle Throw!", "damage", 20, 1)
drink = Ability("QUENCH THY THIRST!", "heal", 20, 1)
protagonist_abilities = AbilityList([smack, throw, drink])
the_protagonist = Character("The Protagonist", 50000, WEAPONS["Protagonist"][0], 
                            None, protagonist_abilities)


ALL_CHARACTERS = {
    "Knight": knight,
    "Thief": thief,
    "Priest": priest,
    "Archer": archer,
    "Mage": mage,
    "Paladin": paladin,
    "Protagonist": the_protagonist
}