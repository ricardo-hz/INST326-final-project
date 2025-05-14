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
bear_trap = Ability("Bear Trap", "damage", 1.2, cooldown = 3)

# Alpha Wolf specific abilities
claw_strike = Ability("Claw Strike", "damage" , 1.1, cooldown = 4, hits = 2)
howl = Ability("Howl", "damage", 1.1, cooldown = 3)

# Cultist Priest specific abilities
fire = Ability("Forgotten Fire", "damage", 1.2, 4, 1)
curse = Ability("Curse", "damage", 1.1, 2, 1, 3)

# Bandit Leader specific abilities
swift_slash = Ability("Swift Slash", "damage", 1.2, cooldown = 3)
dagger_throw = Ability("Dagger Throw", "damage", 1.2, cooldown = 3, hits = 2)

# Harpy Elder Sister specific abilities
sing = Ability("Melodious Hum", "damage", 1, cooldown = 3, hits = 2)
screech = Ability("Dissonant Scream", "damage", 1.3, 4, 2)

# Cyclop ability (since there's two of them only one new ability)
double_smack = Ability("Double Bludgeon", "damage", 1.4, 3, 2)

# Vampire Lord specific abilities
drain = Ability("Blood Drain", "damage", 1.2, 4, 3)
hypnosis = Ability("Hypnosis", "damage", 1, 3, 1, 4)

# Draugr Berserker specific abilities
rage = Ability("Rageful Bash", "damage", 1.2, cooldown = 3) 
great_slash = Ability("Great Slash", "damage", 1.4, 4, 1)

# Wood Elf General Specific Abilities
sniper_shot = Ability("Sniper Shot", "damage", 1.5, 4, 1)
spirit_hex = Ability("Spirit Hex", "damage", 1.2, cooldown = 3, hits = 2)

# Minotaur Abilities
mighty_roar = Ability("Mighty Roar", "damage", 1.5, cooldown = 7, hits = 2)
brute_charge = Ability("Brute Charge", "damage", 1.4, 5, 1)
great_smash = Ability("Great Smash", "damage", 1.5, 4, 1)

# Necromancer Abilities
bone_spear = Ability("Bone Spear", "damage", 1.5, 4, 1)
death_embrace = Ability("Death's Embrace", "damage", 1.75, cooldown = 7)

# Erlkonig Abilities
grand_puncture = Ability("Grand Puncture", "damage", 1.6, 5, 1)
elf_waltz = Ability("The Elf's Waltz", "damage", 1.5, cooldown = 7, hits = 2)
blume_shot = Ability("Blume Shot", "damage", 1.3, 3, 2)

g1 = Enemy("Goblin Leader", 5, 2, 35, 10, "Strong Enemy", 
           AbilityList([spear_throw, bear_trap, basic_attack1]))
g2 = Enemy("Goblin Soldier A", 5, 2, 20, 16, "Normal Enemy", 
           AbilityList([basic_attack1]))
g3 = Enemy("Goblin Soldier B", 5, 2, 20, 12, "Normal Enemy", 
           AbilityList([basic_attack1]))
g4 = Enemy("Goblin Soldier C", 4, 2, 20, 8, "Normal Enemy", 
           AbilityList([basic_attack1]))
g5 = Enemy("Goblin Soldier D", 4, 2, 20, 4, "Normal Enemy", 
           AbilityList([basic_attack1]))

goblins = [g1, g2, g3, g4, g5]
goblin_horde = Enemy_Party("Goblin Horde", goblins, "My Precious...")

w1 = Enemy("Alpha Wolf", 5, 2, 30, 18, "Strong Enemy", 
           AbilityList([howl, claw_strike, basic_attack2]))
w2 = Enemy("Wolf A", 4, 2, 12, 11, "Normal Enemy", 
           AbilityList([basic_attack2]))
w3 = Enemy("Wolf B", 4, 2, 12, 10, "Normal Enemy", 
           AbilityList([basic_attack2]))
w4 = Enemy("Wolf C", 4, 2, 12, 8, "Normal Enemy", 
           AbilityList([basic_attack2]))
w5 = Enemy("Wolf D", 4, 2, 12, 6, "Normal Enemy", 
           AbilityList([basic_attack2]))
wolves = [w1, w2, w3, w4, w5]
wolf_pack = Enemy_Party("Wolf Pack", wolves, "BARK BARK BARK!")

c1 = Enemy("Cultist Priest", 12, 4, 30, 20, "Strong Enemy", 
           AbilityList([curse, fire, basic_attack4]))
c2 = Enemy("Cultist Follower A", 9, 5, 35, 14, "Normal Enemy", 
           AbilityList([basic_attack4]))
c3 = Enemy("Cultist Follower B", 9, 5, 35, 12, "Normal Enemy", 
           AbilityList([basic_attack4]))
c4 = Enemy("Cultist Follower C", 9, 5, 35, 3, "Normal Enemy", 
           AbilityList([basic_attack4]))
cultists = [c1, c2, c3, c4]
cult = Enemy_Party("Cult of the Forgotten", cultists, "For the Forgotten One!")

b1 = Enemy("Bandit Leader", 11, 5, 40, 20, "Strong Enemy",  
           AbilityList([dagger_throw, swift_slash, basic_attack1]))
b2 = Enemy("Bandit Lackey A", 9, 5, 32, 16, "Normal Enemy", 
           AbilityList([basic_attack1]))
b3 = Enemy("Bandit Lackey B", 9, 5, 32, 10, "Normal Enemy", 
           AbilityList([basic_attack1]))
b4 = Enemy("Bandit Lackey C", 9, 5, 32, 8, "Normal Enemy", 
           AbilityList([basic_attack1]))
bandits = [b1, b2, b3, b4]
bandit_group = Enemy_Party("Sunset Mountain Bandits", bandits, 
                           "Give us all your loot!")

h1 = Enemy("Harpy Elder Sister", 20, 9, 125, 12, "Strong Enemy", 
           AbilityList([screech, sing, basic_attack3]))
h2 = Enemy("Harpy Sister A", 18, 9, 100, 16, "Normal Enemy", 
           AbilityList([basic_attack1]))
h3 = Enemy("Harpy Sister B", 18, 9, 110, 10, "Normal Enemy", 
           AbilityList([basic_attack1]))
harpy_trio = Enemy_Party("Winds of Harpies", [h1,h2,h3], "Ugh humans...")

e1 = Enemy("Red Cyclops", 24, 9, 160, 1, "Strong Enemy", 
           AbilityList([double_smack, basic_attack3]))
e2 = Enemy("Blue Cyclops", 26, 9, 160, 0, "Strong Enemy", 
           AbilityList([double_smack, basic_attack3]))
cyclops_duo = Enemy_Party("Pair of Cyclops", [e1,e2], "Puny humans!!!")

v1 = Enemy("Vampire Lord", 45, 15, 260, 10, "Strong Enemy", 
           AbilityList([drain, hypnosis, basic_attack2]))
v2 = Enemy("Vampire Thrall A", 40, 18, 150, 8, "Normal Enemy", 
           AbilityList([basic_attack2]))
v3 = Enemy("Vampire Thrall B", 40, 18, 150, 8, "Normal Enemy", 
           AbilityList([basic_attack2]))
v4 = Enemy("Vampire Thrall C", 40, 18, 150, 8, "Normal Enemy", 
           AbilityList([basic_attack2]))
vampire_sect = Enemy_Party("Cult of the Bloody Moon", [v1,v2,v3,v4], 
                           "We thirst for blood...")

d1 = Enemy("Draugr Berserker", 52, 0, 300, 10, "Strong Enemy", 
           AbilityList([rage, great_slash, basic_attack1]))
d2 = Enemy("Draugr Warrior A", 36, 35, 200, 9, "Normal Enemy", 
           AbilityList([basic_attack1]))
d3 = Enemy("Draugr Warrior B", 36, 35, 200, 9, "Normal Enemy", 
           AbilityList([basic_attack1]))
draugr_berserkers = Enemy_Party("Ancient Draugrs", [d1,d2,d3], 
                                "*rattling noises*")

o1 = Enemy("Orc Chieftain", 65, 24, 400, 14, "Strong Enemy", 
           AbilityList([rage, great_smash, basic_attack3]))
o2 = Enemy("Orc Warrior A", 50, 26, 260, 16, "Normal Enemy", 
           AbilityList([basic_attack3]))
o3 = Enemy("Orc Warrior B", 52, 26, 260, 12, "Normal Enemy", 
           AbilityList([basic_attack3]))
orcs = [o1, o2, o3]
orc_tribe = Enemy_Party("Orsinium Orc Tribe", orcs, 
                        "Fight to the death! We live for battle!")

s1 = Enemy("Wood Elf General", 66, 24, 340, 15, "Strong Enemy", 
           AbilityList([sniper_shot, spirit_hex, basic_attack5]))
s2 = Enemy("Wood Elf Soldier A", 66, 30, 240, 14, "Normal Enemy", 
           AbilityList([basic_attack5]))
s3 = Enemy("Wood Elf Soldier B", 66, 30, 240, 8, "Normal Enemy", 
           AbilityList([basic_attack5]))
elves = [s1, s2, s3]
elf_militia = Enemy_Party("Holz Elf Militia", elves, "Humans never change...")

minotaur = Enemy("Minotaur", 100, 18, 1000, 20, "Boss", 
                 AbilityList([mighty_roar, great_smash, 
                              brute_charge, basic_attack3]))
minotaur_party = Enemy_Party("The Minotaur", [minotaur], 
                             "It seems you are lost. Prepare to die!")

necromancer = Enemy("Necromancer", 80, 30, 600, 10, "Boss", 
                    AbilityList([bone_spear, death_embrace, basic_attack4]))
death_knight = Enemy("Death Knight", 72, 32, 800, 4, "Boss", 
                     AbilityList([great_slash, basic_attack1]))
necromancer_party = Enemy_Party("The Damned", [necromancer, death_knight], 
                                "Death claims all...")

elf_king = Enemy("Elf King", 85, 36, 700, 50, "Boss", 
                 AbilityList([grand_puncture, elf_waltz, 
                              blume_shot, basic_attack5]))
erlkonig_party = Enemy_Party("Erlkonig", [elf_king], 
                             "Humans are interesting...")

ROUND_ONE_ENEMIES = [goblin_horde, wolf_pack]
ROUND_TWO_ENEMIES = [cultists, bandit_group]
ROUND_THREE_ENEMIES = [harpy_trio, cyclops_duo]
ROUND_FOUR_ENEMIES = [vampire_sect, draugr_berserkers]
ROUND_FIVE_ENEMIES = [elf_militia, orc_tribe]
LIST_OF_BOSSES = [minotaur_party, necromancer_party, erlkonig_party]