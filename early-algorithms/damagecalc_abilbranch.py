from math import ceil
from random import uniform
from character_class import *
from ability_test import *

def damage_calculation(attacker, attack, defender, attackModifier = 1.4, defenseModifier = 1.2, \
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
    outgoingDamage = ceil(attacker.attack_stat * attack.potency * attackModifier)
    
    #not much to say, def is just the product of armor, represented by defs
    #and defmod for modifiers as well
    defenseAgainst = ceil(defender.defense_stat * defenseModifier)


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
    
def healing_calculation(healer, heal_ability, healing_target):
    return ceil(healer.attack_stat * heal_ability.potency)
    
def ability_handler(user: Character, ability_used: Ability, target: Character) -> int:
    #i need to return something or it gets all weird =/
    #i don't need to actually, it just helps for purposes
    funny_number = 0
    if ability_used.category == "damage":
        funny_number = damage_calculation(user, ability_used, target)
        target.current_hp -= funny_number
        print(f"{user.name} uses {ability_used.name} to deal {funny_number} damage to {target.name}!")
        # note: should make it so you can't target creatures with no hp.
        # atm it's a demo and will just do More Damage Lol
        if target.current_hp <= 0:
            target.conscious = False
            print(f"{target.name} is knocked unconscious!")
    elif ability_used.category == "heal":
        funny_number = healing_calculation(user, ability_used, target)
        target.current_hp += funny_number
        print(f"{user.name} uses {ability_used.name} to heal {target.name} {funny_number} hitpoints!")
        # make it so you prolly can't heal people with <= 0 hp? idk lol
    else:
        raise ValueError(f"not a valid category: {ability_used.category}")
    
    user.set_cooldown(ability_used)
    return 1

"""
if __name__ == "__main__":
    wepTest = Weapon("Sword", 5)
    armTest = Armor("Chainmail", 5)
    slash = Ability("Slash", "damage", 1)
    p1 = Character("Warrior", 40, 1, wepTest, armTest, character_abilities = AbilityList([slash]))
    p2 = Character("Warrior", 40, 1, wepTest, armTest, character_abilities = AbilityList([slash]))
    #print(f"{p1.name}'s {slash.name} does {dmgcalc(p1, slash, p2)} damage against \
    #{p2.name}!") # test print function. needs work objectively
    print(f"{p1.name} uses {slash.name} with {p1.weapon.name} to do\
    {damage_calculation(p1, p1.abilities.get("Slash"), p2)} damage to {p2.name}!")
"""