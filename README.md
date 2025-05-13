# INST326-final-project
Welcome to the Tournament of Water Bottle. Encounter monsters and progress your 
squadron as you engage in a deadly series of battles for humanity's soul.

This game was created by Nathan Castelo, Ricardo Hernandez, Aviva Solovey, and 
Phoenix Thompson as part of University of Maryland's INST326 Object Oriented
Programming with Python course. 

## Purpose of Each File:
all_enemies.py

    - Creates all the needed enemies to battle in the game and organizes related 
        enemies into their own Enemy_Party.
    - Also creates all the abilities of the enemies in the game and organizes 
        each Enemy_Party into their separate round (this is what is being 
        imported into other files)
enemies.py

    - Contains the Enemy class and Enemy_Party classes’ implementation. The file 
        imports from character_class, random, ability_test, and equipment as 
        they are needed for the creation of an Enemy object.
    - Enemy class is denoted to be a subclass of the Character class in 
        character_class as it shares similar attributes except weapon.
    - enemy_logic is also implemented in this file as it decides how an Enemy 
        will target a corresponding Character during combat based on a few 
        criteria like the defense, attack, and hp of a Character.
all_characters.py

    - Creates all the needed Characters for the user to play in the game. It 
        also creates all the abilities that they have at the start of the game 
        and the abilities they will gain as the game goes on.
    - Imports all_equipment, ability_test, and character_class as they are 
        needed to implement all of these things to create a character.
character_class.py 

    - Implementation for the Character class is in here as well as Player_Party 
        which contains the Characters that the user decides to choose to fight 
        in the game.
all_equipment.py

    - Contains all the weapons and armor that each Character will obtain as the 
        game progresses. Imports from equipment.py to create Armor and Weapon 
        objects.
    - Weapons are categorized by their corresponding Character.
    - Armor is categorized by the type of armor, Characters will share armor, 
        i.e., knights and paladins have “Metal” type armor.
main.py

    - Where the program will essentially run via the console. 
    - Contains the gameloop function and title_screen function, they should run 
        endlessly
gameloop.py

    - The actual loop of the game. Will go through the rounds of each combat and 
        continuously check if the user’s party is still alive and will keep 
        going until the final round, which is separate. 
    - Gameloop ends with the final combat or a message that says you have failed 
        if you previously lost or you lose the final combat.
    - It will also have a final message if you win the game
equipment.py

    - Contains Weapon and Armor classes’ implementation.
combat.py

    - The main part of the game where enemies and characters will fight. The 
        user will be able to select an ability to use for each character to use 
        on an enemy or an ally depending on if it’s a damage/debuff or 
        buff/heal. It uses enemy_logic to figure out how the enemies will target 
        the allies. It also contains some other methods that help with combat, 
        like a combat overview to see turn order and a party overview to see how 
        much HP the party has.
damagecalc_abilbranch.py

    - Essentially handles damage calculations against targets and handles how 
        certain ability types work, i.e., buffs, debuffs, heals etc. 
ability_test.py

    - Implementation of Ability and AbilityList which are the abilities the 
        users and enemies will use to fight in combat. AbilityList also has some 
        other methods to handle things like cooldown and how a user can actually 
        select an ability from their given list.
lore.txt & how_to_play.txt

    - Information about the lore behind the game as well as the instructions on 
        how to play the game
gameplay.py

    - Contains various functions to be used in the game directly that really 
        don’t have a specific class attached to them, i.e., title_screen() which 
        shows the title screen of the game.
shop.py

    - Contains the shop function which allows users to upgrade the weapons/armor 
        of the characters in their party.


## How To Play:
    - Step 1: Choose your character!
        - You will be given a choice of 7 different characters with various 
            abilities and stats (the Protagonist is the one you should select 
            b/c it makes the game quicker)
        - You choose the character based on their given number and put that into
            the console, they will then be added to the party with a max of 
            three characters in a party
    - Step 2: Enter Combat!
        - You will first be given a turn order on which characters or enemies 
            will go first
        - If it's your character's turn you will have the option to choose an 
            ability to attack an enemy, the overall combat overview (status of 
            all parties), or your party overview (can see abilities/stats of 
            each Character in your party)
        - Enemies will attack your Characters based on their given logic.
        - Turn order should repeat until either side dies, meaning that their 
            whole party is completely wiped out

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
- Balatro. Directed by Localthunk, Playstack, 2024. Computer game.
    - Balatro is a roguelike game where players play an absurdly messed up 
        version of poker in order to progress through “antes”, with the scoring 
        requirements getting exponentially higher and higher.
    - Our game takes inspiration from the idea of exponential growth seen in 
        Balatro and games like it; there’s a sense of progression in a given 
        playthrough to being able to take on bigger and bigger threats, with the 
        player and enemy stats growing to match: the characters start at around 
        10-16 HP at the start, but then grow to well over 100 by the end.
- Final Fantasy. Directed by Hironobu Sakaguchi, Square, 1987. Nintendo 
    Entertainment System game.
    - There are a lot of games that preceded Final Fantasy in terms of the 
        turn-based genre, but a fair proportion of turn-based games have some 
        origin in Final Fantasy, a game where the player plays as four “Warriors 
        of Light” fighting against evil.
    - There’s a lot of smaller things our game takes from, but the main one is 
        the idea of choosing from a select few characters that each have their 
        own abilities that progress over time.
- Slay the Spire. Directed by Anthony Giovanetti and Casey Yano, Mega Crit, 
    2019. Computer game.
    - Slay the Spire is a roguelike game where players take one of four 
        characters through a run. Each character has an initial set of abilities 
        (indicated with cards) that they start with, and each character can 
        select an ability unique to them from a randomly assorted list of 
        abilities. Combined with random enemies and bosses, each run is unique 
        and the game is highly replayable (and hard!)
    - The abilities system is based off of Slay the Spire’s: at its peak, each 
        character in our game would have a unique set of abilities so that each 
        run was randomized. This didn’t end up being the case, but the 
        inspiration is there.
- “w3schools.com” w3schools Online Web Tutorials, Refnes Data, 
    www.w3schools.com/python/default.asp.
    - w3schools has some very useful tutorials for Python as well as general 
        refreshers on syntax that were extremely useful.


## Attribution:
| Method/Function     | Primary Author   | Techniques Demonstrated          |
| ---------------     | ---------------  |-------------------------         |
|character_equipment()| Aviva Solovey    | f-strings containing expressions |
|set_buff()           | Aviva Solovey    | composition of two custom classes|
|information()        | Nathan Castelo   | with strings                     |
|Enemy.enemy_logic()  | Nathan Castelo   | comprehensions/generator expr.   |
|Character.__init__() | Phoenix Thompson | use of a key function            |
|Character.__lt__()   | Phoenix Thompson | magic method other than __init__ |