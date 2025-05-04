import gameplay_functions as g
import combat as c # feel free to organize this better this is a mess
import character_btest as ct
import enemies as en
import random as r

ROUNDS_BEFORE_FINALE = 5
OPPOSING_TEAMS = {
    1: en.ROUND_ONE_ENEMIES,
    2: [None, None, None],
    3: [None, None, None],
    4: [None, None, None],
    5: [None, None, None],
    6: [None, None, None]
}
# contains potential enemy teams in reach round -- can absolutely be done in a\
# better way

def gameloop():
    round_counter: int = 1
    alive: bool = True
    # Extremely rough idea for how the gameplay will go and loop
    # we have some fancy info, some fancy text, then it's time to 
    # assemble the team.
    player_team: ct.Player_Party = g.assemble_team()
    
    # we've assembled the team, and it's time to begin the main game loop!
    # i dunno have many rounds, but in either case,
    while round_counter in range(1, ROUNDS_BEFORE_FINALE + 1) and alive == True:
        # start combat
        # there's going to be be a lot of logic here that would be called to
        # a combat function
        alive = c.combat(player_team, OPPOSING_TEAMS[round_counter]
                         [r.randint(0, len(OPPOSING_TEAMS[round_counter] - 1))])

        # also before shop, maybe hints as to what the next enemy team is 
        # should be mentioned before players make decisions? i dunno 
        if alive == True:
            # shopping time!
            g.character_equipment()
            # have to find a way to modify character items -- you can't do 
            # it between files, and it would be preferred to have functions 
            # split between files. could turn an array or Dict of stuff that
            # needs to be updated? i dunno lmao
            # am i allowed to swear in the comments
            # cause UGHH i don't think character_equipment can change 
            # the object's attributes if it's in another file, or i'm missing
            # something horribly. i'm not sure, like, if we initalize Team in
            # here and have character objects in another, surely we should be
            # able to like, i dunno, call methods to modify attributes like a 
            # list ??? i'm annoyed 
            
        else: # it's a boolean. what can it be besides True. None????
            # i dunno if losing an encounter should end the run entirely,
            # or just not give rewards for that round
            # should be discussed!
            # if it doesn't give rewards but allows for continuing, then remove
            # alive == True from the top. please
            pass
    
    # all the normal rounds of combat are over, it's time for the Finale!
    # i dunno. it'd be a custom variant of combat.py, i think
    