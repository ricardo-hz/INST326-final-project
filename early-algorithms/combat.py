from character_class import *
from enemies import *
from ability_test import *
from damagecalc_abilbranch import *

def combat(Player_Team, Enemy_Team) -> bool:
    combat_result = True
    if Enemy_Team.intro_message is not None:
        print(Enemy_Team.intro_message)
    # ultimately, we're going to return a boolean with like, did the player
    # make it out alive or not
    # b/c we're not really concerned with how the player ended up other than
    # "did they win" or "did they die lmao"
    combat_in_progress = True
    initative_tracker = Initative(Player_Team, Enemy_Team)
    initative_order = 0 #im seeing the appeal of arrays starting at 1 now tbh
    combat_action = 1
    active_turn = True
    chosen_ability: None | Ability = None
    chosen_target: None | Ability = None
    print("TURN ORDER:")
    for c in initative_tracker.combat_order:
        ch = initative_tracker.combat_order[c]
        print(f"{c}. {ch.name}{" (YOU)" if ch.player_character == True else ""}")
    while combat_in_progress:
        # phoenix make a setting to determine how to display party list whether it bye alpahbeticla or whatever
        # no i'm not doing that. i'm having fights with myself in the comments
        initative_order = initative_order % (initative_tracker.fight_size)
        active_combatant = initative_tracker.combat_order[initative_order + 1]
        # start of turn shenanigans
        
        initative_order += 1
        active_turn = True
        active_combatant.start_turn()
        
        
        #print(active_combatant.conscious)
        if active_combatant.conscious == True:
            if active_combatant.player_character == True:
                while active_turn == True:
                    # start of turn procedures
                    print(f"Your turn as {active_combatant.name}. "
                          f"Chose action:")
                    combat_action = input("1. Use Ability // 2. Combat "
                                          "Overview // 3. Party Overview // "
                                          "{Choice: ").strip()
                    if combat_action == "1":
                        print(f"{active_combatant.name}'s abilities:\n"
                            f"{active_combatant.character_abilities}")
                        while combat_action != -1:
                            combat_action = input("Choose ability. -1 to go "
                                                  "back. // {Choice: ").strip()
                            try:
                                combat_action = int(combat_action)
                            except:
                                pass
                            chosen_ability = (active_combatant
                                              .character_abilities
                                              .index_to_ability(combat_action))
                            
                            if chosen_ability is not None:
                                if (active_combatant.character_abilities
                                    .ability_available(combat_action)):   
                                    print(initative_tracker)
                                    while combat_action != -1:
                                        combat_action = (input("Choose target. "
                                                              "-1 to go back. "
                                                              "//{Choice: ")
                                                         .strip())
                                        try:
                                            combat_action = int(combat_action)
                                        except:
                                            pass
                                        chosen_target = (initative_tracker
                                                         .combat_order
                                                         .get(combat_action,
                                                              None))
                                        if chosen_target is not None:
                                            ability_handler(active_combatant, 
                                                            chosen_ability,
                                                            chosen_target)
                                            active_turn = False
                                            combat_action = -1
                                        elif ((chosen_target is None) and
                                              (combat_action == -1)):
                                            pass #combat action -1
                                        else:
                                            print("Invalid target.")
                                            combat_action = 0 # so it doesn't fall
                                            # through 
                                else:
                                    print(f"{chosen_ability.name} is on "
                                          f"cooldown!")
                                chosen_ability = None
                                
                            elif (chosen_ability is None and 
                                  combat_action == -1):
                                pass #combat action -1
                            else:
                                print("Invalid ability.")
                       
                    elif combat_action == "2":
                        print(initative_tracker)
                        # active_turn still true, send up to the top!
                    elif combat_action == "3":
                        party_info(Player_Team)
                        # active_turn still true im blue ba ba be ba bo
                    else:
                        print("Invalid action.")
                # end of turn checks for victory and such
            else:
                print(f"Opponent's turn as {active_combatant.name}")
                ability_handler(active_combatant, active_combatant.character_abilities.index_to_ability(1), \
                    active_combatant.enemy_logic(Player_Team))
                 # there's nothing about the enemy logic that returns an ability
                 # so i have no option here lmao 
        else:
            print(f"{active_combatant.name} is unable to act!")
        # end of turn checks very exciting
        initative_tracker.check_consciousness()
        #print(f"{initative_tracker.players_active}")
        #print(f"{initative_tracker.enemies_active}")
        #print(f"{combat_in_progress}")
        if initative_tracker.players_active == False:
            combat_result = False
            combat_in_progress = False
        elif initative_tracker.enemies_active == False:
            combat_result = True
            combat_in_progress = False
            
    # heal everyone to full
    initative_tracker.heal_all()
    return combat_result

def party_info(party, id = -1):
    """Prints out info about everyone in a party.
    
    id (int, optional) : Opens a deeper menu with the list of ... for character
        corresponding to id
    """
    i = 1 # Index in party list that will be iterated over
    for character in party:
        print(f"{i}. {character.name} | {character.current_hp} "
              f"({character.max_hp}) HP")
        i += 1

    browsing_info = True
    while browsing_info == True:
        menu_option = input(f"Enter a number to learn more about a "
                        f"character or -1 to exit. // {{Choice: ").strip()
        try:
            menu_option = int(menu_option)
        except:
            pass   
        if menu_option == -1:
            browsing_info = False
        else:
            if isinstance(menu_option, int):
                if menu_option > 0 and menu_option <= len(party):
                    print(party[menu_option - 1])
                else:
                    print("Invalid option.")
            else:
                print("Invalid option.")
        
        
class Initative(): 
    #aisudgasoikldjawlKdjsakjfhasklfj,shisk
    def __init__(self, party_player: Player_Party, \
        party_enemy: Enemy_Party):
        self.psuedo_order = list()
        for c in party_player:
            c.adjust_cooldowns(adjustment_amount= 99 )
            self.psuedo_order.append(c)
        for c in party_enemy:
            c.adjust_cooldowns(adjustment_amount= 99)
            self.psuedo_order.append(c)
        self.psuedo_order.sort(reverse = True)
        
        self.combat_order: dict = dict()
        starting_order = 1
        for c in self.psuedo_order:
            
            self.combat_order[starting_order] = c
            starting_order += 1
        self.fight_size = len(self.combat_order)
        self.players_active = True
        self.enemies_active = True
        
    def __str__(self) -> str:
        player_view = "YOUR SIDE:  // "
        enemy_view = "ENEMY SIDE: // "
        
        additive_string = str()
        for c in self.combat_order:
            additive_string = f"{c}. {self.combat_order[c].name} "
            f"{self.combat_order[c].current_hp} ({self.combat_order[c].max_hp})"
            f" HP // "
            # maybe hide it for enemies idk 
            if self.combat_order[c].player_character == True:
                player_view = player_view + additive_string
            else:
                enemy_view = enemy_view + additive_string
                
        return f"{player_view}\n{enemy_view}"
    
    def heal_all(self) -> None:
        for c in self.combat_order:
            self.combat_order[c].heal_full()
            
    def check_consciousness(self) -> None:
        p_act = False
        e_act = False
        for c in self.combat_order:
            c_a: Character = self.combat_order[c]
            if c_a.player_character == True:
                if c_a.check_consciousness():
                    p_act = True
            else:
                if c_a.check_consciousness() == True:
                    e_act = True
        self.players_active = p_act
        self.enemies_active = e_act