from textwrap import dedent
import game
import gametiles
import squad

class Conditions():

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
                Conditions.lose_cond()