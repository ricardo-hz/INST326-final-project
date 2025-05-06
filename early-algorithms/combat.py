import character_btest as ct
import enemies as ees

def combat(Player_Team, Enemy_Team) -> bool:
    combat_is_live = True
    # ultimately, we're going to return a boolean with like, did the player
    # make it out alive or not
    # b/c we're not really concerned with how the player ended up other than
    # "did they win" or "did they die lmao"
    
    # i think the bit is that we should have preset enemy teams, choose from a
    # list of random encounters
    # this could be a class, Team class or something. then you can input those
    # in from the gameloop.py. i dunno.
    
    # anyways intro the enemy team and then uhh combat
    
    # i cba to write this it's 2:30am 
    
    return combat_is_live

def party_info(party, id = -1):
    """Prints out info about everyone in a party.
    
    id (int, optional) : Opens a deeper menu with the list of ... for character
        corresponding to id
    """
    i = 0 # Index in party list that will be iterated over
    for character in party:
        print(f"{i}. {character.name} | {character.hp}HP")
        i += 1

    while True:
        menu_option = int(input(f"Enter a number to learn more about a "
                        f" character or -1 to exit. ").strip())
        if menu_option == -1:
            break
        print(party[menu_option])
        
class Initative():
    #aisudgasoikldjawlKdjsakjfhasklfj,shisk
    def __init__(self, party_player: ct.Player_Party, \
        party_enemy: ees.Enemy_Party):
        self.combatOrder = list()
        for c in party_player:
            self.combatOrder.append(c)
        for c in party_enemy:
            self.combatOrder.append(c)
        self.combatOrder.sort(reverse = True)