from character_class import Character
from all_equipment import WEAPONS, ARMOR
from ability_test import Ability, AbilityList

# Knight Abilities/Stuff
slash = Ability("Slash", "damage", 1)
knight_will = Ability("Knight's Fury", "buff", 1.2, cooldown = 3, 
                      round_length = 3)
cross_slash = Ability("Cross Slash", "damage", 1.3, cooldown = 2, hits = 2)
brutal_cleave = Ability("Brutal Cleave", "damage", 1.5, cooldown = 3)
dawnbreaker_rend = Ability("Dawnbreaker Rend", "damage", 2.0, 
                           cooldown = 5)
knight_abilities = AbilityList([slash, knight_will, cross_slash])
knight = Character("Leo the Knight", 14, 5, WEAPONS["Leo the Knight"][0], 
                   ARMOR["Metal"][0], knight_abilities, selection_message= 
                   "Hah! Let's teach some new foes some old tricks!",
                   finale_message = "Just like the ones before! No sweat.",
                   health_progression = [0, 8, 12, 34, 70, 90], armor_type = 
                   "metal")
                    #14, 22, 34, 68, 138, 228
                    
# Priest Abilities/Stuff
light_ray = Ability("Light Ray", "damage", 1.15)
holy_blessing = Ability("Holy Blessing", "heal", 1.5)
lichtgott_protection = Ability("Lichtgott's Protection", "buff", 1.35, 
                               cooldown = 2, round_length = 2)
sanctified_blaze = Ability("Sanctified Blaze", "heal", 3.5, 
                           cooldown = 3, hits = 2)
lichtgott_fury = Ability("Lichtgott's Fury", "damage", 1.5, 
                         cooldown = 5, hits = 3)
priest_abilities = AbilityList([light_ray, holy_blessing, lichtgott_protection])
priest = Character("Aquarius the Priest", 10, 6, WEAPONS["Aquarius the Priest"]
                   [0], ARMOR["Leather"][0], 
                   priest_abilities, selection_message="Lichgott save us...!",
                   finale_message = "We can't lose... I will not let it happen!",
                   health_progression = [0, 8, 12, 30, 50, 75], armor_type = 
                   "leather")
                    #10, 18, 30, 60, 110, 185
# Thief Abilities/Stuff
stab = Ability("Stab", "damage", 1)
pocket_sand = Ability("Pocket Sand", "debuff", 1.3, cooldown = 3, 
                      round_length = 3)
triple_stab = Ability("Triple Stab", "damage", 1.25, cooldown = 2, hits = 3)
twilight_gouge = Ability("Twilight Gouge", "damage", 1.45, cooldown = 3)
death_whisper = Ability("Death's Whisper", "damage", 2, 
                        cooldown = 5, hits = 2)
thief_abilities = AbilityList([stab, pocket_sand, triple_stab])
thief = Character("Gemini the Thief", 12, 99, WEAPONS["Gemini the Thief"][0], 
                  ARMOR["Leather"][0],thief_abilities, selection_message= 
                  "Ran out of options? Heh, I'll come along anyways.",
                  finale_message = "Well, definitely can't back out now, hmmh?",
                  health_progression = [0, 8, 12, 30, 65, 73], armor_type = 
                  "leather")
                    #12, 20, 32, 62, 127, 200
# Archer Abilities/Stuff
arrow_shot = Ability("Arrow Shot", "damage", 1)
double_shot = Ability("Double Shot", "damage", 1.25, cooldown = 1, hits = 2)
sniper_focus = Ability("Sniper's Focus", "damage", 2.5, cooldown = 4)
deadeye_stance = Ability("Deadeye Stance", "buff", 1.5, 
                         cooldown = 3, round_length = 2)
barrage_of_thousand = Ability("Barrage of Thousand", "damage", 1.75, 
                              cooldown = 6, hits = 4)
archer_abilities = AbilityList([arrow_shot, double_shot, sniper_focus])
archer = Character("Sagitarrius the Archer", 11, 15, WEAPONS["Sagitarrius the"
                                                            " Archer"][0], 
                   ARMOR["Leather"][0],
                   archer_abilities, selection_message= "Decisions...",
                   finale_message = "Proceed.",
                   health_progression = [0, 7, 12, 32, 50, 83], armor_type = 
                   "leather")
                    #11, 18, 30, 62, 112, 195
# Mage Abilities/Stuff
blast = Ability("Elemental Blast", "damage", 1)
ice_pillars = Ability("Ice Pillars", "damage", 1.15, cooldown = 1)
fire_bolt = Ability("Fire Bolt", "damage", 1.5, cooldown = 3)
thunder_surge = Ability("Thunderous Surge", "damage", 2.0, cooldown = 3)
absolute_zero = Ability("Absolute Zero", "damage", 2.5, 
                        cooldown = 6, hits = 3)
mage_abilities = AbilityList([blast, ice_pillars, fire_bolt])
mage = Character("Pisces the Mage", 10, 12, WEAPONS["Pisces the Mage"][0], 
                 ARMOR["Cloth"][0], mage_abilities, selection_message = 
                 "Meticiulous planning is imperative for success. "
                 "The opposition will crumble under exquisite power!",
                 finale_message = "Splendid. We shall claim a triumph oncemore.",
                 health_progression = [0, 6, 10, 28, 46, 65], armor_type = 
                 "leather")
                    #10, 16, 26, 54, 100, 165
# Paladin Abilities/Stuff
bludgeon = Ability("Bludgeon", "damage", 1.15)
lichtgott_favor = Ability("Lichtgott's Favor", "heal", 1.2, cooldown = 1)
sword_throw = Ability("Sword Toss", "damage", 1.25, cooldown = 3)
lichtgott_brand = Ability("Lichtgott's Brand", "debuff", 1.5, cooldown = 3, 
                          round_length = 2)
final_edict = Ability("Final Edict", "damage", 2.2, 
                      cooldown = 5, hits = 2)
paladin_abilites = AbilityList([bludgeon, lichtgott_favor, sword_throw])
paladin = Character("Libra the Paladin", 16, 3, WEAPONS["Libra the Paladin"][0],
                    ARMOR["Metal"][0], paladin_abilites, selection_message= 
                    "Triumphant futures! A safe shield! Behind me!",
                    finale_message = "The end approaches! Approach with "
                    "victory on the mind!",
                    health_progression = [0, 8, 16, 40, 90, 100], armor_type =
                    "metal")
                    #16, 24, 40, 80, 170, 270
                    
# The Protagonist Abilities/Stuff (FOR TESTING/GRADING)
smack = Ability("SMACK!", "damage", 10, 1, 2)
throw = Ability("Water Bottle Throw!", "damage", 50, 1)
drink = Ability("QUENCH THY THIRST!", "heal", 20, 1)
drown = Ability("The Drowning", "damage", 50, cooldown = 1, hits = 5)
the_fourth_wall = Ability("The Fourth Wall", "damage", 1000, hits = 2)
protagonist_abilities = AbilityList([smack, throw, drink])
the_protagonist = Character("The Protagonist", 50000, 0, 
                            WEAPONS["The Protagonist"][0], ARMOR["Metal"][0], 
                            protagonist_abilities, selection_message = 
                            "Too easy.", finale_message = "Trivial.")

EXTRA_ABILITIES = {
    "Leo the Knight": [brutal_cleave, dawnbreaker_rend],
    "Aquarius the Priest": [sanctified_blaze, lichtgott_fury],
    "Gemini the Thief": [twilight_gouge, death_whisper],
    "Sagitarrius the Archer": [deadeye_stance, barrage_of_thousand],
    "Pisces the Mage": [thunder_surge, absolute_zero],
    "Libra the Paladin": [lichtgott_brand, final_edict],
    "The Protagonist": [drown, the_fourth_wall]
}

ALL_CHARACTERS = [ 
    knight,
    thief,
    priest,
    archer,
    mage,
    paladin,
    the_protagonist
]