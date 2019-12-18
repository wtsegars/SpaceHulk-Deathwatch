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
                            forwards(squad[i]["action points"],
                                     squad[i]["current_position"])
                        elif motion_1[k] == "Backwards":
                            backwards()
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
                        for c in gametiles.tiles[b]:
                            if gametiles.tiles[b][c] == y:
                                if gametiles[b][c - 1]["connected to"][y] == "south":
                                    gametiles[b][c]["occupied"] == False
                                    gametiles[b][c - 1]["occupied"] == True
                                    x -= 1
                                    break
                                elif gametiles[b][c + 1]["connected to"][y] == "south":
                                    gametiles[b][c]["occupied"] == False
                                    gametiles[b][c + 1]["occupied"] == True
                                    x -= 1
                                    break
                                elif gametiles[b][c - 1]["occupied"] == True or gametiles[b][c + 1]["occupied"] == True:
                                    print("This space is already occupied.")
                                    break
                elif z == "south":
                    for b in gametiles.tiles:
                        for c in gametiles.tiles[b]:

def backwards(x, y):

def turn_left(x, y):

def turn_right(x, y):

def move_other_term(x):

def choose_other_action():