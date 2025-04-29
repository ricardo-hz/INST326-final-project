import warnings
import weaponarmor_btest as et

CATEGORIES_OF_ABILITIES = {"damage", "heal", "debuff", "buff"}

class Ability:
    """Representation of an ability.
    
    Attributes:
        name (str): name of ability
        category (str): category of ability: either damage, heal, debuff, or buff
        potency (potency): potency of ability. multiplicative values 
        replacement (bool): whether or not ability replaces another. by default,
        is False
        replaceAbilityName (str): name of ability that this ability is replacing.
        by default, is None
        replacedByAnother (bool): if ability is replaced by another. if True,
        should not show up in action menu and should not be able to be chosen
        but should be seen when viewing character info. by default, is False
        abilitySource (None/Weapon/Armor): source ability comes from. by default,
        is None (meaning it comes from Shop or is default)
        hits (int): amount of times ability will hit (or go off). by default, 1
        roundLength (int): how long ability will last, if it lasts for multiple
        rounds. by default, 0 (meaning an instantaneous hit)
        
    """
    def __init__(self, name: str, category: str, potency: float, replacement: bool = False, \
        replaceAbilityName: str = None, abilitySource: et.Weapon | et.Armor = None, \
            hits: int = 1, roundLength: int = 0):
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

        
        #some abilities replace others
        if isinstance(replacement, bool) and isinstance(replaceAbilityName, str):
            if replacement == True:
                self.replacement = replacement
                self.replaceAbilityName = replaceAbilityName
            elif replacement == False:
                raise ValueError(f"Replacement false yet include replaceAbil\
                    ityName: {replaceAbilityName}")
        else:
            raise TypeError(f"replacement or replaceAbility name may be invalid:\
                {type(replacement)}, {type(replaceAbilityName)}")
        
        #abilities that are replacedByAnother (by upgrades) should show up
        #when viewing player actions, but not when choosing abilities in-combat
        self.replacedByAnother = False
        
        #want to know where an ability comes from incase the source goes away
        #TODO need find a way to check this lmfao
        self.abilitySource = abilitySource
        
        # amount of times ability will "hit"
        self.hits: int = hits 
        
        
        # duration of ability, if there is an ability that lasts multiple rounds
        # it will last until start of next turn
        # 0 is instananeous abilities (i.e damage)
        if roundLength >= 0:
            self.roundLength = roundLength
        else:
            raise ValueError(f"Round length less than 0: {roundLength}")
        
class AbilityList():
    def __init__(self, initialAbilities: list):
        if isinstance(initialAbilities, list):
            self.abilityList = dict()
            self.abilityOrder = dict()
            self.amountOfAbilities = len(initialAbilities)
            self.disabledList = dict()
            for i, a in enumerate(initialAbilities):
                if isinstance(a, Ability):
                    self.abilityList[a.name] = a
                    self.abilityOrder[i+1] = [a.name]
                else:
                    raise TypeError(f"Invalid type of object in initalization of\
                        AbilityList at {i}: {type(a)}")
        else:
            raise TypeError(f"Invalid type of object for initalization: \
            {type(initialAbilities)}")
            
    def addTo(self, newAbility: Ability) -> None:
        if isinstance(newAbility, Ability):
            self.abilityList[newAbility.name] = newAbility
            self.amountOfAbilities += 1
            self.abilityOrder[self.amountOfAbilities] = newAbility.name
            if newAbility.replacement == True:
                for a in self.abilityList:
                    if self.abilityList[a].name == newAbility.replaceAbilityName:
                        self.abilityList[a].replacedByAnother = True
        else:
            raise TypeError(f"Invalid type of object for AbilityList.addTo()\
            : {type(newAbility)}")