from equipment import Armor, Weapon

WEAPONS = {
        "Libra the Paladin": [Weapon("Basic Sword", 5), 
                   Weapon("Silver Sword", 8),
                   Weapon("Oathkeeper Sword", 14),
                   Weapon("Lionfans Sword", 20),
                   Weapon("Knight Kin's Sword", 26),
                   Weapon("Honorbound", 30)
                   ],
        "Leo the Knight": [Weapon("Rusty Axe", 5),
                    Weapon("Iron Axe", 9,),
                    Weapon("Battleaxe", 18),
                    Weapon("Warrior's Axe", 22),
                    Weapon("Great Axe", 30),
                    Weapon("Nightmare", 38)
                    ], 
        "Pisces the Mage": [Weapon("Magic Staff", 8),
                   Weapon("Enchanted Wand", 16),
                   Weapon("Spellbook", 30),
                   Weapon("Crystal Orb", 45),
                   Weapon("Runed Staff", 60),
                   Weapon("Epitome", 80)
                   ],
        "Aquarius the Priest": [Weapon("Mace", 5),
                   Weapon("Flail", 8),
                   Weapon("Quarterstaff", 13),
                   Weapon("Sacred Tome", 18),
                   Weapon("Herald of Light", 24),
                   Weapon("Piety", 28)
                   ],
        "Magician": [Weapon("Arcane Staff", 8),
                     Weapon("Spell Wand", 16),
                     Weapon("Grimoire", 30),
                     Weapon("Enchanted Ring", 40),
                     Weapon("Crystal Focus", 50),
                     Weapon("Typecast", 60)
                     ], # we don't have a magician. leaving this here anyways
        "Gemini the Thief": [Weapon("Ruined Daggers", 3),
                  Weapon("Bronze Daggers", 7),
                  Weapon("Steel Daggers", 14),
                  Weapon("Trustworthy Daggers", 21),
                  Weapon("Daggers of Redemption", 30),
                  Weapon("Low Bar", 35)
                  ],
        "Sagitarrius the Archer": [Weapon("Wooden Bow", 5),
                   Weapon("Shortbow", 9),
                   Weapon("Mediumbow", 18),
                   Weapon("Longbow", 22),
                   Weapon("Farbow", 30),
                   Weapon("Swoop", 38)
                ],
        "The Protagonist": [Weapon("Generic Weapon 6", 800),
                        Weapon("Generic Weapon 6", 800),
                        Weapon("Generic Weapon 6", 800),
                        Weapon("Generic Weapon 6", 800),
                        Weapon("Generic Weapon 6", 800),
                        Weapon("Generic Weapon 6", 800),
                        Weapon("Generic Weapon 6", 800),
                        Weapon("Generic Weapon 6", 800)
                        ]
}

ARMOR = {
        # just mage
        "Cloth": [Armor("Formal Shirt and Pants", 1), 
                  Armor("Fair Suit", 4),
                  Armor("Quality Suit", 8),
                  Armor("Black Tie Suit", 15),
                  Armor("Eyeraising Suit", 20),
                  Armor("Lichtgott's Finest", 26)],
        
        # priest, archer, thief
        "Leather": [Armor("Leather Armor", 2),
                    Armor("Combat Leather", 5),
                    Armor("Polished Leather", 10),
                    Armor("Great Leather", 18),
                    Armor("Reinforced Leather", 24),
                    Armor("Unbreakable Leather", 32)],
        
        #knight, paladin
        "Metal": [Armor("Dented Armor", 3),
                  Armor("Repaired Armor", 6),
                  Armor("Study Armor", 13),
                  Armor("Half Plate", 20),
                  Armor("Full Plate", 28),
                  Armor("Indestructable Plate", 40)
                  ]
}