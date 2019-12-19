from textwrap import dedent
import squad
import gametiles
import game

def move():
    print("Which terminator would you like to move?")

    for i in squad:
        if squad[i]["action points"] > 0 and squad[i]["alive"] == True:
            print(squad[i])

    movement = input("> ")

    for j in squad:
        if movement == squad[j]:
            print("How would you like to move?")

            motion_1 = ["Forwards", "Backwards",
                        "Turn Left", "Turn Right"]
            motion_2 = ["Forwards", "Turn Left", "Turn Right"]

            move_option = input("> ")

            if squad[j]["action points"] >= 2:
                print(dedent("""
                            Forwards,
                            Backwards,
                            Turn Left,
                            Turn Right,
                            Move Another Terminator,
                            Choose Another Action
                            """))

                for k in motion_1:
                    if move_option == motion_1[k]:
                        if motion_1[k] == "Forwards":
                            forwards(game.command_points,
                                     squad[i]["action points"],
                                     squad[i]["current_position"],
                                     squad[i]["direction"])
                        elif motion_1[k] == "Backwards":
                            backwards(game.command_points,
                                      squad[i]["action points"],
                                      squad[i]["current_position"],
                                      squad[i]["direction"])
                        elif motion_1[k] == "Turn Left":
                            turn_left()
                        elif motion_1[k] == "Turn Right":
                            turn_right()
                        elif motion_1[k] == "Move Another Terminator":
                            move_other_term()
                        elif motion_1[k] == "Choose Another Action":
                            choose_other_action()
                    else:
                        print("Input was invalid. Please try again.")
                        move()
            elif squad[j]["action points"] < 2:
                print(dedent("""
                            Forwards,
                            Turn Left,
                            Turn Right,
                            Move Another Terminator,
                            Choose Another Action
                            """))

                for k in motion_2:
                    if move_option == motion_2[k]:
                        if motion_2[k] == "Forwards":
                            forwards(game.command_points,
                                     squad[j]["action points"],
                                     squad[j]["current_position"],
                                     squad[j]["direction"])
                        elif motion_2[k] == "Turn Left":
                            turn_left()
                        elif motion_2[k] == "Turn Right":
                            turn_right()
                        elif motion_2[k] == "Move Another Terminator":
                            move_other_term()
                        elif motion_2[k] == "Choose Another Action":
                            choose_other_action()
                    else:
                        print("Input was invalid. Please try again.")

def forwards(w, x, y, z):
    print("How far would you like to move forward?")

    forward_move = input('> ')
    movements = 0

    if forward_move <= w + x:
        movements += forward_move

        for a in range(movements):
            if a != 0:
                if z == "north":
                    for b in gametiles.tiles:
                        if gametiles.tiles[b]["connected to"].get(y) == "south":
                            if gametiles.tiles[b]["occupied"] == True:
                                print("You are unable to move to this spot.")
                                move()
                            else:
                                gametiles.tiles[y]["occupied"] == False
                                gametiles.tiles[b]["occupied"] == True
                        else:
                            print("You are unable to move in this direction")
                            move()
                elif z == "south":
                    for b in gametiles.tiles:
                        if gametiles.tiles[b]["connected to"].get(y) == "north":
                            if gametiles.tiles[b]["occupied"] == True:
                                print("You are unable to move to this spot.")
                                move()
                            else:
                                gametiles.tiles[y]["occupied"] == False
                                gametiles.tiles[b]["occupied"] == True
                        else:
                            print("You are unable to move in this direction.")
                            move()
                elif z == "west":
                    for b in gametiles.tiles:
                        if gametiles.tiles[b]["connected to"].get(y) == "east":
                            if gametiles.tiles[b]["occupied"] == True:
                                print("You are unable to move to this spot.")
                                move()
                            else:
                                gametiles.tiles[y]["occupied"] == False
                                gametiles.tiles[b]["occupied"] == True
                        else:
                            print("You are unable to move in this direction.")
                            move()
                elif z == "east":
                    for b in gametiles.tiles:
                        if gametiles.tiles[b]["connected to"].get(y) == "west":
                            if gametiles.tiles[b]["occupied"] == True:
                                print("you are unable to move to this spot.")
                                move()
                            else:
                                gametiles.tiles[y]["occupied"] == False
                                gametiles.tiles[b]["occupied"] == True
                        else:
                            print("You are unable to move in this direction.")
                            move()
            else:
                move()
    elif forward_move > w + x:
        print("You do not have enough action points to move this far.")
        move()

def backwards(w, x, y, z):
    print("How far do you want to move backwards?")

    backwards_move = input('> ')
    movements = 0

    if backwards_move <= w + x:
        movements += backwards_move

def turn_left(x, y):

def turn_right(x, y):

def move_other_term(x):

def choose_other_action():