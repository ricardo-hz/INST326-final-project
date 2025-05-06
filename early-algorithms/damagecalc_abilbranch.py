from math import ceil
from random import uniform
import weaponarmor_btest as et
import character as ct
import ability_test as at

def dmgcalc(attacker, attack, defender, attackModifier = 1, defenseModifier = 1, specialSauce = 1.5, \
    minimumDamage = 1, minVar = 0.95, maxVar = 1.05):
    # you want there to be some damage, so preferring attack over damage with 
    # a 'constant' modifier by default makes sense
    
    # attack potency is a multiplier, so potencies woudl be like x1.1 or x1 or
    # x0.9 and so on. this comes attached to the ability as one of it's attributes
    # attacker attack at the moment is based on weapon damage and weapon damage
    # only -- for simplification, it is labeled just as atk
    # atkmod included just for the sole purpose of variability. not sure what
    # kind of variability, but it's nice to have i think
    # of course, ceiling function because integers are cooler and look better
    outgoingDamage = ceil(specialSauce * attacker.attack_stat * attack.potency * attackModifier)
    
    #not much to say, def is just the product of armor, represented by defs
    #and defmod for modifiers as well
    defenseAgainst = ceil(defender.armor.defense * defenseModifier)


    # aaand here's the output damage, but we're not done yet!
    outputDamage = outgoingDamage - defenseAgainst
    
    # it would be neat to have a bit of slight randomness to damage dealt,
    # but i don't think it'd be appropriate to add it here. it's probably
    # nice to make thigns consistent
    var = uniform(minVar, maxVar)
    
    # finally, return either the actual damage calc or minimum damage, whichever
    # is higher
    return max(outputDamage, minimumDamage)

    # this has room for a lot of modifications and adjustments -- but it's a 
    # flexible dmgcalc function and it's more relevant in use than anything else
    
if __name__ == "__main__":
    wepTest = et.Weapon("Sword", 5)
    armTest = et.Armor("Chainmail", 5)
    slash = at.Ability("Slash", "damage", 1)
    p1 = ct.Character("Warrior", 1, 40, 1, wepTest, armTest, characterAbilities= {f"{slash.name}": slash})
    p2 = ct.Character("Warrior", 1, 40, 1, wepTest, armTest, characterAbilities= {f"{slash.name}": slash})
    #print(f"{p1.name}'s {slash.name} does {dmgcalc(p1, slash, p2)} damage against \
    #{p2.name}!") # test print function. needs work objectively
    print(f"{p1.name} uses {slash.name} with {p1.weapon.name} to do\
 {dmgcalc(p1, p1.abilities.get("Slash"), p2)} damage to {p2.name}!")