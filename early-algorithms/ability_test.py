import warnings
import weaponarmor_btest as et

CATEGORIES_OF_ABILITIES = {"Damage", "Heal", "Debuff", "Buff"}

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
    def __init__(self, name: str, category: str, potency: float, cooldown: int = 1, ability_source: et.Weapon | et.Armor = None, \
            hits: int = 1, round_length: int = 0):
        # name of ability
        if isinstance(name, str):
            self.name: str = name 
        else:
            raise TypeError(f"Invalid type of object for name: {type(name)}")
            
        # the type of ability. this is mainly a documentation thing
        if category in CATEGORIES_OF_ABILITIES:
            self.category = category
        else:
            raise ValueError(f"Not a valid type of ability. Valid categories \
            are: {CATEGORIES_OF_ABILITIES}")
        
        #potency of ability, always as a float
        # for damage/heal it's multipliactive, for buff/debuff it's a percentage
        # (.33 for 33% and so on)
        if isinstance(potency, float) or isinstance(potency, int):
            self.potency: float = potency
            if self.category == "debuff":
                self.potency: float = 1 - self.potency
            elif self.category == "buff":
                self.potency: float = 1 + self.potency
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
        
        
        #want to know where an ability comes from incase the source goes away
        #TODO need find a way to check this lmfao
        self.abilitySource = ability_source
        
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
        return f"Ability Name: {self.name} | Category: {self.category} | Potency: {self.potency} | Cooldown: {self.cooldown} | Hits: {self.hits} | Round Length: {self.roundLength}"
        
        
class AbilityList():
    def __init__(self, initial_abilities: list):
        if isinstance(initial_abilities, list):
            self.abilityList = dict()
            self.abilityOrder = dict()
            self.amountOfAbilities = len(initial_abilities)
            for i, a in enumerate(initial_abilities):
                if isinstance(a, Ability):
                    self.abilityList[a.name] = a
                    self.abilityOrder[i+1] = [a.name]
                else:
                    raise TypeError(f"Invalid type of object in initalization of\
                        AbilityList at {i}: {type(a)}")
        else:
            raise TypeError(f"Invalid type of object for initalization: \
            {type(initialAbilities)}")
            
    def addTo(self, new_ability: Ability) -> None:
        if isinstance(new_ability, Ability):
            self.abilityList[new_ability.name] = new_ability
            self.amountOfAbilities += 1
            self.abilityOrder[self.amountOfAbilities] = new_ability.name
        else:
            raise TypeError(f"Invalid type of object for AbilityList.addTo()\
            : {type(newAbility)}")
            
    def __str__(self) -> str:
        listofabilityamongus = str()
        for a in self.abilityOrder:
            listofabilityamongus = listofabilityamongus + f"#{a}: {self.abilityList(self.abilityOrder(a))}"