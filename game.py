from sys import exit
from random import randint
from textwrap import dedent
import chapters
import squad
import weapons
        
class Openingscene():
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

        return SquadSelect().enter()

class SquadSelect():

    heavy_count = 0

    def enter(self):
        print(dedent("""
                Below is where you can select your squad of five marines from a 
                pre-selected list of chapters. The first marine you select will
                be the squad's sergent while the rest are standard marines. Choose
                wisely because some chapters will have advantages over others.
                """))
        # SquadSelect.chapter_select()
        # SquadSelect.weapon_select()
        Squadplacement.enter(self)

    def chapter_select():
        print("Below is a list of available chapters, choose wisely...")
        print()
        
        for x in chapters.chapters:
            print(x)

        for y in squad.squad:
            if squad.squad[y]["chapter"] == None:
                print()
                print(y)
                print()
                print("Select the chapter for this terminator:")
            
                ch_input = input("> ")

                for z in chapters.chapters:
                    if z == ch_input:
                        squad.squad[y]["chapter"] = ch_input
                        break

                if squad.squad[y]["chapter"] == None:
                    print("The chapter you selected is invalid, please select a valid chapter.")
                    SquadSelect.chapter_select()
            else:
                continue             
        
    def weapon_select():

        for x in weapons.weapon_loadout:
            print(x)

        for y in squad.squad:
            if squad.squad[y]["weapon loadout"] == None:
                print()
                print(y)
                print()
                print("Choose the weapon loadout:")

                for z in weapons.weapon_loadout:
                    print(z)
            
                wpn_input = input("> ")

                for x in weapons.weapon_loadout:
                    if x == wpn_input:
                        if wpn_input == weapons.weapon_loadout[6] or wpn_input == weapons.weapon_loadout[7] or wpn_input == weapons.weapon_loadout[8]:
                            if SquadSelect.heavy_count >= 3:
                                print("You have exceeded the maximum amount of heavy weapons for this squad, another loadout needs to be selected.")
                                SquadSelect.weapon_select()
                            else:
                                SquadSelect.heavy_count += 1
                                squad.squad[y]["weapon loadout"] = wpn_input
                        else:
                            squad.squad[y]["weapon loadout"] = wpn_input
            
                if squad.squad[y]["weapon loadout"] == None:
                    print("An invalid weapon loadout was selected, please select another.")
                    SquadSelect.weapon_select()
            else:
                continue

class Squadplacement():
    order = ["first", "second", "third", "fourth", "fifth"]

    def enter(self):
        print("Select the order in which your squad is to be deployed:")
        print()
        Squadplacement.placement()

    def placement():
        while len(Squadplacement.order) != 0:
            for x in squad.squad:
                if squad.squad[x]["current_place"] == None:
                    for y in Squadplacement.order:
                        print(y)

                    print()
                    print(x)
                    place_input = input("> ")

                    for z in Squadplacement.order:
                        if place_input == z:
                            Squadplacement.place_loop(squad.squad[x], place_input)
                            break

                    print(squad.squad[x]["current_place"])
                    if squad.squad[x]["current_place"] == None:
                        print()
                        print("Your position choice is invalid, please reenter a valid position.")
                        print()
                        continue
                else:
                    continue
                        
    def place_loop(term, start_place):
        if start_place == "first":
            term["current_place"] = "s5"
            Squadplacement.order.remove("first")
        elif start_place == "second":
            term["current_place"] = "s4"
            Squadplacement.order.remove("second")
        elif start_place == "third":
            term["current_place"] = "s3"
            Squadplacement.order.remove("third")
        elif start_place == "fourth":
            term["current_place"] = "s4"
            Squadplacement.order.remove("fourth")
        else:
            term["current_place"] = "s1"
            Squadplacement.order.remove("fifth")

class GameControl(object):

    scenes = {
        'squad_selections': SquadSelect(),
        'opening_scene': Openingscene(),
        'squad_placement': Squadplacement(),
        # 'space_marine_turn': SpaceMarineTurn(),
        # 'genestealer_turn': GeneStealerTurn()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_turn(self, scene_name):
        val = GameControl.scenes.get(scene_name)
        return val

    def opening_turn(self):
        return self.next_turn(self.start_scene)

new_game = Openingscene()
new_game.enter()