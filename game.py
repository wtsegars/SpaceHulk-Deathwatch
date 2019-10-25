from sys import exit
from random import randint
from textwrap import dedent

squad = {
    "Sergent" : {},
    "Terminator1" : {},
    "Terminator2" : {},
    "Terminator3" : {},
    "Terminator4" : {}
}

turn_count = 0

tiles = {
    "starting tiles": {
        "s1": {},
        "s2": {},
        "s3": {},
        "s4": {},
        "s5": {}
    },
    "genestealer tiles": {
        "g1": {
            "entrance": True
        },
        "g2": {},
        "g3": {},
        "g4": {
            "door": {
                "sealed": False
            }
        },
        "g5": {
            "entrance": True
        },
        "g6": {},
        "g7": {},
        "g8": {
            "door": {
                "sealed": False
            }
        },
        "g9": {
            "entrance": True
        },
        "g10": {},
        "g11": {
            "entrance": True
        },
        "g12": {},
        "g13": {
            "entrance": True
        },
        "g14": {},
        "g15": {
            "entrance": True
        },
        "g16": {},
        "g17": {
            "entrance": True
        },
        "g18": {
            "door": {
                "sealed": False
            }
        },
        "g19": {
            "entrance": True
        },
        "g20": {
            "door": {
                "sealed": False
            }
        },
        "g21": {
            "entrance": True
        },
        "g22": {
            "door": {
                "sealed": False
            }
        },
        "g23": {
            "entrance": True
        },
        "g24": {
            "door": {
                "sealed": False
            }
        }
    },
    "center tiles": {
        "c1": {},
        "c2": {},
        "c3": {
            "door": {
                "sealed": False
            }
        },
        "c4": {},
        "c5": {
            "door": {
                "sealed": False
            }
        },
        "c6": {},
        "c7": {},
        "c8": {},
        "c9": {},
        "c10": {},
        "c11": {},
        "c12": {}
    },
    "lower left tiles": {
        "ll1": {},
        "ll2": {},
        "ll3": {},
        "ll4": {},
        "ll5": {}
    },
    "lower right tiles": {
        "lr1": {},
        "lr2": {},
        "lr3": {},
        "lr4": {},
        "lr5": {}
    },
    "left tiles": {
        "l1": {},
        "l2": {},
        "l3": {},
        "l4": {},
        "l5": {},
        "l6": {},
        "l7": {},
        "l8": {},
        "l9": {},
        "l10": {},
        "l11": {},
        "l12": {},
        "l13": {}
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
                        if weapon_choice == weapon_loadout[5] or weapon_choice == weapon_loadout[6]:
                            heavy_count += 1
                            sgt["clip_size"] = 10
                            sgt["clip_num"] = 2
                            break
                        elif weapon_choice == weapon_loadout[7]:
                            heavy_cout += 1
                            sgt["clip_size"] = 8
                            sgt["clip_num"] = 0
                            break
                        elif heavy_count == 3:
                            print("You have reached the maximum amount of heavy weapons for you squad, please try again.")
                            return 'squad_selection'
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
                        if weapon_choice == weapon_loadout[5] or weapon_choice == weapon_loadout[6]:
                            heavy_count += 1
                            terminator["clip_size"] = 10
                            terminator["clip_num"] = 2
                            break
                        elif weapon_choice == weapon_loadout[7]:
                            heavy_count +=1
                            terminator["clip_size"] = 8
                            terminator["clip_num"] = 0
                            break
                        elif heavy_count == 3:
                            print("You have reached the maximum amount of heavy weapons for you squad, please try again.")
                            return 'squad_selection'
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
                        break
                    elif placement_selector != squad_places[j] and j == len(squad_places):
                        print("The placement that you selected is not valid, please try again")
                        return 'squad_placement'
                    elif len(squad_places) == 0:
                        return 'place_holder'

class SpaceMarineTurn(Scene):

    def enter(self):
        turn_count += 1

        if turn_count == 1:


class GeneStealerTurn(Scene):

class GameControl(object):

    scenes = {
        'squad_selections': SquadSelect(),
        'opening_scene': Openingscene(),
        'squad_placement': Squadplacement()
    }