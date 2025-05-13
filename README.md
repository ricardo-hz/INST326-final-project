# INST326-final-project
Welcome to the Tournament of Water Bottle. Encounter monsters and progress your 
squadron as you engage in a deadly series of battles for humanity's soul.

This game was created by Nathan Castelo, Ricardo Hernandez, Aviva Solovey, and 
Phoenix Thompson as part of University of Maryland's INST326 Object Oriented
Programming with Python course. 

## How To Play:
    - Step 1: Choose your character!
        - You will be given a choice of 7 different characters with various abilities and stats 
            (the Protagonist is the one you should select b/c it makes the game quicker)
        - You choose the character based on their given number and put that into the console, 
            they will then be added to the party with a max of three characters in a party
    - Step 2: Enter Combat!
        - You will first be given a turn order on which characters or enemies will go first
        - If it's your character's turn you will have the option to choose an ability to attack an enemy, 
            the overall combat overview (status of all parties), 
            or your party overview (can see abilities/stats of each Character in your party)
        - Enemies will attack your Characters based on their given logic.
        - Turn order should repeat until either side dies, meaning that their whole party is completely wiped out

## How To Start the Game:
- Download latest version of Python 3 from [python.org](https://www.python.org/)
- Download latest release from directory on the side
- Unzip release into a folder of your choice.
- Copy path name of folder contents were unzipped into
    - Windows: 
        - Right click on file bar (next to search bar), click "Copy address as
             text"
    - Mac: 
        - Finder -> View -> Show Path Bar, right click on folder at bottom of 
            window then "Copy '<foldername>' as Pathname"
- Open up terminal/console/command prompt (on most OS with a search bar, this
     can be done by typing 'Terminal')
- Navigate to path name in terminal.
    - For most OS, type `cd ` then paste the path name saved, then hit enter.
- Run `main.py`
    - Windows: 
        - Type ```python main.py```, then hit enter.
    - Unix-Based OS (Including Mac): 
        - Type ```python3 experimental.py```, then hit enter.

For assignment due 2025-04-18:
    - All algorithms implemented for this assignment can be found in gameplay.py

## Annotated Bibliography:
- Markdown: Tables. Codecademy. (n.d.). 
    https://www.codecademy.com/resources/docs/markdown/tables 
        - Used to learn how to create a table in a markdown file.

## Attribution:
| Method/Function   | Primary Author | Techniques Demonstrated          |
| ---------------   | ---------------|-------------------------         |
|character_equipment| Aviva Solovey  | f-strings containing expressions |
|set_buff           | Aviva Solovey  | composition of two custom classes|
