import gameplay as g
import combat as cme
import character_class as ct
import all_enemies as en
import random as r
import all_characters as ac
import shop as s

OPPOSING_TEAMS = {
    1: en.ROUND_ONE_ENEMIES,
    2: en.ROUND_TWO_ENEMIES,
    3: en.ROUND_THREE_ENEMIES,
    4: en.ROUND_FOUR_ENEMIES,
    5: en.ROUND_FIVE_ENEMIES,
    6: en.LIST_OF_BOSSES
}
# contains potential enemy teams in reach round -- can absolutely be done in a\
# better way

def gameloop(rounds: int, team_size: int):
    round_counter: int = 1
    alive: bool = True
    player_team: ct.Player_Party = ct.Player_Party(g.assemble_team(
        ac.ALL_CHARACTERS))
    
    while ((round_counter >= 1) and (round_counter <= rounds) and
           (alive == True)):
        # start combat
        # there's going to be be a lot of logic here that would be called to
        # a combat function
        alive = cme.combat(player_team, OPPOSING_TEAMS[round_counter]
                         [r.randint(0, len(OPPOSING_TEAMS[round_counter]) - 1)])

        if alive == True:
            for p in player_team:
                p.progress_hp
                # shopping time!
                s.shop(p)
            #g.character_equipment()
            if round_counter == 2:
                for p in player_team:
                    p.character_abilities.addTo(ac.EXTRA_ABILITIES[p.name][0])
            if round_counter == 4:
                for p in player_team:
                    p.character_abilities.addTo(ac.EXTRA_ABILITIES[p.name][-1])
            round_counter += 1
            
    # party died lol
    if alive == False:
        print(f"You have failed. Humanity has fallen...")
    
    if round_counter > rounds:
        for c in player_team:
            print(f"{c.name}: {c.finale_message}")
            alive = c.combat(player_team, OPPOSING_TEAMS[round_counter]
                         [r.randint(0, len(OPPOSING_TEAMS[round_counter])-1)])
        if alive == True:
            print(f"Humanity is saved! Civilization can be rebuilt thanks "
                  f"to our three heroes. "
                  f"Lichtgott will continue to give their blessings...")
        else:
            print(f"Despite their journey, the three heroes have fallen. "
                  f"Lichtgott becomes forgotten as the forces of evil "
                  f"triumph...")
    # all the normal rounds of combat are over, it's time for the Finale!
    # i dunno. it'd be a custom variant of combat.py, i think
    
    input("Thanks for playing! Press any key to continue...")