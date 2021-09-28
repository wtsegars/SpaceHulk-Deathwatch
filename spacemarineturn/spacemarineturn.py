from sys import exit
from random import randint
from textwrap import dedent
import move
import squad
import gametiles
import genestealers
import attackaction
import miscaction
import gamemap
import game
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
            SpaceMarineTurn.win_cond()
            return genestealerturn
        else:
            print("The command that you entered in invalid, please try again.")
            SpaceMarineTurn.turn_menu()

    def win_cond():
        if gametiles.tiles['ll5']["door"]["sealed"] == True and gametiles.tiles['lr5']["door"]["sealed"] == True and gametiles.tiles['c3']["door"]["sealed"] == True and gametiles.tiles['c5']["door"]["sealed"] == True and gametiles.tiles['g20']["door"]["sealed"] == True and gametiles.tiles['g18']["door"]["sealed"] == True and gametiles.tiles['g24']["door"]["sealed"] == True and gametiles.tiles['g22']["door"]["sealed"] == True:
            print(dedent("""
                Victory is ours!
                Mission accompished! The xenos filth has been sealed out of this area of the hulk!
            """))
            exit

    def lose_cond():
        if squad.squad['Sergent']['alive'] == False and squad.squad['Terminator1']['alive'] == False and squad.squad['Terminator2']['alive'] == False and squad.squad['Terminator3']['alive'] == False and squad.squad["Terminator4"]["alive"] == False:
            print(dedent("""
                Your squad had been overrun by the xenos filth!
                Mission Failed!

                Try again?
            """))

            try_again = input("> ")

            if try_again == "Y" or try_again == "y":
                new_game = game.Openingscene()
                new_game.enter()
            elif try_again == "N" or try_again == "n":
                exit
            else:
                print("Invalid input, please try again.")
                SpaceMarineTurn.lose_cond()