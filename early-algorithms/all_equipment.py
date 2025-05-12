from equipment import Armor, Weapon

WEAPONS = {
        "Leo the Knight": [Weapon("basic sword", 10), 
                   Weapon("silver sword", 15),
                   Weapon("oathkeeper sword", 20),
                   Weapon("lionfans sword", 25),
                   Weapon("knight kins sword", 30)
                   ],
        "Warrior": [Weapon("steel sword", 15, hitMod = 0),
                    Weapon("iron axe", 25, hitMod = 0),
                    Weapon("warhammer", 30, hitMod = 1),
                    Weapon("heavy spear", 35, hitMod = 1),
                    Weapon("great axe", 40, hitMod = 1)
                    ],
        "Mage": [Weapon("magic staff", 10, None, 0),
                   Weapon("enchanted wand", 20, None, 0),
                   Weapon("spellbook", 32, None, 0),
                   Weapon("crystal orb", 45, None, 0),
                   Weapon("runed dagger", 55, None, 0)
                   ],
        "Priest": [Weapon("mace", 15),
                   Weapon("flail", 20),
                   Weapon("quarterstaff", 30),
                   Weapon("sacred tome", 35),
                   Weapon("lightbringer hammer")
                   ],
        "Magician": [Weapon("arcane staff", 15, None, 0),
                     Weapon("spell wand", 20, None, 1),
                     Weapon("grimoire", 30, None, 1),
                     Weapon("enchanted ring", 35, None, 2),
                     Weapon("crystal focus", 40, None, 2)
                     ], # we don't have a magician. leaving this here anyways
        "The Thief": [Weapon("ruined daggers", 8, hitMod = 1),
                  Weapon("bronze daggers", 12, hitMod = 2),
                  Weapon("steel daggers", 16, hitMod = 3),
                  Weapon("trustworthy daggers", 20, hitMod = 4),
                  Weapon("redemption daggers", 26, hitMod = 5)],
        "The Protagonist": [Weapon("Generic Weapon 6", 800),
                        Weapon("Generic Weapon 6", 800),
                        Weapon("Generic Weapon 6", 800),
                        Weapon("Generic Weapon 6", 800),
                        Weapon("Generic Weapon 6", 800),
                        Weapon("Generic Weapon 6", 800),
                        Weapon("Generic Weapon 6", 800),
                        Weapon("Generic Weapon 6", 800),
                        ]
}

ARMOR = {
        "Armor 1": Armor("Armor 1", 5),
        "Armor 2": Armor("Armor 2", 15),
        "Armor 3": Armor("Armor 3", 10),
        "Armor 4": Armor("Armor 4", 15)
}