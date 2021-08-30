from textwrap import dedent
import squad
import gametiles
import game

class Movement():
    motion_1 = ["Forwards", "Backwards","Turn Left", "Turn Right"]
    motion_2 = ["Forwards", "Turn Left", "Turn Right"]
    movements = 0

    def move():
        print("Which terminator would you like to move?")

        for i in squad.squad:
            if squad.squad[i]["action points"] > 0 and squad.squad[i]["alive"] == True:
                print(squad.squad[i])

        movement = input("> ")

        for j in squad.squad:
            if movement == squad.squad[j]:
                print("How would you like to move?")

                move_option = input("> ")

                if squad.squad[j]["action points"] >= 2:
                    print(dedent("""
                                Forwards,
                                Backwards,
                                Turn Left,
                                Turn Right,
                                Move Another Terminator,
                                Choose Another Action
                                """))

                    for k in Movement.motion_1:
                        if move_option == Movement.motion_1[k]:
                            if Movement.motion_1[k] == "Forwards":
                                Movement.forwards(game.SpaceMarineTurn.command_points,
                                        squad.squad[i]["action points"],
                                        squad.squad[i]["current_position"],
                                        squad.squad[i]["direction"])
                            elif Movement.motion_1[k] == "Backwards":
                                Movement.backwards(game.SpaceMarineTurn.command_points,
                                        squad.squad[i]["action points"],
                                        squad.squad[i]["current_position"],
                                        squad.squad[i]["direction"])
                            elif Movement.motion_1[k] == "Turn Left":
                                Movement.turn_left(game.SpaceMarineTurn.command_points,
                                        squad.squad[i]["action points"],
                                        squad.squad[i]["direction"])
                            elif Movement.motion_1[k] == "Turn Right":
                                Movement.turn_right(game.SpaceMarineTurn.command_points,
                                        squad.squad[i]["action points"],
                                        squad.squad[i]["direction"])
                            elif Movement.motion_1[k] == "Move Another Terminator":
                                Movement.move_other_term()
                            elif Movement.motion_1[k] == "Choose Another Action":
                                Movement.choose_other_action()
                        else:
                            print("Input was invalid. Please try again.")
                            Movement.move()
                elif squad[j]["action points"] < 2:
                    print(dedent("""
                                Forwards,
                                Turn Left,
                                Turn Right,
                                Move Another Terminator,
                                Choose Another Action
                                """))

                    for k in Movement.motion_2:
                        if move_option == Movement.motion_2[k]:
                            if Movement.motion_2[k] == "Forwards":
                                Movement.forwards(game.SpaceMarineTurn.command_points,
                                        squad.squad[j]["action points"],
                                        squad.squad[j]["current_position"],
                                        squad.squad[j]["direction"])
                            elif Movement.motion_2[k] == "Turn Left":
                                Movement.turn_left(game.SpaceMarineTurn.command_points,
                                        squad[i]["action points"],
                                        squad[i]["direction"])
                            elif Movement.motion_2[k] == "Turn Right":
                                Movement.turn_right(game.SpaceMarineTurn.command_points,
                                        squad[i]["action points"],
                                        squad[i]["direction"])
                            elif Movement.motion_2[k] == "Move Another Terminator":
                                Movement.move_other_term()
                            elif Movement.motion_2[k] == "Choose Another Action":
                                Movement.choose_other_action()
                        else:
                            print("Input was invalid. Please try again.")

    def forwards(w, x, y, z):
        print("How far would you like to move forward?")

        forward_move = input('> ')

        if forward_move <= w + x:
            Movement.movements += forward_move

            for a in range(Movement.movements):
                if a != 0:
                    if z == "north":
                        for b in gametiles.tiles:
                            if gametiles.tiles[b]["connected to"].get(y) == "south":
                                if gametiles.tiles[b]["occupied"] == True:
                                    print("You are unable to move to this spot.")
                                    Movement.move()
                                else:
                                    if x < 1 and w > 1:
                                        w -= 1
                                    elif x >= 1:
                                        x -= 1
                                    else:
                                        print("You don't have enough action point and/or command points to do this action.")
                                        Movement.move()

                                    gametiles.tiles[y]["occupied"] = False
                                    gametiles.tiles[b]["occupied"] = True

                                    y = gametiles[b]
                            else:
                                print("You are unable to move in this direction")
                                Movement.move()
                    elif z == "south":
                        for b in gametiles.tiles:
                            if gametiles.tiles[b]["connected to"].get(y) == "north":
                                if gametiles.tiles[b]["occupied"] == True:
                                    print("You are unable to move to this spot.")
                                    Movement.move()
                                else:
                                    if x < 1 and w >= 1:
                                        w -= 1
                                    elif x >= 1:
                                        x -= 1
                                    else:
                                        print("You don't have enough action point and/or command points to do this action.")
                                        Movement.move()

                                    gametiles.tiles[y]["occupied"] = False
                                    gametiles.tiles[b]["occupied"] = True

                                    y = gametiles[b]
                            else:
                                print("You are unable to move in this direction.")
                                Movement.move()
                    elif z == "west":
                        for b in gametiles.tiles:
                            if gametiles.tiles[b]["connected to"].get(y) == "east":
                                if gametiles.tiles[b]["occupied"] == True:
                                    print("You are unable to move to this spot.")
                                    Movement.move()
                                else:
                                    if x < 1 and w > 1:
                                        w -= 1
                                    elif x >= 1:
                                        x -= 1
                                    else:
                                        print("You don't have enough action point and/or command points to do this action.")
                                        Movement.move()

                                    gametiles.tiles[y]["occupied"] = False
                                    gametiles.tiles[b]["occupied"] = True

                                    y = gametiles[b]
                            else:
                                print("You are unable to move in this direction.")
                                Movement.move()
                    elif z == "east":
                        for b in gametiles.tiles:
                            if gametiles.tiles[b]["connected to"].get(y) == "west":
                                if gametiles.tiles[b]["occupied"] == True:
                                    print("you are unable to move to this spot.")
                                    Movement.move()
                                else:
                                    if x < 1 and w > 1:
                                        w -= 1
                                    elif x >= 1:
                                        x -= 1
                                    else:
                                        print("You don't have enough action point and/or command points to do this action.")
                                        Movement.move()

                                    gametiles.tiles[y]["occupied"] = False
                                    gametiles.tiles[b]["occupied"] = True

                                    y = gametiles[b]
                            else:
                                print("You are unable to move in this direction.")
                                Movement.move()
            
            Movement.move()

        elif forward_move > w + x:
            print("You do not have enough action points to move this far.")
            Movement.move()

    def backwards(w, x, y, z):
        print("How far do you want to move backwards?")

        backwards_move = input('> ')
        #movements = 0

        if backwards_move <= w + x:
            Movement.movements += backwards_move

            for a in range(Movement.movements):
                if a != 0:
                    if z == "north":
                        for b in gametiles.tiles:
                            if gametiles.tiles[b]["connected to"].get(y) == "south":
                                if gametiles.tiles[b]["occupied"] == True:
                                    print("You are unable to move to this spot.")
                                    Movement.move()
                                else:
                                    if x < 2 and w >= 2:
                                        w -= 2
                                    elif x >= 2:
                                        x -= 2
                                    else:
                                        print("You don't have enough action point and/or command points to do this action.")
                                        Movement.move()

                                    gametiles.tiles[y]["occupied"] = False
                                    gametiles.tiles[b]["occupied"] = True

                                    y = gametiles[b]
                            else:
                                print("You are unable to move in this direction.")
                                Movement.move()  
                    elif z == "south":
                        for b in gametiles.tiles:
                            if gametiles.tiles[b]["connected to"].get(y) == "north":
                                if gametiles.tiles[b]["occupied"] == True:
                                    print("You are unable to move to this spot")
                                    Movement.move()
                                else:
                                    if x < 2 and w >= 2:
                                        w -= 2
                                    elif x >= 2:
                                        x -=2
                                    else:
                                        print("You don't have enough action points and/or command points to do this action.")
                                        Movement.move()

                                    gametiles.tiles[y]["occupied"] = False
                                    gametiles.tiles[b]["occupied"] = True 

                                    y = gametiles[b]
                            else:
                                print("You are unable to move in this direction.")
                                Movement.move()
                    elif z == "east":
                        for b in gametiles.tiles:
                            if gametiles.tiles[b]["connected to"].get(y) == "west":
                                if gametiles.tiles[b]["occupied"] == True:
                                    print("You are unable to move to this spot.")
                                    Movement.move()
                                else:
                                    if x < 2 and w >= 2:
                                        w -= 2
                                    elif x >= 2:
                                        x -= 2
                                    else:
                                        print("You don't have enough action points and/or command points to do this action.")
                                        Movement.move()

                                    gametiles.tiles[y]["occupied"] = False
                                    gametiles.tiles[b]["occupied"] = True

                                    y = gametiles[b]
                            else:
                                print("You are unable to move in this direction.")
                                Movement.move()
                    elif z == "west":
                        for b in gametiles.tiles:
                            if gametiles.tiles[b]["connected to"].get(y) == "west":
                                if gametiles.tiles[b]["occupied"] == True:
                                    print("You are unable to move to this spot.")
                                    Movement.move()
                                else:
                                    if x < 2 and w >= 2:
                                        w -= 2
                                    elif x >= 2:
                                        x -= 2
                                    else:
                                        print("You don't have enough action points and/or command points to do this action.")
                                        Movement.move()

                                    gametiles.tiles[y]["occupied"] = False
                                    gametiles.tiles[b]["occupied"] = True

                                    y = gametiles[Movement.backwards]
                            else:
                                print("You are unable to move in this direction.")
                                Movement.move()

            Movement.move()

        elif backwards_move > w + x:
            print("You do not have enough action points to move this far.")
            Movement.move()

    def turn_left(x, y, z):
        if y >= 1:
            y -= 1
            if z == "north":
                z = "west"
            elif z == "south":
                z = "east"
            elif z == "east":
                z = "north"
            elif z == "west":
                z = "south"
            else:
                print("Was unable to move left.")
                Movement.move()
        elif x >= 1 and y < 1:
            x -= 1
            if z == "north":
                z = "west"
            elif z == "south":
                z = "east"
            elif z == "east":
                z = "north"
            elif z == "west":
                z = "south"
            else:
                print("Was unable to move left.")
                Movement.move()
        else:
            print("You do not have enough action points/command points to complete this action.")
            Movement.move()

        Movement.move()

    def turn_right(x, y, z):
        if y >= 1:
            y -= 1
            if z == "north":
                z = "east"
            elif z == "south":
                z = "west"
            elif z == "east":
                z = "south"
            elif z == "west":
                z = "north"
            else:
                print("Was unable to move right.")
                Movement.move()
        elif x >= 1 and y < 1:
            x -= 1
            if z == "north":
                z = "east"
            elif z == "south":
                z = "west"
            elif z == "east":
                z = "south"
            elif z == "west":
                z = "north"
            else:
                print("Was unable to move right.")
                Movement.move()
        else:
            print("You do not have enough action points/command points to complete this action.")
            Movement.move()
        
        Movement.move()

    def move_other_term():
        Movement.move()

    def choose_other_action():
        game.SpaceMarineTurn.turn_menu()