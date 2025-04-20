import equipment
from character import *
from gameplay_functions import *

#################################
# The below code is for testing #
#################################

#t1 = Tank_1("Tank1", 500)
#t2 = Tank_2("Tank2", 550)
#d1 = Dmg_1("Damage1", 225)
#d2 = Dmg_2("Damage2", 275)
#s1 = Supp_1("Support1", 150)
#s2 = Supp_2("Support2", 200)

# This code shows how attacking works
#characters = [t1, t2, d1, d2, s1, s2]
#team = assemble_team(characters)
#print(team[1].hp)
#team[0].attack(team[1])
#print(team[1].hp)

c = Tank_1("Kal",250)
p = Dmg_2("Elvi",200)
e = Supp_1("Natt", 300)
s = Supp_2("Squishy", 150)

mon1 = Tank_1("Yllive", 200)
mon2 = Tank_2("Villye", 200)
mon3 = Supp_1("Evilly", 200)
c.add_ability(equipment.Ability("Super Smash"))
# Is there a better way to make it apparent that we're calling a specific 
# ability than abilities[index]?

# I think there might not be because of the menu based nature of the game when 
# it's complete
print(f"health: {p.hp}")
c.abilities[0].use(p)
print(f"health: {p.hp}")

human_party = [c, e, s]
monster_party = [mon1, mon2, mon3]

ComputerTurn(human_party, monster_party)