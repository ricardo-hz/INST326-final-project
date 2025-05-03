from character import Character

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

s = Character("Char1", 250)
def party_info(party, id = -1):
    """Prints out info about everyone in a party.
    
    id (int, optional) : Opens a deeper menu with the list of ... for character
        corresponding to id
    """
    i = 0 # Index in party list that will be iterated over
    for character in party:
        print(f"{i}. {character.name} | {character.hp}HP | {character.role}")
        i += 1
    # Enter -1 to exit or a number for more info on that character
    menu_option = int(input(f"Enter a number to learn more about a character or"
                            f" -1 to exit."))
    while menu_option != -1:
        print(party[menu_option])