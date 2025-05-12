from enemies import Enemy, Enemy_Party
from ability_test import Ability, AbilityList

# Generalized basic attacks for all enemies, what they should default to
basic_attack1 = Ability("Slash", "damage", 1)
basic_attack2 = Ability("Bite", "damage", 1)
basic_attack3 = Ability("Smash", "damage", 1)
basic_attack4 = Ability("Dark Orb", "damage", 1)
basic_attack5 = Ability("Arrow Shot", "damage", 1)

# Goblin Leader specific abilities
spear_throw = Ability("Spear Throw", "damage", 1.25, cooldown = 3)
bear_trap = Ability("Bear Trap", "debuff", 1.2, cooldown = 3, round_length = 5)

# Alpha Wolf specific abilities
claw_strike = Ability("Claw Strike", "damage" , 1.1, cooldown = 4, hits = 2)
howl = Ability("Howl", "debuff", 1.1, cooldown = 3, round_length = 3)

# Cultist Priest specific abilities
heal = Ability("Rejuvanate", "heal", 1.2, 4, 1)
curse = Ability("Curse", "debuff", 1.1, 2, 1, 3)

# Bandit Leader specific abilities
speed_up = Ability("Swiftness", "buff", 1, 3, 1, 4)
dagger_throw = Ability("Dagger Throw", "damage", 1.2, 3, 2)

# Harpy Elder Sister specific abilities
sing = Ability("Melodious Hum", "buff", 1, 5, 1, 3)
screech = Ability("Dissonant Scream", "damage", 1.3, 4, 2)

# Cyclop ability (since there's two of them only one new ability)
double_smack = Ability("Double Bludgeon", "damage", 1.4, 3, 2)

# Vampire Lord specific abilities
drain = Ability("Blood Drain", "damage", 1.2, 4, 3)
hypnosis = Ability("Hypnosis", "debuff", 1, 3, 1, 4)

# Draugr Berserker specific abilities
rage = Ability("Rage", "buff", 1.2, 4, 1, 3) # Will also use for Orc Chieftain
great_slash = Ability("Great Slash", "damage", 1.4, 3, 1)

# Wood Elf General Specific Abilities
sniper_shot = Ability("Sniper Shot", "damage", 1.5, 4, 1)
spirit_hex = Ability("Spirit Hex", "debuff", 1, 3, 1, 2)

# Minotaur Abilities
mighty_roar = Ability("Mighty Roar", "buff", 1.5, 999, 1, 999)
brute_charge = Ability("Brute Charge", "damage", 1.4, 5, 1)
great_smash = Ability("Great Smash", "damage", 1.5, 4, 1)

# Necromancer Abilities
bone_spear = Ability("Bone Spear", "damage", 1.5, 4, 1)
death_embrace = Ability("Death's Embrace", "buff", 1.5, 999, 1, 999)

# Erlkonig Abilities
grand_puncture = Ability("Grand Puncture", "damage", 1.6, 5, 1)
elf_waltz = Ability("The Elf's Waltz", "buff", 1.5, 999, 1, 999)
blume_shot = Ability("Blume Shot", "damage", 1.3, 3, 2)

g1 = Enemy("Goblin Leader", 5, 2, 35, 10, "Strong Enemy", 
           AbilityList([basic_attack1, spear_throw, bear_trap]))
g2 = Enemy("Goblin Soldier A", 5, 2, 20, 16, "Normal Enemy", 
           AbilityList([basic_attack1]))
g3 = Enemy("Goblin Soldier B", 5, 2, 20, 12, "Normal Enemy", 
           AbilityList([basic_attack1]))
g4 = Enemy("Goblin Soldier C", 4, 2, 20, 8, "Normal Enemy", 
           AbilityList([basic_attack1]))
g5 = Enemy("Goblin Soldier d", 4, 2, 20, 4, "Normal Enemy", 
           AbilityList([basic_attack1]))

goblins = [g1, g2, g3, g4, g5]
goblin_horde = Enemy_Party("Goblin Horde", goblins)

w1 = Enemy("Alpha Wolf", 5, 2, 30, 18, "Strong Enemy", 
           AbilityList([basic_attack2, claw_strike, howl]))
w2 = Enemy("Wolf A", 4, 2, 12, 11, "Normal Enemy", 
           AbilityList([basic_attack2]))
w3 = Enemy("Wolf B", 4, 2, 12, 10, "Normal Enemy", 
           AbilityList([basic_attack2]))
w4 = Enemy("Wolf C", 4, 2, 12, 8, "Normal Enemy", 
           AbilityList([basic_attack2]))
w5 = Enemy("Wolf D", 4, 2, 12, 6, "Normal Enemy", 
           AbilityList([basic_attack2]))
wolves = [w1, w2, w3, w4, w5]
wolf_pack = Enemy_Party("Wolf Pack", wolves)

c1 = Enemy("Cultist Priest", 12, 4, 30, 20, "Strong Enemy", 
           AbilityList([basic_attack4, curse, heal]))
c2 = Enemy("Cultist Follower A", 9, 5, 35, 14, "Normal Enemy", 
           AbilityList([basic_attack4]))
c3 = Enemy("Cultist Follower B", 9, 5, 35, 12, "Normal Enemy", 
           AbilityList([basic_attack4]))
c4 = Enemy("Cultist Follower C", 9, 5, 35, 3, "Normal Enemy", 
           AbilityList([basic_attack4]))
cultists = [c1, c2, c3, c4]
cult = Enemy_Party("Cult of the Forgotten", cultists)

b1 = Enemy("Bandit Leader", 11, 5, 40, 20, "Strong Enemy",  
           AbilityList([basic_attack1, speed_up, dagger_throw]))
b2 = Enemy("Bandit Lackey A", 9, 5, 32, 16, "Normal Enemy", 
           AbilityList([basic_attack1]))
b3 = Enemy("Bandit Lackey B", 9, 5, 32, 10, "Normal Enemy", 
           AbilityList([basic_attack1]))
b4 = Enemy("Bandit Lackey C", 9, 5, 32, 8, "Normal Enemy", 
           AbilityList([basic_attack1]))
bandits = [b1, b2, b3, b4]
bandit_group = Enemy_Party("Sunset Mountain Bandits", bandits)

h1 = Enemy("Harpy Elder Sister", 20, 9, 125, 12, "Strong Enemy", 
           AbilityList([basic_attack1, screech, sing]))
h2 = Enemy("Harpy Sister A", 18, 9, 100, 16, "Normal Enemy", 
           AbilityList([basic_attack1]))
h3 = Enemy("Harpy Sister B", 18, 9, 110, 10, "Normal Enemy", 
           AbilityList([basic_attack1]))
harpy_trio = Enemy_Party("Winds of Harpies", [h1,h2,h3])

e1 = Enemy("Red Cyclops", 24, 9, 160, 1, "Strong Enemy", 
           AbilityList([basic_attack3, double_smack]))
e2 = Enemy("Blue Cyclops", 26, 9, 160, 0, "Strong Enemy", 
           AbilityList([basic_attack3, double_smack]))
cyclops_duo = Enemy_Party("Pair of Cyclops", [e1,e2])

v1 = Enemy("Vampire Lord", 45, 15, 260, 50, "Strong Enemy", 
           AbilityList([basic_attack2, drain, hypnosis]))
v2 = Enemy("Vampire Thrall A", 40, 18, 150, 50, "Normal Enemy", 
           AbilityList([basic_attack2]))
v3 = Enemy("Vampire Thrall B", 40, 18, 150, 50, "Normal Enemy", 
           AbilityList([basic_attack2]))
v4 = Enemy("Vampire Thrall C", 40, 18, 150, 50, "Normal Enemy", 
           AbilityList([basic_attack2]))
vampire_sect = Enemy_Party("Cult of the Bloody Moon", [v1,v2,v3,v4])

d1 = Enemy("Draugr Berserker", 52, 0, 300, 0, "Strong Enemy", 
           AbilityList([basic_attack1, rage, great_slash]))
d2 = Enemy("Draugr Warrior A", 36, 35, 200, 30, "Normal Enemy", 
           AbilityList([basic_attack1]))
d3 = Enemy("Draugr Warrior B", 36, 35, 200, 30, "Normal Enemy", 
           AbilityList([basic_attack1]))
draugr_berserkers = Enemy_Party("Ancient Draugrs", [d1,d2,d3])

o1 = Enemy("Orc Chieftain", 65, 24, 400, 14, "Strong Enemy", 
           AbilityList([basic_attack3, rage, great_smash]))
o2 = Enemy("Orc Warrior A", 50, 26, 260, 16, "Normal Enemy", 
           AbilityList([basic_attack3]))
o3 = Enemy("Orc Warrior B", 52, 26, 260, 12, "Normal Enemy", 
           AbilityList([basic_attack3]))
orcs = [o1, o2, o3]
orc_tribe = Enemy_Party("Orsinium Orc Tribe", orcs)

s1 = Enemy("Wood Elf General", 66, 24, 340, 15, "Strong Enemy", 
           AbilityList([basic_attack5, sniper_shot, spirit_hex]))
s2 = Enemy("Wood Elf Soldier A", 66, 30, 240, 14, "Normal Enemy", 
           AbilityList([basic_attack5]))
s3 = Enemy("Wood Elf Soldier B", 66, 30, 240, 8, "Normal Enemy", 
           AbilityList([basic_attack5]))
elves = [s1, s2, s3]
elf_militia = Enemy_Party("Holz Elf Militia", elves)

minotaur = Enemy("Minotaur", 100, 18, 1500, 20, "Boss", 
                 AbilityList([basic_attack3, mighty_roar, 
                              great_smash, brute_charge]))
minotaur_party = Enemy_Party("The Minotaur", [minotaur])

necromancer = Enemy("Necromancer", 80, 30, 600, 10, "Boss", 
                    AbilityList([basic_attack4, bone_spear, death_embrace]))
death_knight = Enemy("Death Knight", 72, 32, 800, 4, "Boss", 
                     AbilityList([basic_attack1, great_slash]))
necromancer_party = Enemy_Party("The Damned", [necromancer, death_knight])

elf_king = Enemy("Elf King", 85, 36, 700, 50, "Boss", 
                 AbilityList([basic_attack5, grand_puncture, elf_waltz, 
                              blume_shot]))
erlkonig_party = Enemy_Party("Erlkonig", [elf_king])

ROUND_ONE_ENEMIES = [goblin_horde, wolf_pack]
ROUND_TWO_ENEMIES = [cultists, bandit_group]
ROUND_THREE_ENEMIES = [harpy_trio, cyclops_duo]
ROUND_FOUR_ENEMIES = [vampire_sect, draugr_berserkers]
ROUND_FIVE_ENEMIES = [elf_militia, orc_tribe]
LIST_OF_BOSSES = [minotaur_party, necromancer_party, erlkonig_party]