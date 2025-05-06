from random import randint
import character_btest

class Enemy:
    """Represents an enemy
    
    Attributes:
        name (str): name of enemy
        atk (int): enemy's base attack to be used for combat
        defs (int): enemy's base defense to be used for combat
        max_hp (int): enemy's total hp
        current_hp (int): enemy's current hp (subject to change during combat)
        agility (int): the agility of an enemy (what turn they take)
        e_type (str): the type of enemy they are
            -Boss
            -Strong Enemy
            -Normal Enemy
    """
    def __init__(self, name, atk, defs, hp, agility, e_type):
        self.name = name
        self.atk = atk
        self.defs = defs
        self.max_hp = hp
        self.current_hp = hp
        self.agility = agility
        self.e_type = e_type
    
    def __lt__(self, other) -> bool:
        return self.agility < other.agility
    
    def enemy_logic(self, character_party):
        """How an enemy will attack
        
        Args:
            character_party: the list of Character objects in a player's party
        Returns:
            A selected Character to attack
        """
        
        selected_target = None
        defs_list = []
        atk_list = []
        hp_list = []
        for char in character_party:
                defs_list.append(char.defense_base)
                atk_list.append(char.attack_base)
                hp_list.append(char.max_hp)
                
        strongest_defense = max(defs_list)
        weakest_defense = min(defs_list)
        strongest_attack = max(atk_list)
        
        for char in character_party:
            if char.hp <= char.max_hp * .10:
                selected_target = char
                return selected_target
            
        if self.e_type == "Normal Enemy":
            for char in character_party:
                if char.defense_base == strongest_defense:
                    chance = randint(0, 100)
                    if chance >= 75:
                        selected_target = char
                        return selected_target
                if char.attack_base == strongest_attack:
                    chance = randint(0, 100)
                    if chance >= 60:
                        selected_target = char
                        return selected_target
            
            if selected_target == None:
                selected_target = character_party[randint(0, len(character_party) - 1)]
                return selected_target
            
        if self.e_type == "Strong Enemy":
            for char in character_party:
                if char.defense_base == weakest_defense:
                    chance = randint(0, 100)
                    if chance >= 70:
                        selected_target = char
                        return selected_target
                
                if char.attack_base == strongest_attack:
                    chance = randint(0, 100)
                    if chance >= 60:
                        selected_target = char
                        return selected_target
            
            if selected_target == None:
                selected_target = character_party[randint(0, len(character_party) - 1)]
                return selected_target
        
class Enemy_Party:
    """Represents an enemy party to fight
    
    Attributes:
        name (str): the name of the party
        enemies (list of Enemy): the enemies to be in the party
        intro_message (str, default: None): What the enemies say upon starting
            battle
    """
    def __init__(self, name, enemies, intro_message = None):
        self.name = name
        self.enemies = enemies
        self.intro_message = intro_message

# need to play around with the enemy's stats
# also if time maybe create some abilities for the bosses/powerful normal enemies

g1 = Enemy("Goblin Leader", 15, 20, 250, 50, "Strong Enemy")
g2 = Enemy("Goblin Soldier A", 10, 15, 150, 30, "Normal Enemy")
g3 = Enemy("Goblin Soldier B", 10, 15, 150, 30, "Normal Enemy")
g4 = Enemy("Goblin Soldier C", 10, 15, 150, 30, "Normal Enemy")
g5 = Enemy("Goblin Soldier d", 10, 15, 150, 30, "Normal Enemy")
goblins = [g1, g2, g3, g4, g5]
goblin_horde = Enemy_Party("Goblin Horde", goblins)

w1 = Enemy("Alpha Wolf", 25, 15, 200, 50, "Strong Enemy")
w2 = Enemy("Wolf A", 10, 10, 150, 30, "Normal Enemy")
w3 = Enemy("Wolf B", 10, 10, 150, 30, "Normal Enemy")
w4 = Enemy("Wolf C", 10, 10, 150, 30, "Normal Enemy")
w5 = Enemy("Wolf D", 10, 10, 150, 30, "Normal Enemy")
wolves = [w1, w2, w3, w4, w5]
wolf_pack = Enemy_Party("Wolf Pack", wolves)

c1 = Enemy("Cultist Priest", 35, 25, 250, 50, "Strong Enemy")
c2 = Enemy("Cultist Follower A", 25, 20, 200, 30, "Normal Enemy")
c3 = Enemy("Cultist Follower B", 25, 20, 200, 30, "Normal Enemy")
c4 = Enemy("Cultist Follower C", 25, 20, 200, 30, "Normal Enemy")
cultists = [c1, c2, c3, c4]
cult = Enemy_Party("Cult of the Forgotten", cultists)

b1 = Enemy("Bandit Leader", 40,  30, 275, 60, "Strong Enemy")
b2 = Enemy("Bandit Lackey A", 30,  25, 250, 50, "Normal Enemy")
b3 = Enemy("Bandit Lackey B", 30,  25, 250, 50, "Normal Enemy")
b4 = Enemy("Bandit Lackey C", 30,  25, 250, 50, "Normal Enemy")
bandits = [b1, b2, b3, b4]
bandit_group = Enemy_Party("Sunset Mountain Bandits", bandits)

h1 = Enemy("Harpy Elder Sister", 50, 30, 275, 80, "Strong Enemy")
h2 = Enemy("Harpy Sister A", 45, 30, 265, 80, "Normal Enemy")
h3 = Enemy("Harpy Sister B", 45, 30, 265, 80, "Normal Enemy")
harpy_trio = Enemy_Party("Winds of Harpies", [h1,h2,h3])

e1 = Enemy("Red Cyclops", 40, 60, 300, 30, "Strong Enemy")
e2 = Enemy("Blue Cyclops", 60, 40, 250, 30, "Strong Enemy")
cyclops_duo = Enemy_Party("Pair of Cyclops", [e1,e2])

v1 = Enemy("Vampire Lord", 65, 40, 400, 50, "Strong Enemy")
v2 = Enemy("Vampire Thrall A", 55, 30, 300, 50, "Normal Enemy")
v3 = Enemy("Vampire Thrall B", 55, 30, 300, 50, "Normal Enemy")
v4 = Enemy("Vampire Thrall C", 55, 30, 300, 50, "Normal Enemy")
vampire_sect = Enemy_Party("Cult of the Bloody Moon", [v1,v2,v3,v4])

d1 = Enemy("Draugr Berserker", 75, 35, 450, 35, "Strong Enemy")
d2 = Enemy("Draugr Warrior A", 60, 35, 325, 30, "Normal Enemy")
d3 = Enemy("Draugr Warrior B", 60, 35, 325, 30, "Normal Enemy")
draugr_berserkers = Enemy_Party("Ancient Draugrs", [d1,d2,d3])

o1 = Enemy("Orc Chieftain", 100, 50, 500, 50, "Strong Enemy")
o2 = Enemy("Orc Warrior A", 75, 35, 300, 30, "Normal Enemy")
o3 = Enemy("Orc Warrior B", 75, 35, 300, 30, "Normal Enemy")
orcs = [o1, o2, o3]
orc_tribe = Enemy_Party("Orsinium Orc Tribe", orcs)

s1 = Enemy("Wood Elf General", 85, 40, 450, 80, "Strong Enemy")
s2 = Enemy("Wood Elf Soldier A", 65, 30, 275, 60, "Normal Enemy")
s3 = Enemy("Wood Elf Soldier B", 55, 30, 275, 60, "Normal Enemy")
elves = [s1, s2, s3]
elf_militia = Enemy_Party("Holz Elf Militia", elves)

minotaur = Enemy("Minotaur", 150, 80, 1000, 70, "Boss")
minotaur_party = Enemy_Party("The Minotaur", [minotaur])

necromancer = Enemy("Necromancer", 200, 40, 650, 25, "Boss")
death_knight = Enemy("Death Knight", 75, 60, 800, 45, "Boss")
necromancer_party = Enemy_Party("The Damned", [necromancer, death_knight])

elf_king = Enemy("Elf King", 125, 65, 750, 100, "Boss")
erlkonig_party = Enemy_Party("Erlkonig", [elf_king])



ROUND_ONE_ENEMIES = [goblin_horde, wolf_pack]
ROUND_TWO_ENEMIES = [cultists, bandit_group]
ROUND_THREE_ENEMIES = [harpy_trio, cyclops_duo]
ROUND_FOUR_ENEMIES = [vampire_sect, draugr_berserkers]
ROUND_FIVE_ENEMIES = [elf_militia, orc_tribe]

LIST_OF_BOSSES = [minotaur_party, necromancer_party, erlkonig_party]
