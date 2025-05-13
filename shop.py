from equipment import *
import character_class as cc
import all_characters as ac
import all_equipment as ae
from gameplay import assemble_team
import copy

def get_next_weapon(character):
    index = 0
    for v in ae.WEAPONS[character.name]:
        if character.weapon.name == v.name:
            return(ae.WEAPONS[character.name][index + 1])
        index += 1
# Source: https://stackoverflow.com/questions/69642889/how-to-use-multiple-cases-in-match-switch-in-other-languages-cases-in-python-3
def get_next_armor(character):
    index = 0
    match(character.name):
        case("Pisces The Mage"):
            armor_designation = "Cloth"
        case("Aquarius the Priest" | "Sagitarrius the Archer" | "Gemini the Thief"):
            armor_designation = "Leather"
        case("Leo the Knight" | "Libra the Paladin"):
            armor_designation = "Metal"
        case _:
            raise NotImplementedError # TODO: Protagonist has no armor
        
    for v in ae.ARMOR[armor_designation]:
        if character.armor.name == v.name:
            return(ae.ARMOR[armor_designation][index + 1])
        index += 1

def shop(character):
    """Gives a player the opportunity to upgrade weapons and armor.
    """
    print(f"Welcome to the shop, {character.name}!")
    #print(f"The shop allows you to upgrade your team's existing armor and"
          #f" weapons.")
    #print(f"Note for each visit to the shop, you may only acquire one item "
            #f"for each character.")
    #for character in team:
    print(f"Current Weapon: {character.weapon} | Next Weapon: {get_next_weapon(character)}")
    print(f"Current Armor: {character.armor} | Next Armor {get_next_armor(character)}")
    
    shop_choice = ""
    while shop_choice not in ["WEAPONS", "ARMOR", "NONE"]:
        print(f"To upgrade to the next available weapon, type 'WEAPON' .")
        print(f"To upgrade to the next available piece of armor, type 'ARMOR' .")
        print(f"Exit the shop by typing 'NONE' .")
        shop_choice = input().strip()
        if shop_choice not in ["WEAPONS", "ARMOR", "NONE"]:
            print(f"{shop_choice} is not a valid entry.")
    
    match(shop_choice):
        case("WEAPON"):
            character.swap_weapon(get_next_weapon(character))
        case("ARMOR"):
            character.swap_armor(get_next_armor(character))
        case("NONE"):
            pass
        
        
        
        
        

"""
# This code gets the next available weapon for knight
k = copy.deepcopy(ac.knight)

print(f"New weapon: {k.weapon.name}")
print("-------")
print(get_next_weapon(k))
print("-------")
print()
print("-------")
print(get_next_armor(k))
print("-------")
"""
"""
m = copy.deepcopy(ac.mage)

i = 0
for v in ae.ARMOR["Cloth"]:
    if m.armor.name == v.name:
        print(m.armor.name)
        print(ae.ARMOR["Cloth"][i + 1].name)
    i += 1
# This code gets the next available armor for mage
        
        
team = assemble_team(ac.ALL_CHARACTERS)
shop(team)
"""