from sys import exit
from random import randint
from textwrap import dedent

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