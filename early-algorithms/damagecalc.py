from math import ceil

class Person():
    # this isn't official. i just felt like hacking this up
    def __init__(self, hp, atk, defs, name):
        self.max_hp = hp 
        self.current_hp = hp
        self.atk = atk
        self.defs = defs # can't use def because that is a keyword lmao
        self.name = name
        # hashtag owned

class Abil():
    def __init__(self, pot, name):
        self.name = name
        self.pot = pot
            
def dmgcalc(attacker, att, defender, atkmod = 1, defmod = 1, attLean = 1.5, \
    minDam = 1):
    # you want there to be some damage, so preferring attack over damage with 
    # a 'constant' modifier by default makes sense
    specialSauce = attLean
    
    # attack potency is a multiplier, so potencies woudl be like x1.1 or x1 or
    # x0.9 and so on. this comes attached to the ability as one of it's attributes
    # attacker attack at the moment is based on weapon damage and weapon damage
    # only -- for simplification, it is labeled just as atk
    # atkmod included just for the sole purpose of variability. not sure what
    # kind of variability, but it's nice to have i think
    # of course, ceiling function because integers are cooler and look better
    outgoingDamage = ceil(specialSauce * attacker.atk * att.pot * atkmod)
    
    #not much to say, def is just the product of armor, represented by defs
    #and defmod for modifiers as well
    defenseAgainst = ceil(defender.defs * defmod)

    # it would feel bad if you did 0 damage and even more nonsensical if you 
    # did negative damage (which would be a heal!!!) so at minimum, you should
    # do one damage
    minimumDamage = minDam
    
    # finally, return either the actual damage calc or minimum damage, whichever
    # is higher
    return max(outgoingDamage - defenseAgainst, minimumDamage)

    # this has room for a lot of modifications and adjustments -- but it's a 
    # flexible dmgcalc function and it's more relevant in use than anything else
    
p1 = Person(10, 2, 2, "Warrior")
p2 = Person(20, 1, 1, "Striking Dummy")
slash = Abil(1, "Slash")
print(f"{p1.name}'s {slash.name} does {dmgcalc(p1, slash, p2)} damage against \
{p2.name}!") # test print function. needs work objectively