from sys import exit
from random import randint
from textwrap import dedent

squad = {
    "Sergent" : {
        "action points": 4
    },
    "Terminator1" : {
        "action points": 4
    },
    "Terminator2" : {
        "action points": 4
    },
    "Terminator3" : {
        "action points": 4
    },
    "Terminator4" : {
        "action points": 4
    }
}

command_points = 0

turn_count = 0

tiles = {
    "starting tiles": {
        "s1": {
            "connected to": {
                "s2": "north"
            }
        },
        "s2": {
            "connected to": {
                "s1": "south",
                "s3": "north"
            }
        },
        "s3": {
            "connected to": {
                "s2": "south",
                "s4": "north"
            }
        },
        "s4": {
            "connected to": {
                "s3": "south",
                "s5": "north"
            }
        },
        "s5": {
            "connected to": {
                "s4": "south",
                "c1": "north"
            }
        }
    },
    "genestealer tiles": {
        "g1": {
            "entrance": True,
            "connected to": {
                "g2": "north"
            }
        },
        "g2": {
            "connected to": {
                "g1": "south",
                "g3": "north"
            }
        },
        "g3": {
            "connected to": {
                "g2": "south",
                "g4": "east"
            }
        },
        "g4": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "g3": "west",
                "ll5": "east"
            }
        },
        "g5": {
            "entrance": True,
            "connected to": {
                "g6": "north"
            }
        },
        "g6": {
            "connected to": {
                "g5": "south",
                "g7": "north"
            }
        },
        "g7": {
            "connected to": {
                "g6": "south",
                "g8": "west"
            }
        },
        "g8": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "g7": "east",
                "lr5": "west"
            }
        },
        "g9": {
            "entrance": True,
            "connected to": {
                "g10": "east"
            }
        },
        "g10": {
            "connected to": {
                "g9": "west",
                "c2": "east"
            }
        },
        "g11": {
            "entrance": True,
            "connected to": {
                "g12": "west"
            }
        },
        "g12": {
            "connected to": {
                "g11": "east",
                "c2": "west"
            }
        },
        "g13": {
            "entrance": True,
            "connected to": {
                "g14": "east"
            }
        },
        "g14": {
            "connected to": {
                "g13": "west",
                "c6": "east"
            }
        },
        "g15": {
            "entrance": True,
            "connected to": {
                "g16": "west"
            }
        },
        "g16": {
            "connected to": {
                "g15": "east",
                "c6": "west"
            }
        },
        "g17": {
            "entrance": True,
            "connected to": {
                "g18": "west"
            }
        },
        "g18": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "g17": "east",
                "c7": "west"
            }
        },
        "g19": {
            "entrance": True,
            "connected to": {
                "g20": "east"
            }
        },
        "g20": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "g19": "west",
                "c7": "east"
            }
        },
        "g21": {
            "entrance": True,
            "connected to": {
                "g22": "west"
            }
        },
        "g22": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "g21": "east",
                "c12": "west"
            }
        },
        "g23": {
            "entrance": True,
            "connected to": {
                "g24": "east"
            }
        },
        "g24": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "g23": "west",
                "c12": "east"
            }
        }
    },
    "center tiles": {
        "c1": {
            "connected to": {
                "s5": "south",
                "lr1": "east",
                "ll1": "west"
            }
        },
        "c2": {
            "connected to": {
                "g10": "west",
                "g12": "east",
                "c3": "north"
            }
        },
        "c3": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "c2": "south",
                "c4": "norht"
            }
        },
        "c4": {
            "connected to": {
                "c3": "south",
                "cl4": "west",
                "c5": "north",
                "cr4": "east"
            }
        },
        "c5": {
            "door": {
                "sealed": False
            },
            "connected to": {
                "c4": "south",
                "c6": "north"
            }
        },
        "c6": {
            "connected to": {
                "c5": "south",
                "g14": "west",
                "g16": "east"
            }
        },
        "c7": {
            "connected to": {
                "g18": "east",
                "g20": "west"
            }
        },
        "c8": {
            "connected to": {
                "c7": "south",
                "c9": "north"
            }
        },
        "c9": {
            "connected to": {
                "c8": "south",
                "c10": "north"
            }
        },
        "c10": {
            "connected to": {
                "c9": "south",
                "ur4": "east",
                "ul4": "west",
                "c11": "north"
            }
        },
        "c11": {
            "connected to": {
                "c10": "south",
                "c12": "north"
            }
        },
        "c12": {
            "connected to": {
                "c11": "south",
                "g22": "east",
                "g24": "west"
            }
        }
    },
    "lower left tiles": {
        "ll1": {
            "connected to": {
                "c1": "east",
                "ll2": "west"
            }
        },
        "ll2": {
            "connected to": {
                "ll1": "east",
                "ll3": "west"
            }
        },
        "ll3": {
            "connected to": {
                "ll2": "east",
                "ll4": "west"
            }
        },
        "ll4": {
            "connected to": {
                "ll3": "east",
                "ll5": "west"
            }
        },
        "ll5": {
            "connected to": {
                "ll4": "east",
                "g4": "west",
                "l1": "north"
            }
        }
    },
    "lower right tiles": {
        "lr1": {
            "connected to": {
                "c1": "west",
                "lr1": "east"
            }
        },
        "lr2": {
            "connected to": {
                "lr1": "west",
                "lr3": "east"
            }
        },
        "lr3": {
            "connected to": {
                "lr2": "west",
                "lr4": "east" 
            }
        },
        "lr4": {
            "connected to": {
                "lr3": "west",
                "lr5": "east"
            }
        },
        "lr5": {
            "connected to": {
                "lr4": "west",
                "g8": "east",
                "r1": "north"
            }
        }
    },
    "left tiles": {
        "l1": {
            "connected to": {
                "ll5": "south",
                "l2": "north"
            }
        },
        "l2": {
            "connected to": {
                "l1": "south",
                "l3": "north"
            }
        },
        "l3": {
            "connected to": {
                "l2": "south",
                "l4": "north"
            }
        },
        "l4": {
            "connected to": {
                "l3": "south",
                "l5": "north"
            }
        },
        "l5": {
            "connected to": {
                "l4": "south",
                "l6": "north"
            }
        },
        "l6": {
            "connected to": {
                "l5": "south",
                "l7": "north",
                "cl1": "east"
            }
        },
        "l7": {
            "connected to": {
                "l6": "south",
                "l8": "north"
            }
        },
        "l8": {
            "connected to": {
                "l7": "south",
                "l9": "north"
            }
        },
        "l9": {
            "connected to": {
                "l8": "south",
                "l10": "north"
            }
        },
        "l10": {
            "connected to": {
                "l9": "south",
                "l11": "north"
            }
        },
        "l11": {
            "connected to": {
                "l10": "south",
                "l12": "north"
            }
        },
        "l12": {
            "connected to": {
                "l11": "south",
                "l13": "north"
            }
        },
        "l13": {
            "connected to": {
                "l12": "south",
                "ul1": "east"
            }
        }
    },
    "right tiles": {
        "r1": {},
        "r2": {},
        "r3": {},
        "r4": {},
        "r5": {},
        "r6": {},
        "r7": {},
        "r8": {},
        "r9": {},
        "r10": {},
        "r11": {},
        "r12": {},
        "r13": {}
    },
    "upper left tiles": {
        "ul1": {},
        "ul2": {},
        "ul3": {},
        "ul4": {}
    },
    "upper right tiles": {
        "ur1": {},
        "ur2": {},
        "ur3": {},
        "ur4": {}
    }
}

class Scene(object):

    def enter(self):
        print("This scene has not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):

    def __init__(self, turn):
        self.turn = turn

    def play(self, turn):
        current_turn = self.turn.opening_scene()
        last_turn = self.turn.next_turn('finished')

        while current_turn != last_turn:
            next_turn_name = current_turn.enter()
            current_turn = self.turn.next_turn(next_turn_name)

        current_turn.enter()

class Openingscene(Scene):

    def enter(self):
        print(dedent("""
                Welcome to Space Hulk Deathwatch, a console-based game that
                is based on the classic Games Workshop game, Space Hulk. This, 
                along with many other games that are created by Game Workshop,
                is based in the Warhammer 40,000 universe.
                """))

        print(dedent("""
                This game is set inside of a space hulk (hence the name), which
                is a floating mass of ships that have been fused together while
                being lost in the warp. Sometimes these space hulks will appear
                in realspace and, from time to time, the superhuman Adeptus 
                Astartes (space marines) will send a squad or two into these
                space hulks to cleanse them of alien life, find lost relics and
                technologies from the past, or any number of other reasons.
                """))

        print(dedent("""
                The Deathwatch are an elite chaper of the space marines that are
                made up from veteran marines from various chapers from all across
                the Imperium of Man. The Deathwatch acts as the chamber militant 
                (military branch) for the Ordo Xenos branch of the Inquisition (
                secret police that help keep the Imperium stable). Your goal is 
                to try and get your squad out of the space hulk before they are 
                overrun by genestealers (a form of Tyranid that are commonly found
                on board of space hulks).
                """))

        return 'squad_selection'

class SquadSelect(Scene):

    def enter(self):
        print(dedent("""
                Below is where you can select your squad of five marines from a 
                pre-selected list of chapters. The first marine you select will
                be the squad's sergent while the rest are standard marines. Choose
                wisely because some chapters will have advantages over others.
                """))

        chapters = [
            "Ultramarines", 
            "Space Wolves", 
            "White Scars",
            "Blood Angels",
            "Salamanders",
            "Dark Angels",
            "Imperial Fists",
            "Iron Hands",
            "Raven Guard",
            "Crimson Fists",
            "Blood Ravens",
            "Howling Griffons",
            "Black Templars",
            "Lementers",
            "Novamarines",
            "Carcarodons",
            "Brazen Claws",
            "Death Eagles",
            "Red Talons",
            "Angels of Vengence",
            "Angels of Absolution",
            "Flesh Tearers",
            "Storm Giants",
            "Storm Lords",
            "Storm Wardens",
            "Raptors",
            "Silver Skulls",
            "Iron Snakes",
            "Mantis Warriors"]

        weapon_loadout = [
            "Storm Bolter and Powerfist",
            "Power Sword and Storm Bolter",
            "Thunder Hammer and Storm Shield",
            "Lightning Claws",
            "Storm Bolter and Chainfist",
            "Storm Bolter and Power Axe",
            "Assault Cannon and Powerfist",
            "Heavy Flamer and Powerfist",
            "Cyclone Missile Launcher, Storm Bolter and Powerfist",
            "Storm Bolter and Power Maul"
        ]

        print(chapters)

        terminator_count = 1
        heavy_count = 0

        while len(squad) < 6:
            if len(squad) == 0:
                print("Choose your Sergent:")

                sgt = {}
                sgt_choice = input("> ")

                for i in chapters:
                    if sgt_choice == chapters[i]:
                        sgt["chapter"] = sgt_choice
                        break
                    elif sgt_choice != chapters[i] and i == len(chapters):
                        print("The chapter you entered is not valid, please try again.")
                        return 'squad_selection'

                print("Choose your weapon loadout:")
                print(weapon_loadout)

                weapon_choice = input("> ")

                for j in weapon_loadout:
                    if weapon_choice == weapon_loadout[j]:
                        sgt["weapon loadout"] = weapon_choice
                        if weapon_choice == weapon_loadout[6] or weapon_choice == weapon_loadout[7]:
                            if weapon_choice == weapon_loadout[6]:
                                sgt["overwatch"] = False
                            heavy_count += 1
                            sgt["clip_size"] = 10
                            sgt["clip_num"] = 2
                            break
                        elif weapon_choice == weapon_loadout[8]:
                            heavy_cout += 1
                            sgt["clip_size"] = 8
                            sgt["clip_num"] = 0
                            break
                        elif heavy_count == 3:
                            print("You have reached the maximum amount of heavy weapons for you squad, please try again.")
                            return 'squad_selection'
                        elif weapon_choice == weapon_loadout[0] or weapon_choice == weapon_loadout[1] or weapon_choice == weapon_loadout[4] or weapon_choice == weapon_loadout[5] or weapon_choice == weapon_loadout[8] or weapon_choice == weapon_loadout[9]:
                            sgt["overwatch"] = False
                            sgt["jammed"] = False
                            break
                        else:
                            break
                    elif weapon_choice != weapon_loadout[j] and j == len(weapon_loadout):
                        print("The weapon loadout you picked is not valid, please try again.")
                        return 'squad_selection'

                sgt["alive"] = True
                squad["Sergent"] = sgt

            else:
                print("Choose your terminator:")

                terminator = {}
                term_choice = input("> ")

                for i in chapters:
                    if term_choice == chapters[i]:
                        terminator["chapter"] = term_choice
                        break
                    elif term_choice != chapters[i] and i == len(chapters):
                        print("The chapter that you picked is not valid, please try again")
                        return 'squad_selection'

                print("Choose your weapon loadout:")
                print(weapon_loadout)

                weapon_choice = input("> ")

                for j in weapon_loadout:
                    if weapon_choice == weapon_loadout[j]:
                        terminator["weapon loadout"] = weapon_choice
                        if weapon_choice == weapon_loadout[6] or weapon_choice == weapon_loadout[7]:
                            if weapon_choice == weapon_loadout[6]:
                                terminator["overwatch"] = False
                            heavy_count += 1
                            terminator["clip_size"] = 10
                            terminator["clip_num"] = 2
                            break
                        elif weapon_choice == weapon_loadout[8]:
                            heavy_count +=1
                            terminator["clip_size"] = 8
                            terminator["clip_num"] = 0
                            break
                        elif heavy_count == 3:
                            print("You have reached the maximum amount of heavy weapons for you squad, please try again.")
                            return 'squad_selection'
                        elif weapon_choice == weapon_loadout[0] or weapon_choice == weapon_loadout[1] or weapon_choice == weapon_loadout[4] or weapon_choice == weapon_loadout[5] or weapon_choice == weapon_loadout[8] or weapon_choice == weapon_loadout[9]:
                            terminator["overwatch"] = False
                            terminator["jammed"] = False
                            break
                        else:
                            break
                    elif weapon_choice != weapon_loadout[j] and j == len(weapon_loadout):
                        print("The weapon loadout you picked is not valid, please try again.")
                        return 'squad_selection'
                
                terminator["alive"] = True
                squad[f"Terminator{terminator_count}"]

                terminator_count += 1

                if terminator_count == 4:
                    return 'squad_placement'

class Squadplacement(Scene):

    def enter(self):
        print("Select the order in which your squad is to be deployed:")

        squad_places = ["First", "Second", "Third", "Fourth", "Fifth"]

        for i in squad:
            print(f"Where do you want to place {squad[i]}?")
            print(squad_places)
            placement_selector = input("> ")
            term_place = {}

            if placement_selector:
                for j in squad_places:
                    if placement_selector == squad_places[j]:
                        term_place["starting_position"] = squad_places[j]
                        squad_places.pop(j)
                        squad[i]["starting_place"] = term_place
                        term_place.clear()
                        break
                    elif placement_selector != squad_places[j] and j == len(squad_places):
                        print("The placement that you selected is not valid, please try again")
                        return 'squad_placement'
                    elif len(squad_places) == 0:
                        return 'space_marine_turn'

class SpaceMarineTurn(Scene):

    def enter(self):
        turn_count += 1

        if turn_count == 1:
            for i in squad:
                if squad[i]["starting_place"] == "First":
                    tiles["starting tiles"]["s1"]["occupied"] = True
                elif squad[i]["starting_place"] == "Second":
                    tiles["starting tiles"]["s2"]["occupied"] = True
                elif squad[i]["starting_place"] == "Third":
                    tiles["starting tiles"]["s3"]["occupied"] = True
                elif squad[i]["starting_place"] == "Fourth":
                    tiles["starting tiles"]["s4"]["occupied"] = True
                elif squad[i]["starting_place"] == "Fifth":
                    tiles["starting tiles"]["s5"]["occupied"] = True

        for i in squad:
            if squad[i]["action points"] != 4:
                squad[i]["action points"] = 4

        command_points = 0
        command_points = randint(1, 6)

        if squad["Sergent"]["alive"] == True:
            print("Would you like to re-roll your command points, yes or no?")

            choice = input("> ")

            if choice == "yes":
                command_points = 0
                command_points = rantint(1, 6)
            elif choice == "no":
                print("Did not re-roll command points")
            else:
                print("Your answer is not valid, please try again")
                return 'space_marine_turn'

            turn_menu()
        
        def turn_menu():
            print("What would you like to do?")
            print(dedent("""
                    Move,
                    Attack,
                    Other Action,
                    End Turn
                    """))

            action_choice = input("> ")

            if action_choice == "Move":
                move()
                
                def move():
                    print("Which terminator would you like to move?")

                    for i in squad:
                        if squad[i]["action points"] > 0:
                            print(squad[i])

                    movement = input("> ")

                    for j in squad:
                        if movement == squad[j]:
                            print("How would you like to move?")

class GeneStealerTurn(Scene):

class GameControl(object):

    scenes = {
        'squad_selections': SquadSelect(),
        'opening_scene': Openingscene(),
        'squad_placement': Squadplacement(),
        'space_marine_turn': SpaceMarineTurn()
    }