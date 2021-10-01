from random import randint
from textwrap import dedent
import move
import squad
import gametiles
import genestealers
import attackaction
import miscaction
import gamemap
import genestealerturn

class SpaceMarineTurn():
    command_points = randint(1, 7)

    def enter(turn_count):
        turn_count +=1
        print("It is now the space marines' turn.")
        print("(press enter to continue)")
        input('')
        SpaceMarineTurn.pre_turn()
        SpaceMarineTurn.turn_menu()

    def pre_turn():
        for x in squad.squad:
            if squad.squad[x]["action points"] != 4:
                squad.squad[x]["action points"] = 4

            if squad.squad[x]["overwatch"] == True:
                squad.squad[x]["action points"] -= 2

        for y in gametiles.tiles:
            if gametiles.tiles[y]["on fire"] == True:
                gametiles.tiles[y]["on fire"] == False
                gametiles.tiles[y]["occupied"] == False
                for z in genestealers.genestealers:
                    if genestealers.genestealers[z]["current location"] == y:
                        gametiles.tiles[y]["occupied"] == True

    def turn_menu():
        print(f"Command Points: {SpaceMarineTurn.command_points}")
        print(dedent("""
            Move
            Attack
            Other Action
            View Map
            End Turn
        """))

        menu_choice = input("> ")

        if menu_choice == "Move":
            move.MoveAction.move(SpaceMarineTurn.command_points)
        elif menu_choice == "Attack":
            attackaction.Attack.attack()
        elif menu_choice == "Other Action":
            miscaction.OtherActions.other_action()
        elif menu_choice == "View Map":
            gamemap.map()
        elif menu_choice == "End Turn":
            
            return genestealerturn
        else:
            print("The command that you entered in invalid, please try again.")
            SpaceMarineTurn.turn_menu()
