class Enemy:
    """Represents an enemy
    
    Attributes:
        name (str): name of enemy
        atk (int): enemy's base attack to be used for combat
        defs (int): enemy's base defense to be used for combat
        max_hp (int): enemy's total hp
        current_hp (int): enemy's current hp (subject to change during combat)
    """
    def __init__(self, name, atk, defs, hp):
        self.name = name
        self.atk = atk
        self.defs = defs
        self.max_hp = hp
        self.current_hp = hp
        
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
# orcs are supposed to be strong so they shouldn't be in round 1
# to face our weak/base party before they get any stronger
# maybe create seperate lists of enemies for each round interval,
# i.e. goblins can appear rounds 1-2, orcs can appear 3-5, etc.

g1 = Enemy("Goblin Leader", 35, 20, 250)
g2 = Enemy("Goblin Soldier A", 15, 15, 150)
g3 = Enemy("Goblin Soldier B", 15, 15, 150)
g4 = Enemy("Goblin Soldier C", 15, 15, 150)
goblins = [g1, g2, g3, g4]
goblin_horde = Enemy_Party("Goblin Horde", goblins)

w1 = Enemy("Alpha Wolf", 25, 15, 200)
w2 = Enemy("Wolf A", 10, 10, 150)
w3 = Enemy("Wolf B", 10, 10, 150)
w4 = Enemy("Wolf C", 10, 10, 150)
w5 = Enemy("Wolf D", 10, 10, 150)
wolves = [w1, w2, w3, w4, w5]
wolf_pack = Enemy_Party("Wolf Pack", wolves)

o1 = Enemy("Orc Chieftain", 50, 30, 400)
o2 = Enemy("Orc Warrior A", 35, 25, 275)
o3 = Enemy("Orc Warrior B", 35, 25, 275)
orcs = [o1, o2, o3]
orc_tribe = Enemy_Party("Orc Tribe", orcs)

c1 = Enemy("Cultist Priest", 35, 25, 250)
c2 = Enemy("Cultist Follower A", 25, 20, 200)
c3 = Enemy("Cultist Follower B", 25, 20, 200)
c4 = Enemy("Cultist Follower C", 25, 20, 200)
cultists = [c1, c2, c3, c4]
cult = Enemy_Party("Cult of the Forgotten", cultists)

s1 = Enemy("Snow Elf General", 40, 30, 275)
s2 = Enemy("Snow Elf Soldier A", 35, 20, 250)
s3 = Enemy("Snow Elf Soldier B", 35, 20, 250)
elves = [s1, s2, s3]
elf_militia = Enemy_Party("Snow Elf Militia", elves)


LIST_OF_ENEMY_PARTIES = [goblin_horde, wolf_pack, orc_tribe, 
                         cult, elf_militia]

minotaur = Enemy("Minotaur", 100, 50, 750)
minotaur_party = Enemy_Party("The Minotaur", [minotaur])

LIST_OF_BOSSES = [minotaur_party]