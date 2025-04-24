import warnings

CATEGORIES_OF_ABILITIES = {"damage", "heal", "debuff", "buff"}

class Ability:
    def __init__(self, name: str, potency: float, category: str, hits: int = 1, \
        roundLength: int = 0):
        # it's the name of the ability, self-explanatory
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
            
        # numeric value. always a either a multiplier or a percent
        
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
        
        # amount of times ability will "hit"
        self.hits: int = hits 
        
        # duration of ability, if there is an ability that lasts multiple rounds
        # it will last until start of next turn
        # 0 is instananeous abilities (i.e damage)
        if roundLength >= 0:
            self.roundLength = roundLength
        else:
            raise ValueError(f"Round length less than 0: {roundLength}")