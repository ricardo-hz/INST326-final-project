import warnings

CATEGORIES_OF_ABILITIES = {"damage", "heal", "debuff", "buff"}
# all lowercase, actually. please look forward to it.


class Ability:
    """Representation of an ability.
    
    Attributes:
        name (str): name of ability
        category (str): category of ability: either damage, heal, debuff, or buff
        potency (potency): potency of ability. multiplicative values 
        replacement (bool): whether or not ability replaces another. by default,
            is False
        cooldown (int): how many rounds an ability waits before used. by default,
            is 1 (so can be used every turn)
        ability_source (None/Weapon/Armor): source ability comes from. by default,
            is None (meaning it comes from Shop or is default)
        hits (int): amount of times ability will hit (or go off). by default, 1
        roundLength (int): how long ability will last, if it lasts for multiple
            rounds. by default, 0 (meaning an instantaneous hit)
        
    """
    def __init__(self, name: str, category: str, potency: float, cooldown: int = 1, \
            hits: int = 1, round_length: int = 0):
        # name of ability
        if isinstance(name, str):
            self.name: str = name 
        else:
            raise TypeError(f"Invalid type of object for name: {type(name)}")
            
        # the type of ability. this is mainly a documentation thing
        if category.lower() in CATEGORIES_OF_ABILITIES:
            self.category = category.lower()
        else:
            raise ValueError(f"Not a valid type of ability. Valid categories \
            are: {CATEGORIES_OF_ABILITIES}")
        
        #potency of ability, always as a float
        # for damage/heal it's multipliactive, for buff/debuff it's a percentage
        # (.33 for 33% and so on)
        if isinstance(potency, float) or isinstance(potency, int):
            self.potency: float = potency
            if self.potency < 0:
                warnings.warn(f"Potency on {self.name} with category \
                    {self.category} is less than 0: {self.potency}")
        else:
            raise TypeError(f"Invalid type of object for potency: \
                {type(potency)}")

        if isinstance(cooldown, int):
            if cooldown >= 1:
                self.cooldown = cooldown
            else:
                raise ValueError(f"Cooldown not greater than or equal to\
                    1: {cooldown}")
        else:
            raise TypeError(f"Invalid type of object for cooldown:\
                {type(cooldown)}")
        
        # amount of times ability will "hit"
        self.hits: int = hits 
        
        
        # duration of ability, if there is an ability that lasts multiple rounds
        # it will last until start of next turn
        # 0 is instananeous abilities (i.e damage)
        if round_length >= 0:
            self.roundLength = round_length
        else:
            raise ValueError(f"Round length less than 0: {round_length}")
        
    def __str__(self) -> str:
        """Returns detailed information on an ability

        Returns:
            str: Detailed information on an ability
        """
        return f"Ability Name: {self.name} | Category: {self.category} | Potency: {self.potency} | Cooldown: {self.cooldown} | Hits: {self.hits} | Round Length: {self.roundLength}"
        
        
class AbilityList():
    """Representation of the abilities a character has access to, including the
    order they were acquired in, the ability's name, and how long they're on 
    cooldown.
    
    Attributes:
        abilityList (dict of str: Ability): a dictionary of abilities, ability name -> ability.
        abilityOrder (dict of int: str):  a dictionary of order abilities are acquired (and
        listed thereafter). index of ability -> ability name. Index starts at 1.
        cooldowns (list of int): cooldown on abilities, linked up with ability order
        (index for this starts at 1 -- 0 index is a placeholder.)
        self.amountOfAbilities (int): the amount of abilities a character has.

    """
    def __init__(self, initial_abilities: list):
        """Initalizes an AbilityList for a character

        Args:
            initial_abilities (list of Abilities): list of abilities character
            has to start out with.

        Raises:
            TypeError: if initial_abilities isn't a list
            TypeError: if item in initial_abilities isn't actually a Ability, 
            returns typeerror
            
        Side effects:
            Initalizes abilityList, abilityOrder, cooldowns, and amountofAbilities
            attributes.
        """
        if isinstance(initial_abilities, list):
            self.abilityList = {}
            self.abilityOrder = {}
            self.cooldowns = ["This should not be accessed."]
            self.amountOfAbilities = len(initial_abilities)
            i = 1
            for a in initial_abilities:
                if isinstance(a, Ability):
                    #print(i)
                    self.abilityList[a.name] = a
                    self.abilityOrder[i] = a.name
                    self.cooldowns.append(a.cooldown)
                    i += 1
                    #print(self.abilityList)
                    #print(self.abilityOrder)
                else:
                    raise TypeError(f"Invalid type of object in initalization of\
                        AbilityList at {i}: {type(a)}")
        else:
            raise TypeError(f"Invalid type of object for initalization: {type(initial_abilities)}")
            
    def addTo(self, new_ability: Ability) -> None:
        """Adds ability to character's list of abilities they can use.

        Args:
            new_ability (Ability): Ability to be added.

        Raises:
            TypeError: If new ability isn't an ability.
        """
        if isinstance(new_ability, Ability):
            self.abilityList[new_ability.name] = new_ability
            self.amountOfAbilities += 1
            self.abilityOrder[self.amountOfAbilities] = new_ability.name
            self.cooldowns.append
        else:
            raise TypeError(f"Invalid type of object for AbilityList.addTo()\
            : {type(newAbility)}")
            
    def simplified_view(self) -> str:
        """Simplified view of ability list, containing just all abilities in a line.

        Returns:
            str: names of all abilities neatly
        """
        hhhh = str()
        for a in self.abilityList:
            hhhh = hhhh + f"{a} //"
        return hhhh
    
    def ability_to_index(self, ability_input: Ability) -> int:
        """Given an ability in abilityList, find it's place in self.orderList

        Args:
            ability_input (Ability): Ability to find index of.

        Raises:
            ValueError: If ability is not in orderList

        Returns:
            int: index of ability in orderList
        """
        for i in self.abilityOrder: 
            if self.abilityOrder[i] == ability_input.name:
                return i
        raise ValueError(f"Ability not found in abilityOrder: {ability_input}, {ability_input.name}")    
        
    def set_cooldown(self, ability_to_set: int | Ability) -> None:
        """Sets running cooldown of ability in self.cooldowns back to ability's
        cooldown (to be used when ability is used)

        Args:
            ability_to_set (int | Ability): ability to set cooldown of.
            can be integer (representing it's order in Orderlist), or the ability itself.
            
        Side effects:
            Changes representation of ability's cooldown in self.cooldown back to
            ability's cooldown.
        """
        if isinstance(ability_to_set, int):
            self.cooldowns[ability_to_set] = self.index_to_ability(ability_to_set).cooldown
        elif isinstance(ability_to_set, Ability):
            index = self.ability_to_index(ability_to_set)
            self.set_cooldown(index)
        
    def adjust_cooldowns(self, adjustment_amount = 1) -> None:
        """Moves cooldown of all abilities by adjustment_amount. By default,
        this is 1. Used at start of a character's turn.

        Args:
            adjustment_amount (int, optional): Amount to adjust cooldowns by. Defaults to 1.
            
        Side effects:
            adjusts each value in self.cooldowns by adjustment amount, min 0 
            (because it shouldn't be negative)
        """
        # anyone want music recommendations
        # check out the new sleep token album it's really good
        for c in self.cooldowns:
            c = max(c - adjustment_amount, 0)
    
    def index_to_ability(self, order_index) -> Ability | None:
        """Given an order of ability, turn out it's ability.

        Args:
            order_index (Ability): Ability to find index of.

        Returns:
            Ability | None: Ability, if it exists. Returns None otherwise
        """
        # immortalizing this genuinely awful piece of code here ebcause it's funny
        # chosen_ability = active_combatant.character_abilities.abilityList.get(active_combatant.character_abilities.abilityOrder.get(combat_action, None), None)
        return self.abilityList.get(self.abilityOrder.get(order_index, None), None)

        # abilityOrder index -> name, abilityList name -> ability
        # abilityList * abilityOrder index -> name -> ability 
        
    def ability_available(self, order_index: int) -> bool:
        """Returns if ability is available for an ability's index. True if
        it's represnetation in self.cooldowns is 0.

        Args:
            order_index (int): order/index of ability

        Returns:
            bool: whether or not ability is available (cooldown is 0)
        """
        if self.cooldowns[order_index] == 0:
            return True
        else:
            return False
        
    def __len__(self) -> int:
        """Returns many abilities are in ability list (or, how many abilities
        a character has)

        Returns:
            int: self.amountofAbilities
        """
        return self.amountOfAbilities
    
    def __str__(self) -> str:
        """Returns detailed printout of a character's abilities. 
        Calls Ability.__str__() for each ability.

        Returns:
            str: printout of a character's entire abilities, including details
        """
        listofabilityamongus = str() #why did i name it this
        i = 1
        #print(self.abilityOrder.get(i, None))
        while self.abilityOrder.get(i, None):
            listofabilityamongus = listofabilityamongus + f"#{i}: {self.abilityList.get(self.abilityOrder.get(i))}\n"
            i = i + 1
        return listofabilityamongus