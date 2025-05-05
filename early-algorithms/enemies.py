class Enemy:
    """Represents an enemy
    
    Attributes:
        name (str): name of enemy
        atk (int): enemy's base attack to be used for combat
        defs (int): enemy's base defense to be used for combat
        max_hp (int): enemy's total hp
        current_hp (int): enemy's current hp (subject to change during combat)
        agility (int): the agility of an enemy (what turn they take)
    """
    def __init__(self, name, atk, defs, hp, agility):
        self.name = name
        self.atk = atk
        self.defs = defs
        self.max_hp = hp
        self.current_hp = hp
        self.agility = agility
    
    def __lt__(self, other) -> bool:
        return self.agility < other.agility
        
class Enemy_Party:
    """Represents an enemy party to fight
    
    Attributes:
        name (str): the name of the party
        enemies (list of Enemy): the enemies to be in the party
    """
    def __init__(self, name, enemies):
        self.name = name
        self.enemies = enemies

# need to play around with the enemy's stats
# also if time maybe create some abilities for the bosses/powerful normal enemies

g1 = Enemy("Goblin Leader", 15, 20, 250, 50)
g2 = Enemy("Goblin Soldier A", 10, 15, 150, 30)
g3 = Enemy("Goblin Soldier B", 10, 15, 150, 30)
g4 = Enemy("Goblin Soldier C", 10, 15, 150, 30)
g5 = Enemy("Goblin Soldier d", 10, 15, 150, 30)
goblins = [g1, g2, g3, g4, g5]
goblin_horde = Enemy_Party("Goblin Horde", goblins)

w1 = Enemy("Alpha Wolf", 25, 15, 200, 50)
w2 = Enemy("Wolf A", 10, 10, 150, 30)
w3 = Enemy("Wolf B", 10, 10, 150, 30)
w4 = Enemy("Wolf C", 10, 10, 150, 30)
w5 = Enemy("Wolf D", 10, 10, 150, 30)
wolves = [w1, w2, w3, w4, w5]
wolf_pack = Enemy_Party("Wolf Pack", wolves)

c1 = Enemy("Cultist Priest", 35, 25, 250, 50)
c2 = Enemy("Cultist Follower A", 25, 20, 200, 30)
c3 = Enemy("Cultist Follower B", 25, 20, 200, 30)
c4 = Enemy("Cultist Follower C", 25, 20, 200, 30)
cultists = [c1, c2, c3, c4]
cult = Enemy_Party("Cult of the Forgotten", cultists)

b1 = Enemy("Bandit Leader", 40,  30, 275, 60)
b2 = Enemy("Bandit Lackey A", 30,  25, 250, 50)
b3 = Enemy("Bandit Lackey B", 30,  25, 250, 50)
b4 = Enemy("Bandit Lackey C", 30,  25, 250, 50)
bandits = [b1, b2, b3, b4]
bandit_group = Enemy_Party("Sunset Mountain Bandits", bandits)

h1 = Enemy("Harpy Elder Sister", 50, 30, 275, 80)
h2 = Enemy("Harpy Sister A", 45, 30, 265, 80)
h3 = Enemy("Harpy Sister B", 45, 30, 265, 80)
harpy_trio = Enemy_Party("Winds of Harpies", [h1,h2,h3])

e1 = Enemy("Red Cyclops", 40, 60, 300, 30)
e2 = Enemy("Blue Cyclops", 60, 40, 250, 30)
cyclops_duo = Enemy_Party("Pair of Cyclops", [e1,e2])

v1 = Enemy("Vampire Lord", 65, 40, 400, 50)
v2 = Enemy("Vampire Thrall A", 55, 30, 300, 50)
v3 = Enemy("Vampire Thrall B", 55, 30, 300, 50)
v4 = Enemy("Vampire Thrall C", 55, 30, 300, 50)
vampire_sect = Enemy_Party("Cult of the Bloody Moon", [v1,v2,v3,v4])

d1 = Enemy("Draugr Berserker", 75, 35, 450, 35)
d2 = Enemy("Draugr Warrior A", 60, 35, 325, 30)
d3 = Enemy("Draugr Warrior B", 60, 35, 325, 30)
draugr_berserkers = Enemy_Party("Ancient Draugrs", [d1,d2,d3])

o1 = Enemy("Orc Chieftain", 100, 50, 500, 50)
o2 = Enemy("Orc Warrior A", 75, 35, 300, 30)
o3 = Enemy("Orc Warrior B", 75, 35, 300, 30)
orcs = [o1, o2, o3]
orc_tribe = Enemy_Party("Orsinium Orc Tribe", orcs)

s1 = Enemy("Wood Elf General", 85, 40, 450, 80)
s2 = Enemy("Wood Elf Soldier A", 65, 30, 275, 60)
s3 = Enemy("Wood Elf Soldier B", 55, 30, 275, 60)
elves = [s1, s2, s3]
elf_militia = Enemy_Party("Holz Elf Militia", elves)

minotaur = Enemy("Minotaur", 150, 80, 1000, 70)
minotaur_party = Enemy_Party("The Minotaur", [minotaur])

necromancer = Enemy("Necromancer", 200, 40, 650, 25)
death_knight = Enemy("Death Knight", 75, 60, 800, 45)
necromancer_party = Enemy_Party("The Damned", [necromancer, death_knight])

elf_king = Enemy("Elf King", 125, 65, 750, 100)
erlkonig_party = Enemy_Party("Erlkonig", [elf_king])



ROUND_ONE_ENEMIES = [goblin_horde, wolf_pack]
ROUND_TWO_ENEMIES = [cultists, bandit_group]
ROUND_THREE_ENEMIES = [harpy_trio, cyclops_duo]
ROUND_FOUR_ENEMIES = [vampire_sect, draugr_berserkers]
ROUND_FIVE_ENEMIES = [elf_militia, orc_tribe]

LIST_OF_BOSSES = [minotaur_party, necromancer_party, erlkonig_party]
