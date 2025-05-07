from gameloop import *
from combat import *
from argparse import ArgumentParser
import sys

def parse_args(args):
    parser = ArgumentParser()
    parser.add_argument("file", help="demo file")
    return parser.parse_args(args)

if __name__ == "__main__":
    arguments = parse_args(sys.argv[1:])
    while True:
        # title screen loop here, that's probably it's own function
        # title screen /should/ have some fancy title in ascii or w/e
        # play, how-to, then quit
        
        # then, go to gameloop, who's contents are contained in gameloop.py
        
        # then once the entire game is finished, it'll take us back to the title
        # screen loop
        break