from equipment import *
import all_equipment as ae
import all_characters as ac


def get_next_weapon(character):
    """Gets the next available weapon for a character from the WEAPONS dict.
    
    Args:
        character (Character) : The character object to check the weapons of.
    """
    index = 0
    for v in ae.WEAPONS[character.name]:
        if character.weapon.name == v.name:
            # Checks that a user doesn't already have max weapon to avoid
                # index out of bounds
            return ae.WEAPONS[character.name][index + 1] if \
                index + 1 < len(ae.WEAPONS[character.name]) else \
                    ae.WEAPONS[character.name][index]
        index += 1
# Source: https://stackoverflow.com/questions/69642889/how-to-use-multiple-cases-in-match-switch-in-other-languages-cases-in-python-3
def get_next_armor(character):
    """Gets the next available armor for a character from the ARMOR dict.
    
    Args:
        character (Character) : The character object to check the armor of.
    """
    index = 0
        
    match(character.name):
        case("Pisces The Mage"):
            armor_designation = "Cloth"
        case("Aquarius the Priest" | "Sagitarrius the Archer" | 
                "Gemini the Thief"):
            armor_designation = "Leather"
        case("Leo the Knight" | "Libra the Paladin"):
            armor_designation = "Metal"
        case _:
            return NotImplementedError # TODO: Protagonist has no armor
        
    for v in ae.ARMOR[armor_designation]:
        if character.armor.name == v.name:
            # Checks that a user doesn't already have max armor to avoid
                # index out of bounds
            return ae.ARMOR[armor_designation][index + 1] if \
                index + 1 < len(ae.ARMOR[armor_designation]) else \
                    ae.WEAPONS[character.name][index]
        index += 1

def shop(character):
    """Gives a player the opportunity to upgrade weapons and armor.
    
    Args:
        Character (character) : The character which the shop is relevant for.
        
    Side effects:
        May update attributes of character.
    """
    # Introductory messages
    print(f"Welcome to the shop, {character.name}!")
    print(f"Current Weapon: {character.weapon} |"
            f"Next Weapon: {get_next_weapon(character)}")
    
    print(f"Current Armor: {character.armor} |"
            f"Next Armor {get_next_armor(character)}")
    
    # Get choice
    shop_choice = ""
    while shop_choice not in ["WEAPON", "ARMOR", "NONE"]:
        print(f"To upgrade to the next available weapon, type 'WEAPON' .")
        print(f"To upgrade to the next available piece of armor, "
                f"type 'ARMOR' .")
        print(f"Exit the shop by typing 'NONE' .")
        shop_choice = input().strip()
        if shop_choice not in ["WEAPON", "ARMOR", "NONE"]:
            print(f"{shop_choice} is not a valid entry.")
    
    # Upgrade equipment according to choice
    match(shop_choice):
        case("WEAPON"):
            character.swap_weapon(get_next_weapon(character))
        case("ARMOR"):
            character.swap_armor(get_next_armor(character))
        case("NONE"):
            pass
        
p = ac.knight
print(f"BEFORE: {p.weapon.name} | {p.armor.name}")
shop(p)
print(f"AFTER: {p.weapon.name} | {p.armor.name}")