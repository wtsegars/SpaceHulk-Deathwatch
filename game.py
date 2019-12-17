from sys import exit
from random import randint
from textwrap import dedent
import gametiles
import squad
import chapters
import weapons
import movement
import attackaction
import miscaction

command_points = 0

turn_count = 0

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
                print(weapons.weapon_loadout)

                weapon_choice = input("> ")

                for j in weapons.weapon_loadout:
                    if weapon_choice == weapons.weapon_loadout[j]:
                        sgt["weapon loadout"] = weapon_choice
                        if weapon_choice == weapons.weapon_loadout[6] or weapon_choice == weapons.weapon_loadout[7]:
                            if weapon_choice == weapons.weapon_loadout[6]:
                                sgt["overwatch"] = False
                            heavy_count += 1
                            sgt["clip_size"] = 10
                            sgt["clip_num"] = 2
                            break
                        elif weapon_choice == weapons.weapon_loadout[8]:
                            heavy_count += 1
                            sgt["clip_size"] = 8
                            sgt["clip_num"] = 0
                            break
                        elif heavy_count == 3:
                            print("You have reached the maximum amount of heavy weapons for you squad, please try again.")
                            return 'squad_selection'
                        elif weapon_choice == weapons.weapon_loadout[0] or weapon_choice == weapons.weapon_loadout[1] or weapon_choice == weapons.weapon_loadout[4] or weapon_choice == weapons.weapon_loadout[5] or weapon_choice == weapons.weapon_loadout[8] or weapon_choice == weapons.weapon_loadout[9]:
                            sgt["overwatch"] = False
                            sgt["jammed"] = False
                            break
                        else:
                            break
                    elif weapon_choice != weapons.weapon_loadout[j] and j == len(weapons.weapon_loadout):
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
                print(weapons.weapon_loadout)

                weapon_choice = input("> ")

                for j in weapons.weapon_loadout:
                    if weapon_choice == weapons.weapon_loadout[j]:
                        terminator["weapon loadout"] = weapon_choice
                        if weapon_choice == weapons.weapon_loadout[6] or weapon_choice == weapons.weapon_loadout[7]:
                            if weapon_choice == weapons.weapon_loadout[6]:
                                terminator["overwatch"] = False
                            heavy_count += 1
                            terminator["clip_size"] = 10
                            terminator["clip_num"] = 2
                            break
                        elif weapon_choice == weapons.weapon_loadout[8]:
                            heavy_count +=1
                            terminator["clip_size"] = 8
                            terminator["clip_num"] = 0
                            break
                        elif heavy_count == 3:
                            print("You have reached the maximum amount of heavy weapons for you squad, please try again.")
                            return 'squad_selection'
                        elif weapon_choice == weapons.weapon_loadout[0] or weapon_choice == weapons.weapon_loadout[1] or weapon_choice == weapons.weapon_loadout[4] or weapon_choice == weapons.weapon_loadout[5] or weapon_choice == weapons.weapon_loadout[8] or weapon_choice == weapons.weapon_loadout[9]:
                            terminator["overwatch"] = False
                            terminator["jammed"] = False
                            break
                        else:
                            break
                    elif weapon_choice != weapons.weapon_loadout[j] and j == len(weapons.weapon_loadout):
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
            term_direction = {}

            if placement_selector:
                for j in squad_places:
                    if placement_selector == squad_places[j]:
                        term_place["starting_position"] = squad_places[j]
                        squad[i]["starting_place"] = term_place
                        term_place.clear()
                        term_place["current_postion"] = squad_places[j]
                        squad[i]["current_place"] = term_place
                        squad_places.pop(j)
                        term_place.clear()
                        term_direction["direction"] = "north"
                        squad[i]["direction"] = term_direction
                        term_direction.clear()
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
                command_points = randint(1, 6)
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
                movement.move()     
            elif action_choice == "Attack":
                attackaction.attack()
            elif action_choice == "Other Action":
                miscaction.other_action()
            elif action_choice == "End Turn":
                return 'genestealer_turn'
            else:
                print("You entered an invalid command, please try again.")
                turn_menu()
                                
#class GeneStealerTurn(Scene):

class GameControl(object):

    scenes = {
        'squad_selections': SquadSelect(),
        'opening_scene': Openingscene(),
        'squad_placement': Squadplacement(),
        'space_marine_turn': SpaceMarineTurn(),
        'genestealer_turn': GeneStealerTurn()
    }