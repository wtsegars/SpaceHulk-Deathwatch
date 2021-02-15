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
                                  squad[j]["current_place"],
                                  squad[j]["direction"],
                                  squad[j]["alive"],
                                  attack_choice)
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
                                  squad[j]["current_place"],
                                  squad[j]["direction"],
                                  squad[j]["alive"],
                                  attack_choice)
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
                                  squad[j]["current_place"],
                                  squad[j]["direction"],
                                  squad[j]["alive"],
                                  attack_choice)
                elif attack_choice == "Chainfist":
                    close_combat()
                elif attack_choice == "Cancel":
                    attack()
                else:
                    print("You entered an invalid command, please try again.")
                    attack()
            elif squad[i]["weapon loadout"] == "Storm Bolter and Power Axe":
                print("Storm Bolter")
                print("Power Axe")
                print("Cancel")

                attack_choice = input("> ")

                if attack_choice == "Storm Bolter":
                    ranged_combat(game.command_points,
                                  squad[j]["action points"],
                                  squad[j]["current_place"],
                                  squad[j]["direction"],
                                  squad[j]["alive"],
                                  attack_choice)
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
                                  squad[j]["current_place"],
                                  squad[j]["direction"],
                                  squad[j]["alive"],
                                  attack_choice,
                                  squad[j]["clip size"])
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
                                  squad[j]["current_place"],
                                  squad[j]["direction"],
                                  squad[j]["alive"],
                                  attack_choice,
                                  squad[j]["clip size"])
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
                                  squad[j]["current_place"],
                                  squad[j]["direction"],
                                  squad[j]["alive"],
                                  attack_choice)
                elif attack_choice == "Cyclone Missile Launcher":
                    ranged_combat(game.command_points,
                                  squad[j]["action points"],
                                  squad[j]["current_place"],
                                  squad[j]["direction"],
                                  squad[j]["alive"],
                                  attack_choice,
                                  squad[j]["clip size"])
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
                                  squad[j]["current_place"],
                                  squad[j]["direction"],
                                  squad[j]["alive"],
                                  attack_choice)
                elif attack_choice == "Power Maul":
                    close_combat()
                elif attack_choice == "Cancel":
                    attack()
                else:
                    print("You entered an invalid command, please try again.")
        elif attack_with == "Cancel":
            game.SpaceMarineTurn.enter.turn_menu()

def ranged_combat(a, b, c, d, e, f, g):
    if a >= 1 or b >= 1:
        if c == "c1":
            if d == "south":
                for x in range(5, -1, -1):
                    if linesight.line_of_sight[0][x] == gametiles.tiles[linesight.line_of_sight[0][x]]:
                        if gametiles.tiles[linesight.line_of_sight[0][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[0][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(a,
                                                    b,
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[0][x]])
                                    elif f == "Assault Cannon":
                                        if squad.g >= 1:
                                            assault_cannon(a,
                                                            b,
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[0][x]],
                                                            e,
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if g >= 1:
                                            heavy_flamer(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[0][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if g>= 1:
                                            cyclone_missle(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[0][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[0][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "east":
                for x in range(0, 8, 1):
                    if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                        if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(a,
                                                    b,
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[1][x]])
                                    elif f == "Assault Cannon":
                                        if g >= 1:
                                            assault_cannon(a,
                                                            b,
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            e,
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if g >= 1:
                                            heavy_flamer(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if g >= 1:
                                            cyclone_missle(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "west":
                for x in range(8, 15, 1):
                    if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                        if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(a,
                                                    b,
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[1][x]])
                                    elif f == "Assault Cannon":
                                        if g >= 1:
                                            assault_cannon(a,
                                                            b,
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            e,
                                                            f)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if g >= 1:
                                            heavy_flamer(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if g >= 1:
                                            cyclone_missle(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                            print(
                                                "You can't fire on your own men.")
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
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(a,
                                                    b,
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[4][x]])
                                    elif f == "Assault Cannon":
                                        if g >= 1:
                                            assault_cannon(a,
                                                            b,
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            e,
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if g >= 1:
                                            heavy_flamer(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if g >= 1:
                                            cyclone_missle(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "east":
                for x in range(2, -1, -1):
                    if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                        if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(a,
                                                    b,
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[1][x]])
                                    elif f == "Assault Cannon":
                                        if g >= 1:
                                            assault_cannon(a,
                                                            b,
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            e,
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if g:
                                            heavy_flamer(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if g:
                                            cyclone_missle(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "west":
                for x in range(2, 15, 1):
                    if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                        if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(a,
                                                    b,
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[1][x]])
                                    elif f == "Assault Cannon":
                                        if g >= 1:
                                            assault_cannon(a,
                                                            b,
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            e,
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if g >= 1:
                                            heavy_flamer(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if g >= 1:
                                            cyclone_missle(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack() 
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
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
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(a,
                                                    b,
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[5][x]])
                                    elif f == "Assault Cannon":
                                        if g >= 1:
                                            assault_cannon(a,
                                                            b,
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[5][x]],
                                                            e,
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if g >= 1:
                                            heavy_flamer(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[5][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if g >= 1:
                                            cyclone_missle(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[5][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                                elif x < 0:
                                    print(
                                        "There is not here for you to fire upon.")
                                    attack()
            elif d == "east":
                for x in range(12, -1, -1):
                    if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                        if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(a,
                                                    b,
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[1][x]])
                                    elif f == "Assault Cannon":
                                        if g >= 1:
                                            assault_cannon(a,
                                                            b,
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            e,
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if g >= 1:
                                            heavy_flamer(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if g >= 1:
                                            cyclone_missle(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "west":
                for x in range(13, 15, 1):
                    if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                        if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(a,
                                                    b,
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[1][x]])
                                    elif f == "Assault Cannon":
                                        if g >= 1:
                                            assault_cannon(a,
                                                            b,
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            e,
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if g >= 1:
                                            heavy_flamer(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if g >= 1:
                                            cyclone_missle(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
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
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(a,
                                                    b,
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[4][x]])
                                    elif f == "Assault Cannon":
                                        if g >= 1:
                                            assault_cannon(a,
                                                            b,
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            e,
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if g >= 1:
                                            heavy_flamer(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if g >= 1:
                                            cyclone_missle(a,
                                                            b,
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                                elif x < 0:
                                    print(
                                        "There is not here for you to fire upon.")
                                    attack()
            elif d == "east":
                for x in range(13, 15, 1):
                    if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                        if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(a,
                                                    b,
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[1][x]])
                                    elif f == "Assault Cannon":
                                        if g >= 1:
                                            assault_cannon(a,
                                                            b,
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            e,
                                                            g)
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "west":
                for x in range(12, -1, -1):
                    if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                        if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[1][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
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
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[2][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[2][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[2][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[2][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "east":
                for x in range(1, 15, 1):
                    if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                        if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[1][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
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
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[2][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[2][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[2][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"]:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[2][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "west":
                for x in range(13, -1, -1):
                    if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                        if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[1][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"]:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[1][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
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
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[4][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f = "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "north":
                for x in range(7, 14, 1):
                    if linesight.line_of_sight[4][x] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                        if gametiles.tiles[linesight.line_of_sight[4][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[4][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "east":
                for x in range(1, 10, 1):
                    if linesight.line_of_sight[6][x] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                        if gametiles.tiles[linesight.line_of_sight[6][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[6][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[6][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[6][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[6][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
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
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[5][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[5][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[5][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"]:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[5][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "north":
                for x in range(7, 14, 1):
                    if linesight.line_of_sight[5][x] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                        if gametiles.tiles[linesight.line_of_sight[5][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[5][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[5][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[5][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[5][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "west":
                for x in range(9, -1, -1):
                    if linesight.line_of_sight[6][x] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                        if gametiles.tiles[linesight.line_of_sight[6][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[6][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[6][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[6][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[6][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
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
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[7][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[7][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[7][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[7][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "north":
                for x in range(3, 5, 1):
                    if linesight.line_of_sight[7][x] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                        if gametiles.tiles[linesight.line_of_sight[7][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[7][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[7][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[7][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"]:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[7][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "east":
                for x in range(6, 10, 1):
                    if linesight.line_of_sight[6][x] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                        if gametiles.tiles[linesight.line_of_sight[6][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[6][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[6][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[6][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[6][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "west":
                for x in range(4, -1, -1):
                    if linesight.line_of_sight[6][x] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                        if gametiles.tiles[linesight.line_of_sight[6][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[6][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[6][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[6][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[6][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
        elif c == "c2":
            if d == "north":
                for x in range(1, 5, 1):
                    if linesight.line_of_sight[7][x] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                        if gametiles.tiles[linesight.line_of_sight[7][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[7][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[7][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[7][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[7][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "east":
                for x in range(3, 5, 1):
                    if linesight.line_of_sight[8][x] == gametiles.tiles[linesight.line_of_sight[8][x]]:
                        if gametiles.tiles[linesight.line_of_sight[8][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[8][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[8][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[8][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[8][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "west":
                for x in range(1, -1, -1):
                    if linesight.line_of_sight[8][x] == gametiles.tiles[linesight.line_of_sight[8][x]]:
                        if gametiles.tiles[linesight.line_of_sight[8][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[8][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[8][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[8][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missle Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[8][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
        elif c == "c6":
            if d == "south":
                for x in range(3, -1, -1):
                    if linesight.line_of_sight[7][x] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                        if gametiles.tiles[linesight.line_of_sight[7][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[7][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[7][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[7][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[7][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "east":
                for x in range(3, 5, 1):
                    if linesight.line_of_sight[9][x] == gametiles.tiles[linesight.line_of_sight[9][x]]:
                        if gametiles.tiles[linesight.line_of_sight[9][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[9][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[9][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[9][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[9][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "west":
                for x in range(2, -1, -1):
                    if linesight.line_of_sight[9][x] == gametiles.tiles[linesight.line_of_sight[9][x]]:
                        if gametiles.tiles[linesight.line_of_sight[9][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[9][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[9][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[9][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[9][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
        elif c == "c7":
            if d == "north":
                for x in range(1, 6, 1):
                    if linesight.line_of_sight[10][x] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                        if gametiles.tiles[linesight.line_of_sight[10][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[10][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[10][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[10][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[10][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "east":
                for x in range(3, 5, 1):
                    if linesight.line_of_sight[11][x] == gametiles.tiles[linesight.line_of_sight[11][x]]:
                        if gametiles.tiles[linesight.line_of_sight[9][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[11][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[11][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[11][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[11][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "west":
                for x in range(1, -1, -1):
                    if linesight.line_of_sight[11][x] == gametiles.tiles[linesight.line_of_sight[11][x]]:
                        if gametiles.tiles[linesight.line_of_sight[9][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[11][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[11][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[11][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[11][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
        elif c == "l13":
            if d == "south":
                for x in range(12, -1, -1):
                    if linesight.line_of_sight[4][x] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                        if gametiles.tiles[linesight.line_of_sight[4][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[4][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                                heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[4][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "east":
                for x in range(1, 11, 1):
                    if linesight.line_of_sight[13][x] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                        if gametiles.tiles[linesight.line_of_sight[13][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[13][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[13][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[13][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[13][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
        elif c == "r13":
            if d == "south":
                for x in range(12, -1, -1):
                    if linesight.line_of_sight[5][x] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                        if gametiles.tiles[linesight.line_of_sight[5][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[5][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[5][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[5][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[5][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "west":
                for x in range(9, -1, -1):
                    if linesight.line_of_sight[13][x] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                        if gametiles.tiles[linesight.line_of_sight[13][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[13][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[13][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[13][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[13][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
        elif c == "c10":
            if d == "south":
                for x in range(2, -1, -1):
                    if linesight.line_of_sight[10][x] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                        if gametiles.tiles[linesight.line_of_sight[10][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[10][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[10][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[10][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[10][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "north":
                for x in range(4, 6, 1):
                    if linesight.line_of_sight[10][x] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                        if gametiles.tiles[linesight.line_of_sight[10][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[10][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[10][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[10][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[10][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "east":
                for x in range(6, 11, 1):
                    if linesight.line_of_sight[13][x] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                        if gametiles.tiles[linesight.line_of_sight[13][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[13][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[13][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[13][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[13][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "west":
                for x in range(4, -1, -1):
                    if linesight.line_of_sight[13][x] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                        if gametiles.tiles[linesight.line_of_sight[13][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[13][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[13][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[13][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[13][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
        elif c == "c12":
            if d == "south":
                for x in range(4, -1, -1):
                    if linesight.line_of_sight[10][x] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                        if gametiles.tiles[linesight.line_of_sight[10][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[10][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[10][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[10][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[10][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "east":
                for x in range(3, 5, 1):
                    if linesight.line_of_sight[12][x] == gametiles.tiles[linesight.line_of_sight[12][x]]:
                        if gametiles.tiles[linesight.line_of_sight[12][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[12][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[12][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[12][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[12][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
            elif d == "west":
                for x in range(1, -1, -1):
                    if linesight.line_of_sight[12][x] == gametiles.tiles[linesight.line_of_sight[12][x]]:
                        if gametiles.tiles[linesight.line_of_sight[12][x]]["occupied"] == True:
                            for y in genestealers.genestealers:
                                if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][x]]:
                                    if f == "Storm Bolter":
                                        bolter_fire(game.command_points,
                                                    squad[j]["action points"],
                                                    genestealers.genestealers[y]["alive"],
                                                    gametiles.tiles[linesight.line_of_sight[12][x]])
                                    elif f == "Assault Cannon":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            assault_cannon(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers[y]["alive"],
                                                            gametiles.tiles[linesight.line_of_sight[12][x]],
                                                            squad[j]["alive"],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Heavy Flamer":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            heavy_flamer(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[12][x]],
                                                            squad[j]["clip_size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                    elif f == "Cyclone Missile Launcher":
                                        if squad.squad[j]["clip_size"] >= 1:
                                            cyclone_missle(game.command_points,
                                                            squad[j]["action points"],
                                                            genestealers.genestealers,
                                                            gametiles.tiles[linesight.line_of_sight[12][x]],
                                                            squad[j]["clip-size"])
                                        else:
                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                            attack()
                                elif y == len(genestealers.genestealers):
                                    for z in squad.squad:
                                        if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][x]]:
                                            print(
                                                "You can't fire on your own men.")
                                            attack()
                                        elif z == len(squad.squad):
                                            print(
                                                "There is nothing here for you to fire upon.")
                                            attack()
                        elif x < 0:
                            print("There is not here for you to fire upon.")
                            attack()
        else:
            for x in linesight.line_of_sight:
                for y in linesight.line_of_sight[x]:
                    if linesight.line_of_sight[x][y] == c:
                        o = 1
                        n = -1
                        if linesight.line_of_sight[x] == "starting hall":
                            if d == "south":
                                for z in range(y + 1, 6, o):
                                    if linesight.line_of_sight[0][z] == gametiles.tiles[linesight.line_of_sight[0][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[0][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[0][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[0][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[0][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[0][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[0][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[0][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            elif d == "north":
                                for z in range(y + 1, -1, n):
                                    if linesight.line_of_sight[0][z] == gametiles.tiles[linesight.line_of_sight[0][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[0][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[0][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[0][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[0][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[0][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[0][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[0][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            else:
                                print("You cannot fire in this direction.")
                                attack()
                        elif linesight.line_of_sight[x] == "lower hall":
                            if d == "east":
                                for z in range(y + 1, 15, o):
                                    if linesight.line_of_sight[1][z] == gametiles.tiles[linesight.line_of_sight[1][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[1][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[1][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[1][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[1][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[1][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            elif d == "west":
                                for z in range(y + 1, -1, n):
                                    if linesight.line_of_sight[1][z] == gametiles.tiles[linesight.line_of_sight[1][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[1][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[1][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[1][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[1][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[1][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            else:
                                print("You cannot fire in this direction.")
                                attack()
                        elif linesight.line_of_sight[x] == "lower left genestealer entrance":
                            if d == "north":
                                for z in range(y + 1, 3, o):
                                    if linesight.line_of_sight[2][z] == gametiles.tiles[linesight.line_of_sight[2][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[2][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[2][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[2][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[2][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[2][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            elif d == "south":
                                for z in range(y + 1, -1, n):
                                    if linesight.line_of_sight[2][z] == gametiles.tiles[linesight.line_of_sight[2][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[2][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[2][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[2][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[2][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[2][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            else:
                                print("You cannot fire in this direction.")
                                attack()
                        elif linesight.line_of_sight[x] == "lower right genestealer entrance":
                            if d == "north":
                                for z in range(y + 1, 3, o):
                                    if linesight.line_of_sight[3][z] == gametiles.tiles[linesight.line_of_sight[3][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[3][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[3][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[3][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[3][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[3][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[3][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[3][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            elif d == "south":
                                for z in range(y + 1, -1, n):
                                    if linesight.line_of_sight[3][z] == gametiles.tiles[linesight.line_of_sight[3][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[3][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[3][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[3][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[3][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[3][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[3][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[3][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            else:
                                print("You cannot fire in this direction.")
                                attack()
                        elif linesight.line_of_sight[x] == "left hallway":
                            if d == "north":
                                for z in range(y + 1, 14, o):
                                    if linesight.line_of_sight[4][z] == gametiles.tiles[linesight.line_of_sight[4][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[4][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[4][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[4][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[4][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[4][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            elif d == "south":
                                for z in range(y + 1, -1, -1):
                                    if linesight.line_of_sight[4][z] == gametiles.tiles[linesight.line_of_sight[4][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[4][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[4][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[4][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[4][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[4][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            else:
                                print("You cannot fire in this direction.")
                                attack()
                        elif linesight.line_of_sight[x] == "right hallway":
                            if d == "north":
                                for z in range(y + 1, 14, o):
                                    if linesight.line_of_sight[5][z] == gametiles.tiles[linesight.line_of_sight[5][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[5][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[5][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[5][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[5][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[5][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            elif d == "south":
                                for z in range(y + 1, -1, n):
                                    if linesight.line_of_sight[5][z] == gametiles.tiles[linesight.line_of_sight[5][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[5][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[5][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[5][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[5][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[5][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            else:
                                print("You cannot fire in this direction.")
                                attack()
                        elif linesight.line_of_sight[x] == "center hall":
                            if d == "east":
                                for z in range(y + 1, 11, o):
                                    if linesight.line_of_sight[6][z] == gametiles.tiles[linesight.line_of_sight[6][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[6][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[6][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[6][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[6][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[6][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            elif d == "west":
                                for z in range(y + 1, -1, n):
                                    if linesight.line_of_sight[6][z] == gametiles.tiles[linesight.line_of_sight[6][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[6][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[6][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[6][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[6][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[6][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            else:
                                print("You cannot fire in this direction.")
                                attack()
                        elif linesight.line_of_sight[x] == "lower middle hall":
                            if d == "north":
                                for z in range(y + 1, 5, o):
                                    if linesight.line_of_sight[7][z] == gametiles.tiles[linesight.line_of_sight[7][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[7][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[7][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[7][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[7][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[7][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            elif d == "south":
                                for z in range(y + 1, -1, n):
                                    if linesight.line_of_sight[7][z] == gametiles.tiles[linesight.line_of_sight[7][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[7][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[7][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[7][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[7][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[7][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            else:
                                print("You cannot fire in this direction.")
                                attack()
                        elif linesight.line_of_sight[x] == "lower middle genestealer entrance":
                            if d == "east":
                                for z in range(y + 1, 5, o):
                                    if linesight.line_of_sight[8][z] == gametiles.tiles[linesight.line_of_sight[8][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[8][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[8][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[8][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[8][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[8][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            elif d == "west":
                                for z in range(y + 1, -1, n):
                                    for z in range(y + 1, 5, o):
                                    if linesight.line_of_sight[8][z] == gametiles.tiles[linesight.line_of_sight[8][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[8][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[8][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[8][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[8][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[8][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            else:
                                print("You cannot fire in this direction.")
                                attack()
                        elif linesight.line_of_sight[x] == "upper middle genestealer entrance":
                            if d == "east":
                                for z in range(y + 1, 5, o):
                                    if linesight.line_of_sight[9][z] == gametiles.tiles[linesight.line_of_sight[9][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[9][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[9][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[9][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[9][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[9][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            elif d == "west":
                                for z in range(y + 1, -1, n):
                                    if linesight.line_of_sight[9][z] == gametiles.tiles[linesight.line_of_sight[9][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[9][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[9][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[9][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[9][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[9][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            else:
                                print("You cannot fire in this direction.")
                                attack()
                        elif linesight.line_of_sight[x] == "upper middle hall":
                            if d == "north":
                                for z in range(y + 1, 6, o):
                                    if linesight.line_of_sight[10][z] == gametiles.tiles[linesight.line_of_sight[10][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[10][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[10][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[10][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[10][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[10][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            elif d == "south":
                                for z in range(y + 1, -1, n):
                                    if linesight.line_of_sight[10][z] == gametiles.tiles[linesight.line_of_sight[10][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[10][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[10][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[10][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[10][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[10][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            else:
                                print("You cannot fire in this direction.")
                                attack()
                        elif linesight.line_of_sight[x] == "lower top genestealer entrance":
                            if d == "east":
                                for z in range(y + 1, 5, o):
                                    if linesight.line_of_sight[11][z] == gametiles.tiles[linesight.line_of_sight[11][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[11][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[11][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[11][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[11][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[11][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            elif d == "west":
                                for z in range(y + 1, -1, n):
                                    if linesight.line_of_sight[11][z] == gametiles.tiles[linesight.line_of_sight[11][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[11][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[11][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[11][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[11][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[11][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            else:
                                print("You cannot fire in this direction.")
                                attack()
                        elif linesight.line_of_sight[x] == "upper top genestealer entrance":
                            if d == "east":
                                for z in range(y + 1, 5, o):
                                    if linesight.line_of_sight[12][z] == gametiles.tiles[linesight.line_of_sight[12][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[12][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[12][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[12][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[12][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[12][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            elif d == "west":
                                for z in range(y + 1, -1, n):
                                    if linesight.line_of_sight[12][z] == gametiles.tiles[linesight.line_of_sight[12][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[12][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[12][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[12][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[12][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[12][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            else:
                                print("You cannot fire in this direction.")
                                attack()
                        elif linesight.line_of_sight[x] == "upper hall":
                            if d == "east":
                                for z in range(y + 1, 11, o):
                                    if linesight.line_of_sight[13][z] == gametiles.tiles[linesight.line_of_sight[13][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[13][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[13][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[13][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[13][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[13][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            elif d == "west":
                                for z in range(y + 1, -1, n):
                                    if linesight.line_of_sight[13][z] == gametiles.tiles[linesight.line_of_sight[13][z]]:
                                        if gametiles.tiles[linesight.line_of_sight[13][z]]["occupied"] == True:
                                            for g in genestealers.genestealers:
                                                if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][z]]:
                                                    if f == "Storm Bolter":
                                                        bolter_fire(game.command_points,
                                                                    squad[j]["action points"],
                                                                    genestealers.genestealers[g]["alive"],
                                                                    gametiles.tiles[linesight.line_of_sight[13][z]])
                                                    elif f == "Assault Cannon":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            assault_cannon(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[13][z]],
                                                                            squad[j]["alive"],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Heavy Flamer":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            heavy_flamer(game.command_points,
                                                                        squad[j]["action points"],
                                                                        genestealers.genestealers,
                                                                        gametiles.tiles[linesight.line_of_sight[13][z]],
                                                                        squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                    elif f == "Cyclone Missile Launcher":
                                                        if squad.squad[j]["clip_size"] >= 1:
                                                            cyclone_missle(game.command_points,
                                                                            squad[j]["action points"],
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[13][z]],
                                                                            squad[j]["clip_size"])
                                                        else:
                                                            print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                            attack()
                                                elif g == len(genestealers.genestealers):
                                                    for h in squad.squad:
                                                        if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][z]]:
                                                            print(
                                                                "You can't fire on your own men.")
                                                            attack()
                            else:
                                print("You cannot fire in this direction.")
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
                            if genestealers.genestealers[z]["current_place"] == gametiles.tiles[y]:
                                if genestealers.genestealers[z]["direction"] == "north" and d == "south":
                                    if f == "Powerfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Sword":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            parry(spacemarine_roll)

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print(
                                                    "The attacking terminator has perished in combat.")
                                                game.SpaceMarineTurn.enter.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                attack()
                                            else:
                                                print(
                                                    "There was a draw in combat")
                                                attack()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Thunder Hammer":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Lightning Claws":
                                        spacemarine_rolls = [
                                            randint(1, 6), randint(1, 6)]
                                        genestealer_rolls = [
                                            randint(1, 6), randint(1, 6), randint(1, 6)]

                                        spacemarine_rolls.sort()
                                        genestealer_rolls.sort()

                                        if genestealer_rolls[2] > spacemarine_rolls[1]:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[2] < spacemarine_rolls[1]:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Chainfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Axe":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Maul":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    else:
                                        print(
                                            "You entered an invalid weapon type, please try again.")
                                        attack()

                                    attack()
                                elif genestealers.genestealers[z]["direction"] == "south" and d == "north":
                                    if f == "Powerfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Sword":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            parry(spacemarine_roll)

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print(
                                                    "The attacking terminator has perished in combat.")
                                                game.SpaceMarineTurn.enter.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                attack()
                                            else:
                                                print(
                                                    "There was a draw in combat")
                                                attack()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Thunder Hammer":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Lightning Claws":
                                        spacemarine_rolls = [
                                            randint(1, 6), randint(1, 6)]
                                        genestealer_rolls = [
                                            randint(1, 6), randint(1, 6), randint(1, 6)]

                                        spacemarine_rolls.sort()
                                        genestealer_rolls.sort()

                                        if genestealer_rolls[2] > spacemarine_rolls[1]:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[2] < spacemarine_rolls[1]:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Chainfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Axe":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Maul":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    else:
                                        print(
                                            "You entered an invalid weapon type, please try again.")
                                        attack()

                                    attack()
                                elif genestealers.genestealers[z]["direction"] == "east" and d == "west":
                                    if f == "Powerfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Sword":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            parry(spacemarine_roll)

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print(
                                                    "The attacking terminator has perished in combat.")
                                                game.SpaceMarineTurn.enter.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                attack()
                                            else:
                                                print(
                                                    "There was a draw in combat")
                                                attack()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Thunder Hammer":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Lightning Claws":
                                        spacemarine_rolls = [
                                            randint(1, 6), randint(1, 6)]
                                        genestealer_rolls = [
                                            randint(1, 6), randint(1, 6), randint(1, 6)]

                                        spacemarine_rolls.sort()
                                        genestealer_rolls.sort()

                                        if genestealer_rolls[2] > spacemarine_rolls[1]:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[2] < spacemarine_rolls[1]:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Chainfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Axe":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Maul":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    else:
                                        print(
                                            "You entered an invalid weapon type, please try again.")
                                        attack()

                                    attack()
                                elif genestealers.genestealers[z]["direction"] == "west" and d == "east":
                                    if f == "Powerfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Sword":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            parry(spacemarine_roll)

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print(
                                                    "The attacking terminator has perished in combat.")
                                                game.SpaceMarineTurn.enter.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                attack()
                                            else:
                                                print(
                                                    "There was a draw in combat")
                                                attack()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Thunder Hammer":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Lightning Claws":
                                        spacemarine_rolls = [
                                            randint(1, 6), randint(1, 6)]
                                        genestealer_rolls = [
                                            randint(1, 6), randint(1, 6), randint(1, 6)]

                                        spacemarine_rolls.sort()
                                        genestealer_rolls.sort()

                                        if genestealer_rolls[2] > spacemarine_rolls[1]:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[2] < spacemarine_rolls[1]:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Chainfist":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Axe":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    elif f == "Power Maul":
                                        spacemarine_roll = randint(1, 6)
                                        genestealer_rolls = {
                                            randint(1, 6), randint(1, 6), randint(1, 6)}

                                        if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                            e = False
                                            gametiles.tiles["occupied"] = False
                                            print(
                                                "The attacking terminator has perished in combat.")
                                            game.SpaceMarineTurn.enter.turn_menu()
                                        elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                            genestealers.genestealers[z]["alive"] == False
                                            gametiles.tiles[y]["occupied"] == False
                                            print(
                                                "The attacking terminator has sucessfully slain the xenos filth.")
                                            attack()
                                        else:
                                            print("There was a draw in combat")
                                            attack()
                                    else:
                                        print(
                                            "You entered an invalid weapon type, please try again.")
                                        attack()

                                    attack()
                            elif z >= len(genestealers.genestealers):
                                print(
                                    "There is no foe that you can attack at your current_place.")
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

def bolter_fire(a, b, c, d):
    bolt_shot_1 = randint(1, 6)
    bolt_shot_2 = randint(1, 6)

    if b >= 1:
        b -= 1
    elif b < 1 and a >= 1:
        a -= 1

    if bolt_shot_1 >= 5 or bolt_shot_2 >= 5:
        c = False
        d = False
        print("The xenos menace has been slain by bolter fire.")
        attack()
    else:
        print("Your shot missed its target.")
        attack()

def assault_cannon(a, b, c, d, e, f):
    assault_shot_1 = randint(1, 6)
    assault_shot_2 = randint(1, 6)
    assault_shot_3 = randint(1, 6)

    if b >= 1:
        b -= 1
        f -= 1
    elif b < 1 and a >= 1:
        a -= 1
        f -= 1

    if assault_shot_1 >= 5 or assault_shot_2 >= 5 or assault_shot_3 >= 5:
        c = False
        d = False
        print("The xenos menace has been slain by assault cannon fire.")
        attack()
    elif assault_shot_1 == assault_shot_2 and assault_shot_2 == assault_shot_3:
        e = False
        print("The terminator's assault cannon malfunctioned resulting in instant death.")
        attack()
    else:
        print("The assault cannon volly missed its target.")
        attack()

def heavy_flamer(a, b, c, d, e):
    if b >= 1:
        b -= 1
        e -= 1
    elif b < 1 and a >= 1:
        a -= 1
        e -= 1

    fire_shot = randint(1, 6)

    if d["occupied"] == True:
        for h in c:
            if c[h]["current_place"] == d:
                if fire_shot >= 2:
                    c[h]["alive"] = False
                    d["on fire"] = True
                    print("The flamer shot hit a target.")
                else:
                    d["on fire"] = True
                    print("The flamer shot didn't hit anything.")
        
        for i in squad.squad:
            if squad.squad[i]["current_place"] == d:
                if fire_shot >= 2:
                    squad.squad[i]["alive"] = False
                    d["on fire"] = True
                    print("The flamer shot hit some of your own men.")
                else:
                    d["on fire"] = True
                    print("The flamer shot didn't hit anything.")
    else:
        d["on fire"] = True
        print("The flamer shot didn't hit anything.")

    for g in d["connected to"]:
        flamer_shot = randint(1, 6)

        if d[d[g]["connected to"]]["occupied"] == True:
            for h in c:
                if c[h]["current_place"] == d[d[g]["connected to"]]:
                    if flamer_shot >= 2:
                        c[h]["alive"] = False
                        d[d[g]["connected to"]]["on fire"] = True
                        print("The flamer shot hit a target.")
                    else:
                        d[d[g]["connected to"]]["on fire"] = True
                        print("The flamer shot didn't hit anything.")

            for i in squad.squad:
                if squad.squad[i]["current_place"] == d[d[g]["connected to"]]:
                    if flamer_shot >= 2:
                        squad.squad[i]["alive"] = False
                        d[d[g]["connected to"]]["on fire"] = True
                        print("The flamer shot hit some of your own men.")
                    else:
                        d[d[g]["connected to"]]["on fire"] = True
                        print("The flamer shot missed some of your own men.")
    
    attack()

def cyclone_missle(a, b, c, d, e):
    if b >= 1:
        b -= 1
        e -= 1
    elif b < 1 and a >= 1:
        a -= 1
        e -= 1

    cyclone_blast = randint(1, 6)

    if d["occupied"] == True:
        for h in c:
            if c[h]["current_place"] == d:
                if cyclone_blast >= 3:
                    c[h]["alive"] = False
                    d["occupied"] = False
                    print("The cyclone missle made a kill.")
                else:
                    print("The cyclone missle missed its target.")
        
        for i in squad.squad:
            if squad.squad[i]["current_place"] == d:
                if cyclone_blast >= 3:
                    squad.squad[i]["alive"] = False
                    d["occupied"] = False
                    print("The cyclone missle hit some of your own men.")
                else:
                    print("The cyclone missle missed some of your men.")
    else:
        print("The cyclone missle did not hit anything.")

    for g in d["connected to"]:
        cyclone_shot = randint(1, 6)

        if d[d[g]["connected to"]]["occupied"]:
            for h in c:
                if c[h]["current_place"] == d[d[g]["connected to"]]:
                    if cyclone_shot >= 3:
                        c[h]["alive"] = False
                        d[d[g]["connected to"]]["occupied"] = False
                        print("The cyclone missle blast hit a target")
                    else:
                        print("The cyclone missle blast missed a target")

            for i in squad.squad:
                if squad.squad[i]["current_place"] == d[d[g]["connected to"]]:
                    if cyclone_shot >= 3:
                        squad.squad[i]["alive"] = False
                        d[d[g]["connected to"]]["occupied"] = False
                        print("The cyclone missle blast hit some of your own men.")
                    else:
                        print("The cyclone missle blast missed some of your men.")

    attack()