from gameloop import gameloop
from gameplay import title_screen
from all_characters import RESET_CHARACTERS

if __name__ == "__main__":
    """Main function! Plays title screen, then gameloop, then resets characters
    after each run so stats don't get all weird
    
    """
    rounds = 5
    team_size = 3

    while True:
        # title screen loop here, that's probably it's own function
        # title screen /should/ have some fancy title in ascii or w/e
        # play, how-to, then quit
        title_screen()
        # then, go to gameloop, who's contents are contained in gameloop.py
        gameloop(rounds, team_size)
        # then once the entire game is finished, it'll take us back to the title
        # screen loop
        RESET_CHARACTERS()