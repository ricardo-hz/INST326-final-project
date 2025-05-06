from character import *
# Modules used from character:
# - print_characters()
# - CHARACTERS dictionary
from gameplay import *
# Modules used from gameplay:
# - assemble_team()

# The above comments are there because import statements that require . are ugly
# May be removed later

# Start off by printing menu
print(f"This is an irrelevant piece of text meant to represent the starting"
      f" menu. It should be changed before demonstration.")
print("Welcome!")

# Print character options
print_characters(CHARACTER_LIST)

print()
print(f"Enter the name of a character to add them to your team. "
      f"Obtain more information about a character by using the flag '--v'."
      f"\n\n Example: {CHARACTER_LIST[0].name} --v")

# Get team selection
team = assemble_team(CHARACTER_LIST)
# Generate an enemy team
# Battle???
# Display shop if character won