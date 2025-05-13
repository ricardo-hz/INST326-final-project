import gameplay as g
import combat as cme
import character_class as ct
import all_enemies as en
import random as r
import all_characters as ac

ROUNDS_BEFORE_FINALE = 5
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
    # Extremely rough idea for how the gameplay will go and loop
    # we have some fancy info, some fancy text, then it's time to 
    # assemble the team.
    player_team: ct.Player_Party = ct.Player_Party(g.assemble_team(
        ac.ALL_CHARACTERS))
    
    # we've assembled the team, and it's time to begin the main game loop!
    # i dunno have many rounds, but in either case,
    while ((round_counter >= 1) and (round_counter <= rounds) and
           (alive == True)):
        # start combat
        # there's going to be be a lot of logic here that would be called to
        # a combat function
        alive = cme.combat(player_team, OPPOSING_TEAMS[round_counter]
                         [r.randint(0, len(OPPOSING_TEAMS[round_counter]) - 1)])

        # also before shop, maybe hints as to what the next enemy team is 
        # should be mentioned before players make decisions? i dunno 
        if alive == True:
            for p in player_team:
                p.progress_hp
            # shopping time!
            g.character_equipment()
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
    
    # all the normal rounds of combat are over, it's time for the Finale!
    # i dunno. it'd be a custom variant of combat.py, i think
    