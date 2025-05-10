from equipment import *
from character_class import CHARACTER_LIST
from gameplay import assemble_team
def shop(team):
    print("Welcome to the shop!")
    print(f"The shop allows you to upgrade your team's existing armor/weapons "
          f"and purchase new abilities.")
    print(f"Note for each visit to the shop, you may only acquire one item "
            f"for each character.")
    for character in team:
        print(f"Current character: {character.name}")
        print("WEAPONS")
        print("ARMOR")
        print("ABILITIES")
        
        shop_choice = ''
        while shop_choice not in ["WEAPONS", "ARMOR", "ABILITIES", "NONE"]:
            shop_choice = input(f"Please select which shop you would like to view. "
                                f"Enter NONE to skip the shop for this character. ")
            match(shop_choice):
                case("WEAPONS"):
                    for weapon in WEAPONS:
                        print(weapon)
                    character.swap_weapon(Weapon(input().strip()))
                    
                case("ARMOR"):
                    break
                
                case("ABILITIES"):
                    print()
                    print("Choose from one of the following abilities:")
                    for ability in ABILITIES:
                        print(ability)
                    character.add_ability(Ability(input().strip()))
                case("NONE"):
                    break
                case(default):
                    print(f"{default} is not a valid entry.")

team = assemble_team(CHARACTER_LIST)
shop(team)