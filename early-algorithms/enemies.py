from random import randint
from character_class import Character
from ability_test import *
from equipment import *

# need these just as placeholders
ENEMY_ATTACK_ABILITY = Ability("EnemyAttack", "damage", 1)
ENEMY_WEAPON = Weapon("EnemyWeapon", 0)
ENEMY_ARMOR = Armor("EnemyArmor", 0)

class Enemy(Character): 
    """Represents an enemy to fight
    
    Attributes:
        name (str): name of enemy
        attack_stat (int): enemy's base attack to be used for combat
        defense_stat (int): enemy's base defense to be used for combat
        max_hp (int): enemy's total hp
        current_hp (int): enemy's current hp (subject to change during combat)
        agility (int): the agility of an enemy (what turn they take)
        e_type (str): the type of enemy they are
            -Boss
            -Strong Enemy
            -Normal Enemy
        player_character (bool): if enemy is a player character. 
            SHOULD ALWAYS BE FALSE
        conscious (bool): whether or not enemy can act
    """
    def __init__(self, name, atk, defs, hp, agility, e_type, 
                 character_abilities: AbilityList):
        """Initializes an Enemy object
        
        Args:
            name (str): name of an Enemy
            atk (int): the base attack stat of an enemy
            defs (int): the base defense stat of an enemy
            hp (int): the base health points of an enemy
            agility (int): the agility of an enemy, decides turn order
            e_type (str): the enemy type of an Enemy, deals with enemy_logic
            character_abilities (AbilityList): the Abilities an enemy could use 
        """
        super().__init__(name, hp, agility, ENEMY_WEAPON, ENEMY_ARMOR, 
                         character_abilities)
        self.attack_base: int = atk
        self.attack_stat: int = self.attack_base
        
        self.defense_base: int = defs
        self.defense_stat: int = self.defense_base
        
        self.e_type: str = e_type
    
    def __lt__(self, other) -> bool:
        return self.agility_stat < other.agility_stat
    
    def enemy_logic(self, character_party) -> Character:
        """How an enemy will attack. By Nathan Castelo
        
        Args:
            character_party: the list of Character objects in a player's party
        Returns:
            A selected Character to attack
        """
        
        selected_target = None
                
        strongest_defense = max([char.defense_stat for char in character_party])
        weakest_defense = min([char.defense_stat for char in character_party])
        strongest_attack = max([char.attack_stat for char in character_party])
        
        for char in character_party:
            if char.current_hp <= char.max_hp * .10:
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
                selected_target = character_party[randint(0, 
                                                          len(character_party) 
                                                          - 1)]
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
                selected_target = character_party[randint(0, 
                                                          len(character_party) 
                                                          - 1)]
                return selected_target
        
        if self.e_type == "Boss":
            if self.current_hp <= self.max_hp // 2:
                for char in character_party:
                    if char.defense_base == weakest_defense:
                        chance = randint(0, 100)
                        if chance >= 70:
                            selected_target = char
                            return selected_target
                    if char.defense_base == strongest_defense:
                        chance = randint(0, 100)
                        if chance >= 90:
                            selected_target = char
                            return selected_target
                
                if selected_target == None:
                    selected_target = character_party[randint(0, 
                                                              len
                                                              (character_party) 
                                                              - 1)]
                    return selected_target
            else:
                for char in character_party:
                    if char.defense_base == strongest_defense:
                        chance = randint(0, 100)
                        if chance >= 80:
                            selected_target = char
                            return selected_target
                    if char.attack_base == strongest_attack:
                        chance = randint(0, 100)
                        if chance >= 90:
                            selected_target = char
                            return selected_target
                if selected_target == None:
                    selected_target = character_party[randint(0, 
                                                              len
                                                              (character_party) 
                                                              - 1)]
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

    def __getitem__(self, index) -> Enemy:
        return self.enemies[index]

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
