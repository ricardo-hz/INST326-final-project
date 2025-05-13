from equipment import *
import random
from ability_test import *

class Character:
    """Representation of a character.
    
    Attributes:
        name (str): The character's name
        character_id (int): The numeric, unique id of the character
        current_hp (int): current health of character
        max_hp (int): maximum health of character
        weapon (Weapon): weapon character wields
        armor (Armor): armor character wields
        character_abilities (AbilityList): abilities character has access to
        
        attack_base (int): base attack stat character has. based off of weapon
        Should not be modified unless getting new weapon
        attack_stat (int): attack stat used in calculations, incl. modifications
        attack_mods (list of float): attack multipliers being applied to 
            character
        attack_mods_duration (list of int): how long attack multipliers are 
            being applied to character
        
        defense_base (int): base defense stat character has, based off of armor
        defense_stat (int): defense stat used in calculations, incl. 
            modifications
        
        agility_base (int): base agility stat character has
        agility_stat (int): agility stat used in party order
        
        player_character (bool): whether or not character is controlled by 
            player. false unless chosen in character select
        conscious (bool): whether or not character can act
        
        selection_message (str): message character says when selected
        finale_message (str): message character says before final boss
        
        progression (int): how far character's are along in terms of rounds
        health_progression (list of int): how much health each character should 
        get between rounds (incl 0.)
        
        armor_type (str): type of armor character uses (cloth, leather, metal)
        
    """
    
    def __init__(self, name: str, hp: int, agility: int, weapon: Weapon, 
            armor: Armor, character_abilities: AbilityList, selection_message: 
                str = None, finale_message: str = None,
            health_progression: list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            armor_type: str = ""):
        """Initializes a new character object.
        
        Args:
            name (str) : The character's name
            hp (int): The character's starting health points.
            agility (int): The character's agility
            weapon (Weapon) : The character's starting weapon.
            armor (Armor) : The character's starting armor.
            abilities (AbilityList) : The character's starting abilities.
                Empty list if ommitted. 
            health_progression (list of int): How much health character
            should get after a round. list of all 0s if ommitted
        
        Side effects:
            Initalizes character object, setting a whole bunch of attributes
            seen in above docstring
        """
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f"Not valid type for name: {type(name)}")
        
        if isinstance(hp, int):
            self.current_hp = hp
            self.max_hp = hp
        else:
            raise TypeError(f"Not valid type for hp: {type(hp)}")
        
        if isinstance(weapon, Weapon):
            self.weapon: Weapon = weapon
            self.attack_base: int = self.weapon.damage
            self.attack_stat: int = self.attack_base
            self.attack_mods: list = list()
            self.attack_mods_duration: list = list()
        else:
            raise TypeError(f"Not valid type for weapon: {type(weapon)}")
        
        if isinstance(armor, Armor):
            self.armor: Armor = armor
            self.defense_base: int = self.armor.defense
            self.defense_stat: int = self.defense_base
        else:
            raise TypeError(f"Not valid type for armor: {type(armor)}")
        
        if isinstance(character_abilities, AbilityList):
            self.character_abilities = character_abilities
        else:
            raise TypeError(f"Not valid type for character_abilities: \
            {type(character_abilities)}")
        
        self.agility_base: int = agility
        self.agility_stat: int = self.agility_base
        
        self.character_abilities: AbilityList = character_abilities
        self.player_character: bool = False
        self.conscious: bool = True
        self.selection_message: str = selection_message
        self.health_progression: list = health_progression
        self.progression: int = 1
        self.armor_type: str = armor_type
    
    def swap_weapon(self, new_weapon) -> None:
        """Swaps one weapon for a new one, modifying attack accordingly.

        Args:
            new_weapon (Weapon): New weapon to replace old weapon with.
            
        Side effects:
            updates self's weapon, attack_base, and attack_stat
        """
        self.weapon: Weapon = new_weapon
        self.attack_base: int = self.weapon.damage
        self.attack_stat: int = self.attack_base
    
    def swap_armor(self, new_armor) -> None:
        """Swaps one armor out for a new one, modifying defense accordingly

        Args:
            new_armor (Armor): New armor to replace old armor with.
            
        Side effects:
            updates self's armor, defense_base, and defense_stat
        """
        self.armor: Armor = new_armor
        self.defense_base: int = self.armor.defense
        self.defense_stat: int = self.defense_base
        
    def add_ability(self, ability: Ability) -> None:
        """Adds an ability object to a character's abilities list.
        
        Args:
            ability (Ability) : The ability to add.
            
        Side effects:
            adds new ability to character's ability list
        """
        self.character_abilities.addTo(Ability)
    
    def set_cooldown(self, ability: Ability) -> None:
        """Sets cooldown of an ability. Calls upon character's 
        character_abilities, which actually does the work in 
        AbilityList.set_cooldown()

        Args:
            ability (Ability): ability to adjust cooldown of
            
        Side effects:
            adjusts cooldown of ability to be at it's maximum
        """
        self.character_abilities.set_cooldown(ability)
        
    def set_buff(self, ability: Ability):
        """Sets buffs to affect attack_stat of character
        
        Args:
            ability (Ability): the ability that is increasing attack_stat
            
        Side effects:
            adds attack_stat modifications to character
        """
        self.attack_mods.append(ability.potency)
        self.attack_mods_duration.append(ability.roundLength)
        
    def set_debuff(self, ability: Ability):
        """Sets debuffs to affect attack_stat of character
        
        Args:
            ability (Ability): the ability that is decreasing attack_stat
            
        Side effects:
            adds attack_stat modifications to character
        """
        self.attack_mods.append(1 / ability.potency)
        self.attack_mods_duration.append(ability.roundLength)
        
    def set_attack_stat(self) -> None:
        """Sets attack_stat to be all modifiers applied to it
        
        Side effects:
            modifies attack_stat
        """
        i = 0
        self.attack_stat = self.attack_base
        # len self.attack_mods should equal self.attack_mods_duration. PELASEE
        while i < len(self.attack_mods):
            self.attack_stat *= self.attack_mods[i]
        
    def reduce_attack_mods(self) -> None:
        """Reduces attack mods' round duration, removing all who have expired
        durations
        
        Side effects:
            adjusts attack_mods_duration by 1, kicks out all that are at 0 
            (and have as such expired)
            
        """
        i = 0
        while i < len(self.attack_mods_duration):
            self.attack_mods_duration[i] -= 1
            if self.attack_mods_duration == 0:
                self.attack_mods_duration.pop(i)
                self.attack_mods.pop(i)
                i -= 1 
                
    def adjust_cooldowns(self, adjustment_amount = 1) -> None:
        """Calls the adjust_cooldown method of character_abilities
        
         Args:
            adjustment_amount (int, optional): Amount to adjust cooldowns by. 
                Defaults to 1.
                
        Side effects:
            Adjusts cooldowns, as character_abilities
        """
        self.character_abilities.adjust_cooldowns(adjustment_amount)
    
        
    def start_turn(self) -> None:
        """Does start of turn adjustments for character -- attack mods and 
        cooldowns
        
        Side effects:
            Calls character_abilities adjust_cooldowns() (modifies cooldowns),
            reduce_attack_mods (reduces attack mods duration, kicks out some),
            sets attack_stat based on mods
        """
        self.character_abilities.adjust_cooldowns(adjustment_amount = 1)
        self.reduce_attack_mods()
        self.set_attack_stat()
            
    def heal_full(self) -> None:
        """Heals character to full
        
        Side effects:
            Sets hp to full
        """
        self.current_hp = self.max_hp
        self.conscious = True
        
    def progress_hp(self) -> None:
        """Progresses character's health by set amount (starts at 1), then
        heals to full
        
        Side effects:
            modifies character's max_hp, health_progression, heals character to 
            full
        """
        self.max_hp += self.progress_hp[self.health_progression]
        self.health_progression += 1
        self.heal_full()
        
    def check_consciousness(self) -> bool:
        """Checks if character is conscious (has more than 0 hp), assigns
        self.conscious

        Returns:
            bool: conscious status of character
            
        Side effects:
            modifies self.conscious based on character consciousness state
        """
        if self.current_hp <= 0:
            self.conscious = False
            return False
        if self.current_hp > 0:
            self.conscious = True
            return True
        
        
    def __str__(self) -> str:
        """Prints detailed information about a character.
        """
        return f"Name: {self.name}\n" + \
        f"HP: {self.current_hp} (Base: {self.max_hp})\n" + \
        f"Weapon: {self.weapon.name} - {self.attack_stat} (Base: {self.attack_base}) ATK\n" + \
        f"Armor: {self.armor.name} - {self.defense_stat} (Base: {self.defense_base}) DEF\n" + \
        f"Abilities: {self.character_abilities}\n"
        
    def __lt__(self, other) -> bool:
        """Compares character to other based on agility

        Args:
            other (Character): character to be compared by

        Returns:
            bool: whatever character has more agility
        """
        return self.agility_stat < other.agility_stat
    
    def __rt__(self, other) -> bool:
        """Compares other character to self based on agility

        Args:
            other (Character): character to be compared by

        Returns:
            bool: whatever character has more agility
        """
        return self.agility_stat > other.agility_stat

# I know constants are traditionally placed at top, this
# line won't work due to Character not being defined if it's placed there

class Party():
    def __init__(self, party_list: list):
        self.party_list = party_list
        
    def __str__(self) -> str:
        listofcharacteramongus = str()
        for c in self.party_list:
            listofcharacteramongus = listofcharacteramongus + f"Name: {c.name}"
            f"| HP: {c.current_hp} ({c.max_hp})\n"
        return listofcharacteramongus
        
class Player_Party(Party):
    def __init__(self, party_list: list):
        for p in party_list:
            p.player_character = True
        self.party_list = party_list

    def __getitem__(self, index) -> Character:
        return self.party_list[index]
    
    def __len__(self) -> int:
        return len(self.party_list)