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
        chosen_ability = None
        
        strongest_defense = max([char.defense_stat for char in character_party])
        weakest_defense = min([char.defense_stat for char in character_party])
        strongest_attack = max([char.attack_stat for char in character_party])
        
        for char in character_party:
            # Should target a character if they are low hp
            if (char.current_hp <= char.max_hp * .10) and (char.current_hp > 0):
                selected_target = char
                for ability in range(self.character_abilities.amountOfAbilities):
                    if self.character_abilities.ability_available(ability) == True:
                        chosen_ability = self.character_abilities.index_to_ability(ability)
                return selected_target, chosen_ability
            
        if self.e_type == "Normal Enemy":
            for char in character_party:
                if char.defense_base == strongest_defense:
                    chance = randint(0, 100)
                    if chance >= 75:
                        selected_target = char
                        return selected_target, self.character_abilities.index_to_ability(1)
                if char.attack_base == strongest_attack:
                    chance = randint(0, 100)
                    if chance >= 60:
                        selected_target = char
                        return selected_target, self.character_abilities.index_to_ability(1)
            
            if selected_target == None:
                selected_target = character_party[randint(0, 
                                                          len(character_party) 
                                                          - 1)]
                return selected_target, self.character_abilities.index_to_ability(1)
            
        if self.e_type == "Strong Enemy":
            for char in character_party:
                if char.defense_base == weakest_defense:
                    chance = randint(0, 100)
                    if chance >= 70:
                        selected_target = char
                        for ability in range(self.character_abilities.amountOfAbilities):
                            if self.character_abilities.ability_available(ability) == True:
                                chosen_ability = self.character_abilities.index_to_ability(ability)
                        if chosen_ability == None:
                            chosen_ability = self.character_abilities.index_to_ability(3)
                        return selected_target, chosen_ability
                
                if char.attack_base == strongest_attack:
                    chance = randint(0, 100)
                    if chance >= 60:
                        selected_target = char
                        for ability in range(self.character_abilities.amountOfAbilities):
                            if self.character_abilities.ability_available(ability) == True:
                                chosen_ability = self.character_abilities.index_to_ability(ability)
                        if chosen_ability == None:
                            chosen_ability = self.character_abilities.index_to_ability(3)
                        return selected_target, chosen_ability
            
            if selected_target == None:
                selected_target = character_party[randint(0, 
                                                          len(character_party) 
                                                          - 1)]
                for ability in range(self.character_abilities.amountOfAbilities):
                    if self.character_abilities.ability_available(ability) == True:
                        chosen_ability = self.character_abilities.index_to_ability(ability)
                if chosen_ability == None:
                            chosen_ability = self.character_abilities.index_to_ability(3)
                return selected_target, chosen_ability
        
        if self.e_type == "Boss":
            if self.current_hp <= self.max_hp // 2:
                for char in character_party:
                    if char.defense_base == weakest_defense:
                        chance = randint(0, 100)
                        if chance >= 70:
                            selected_target = char
                            for ability in range(self.character_abilities.amountOfAbilities):
                                if self.character_abilities.ability_available(ability) == True:
                                    chosen_ability = self.character_abilities.index_to_ability(ability)
                            return selected_target, chosen_ability
                    if char.defense_base == strongest_defense:
                        chance = randint(0, 100)
                        if chance >= 90:
                            selected_target = char
                            for ability in range(self.character_abilities.amountOfAbilities):
                                if self.character_abilities.ability_available(ability) == True:
                                    chosen_ability = self.character_abilities.index_to_ability(ability)
                            if chosen_ability == None:
                                chosen_ability = self.character_abilities.index_to_ability(4)
                            return selected_target, chosen_ability
                
                if selected_target == None:
                    selected_target = character_party[randint(0, 
                                                              len
                                                              (character_party) 
                                                              - 1)]
                    for ability in range(self.character_abilities.amountOfAbilities):
                        if self.character_abilities.ability_available(ability) == True:
                            chosen_ability = self.character_abilities.index_to_ability(ability)
                        if chosen_ability == None:
                            chosen_ability = self.character_abilities.index_to_ability(4)
                    return selected_target, chosen_ability
            else:
                for char in character_party:
                    if char.defense_base == strongest_defense:
                        chance = randint(0, 100)
                        if chance >= 80:
                            selected_target = char
                            for ability in range(self.character_abilities.amountOfAbilities):
                                if self.character_abilities.ability_available(ability) == True:
                                    chosen_ability = self.character_abilities.index_to_ability(ability)
                            if chosen_ability == None:
                                chosen_ability = self.character_abilities.index_to_ability(4)
                            return selected_target, chosen_ability
                    if char.attack_base == strongest_attack:
                        chance = randint(0, 100)
                        if chance >= 90:
                            selected_target = char
                            for ability in range(self.character_abilities.amountOfAbilities):
                                if self.character_abilities.ability_available(ability) == True:
                                    chosen_ability = self.character_abilities.index_to_ability(ability)
                            if chosen_ability == None:
                                chosen_ability = self.character_abilities.index_to_ability(4)
                            return selected_target, chosen_ability
                if selected_target == None:
                    selected_target = character_party[randint(0, 
                                                              len
                                                              (character_party) 
                                                              - 1)]
                    for ability in range(self.character_abilities.amountOfAbilities):
                        if self.character_abilities.ability_available(ability) == True:
                            chosen_ability = self.character_abilities.index_to_ability(ability)
                    if chosen_ability == None:
                        chosen_ability = self.character_abilities.index_to_ability(4)
                    return selected_target, chosen_ability
                            

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
