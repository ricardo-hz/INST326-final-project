from character import *
# Modules used from character:
# - print_characters()
# - CHARACTERS dictionary
from gameplay import *
# Modules used from gameplay:
# - assemble_team()
from enemies import *
from combat import *

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
      f"\n\n Example: {CHARACTER_LIST[0].name} --v ")
print()

# Get team selection

team = assemble_team(CHARACTER_LIST)
print_characters(team)

# Generate an enemy team
g1 = Enemy("Goblin Leader", 15, 20, 250, 50, "Strong Enemy")
g2 = Enemy("Goblin Soldier A", 10, 15, 150, 30, "Normal Enemy")
g3 = Enemy("Goblin Soldier B", 10, 15, 150, 30, "Normal Enemy")
g4 = Enemy("Goblin Soldier C", 10, 15, 150, 30, "Normal Enemy")
g5 = Enemy("Goblin Soldier d", 10, 15, 150, 30, "Normal Enemy")
goblins = [g1, g2, g3, g4, g5]
goblin_horde = Enemy_Party("Goblin Horde", goblins, "GIMME YOUR BELONGINGS!!!")
# Battle??? combat should be called here
combat(team, goblin_horde)
# Display shop if character won