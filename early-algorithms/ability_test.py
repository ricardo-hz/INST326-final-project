TYPES_OF_ABILITIES = {"damage", "heal", "debuff"}

class Ability:
    def __init__(self, name: str, potency: float, type: str, hits: int = 1, \
        roundLength: int = 0):
        # it's the name of the ability, self-explanatory
        self.name: str = name 
        
        # numeric value. always a multiplier, something like x1.1, x1, x0.9, etc
        self.potency: float = potency 
        
        # the type of ability. this is mainly a documentation thing
        if type in TYPES_OF_ABILITIES:
            self.type = type
        else:
            raise ValueError(f"Not a valid type of ability. Valid types are:\
         {TYPES_OF_ABILITIES}")
            
        # amount of times ability will "hit"
        self.hits: int = hits 
        
        # duration of ability, if there is an ability that lasts multiple rounds
        # it will last until start of next turn
        # 0 is instananeous abilities (i.e damage)
        self.roundLength = roundLength