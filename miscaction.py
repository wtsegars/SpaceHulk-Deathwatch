from textwrap import dedent
import game
import squad
import gametiles

class OtherActions():
    def other_action():
        print("Which terminator would you like to take action?")
        for x in squad:
            if squad[x]["action points"] > 0 and squad[x]["alive"] == True:
                print(squad[x])
        
        term_choice = input("> ")

        if term_choice == squad[x]:
            print("What would you like to do?")
            print(dedent("""
                    Reload,
                    Toggle Door,
                    Overwatch,
                    Clear Jam,
                    Cancel
                    """))

            action_choice = input("> ")

            if action_choice == "Reload":
                OtherActions.reload(game.SpaceMarineTurn.command_points,
                        squad[x]["action points"],
                        squad[x]["clip_size"],
                        squad[x]["clip_num"],
                        squad[x]["weapon loadout"])
            elif action_choice == "Toggle Door":
                OtherActions.toggle_door(game.SpaceMarineTurn.command_points,
                            squad[x]["action points"],
                            gametiles.tiles,
                            squad[x]["current_place"],
                            squad[x]["direction"])
            elif action_choice == "Overwatch":
                OtherActions.overwatch(game.SpaceMarineTurn.command_points,
                            squad[x]["action points"],
                            squad[x]["overwatch"],
                            squad[x]["jammed"])
            elif action_choice == "Clear Jam":
                OtherActions.clear_jam(game.SpaceMarineTurn.command_points,
                            squad[x]["action points"],
                            squad[x]["jammed"])
            elif action_choice == "Cancel":
                game.SpaceMarineTurn.enter.turn_menu()
            else:
                print("You have entered an invalid command, please try again.")
                OtherActions.other_action()

    def reload(a, b, c, d, e):
        if d == 0:
            print("You don't have any more clips to reload your weapon with.")
            OtherActions.other_action()
        
        if e != "Assault Cannon and Powerfist" and e != "Heavy Flamer and Powerfist":
            print("Your don't have a weapon that needs to be reloaded")
            OtherActions.other_action()

        if b >= 4:
            b -= 4
        else:
            diff = 4 - b

            b = 0
            a -= diff

        if e == "Assault Cannon and Powerfist":
            c = 10
            d -= 1
            print("Your assault cannon has been reloaded.")
            OtherActions.other_action()
        elif e == "Heavy Flamer and Powerfist":
            c = 10
            d -= 1
            print("Your heavy flamer has been reloaded.")
            OtherActions.other_action()

    def toggle_door(a, b, c, d, e):
        if d == "ll5" and e == "west":
            if b >= 1:
                b -= 1
            elif b < 1 and a >= 1:
                a -= 1
            elif b < 1 and a < 1:
                print("You don't have enough action points to complete this action.")
                OtherActions.other_action()

            print("The lower left door has been sucessfully sealed.")
            c["g4"]["door"]["sealed"] == True
            OtherActions.other_action()
        elif d == "lr5" and e == "east":
            if b >= 1:
                b -= 1
            elif b < 1 and a >= 1:
                a -= 1
            elif b < 1 and a < 1:
                print("You don't have enough action points to complete this action.")
                OtherActions.other_action()
            
            print("The lower right door has been sucessfully sealed.")
            c["g8"]["door"]["sealed"] == True
            OtherActions.other_action()
        elif d == "c3" and e == "south":
            if b >= 1:
                b -= 1
            elif b < 1 and a >= 1:
                a -= 1
            elif b < 1 and a < 1:
                print("You don't have enough action points to complete this action.")
                OtherActions.other_action()
            
            print("The lower center door has been sucessfully sealed.")
            c["c3"]["door"]["sealed"] == True
            OtherActions.other_action()
        elif d == "c5" and e == "north":
            if b >= 1:
                b -= 1
            elif b < 1 and a >= 1:
                a -= 1
            elif b < 1 and a < 1:
                print("You don't have enough action points to complete this action.")
                OtherActions.other_action()
            
            print("The upper center door has been sucessfully sealed.")
            c["c5"]["door"]["sealed"] == True
            OtherActions.other_action()
        elif d == "g20" and e == "west":
            if b >= 1:
                b -= 1
            elif b < 1 and a >= 1:
                a -= 1
            elif b < 1 and a < 1:
                print("You don't have enough action points to complete this action.")
                OtherActions.other_action()

            print("The lower top left door has been sucessfully sealed.")
            c["g20"]["door"]["sealed"] == True
            OtherActions.other_action()
        elif d == "g18" and e == "east":
            if b >= 1:
                b -= 1
            elif b < 1 and a >= 1:
                a -= 1
            elif b < 1 and a < 1:
                print("You don't have enough action points to complete this action.")
                OtherActions.other_action()

            print("The lower top right door has been sucessfully sealed.")
            c["g18"]["door"]["sealed"] == True
            OtherActions.other_action()
        elif d == "g24" and e == "west":
            if b >= 1:
                b -= 1
            elif b < 1 and a >= 1:
                a -= 1
            elif b < 1 and a < 1:
                print("You don't have enough action points to complete this action.")
                OtherActions.other_action()

            print("The upper top left door has been sucessfully sealed.")
            c["g24"]["door"]["sealed"] == True
            OtherActions.other_action()
        elif d == "g22" and e == "east":
            if b >= 1:
                b -= 1
            elif b < 1 and a >= 1:
                a -= 1
            elif b < 1 and a < 1:
                print("You don't have enough action points to complete this action.")
                OtherActions.other_action()
        
            print("The upper top right door has been sucessfully sealed.")
            c["g22"]["door"]["sealed"] == True
            OtherActions.other_action()
        else:
            print("There is no door for you to seal.")
            OtherActions.other_action()

    def overwatch(a, b, c, d):
        if d == True:
            print("You weapon is jammed. You need to clear the jam before you can go on overwatch.")
            OtherActions.other_action()
        else:
            if c == False:
                if b >= 2:
                    b -= 2
                elif b < 2 and a >= 2:
                    diff = a - b
                    a -= diff
                else:
                    print("You don't have enough action points to complete this action.")
                    OtherActions.other_action()
            
                print("This marine is now on overwatch.")
                c = True
                OtherActions.other_action()
            elif c == True:
                b += 2

                print("This marine is no longer on overwatch.")
                OtherActions.other_action()

    def clear_jam(a, b, c):
        if b >= 1:
            b -= 1
        elif b < 1 and a >= 1:
            a -= 1
        else:
            print("You do not have enough action points to complete this action.")
            OtherActions.other_action()

        c = False
        print("Your storm bolter is no longer jammed.")
        OtherActions.other_action()