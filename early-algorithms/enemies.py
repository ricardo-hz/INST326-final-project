from random import randint
from character import Character
from ability_test import *

ENEMY_ATTACK_ABILITY = Ability("Attack", "damage", 1) # this is bad but
# yknow

class Enemy(Character): # honestly this should totally just be a child class of character
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
    def __init__(self, name, atk, defs, hp, agility, e_type):
        super.__init__(name, hp, agility, weapon = None, armor = None, 
                       character_abilities = AbilityList())
        self.attack_stat = atk
        self.defense_stat = defs
        self.e_type = e_type
        self.player_character = False # this is critically important i swear
        self.conscious = True
    
    def __lt__(self, other) -> bool:
        return self.agility_stat < other.agility_stat
    
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
                defs_list.append(char.defense_stat)
                atk_list.append(char.attack_stat)
                hp_list.append(char.max_hp)
                
        strongest_defense = max(defs_list)
        weakest_defense = min(defs_list)
        strongest_attack = max(atk_list)
        
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
                    selected_target = character_party[randint(0, len(character_party) - 1)]
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

    def __getitem__(self, index):
        return self.enemies[index]
# need to play around with the enemy's stats
# also if time maybe create some abilities for the bosses/powerful normal enemies
