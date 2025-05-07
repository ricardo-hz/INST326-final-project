from character import *
# Modules used from character:
# - print_characters()
# - CHARACTERS dictionary
from gameplay import *
# Modules used from gameplay:
# - assemble_team()
from combat import *
# please can we not import things like this it makes it really hard to track
# - ...using combat()

CHARACTER_DICT = {
    "Char1" : Character("Char1", 100, 30, WEAPONS["Weapon 1"], ARMOR["Armor 1"], AbilityList([ABILITIES["Strike"], ABILITIES["Mend Injury"]])),
    "Char2" : Character("Char2", 150, 20, WEAPONS["Weapon 2"], ARMOR["Armor 2"], AbilityList([ABILITIES["Strike"], ABILITIES["Water Bottle"]])),
    "Char3" : Character("Char3", 200, 2, WEAPONS["Weapon 3"], ARMOR["Armor 3"], AbilityList([ABILITIES["Strike"]])),
    "Char4" : Character("Char4", 250, 1, WEAPONS["Weapon 4"], ARMOR["Armor 4"], AbilityList([ABILITIES["Strike"]]))
}
# The above comments are there because import statements that require . are ugly
# May be removed later

if __name__ == "__main__":
      # Start off by printing menu
      print(f"This is an irrelevant piece of text meant to represent the starting"
            f" menu. It should be changed before demonstration.")
      print("Welcome!")

      # Print character options
      for c in CHARACTER_DICT:
            print(f"{CHARACTER_DICT[c].name} | {CHARACTER_DICT[c].current_hp} HP") 

      print()
      print(f"Enter the name of a character to add them to your team. "
            f"Obtain more information about a character by using the flag '--v'."
            f"\n\n Example: {CHARACTER_DICT["Char1"].name} --v")
      print()

      # Get team selection

      team = Player_Party(assemble_team(CHARACTER_DICT))
      print(team)

      opposition = Enemy_Party("Testing Squadron", [Enemy("Test Fighter I", 15, 20, 50, 15, "Normal Enemy"),
                                                Enemy("Test Fighter II", 20, 10, 50, 5, "Normal Enemy"),
                                                Enemy("Test Fighter III", 30, 10, 15, 1, "Normal Enemy"),
                                                Enemy("Test Fighter IV", 10, 17, 30, 8, "Normal Enemy")])
      # Generate an enemy team
      # Battle??? combat should be called here
      combat_result = combat(team, opposition)
      # Display shop if character won
      if combat_result:
            print("Congrats on winning! I don't know what else to say.")
      else:
            print("Congrats on not-winning! Uhm. Yeah.")