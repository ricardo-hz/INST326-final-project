from gameloop import *
from combat import *
from gameplay import *
from all_characters import *

if __name__ == "__main__":

    while True:
        # title screen loop here, that's probably it's own function
        # title screen /should/ have some fancy title in ascii or w/e
        # play, how-to, then quit
        assemble_team(ALL_CHARACTERS)
        # then, go to gameloop, who's contents are contained in gameloop.py
        
        # then once the entire game is finished, it'll take us back to the title
        # screen loop
        break