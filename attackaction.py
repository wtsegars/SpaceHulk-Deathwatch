from random import randint
import squad
import game
import gametiles
import genestealers
import linesight

def attack():
    print("Which terminator would you like to attack with?")

    for i in squad.squad:
        if squad[i]["action points"] > 0 and squad[i]["alive"] == True:
            print(squad[i])

    print("Cancel")

    attack_with = input("> ")

    for j in squad.squad:
        if attack_with == squad[j]:
            print("How would you like to attack?")

            if squad[j]["weapon loadout"] == "Storm Bolter and Powerfist":
                print("Storm Bolter")
                print("Powerfist")
                print("Cancel")

                attack_choice = input("> ")

                if attack_choice == "Storm Bolter":
                    ranged_combat(game.command_points,
                                    squad[j]["action points"],
                                    squad[j]["current position"],
                                    squad[j]["direction"],
                                    squad[j]["alive"])
                elif attack_choice == "Powerfist":
                    close_combat()
                elif attack_choice == "Cancel":
                    attack()
                else:
                    print("You entered an invalid command, please try again.")
                    attack()
            elif squad[i]["weapon loadout"] == "Power Sword and Storm Bolter":
                print("Storm Bolter")
                print("Power Sword")
                print("Cancel")

                attack_choice = input("> ")

                if attack_choice == "Storm Bolter":
                    ranged_combat(game.command_points,
                                    squad[j]["action points"],
                                    squad[j]["current position"],
                                    squad[j]["direction"],
                                    squad[j]["alive"])
                elif attack_choice == "Power Sword":
                    close_combat()
                elif attack_choice == "Cancel":
                    attack()
                else:
                    print("You entered an invalid command, please try again.")
                    attack()
            elif squad[i]["weapon loadout"] == "Thunder Hammer and Storm Shield":
                print("Thunder Hammer")
                print("Cancel")

                attack_choice = input("> ")

                if attack_choice == "Thunder Hammer":
                    close_combat()
                elif attack_choice == "Cancel":
                    attack()
                else:
                    print("You entered an invalid command, please try again.")
                    attack()
            elif squad[i]["weapon loadout"] == "Lightning Claws":
                print("Lightning Claws")
                print("Cancel")

                attack_choice = input("> ")

                if attack_choice == "Lightning Claws":
                    close_combat()
                elif attack_choice == "Cancel":
                    attack()
                else:
                    print("You entered an invalid command, please try again.")
                    attack()
            elif squad[i]["weapon loadout"] == "Storm Bolter and Chainfist":
                print("Storm Bolter")
                print("Chainfist")
                print("Cancel")

                attack_choice = input("> ")

                if attack_choice == "Storm Bolter":
                    ranged_combat(game.command_points,
                                    squad[j]["action points"],
                                    squad[j]["current position"],
                                    squad[j]["direction"],
                                    squad[j]["alive"])
                elif attack_choice == "Chainfist":
                    close_combat()
                elif attack_choice == "Cancel":
                    attack()
                else:
                    print("You entered an invalid command, please try again.")
                    attack()
            elif squad[i]["weapon loadout"] == "Storm Bolter and Power Axe":
                print("Strom Bolter")
                print("Power Axe")
                print("Cancel")

                attack_choice = input("> ")

                if attack_choice == "Storm Bolter":
                    ranged_combat(game.command_points,
                                    squad[j]["action points"],
                                    squad[j]["current position"],
                                    squad[j]["direction"],
                                    squad[j]["alive"])
                elif attack_choice == "Power Axe":
                    close_combat()
                elif attack_choice == "Cancel":
                    attack()
                else:
                    print("You entered an invalid command, please try again.")
                    attack()
            elif squad[i]["weapon loadout"] == "Assault Cannon and Powerfist":
                print("Assault Cannon")
                print("Powerfist")
                print("Cancel")

                attack_choice = input("> ")

                if attack_choice == "Assault Cannon":
                    ranged_combat(game.command_points,
                                    squad[j]["action points"],
                                    squad[j]["current position"],
                                    squad[j]["direction"],
                                    squad[j]["alive"])
                elif attack_choice == "Powerfist":
                    close_combat()
                elif attack_choice == "Cancel":
                    attack()
                else:
                    print("You entered an invalid command, please try again.")
                    attack()
            elif squad[i]["weapon loadout"] == "Heavy Flamer and Powerfist":
                print("Heavy Flamer")
                print("Powerfist")
                print("Cancel")

                attack_choice = input("> ")

                if attack_choice == "Heavy Flamer":
                    ranged_combat(game.command_points,
                                    squad[j]["action points"],
                                    squad[j]["current position"],
                                    squad[j]["direction"],
                                    squad[j]["alive"])
                elif attack_choice == "Powerfist":
                    close_combat()
                elif attack_choice == "Cancel":
                    attack()
                else:
                    print("You entered an invalid command, please try again.")
                    attack()
            elif squad[i]["weapon loadout"] == "Cyclone Missile Launcher, Storm Bolter and Powerfist":
                print("Storm Bolter")
                print("Cyclone Missile Launcher")
                print("Powerfist")
                print("Cancel")

                attack_choice = input("> ")

                if attack_choice == "Storm Bolter":
                    ranged_combat(game.command_points,
                                    squad[j]["action points"],
                                    squad[j]["current position"],
                                    squad[j]["direction"],
                                    squad[j]["alive"])
                elif attack_choice == "Cyclone Missile Launcher":
                    ranged_combat(game.command_points,
                                    squad[j]["action points"],
                                    squad[j]["current position"],
                                    squad[j]["direction"],
                                    squad[j]["alive"])
                elif attack_choice == "Powerfist":
                    close_combat()
                elif attack_choice == "Cancel":
                    attack()
                else:
                    print("You entered and invalid command, please try again.")
                    attack()
            elif squad[i]["weapon loadout"] == "Storm Bolter and Power Maul":
                print("Storm Bolter")
                print("Power Maul")
                print("Cancel")

                attack_choice = input("> ")

                if attack_choice == "Storm Bolter":
                    ranged_combat(game.command_points,
                                    squad[j]["action points"],
                                    squad[j]["current position"],
                                    squad[j]["direction"],
                                    squad[j]["alive"],
                                    attack_choice = input("> "))
                elif attack_choice == "Power Maul":
                    close_combat()
                elif attack_choice == "Cancel":
                    attack()
                else:
                    print("You entered an invalid command, please try again.")
        elif attack_with == "Cancel":
            game.SpaceMarineTurn.enter.turn_menu()

def ranged_combat(a, b, c, d, e, f):
    if a >= 1 or b >= 1:
        if f == "Storm Bolter":
            if c == "c1":
                if d == "south":
                    for x in range(5, -1, -1):
                        if linesight.line_of_sight[0][x] == gametiles.tiles[linesight.line_of_sight[0][x]]:
                            if gametiles.tiles[linesight.line_of_sight[0][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[0][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[0][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "east":
                    for x in range(0, 8, 1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "west":
                    for x in range(8, 15, 1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
            elif c == "ll5":
                if d == "north":
                    for x in range(1, 15, 1):
                        if linesight.line_of_sight[4][x] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                            if gametiles.tiles[linesight.line_of_sight[4][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "east":
                    for x in range(2, -1, -1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "west":
                    for x in range(2, 15, 1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
            elif c == "lr5":
                if d == "north":
                    for x in range(1, 15, 1):
                        if linesight.line_of_sight[5][x] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                            if gametiles.tiles[linesight.line_of_sight[5][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                                    elif x < 0:
                                        print("There is not here for you to fire upon.")
                                        attack()
                elif d == "east":
                    for x in range(12, -1, -1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "west":
                    for x in range(13, 15, 1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
            elif c == "ll5":
                if d == "north":
                    for x in range(1, 15, 1):
                        if linesight.line_of_sight[4][x] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                            if gametiles.tiles[linesight.line_of_sight[4][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                                    elif x < 0:
                                        print("There is not here for you to fire upon.")
                                        attack()
                elif d == "east":
                    for x in range(13, 15, 1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "west":
                    for x in range(12, -1, -1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
            elif c == "g3":
                if d == "south":
                    for x in range(1, 3, 1):
                        if linesight.line_of_sight[2][x] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                            if gametiles.tiles[linesight.line_of_sight[2][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "east":
                    for x in range(1, 15, 1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
            elif c == "g7":
                if d == "south":
                    for x in range(1, 3, 1):
                        if linesight.line_of_sight[2][x] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                            if gametiles.tiles[linesight.line_of_sight[2][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "west":
                    for x in range(13, -1, -1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
            elif c == "l6":
                if d == "south":
                    for x in range(5, -1, -1):
                        if linesight.line_of_sight[4][x] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                            if gametiles.tiles[linesight.line_of_sight[4][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "north":
                    for x in range(7, 14, 1):
                        if linesight.line_of_sight[4][x] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                            if gametiles.tiles[linesight.line_of_sight[4][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "east":
                    for x in range(1, 10, 1):
                        if linesight.line_of_sight[6][x] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                            if gametiles.tiles[linesight.line_of_sight[6][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
            elif c == "r6":
                if d == "south":
                    for x in range(5, -1, -1):
                        if linesight.line_of_sight[5][x] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                            if gametiles.tiles[linesight.line_of_sight[5][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "north":
                    for x in range(7, 14, 1):
                        if linesight.line_of_sight[5][x] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                            if gametiles.tiles[linesight.line_of_sight[5][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "west":
                    for x in range(9, -1, -1):
                        if linesight.line_of_sight[6][x] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                            if gametiles.tiles[linesight.line_of_sight[6][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
            elif c == "c4":
                if d == "south":
                    for x in range(1, -1, -1):
                        if linesight.line_of_sight[7][x] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                            if gametiles.tiles[linesight.line_of_sight[7][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "north":
                    for x in range(3 , 5, 1):
                        if linesight.line_of_sight[7][x] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                            if gametiles.tiles[linesight.line_of_sight[7][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "east":
                    for x in range(6, 10, 1):
                        if linesight.line_of_sight[6][x] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                            if gametiles.tiles[linesight.line_of_sight[6][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
                elif d == "west":
                    for x in range(4, -1, -1):
                        if linesight.line_of_sight[6][x] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                            if gametiles.tiles[linesight.line_of_sight[6][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current position"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                        bolter_fire()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current position"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                                print("You can't fire on your own men.")
                                                attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                attack()
    else:
        print("You don't have enough action points to complete this action.")
        attack()

def close_combat(a, b, c, d, e, f):
    if a >= 1 or b >= 1:
        for x in gametiles.tiles:
            if gametiles.tiles[x] == c:
                for y in gametiles.tiles[x]["connected to"]:
                    if gametiles.tiles[y]["occupied"] == True:
                        for z in genestealers.genestealers:
                            if genestealers.genestealers[z]["current position"] == gametiles.tiles[y]:
                                if genestealers.genestealers[z]["direction"] == "north" and d == "south":
                                    if f == "Powerfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Sword":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            parry(spacemarine_roll)

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                game.SpaceMarineTurn.enter.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print("The attacking terminator has sucessfully slain the xenos filth.")
                                                attack()
                                            else:
                                                print("There was a draw in combat")
                                                attack()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Thunder Hammer":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Lightning Claws":
                                        spacemarine_rolls = [randint(1, 6), randint(1, 6)]
                                        genestealer_rolls = [randint(1, 6), randint(1, 6), randint(1, 6)]

                                        spacemarine_rolls.sort()
                                        genestealer_rolls.sort()

                                        if genestealer_rolls[2] > spacemarine_rolls[1]:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[2] < spacemarine_rolls[1]:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Chainfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Axe":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}
                                        
                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Maul":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    else: 
                                        print("You entered an invalid weapon type, please try again.")
                                        attack()
                                    
                                    attack()
                                elif genestealers.genestealers[z]["direction"] == "south" and d == "north":
                                    if f == "Powerfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Sword":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            parry(spacemarine_roll)

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                game.SpaceMarineTurn.enter.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print("The attacking terminator has sucessfully slain the xenos filth.")
                                                attack()
                                            else:
                                                print("There was a draw in combat")
                                                attack()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Thunder Hammer":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Lightning Claws":
                                        spacemarine_rolls = [randint(1, 6), randint(1, 6)]
                                        genestealer_rolls = [randint(1, 6), randint(1, 6), randint(1, 6)]

                                        spacemarine_rolls.sort()
                                        genestealer_rolls.sort()

                                        if genestealer_rolls[2] > spacemarine_rolls[1]:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[2] < spacemarine_rolls[1]:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Chainfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Axe":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}
                                        
                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Maul":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    else: 
                                        print("You entered an invalid weapon type, please try again.")
                                        attack()
                                    
                                    attack()
                                elif genestealers.genestealers[z]["direction"] == "east" and d == "west":
                                    if f == "Powerfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Sword":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            parry(spacemarine_roll)

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                game.SpaceMarineTurn.enter.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print("The attacking terminator has sucessfully slain the xenos filth.")
                                                attack()
                                            else:
                                                print("There was a draw in combat")
                                                attack()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Thunder Hammer":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Lightning Claws":
                                        spacemarine_rolls = [randint(1, 6), randint(1, 6)]
                                        genestealer_rolls = [randint(1, 6), randint(1, 6), randint(1, 6)]

                                        spacemarine_rolls.sort()
                                        genestealer_rolls.sort()

                                        if genestealer_rolls[2] > spacemarine_rolls[1]:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[2] < spacemarine_rolls[1]:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Chainfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Axe":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}
                                        
                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Maul":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    else: 
                                        print("You entered an invalid weapon type, please try again.")
                                        attack()
                                    
                                    attack()
                                elif genestealers.genestealers[z]["direction"] == "west" and d == "east":
                                    if f == "Powerfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Sword":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            parry(spacemarine_roll)

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                game.SpaceMarineTurn.enter.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print("The attacking terminator has sucessfully slain the xenos filth.")
                                                attack()
                                            else:
                                                print("There was a draw in combat")
                                                attack()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Thunder Hammer":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Lightning Claws":
                                        spacemarine_rolls = [randint(1, 6), randint(1, 6)]
                                        genestealer_rolls = [randint(1, 6), randint(1, 6), randint(1, 6)]

                                        spacemarine_rolls.sort()
                                        genestealer_rolls.sort()

                                        if genestealer_rolls[2] > spacemarine_rolls[1]:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[2] < spacemarine_rolls[1]:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Chainfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Axe":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}
                                        
                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Maul":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print("The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print("The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    else: 
                                        print("You entered an invalid weapon type, please try again.")
                                        attack()
                                    
                                    attack()
                            elif z >= len(genestealers.genestealers):
                                print("There is no foe that you can attack at your current position.")
                                attack()
    else: 
        print("You don't have enough action points and/or command points to complete this action.")
        attack()

def parry(x):
    print("Your terminator's roll was lower than the highest genestealer roll, do you wish to re-roll?(Y/N)")

    choice = input("> ")

    if choice == "Y":
        spacemarine_reroll = randint(1, 6)
        x = spacemarine_reroll
    elif choice == "N":
        print("Did not re-roll.")
    else:
        print("Your response was not valid, please try again.")
        parry(spacemarine_reroll)

def bolter_fire():
