from sys import exit
from random import randint
from textwrap import dedent
import chapters
import squad
import weapons
import gametiles
import genestealers
import miscaction
import gamemap
import radarblips
import genestealermove
import linesight

turn_count = 0
        
class Openingscene():
    def enter(self):
        print(dedent("""
                Welcome to Space Hulk Deathwatch, a console-based game that
                is based on the classic Games Workshop game, Space Hulk. This, 
                along with many other games that are created by Game Workshop,
                is based in the Warhammer 40,000 universe.
                (press enter to continue)
                """))
        
        input('')

        print(dedent("""
                This game is set inside of a space hulk (hence the name), which
                is a floating mass of ships that have been fused together while
                being lost in the warp. Sometimes these space hulks will appear
                in realspace and, from time to time, the superhuman Adeptus 
                Astartes (space marines) will send a squad or two into these
                space hulks to cleanse them of alien life, find lost relics and
                technologies from the past, or any number of other reasons.
                (press enter to continue)
                """))

        input('')

        print(dedent("""
                The Deathwatch are an elite chaper of the space marines that are
                made up from veteran marines from various chapers from all across
                the Imperium of Man. The Deathwatch acts as the chamber militant 
                (military branch) for the Ordo Xenos branch of the Inquisition (
                secret police that help keep the Imperium stable). Your goal is 
                to try and get your squad out of the space hulk before they are 
                overrun by genestealers (a form of Tyranid that are commonly found
                on board of space hulks).
                (press enter to continue)
                """))
        
        input('')

        return SquadSelect().enter()

class SquadSelect():
    heavy_count = 0

    def enter(self):
        print(dedent("""
                Below is where you can select your squad of five marines from a 
                pre-selected list of chapters. The first marine you select will
                be the squad's sergent while the rest are standard marines. Choose
                wisely because some chapters will have advantages over others.
                (press enter to continue)
                """))

        input('')

        # SquadSelect.chapter_select()
        # SquadSelect.weapon_select()
        # Squadplacement.enter(self)
        SpaceMarineTurn.enter(turn_count)

    def chapter_select():
        
        for x in chapters.chapters:
            print(x)

        for y in squad.squad:
            if squad.squad[y]["chapter"] == None:
                print()
                print(y)
                print()
                print("Select the chapter for this terminator:")
            
                ch_input = input("> ")

                for z in chapters.chapters:
                    if z == ch_input:
                        squad.squad[y]["chapter"] = ch_input
                        break

                if squad.squad[y]["chapter"] == None:
                    print("The chapter you selected is invalid, please select a valid chapter.")
                    SquadSelect.chapter_select()
            else:
                continue             
        
    def weapon_select():

        for x in weapons.weapon_loadout:
            print(x)

        for y in squad.squad:
            if squad.squad[y]["weapon loadout"] == None:
                print()
                print(y)
                print()
                print("Choose the weapon loadout:")

                for z in weapons.weapon_loadout:
                    print(z)
            
                wpn_input = input("> ")

                for x in weapons.weapon_loadout:
                    if x == wpn_input:
                        if wpn_input == weapons.weapon_loadout[6] or wpn_input == weapons.weapon_loadout[7] or wpn_input == weapons.weapon_loadout[8]:
                            if SquadSelect.heavy_count >= 3:
                                print("You have exceeded the maximum amount of heavy weapons for this squad, another loadout needs to be selected.")
                                SquadSelect.weapon_select()
                            else:
                                SquadSelect.heavy_count += 1
                                squad.squad[y]["weapon loadout"] = wpn_input
                                break
                        else:
                            squad.squad[y]["weapon loadout"] = wpn_input
                            break
            
                if squad.squad[y]["weapon loadout"] == None:
                    print("An invalid weapon loadout was selected, please select another.")
                    SquadSelect.weapon_select()
            else:
                continue

class Squadplacement():
    order = ["first", "second", "third", "fourth", "fifth"]

    def enter(self):
        print("Select the order in which your squad is to be deployed:")
        print("(press enter to continue)")
        input('')
        Squadplacement.placement()

    def placement():
        while len(Squadplacement.order) != 0:
            for x in squad.squad:
                if squad.squad[x]["current_place"] == None:
                    for y in Squadplacement.order:
                        print(y)

                    print()
                    print(x)
                    place_input = input("> ")

                    for z in Squadplacement.order:
                        if place_input == z:
                            Squadplacement.place_loop(squad.squad[x], place_input)
                            break

                    print(squad.squad[x]["current_place"])
                    if squad.squad[x]["current_place"] == None:
                        print()
                        print("Your position choice is invalid, please reenter a valid position.")
                        print()
                        break
                else:
                    continue
                        
    def place_loop(term, start_place):
        if start_place == "first":
            term["current_place"] = "s5"
            term["direction"] = "north"
            Squadplacement.order.remove("first")
        elif start_place == "second":
            term["current_place"] = "s4"
            term["direction"] = "north"
            Squadplacement.order.remove("second")
        elif start_place == "third":
            term["current_place"] = "s3"
            term["direction"] = "north"
            Squadplacement.order.remove("third")
        elif start_place == "fourth":
            term["current_place"] = "s4"
            term["direction"] = "north"
            Squadplacement.order.remove("fourth")
        else:
            term["current_place"] = "s1"
            term["direction"] = "north"
            Squadplacement.order.remove("fifth")

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
            MoveAction.move(SpaceMarineTurn.command_points)
        elif menu_choice == "Attack":
            Attack.attack()
        elif menu_choice == "Other Action":
            miscaction.OtherActions.other_action()
        elif menu_choice == "View Map":
            gamemap.map()
        elif menu_choice == "End Turn":
            SpaceMarineTurn.win_cond()
            return GenestealerTurn.enter(turn_count)
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
                new_game = Openingscene()
                new_game.enter()
            elif try_again == "N" or try_again == "n":
                exit
            else:
                print("Invalid input, please try again.")
                SpaceMarineTurn.lose_cond()

class GenestealerTurn():
    blips_to_deploy = 0

    def enter(turn_count):
        print("Genestealers are now moving.")
        print("(press enter to continue)")
        input('')
        turn_count += 1
        GenestealerTurn.blip_count()
        radarblips.RadarBlips.blip_deployment(GenestealerTurn.blips_to_deploy)
        genestealermove.GenestealerMove.genestealer_movement()

    def blip_count():
        if turn_count <= 2:
            GenestealerTurn.blips_to_deploy += 3
        elif 2 < turn_count <= 4:
            GenestealerTurn.blips_to_deploy += 2
        elif turn_count > 5:
            GenestealerTurn.blips_to_deploy += 1

    def end_turn():
        print("End of Genestealer turn.")
        print("(press enter to continue)")
        input('')
        return SpaceMarineTurn.enter(turn_count)

class MoveAction():
    motion_1 = ["Forwards", "Backwards","Turn Left", "Turn Right"]
    motion_2 = ["Forwards", "Turn Left", "Turn Right"]
    movement = 0

    def move(command_pts):
        print("Which terminator would you like to move?")

        for i in squad.squad:
            if squad.squad[i]["action points"] > 0 and squad.squad[i]["alive"] == True:
                print(i)

        movement = input("> ")

        for j in squad.squad:
            #print(j)
            if movement == j:
                print("How would you like to move?")
                print()
                print(dedent("""
                                Forwards,
                                Backwards,
                                Turn Left,
                                Turn Right,
                                Move Another Terminator,
                                Choose Another Action
                                """))

                move_option = input("> ")

                if squad.squad[j]["action points"] >= 2:

                    if move_option == "Forwards":
                        MoveAction.forwards(command_pts,
                                squad.squad[j]["action points"],
                                squad.squad[j]["current_place"],
                                squad.squad[j]["direction"])
                    elif move_option == "Backwards":
                        MoveAction.backwards(command_pts,
                                squad.squad[j]["action points"],
                                squad.squad[j]["current_place"],
                                squad.squad[j]["direction"])
                    elif move_option == "Turn Left":
                        MoveAction.turn_left(command_pts,
                                squad.squad[j]["action points"],
                                squad.squad[j]["direction"])
                    elif move_option == "Turn Right":
                        MoveAction.turn_right(command_pts,
                                squad.squad[j]["action points"],
                                squad.squad[j]["direction"])
                    elif move_option == "Move Another Terminator":
                        MoveAction.move_other_term(command_pts)
                    elif move_option == "Choose Another Action":
                        MoveAction.choose_other_action()
                    else:
                        print("Input was invalid. Please try again.")
                        MoveAction.move(SpaceMarineTurn.command_points)

                elif squad[j]["action points"] < 2:
                    print(dedent("""
                                Forwards,
                                Turn Left,
                                Turn Right,
                                Move Another Terminator,
                                Choose Another Action
                                """))

                    if move_option == "Forwards":
                        MoveAction.forwards(command_pts,
                                squad.squad[j]["action points"],
                                squad.squad[j]["current_place"],
                                squad.squad[j]["direction"])
                    elif move_option == "Turn Left":
                        MoveAction.turn_left(command_pts,
                                squad[j]["action points"],
                                squad[j]["direction"])
                    elif move_option == "Turn Right":
                        MoveAction.turn_right(command_pts,
                                squad[j]["action points"],
                                squad[j]["direction"])
                    elif move_option == "Move Another Terminator":
                        MoveAction.move_other_term(command_pts)
                    elif move_option == "Choose Another Action":
                        MoveAction.choose_other_action()
                else:
                    print("Input was invalid. Please try again.")
                    MoveAction.move(SpaceMarineTurn.command_points)

    def forwards(w, x, y, z):
        print("How far would you like to move forward?")

        forward_move = int(input('> '))

        if forward_move <= w + x:
            MoveAction.movement += forward_move

            for a in range(MoveAction.movement):
                if a != 0:
                    if z == "north":
                        for b in gametiles.tiles:
                            for c in gametiles.tiles[b]["connected to"]:
                                direction_find = gametiles.tiles[b]["connected to"].get(c)
                                print(direction_find)
                                if direction_find == "south":
                                    if gametiles.tiles[b]["occupied"] == True:
                                        print("You are unable to move to this spot.")
                                        MoveAction.move(w)
                                    else:
                                        if x < 1 and w > 1:
                                            w -= 1
                                        elif x >= 1:
                                            x -= 1
                                        else:
                                            print("You don't have enough action point and/or command points to do this action.")
                                            MoveAction.move(w)

                                        gametiles.tiles[y]["occupied"] = False
                                        gametiles.tiles[b]["occupied"] = True

                                        y = gametiles[b]
                                else:
                                    print("You are unable to move in this direction")
                                    MoveAction.move(w)
                    elif z == "south":
                        for b in gametiles.tiles:
                            for c in gametiles.tiles[b]["connected to"]:
                                direction_find = gametiles.tiles[b]["connected to"].get(c)
                                print(direction_find)
                                if direction_find == "north":
                                    if gametiles.tiles[b]["occupied"] == True:
                                        print("You are unable to move to this spot.")
                                        MoveAction.move(w)
                                    else:
                                        if x < 1 and w >= 1:
                                            w -= 1
                                        elif x >= 1:
                                            x -= 1
                                        else:
                                            print("You don't have enough action point and/or command points to do this action.")
                                            MoveAction.move(w)

                                        gametiles.tiles[y]["occupied"] = False
                                        gametiles.tiles[b]["occupied"] = True

                                        y = gametiles[b]
                                else:
                                    print("You are unable to move in this direction.")
                                    MoveAction.move(w)
                    elif z == "west":
                        for b in gametiles.tiles:
                            for c in gametiles.tiles[b]["connected to"]:
                                direction_find = gametiles.tiles[b]["connected to"].get(c)
                                print(direction_find)
                                if direction_find == "east":
                                    if gametiles.tiles[b]["occupied"] == True:
                                        print("You are unable to move to this spot.")
                                        MoveAction.move(w)
                                    else:
                                        if x < 1 and w > 1:
                                            w -= 1
                                        elif x >= 1:
                                            x -= 1
                                        else:
                                            print("You don't have enough action point and/or command points to do this action.")
                                            MoveAction.move(w)

                                        gametiles.tiles[y]["occupied"] = False
                                        gametiles.tiles[b]["occupied"] = True

                                        y = gametiles[b]
                                else:
                                    print("You are unable to move in this direction.")
                                    MoveAction.move(w)
                    elif z == "east":
                        for b in gametiles.tiles:
                            for c in gametiles.tiles[b]["connected to"]:
                                direction_find = gametiles.tiles[b]["connected to"]
                                if direction_find == "west":
                                    if gametiles.tiles[b]["occupied"] == True:
                                        print("you are unable to move to this spot.")
                                        MoveAction.move(w)
                                    else:
                                        if x < 1 and w > 1:
                                            w -= 1
                                        elif x >= 1:
                                            x -= 1
                                        else:
                                            print("You don't have enough action point and/or command points to do this action.")
                                            MoveAction.move(w)

                                        gametiles.tiles[y]["occupied"] = False
                                        gametiles.tiles[b]["occupied"] = True

                                        y = gametiles[b]
                                else:
                                    print("You are unable to move in this direction.")
                                    MoveAction.move(w)
            
            MoveAction.move(w)

        elif forward_move > w + x:
            print("You do not have enough action points to move this far.")
            MoveAction.move(w)

    def backwards(w, x, y, z):
        print(z)
        print("How far do you want to move backwards?")

        backwards_move = int(input('> '))
        #movement = 0

        if backwards_move <= w + x:
            MoveAction.movement += backwards_move

            for a in range(MoveAction.movement):
                #print(a)
                if a != 0:
                    if z == "north":
                        for b in gametiles.tiles:
                            for c in gametiles.tiles[b]["connected to"]:
                                direction_find = gametiles.tiles[b]["connected to"].get(c)
                                print(direction_find)
                                if direction_find == "south":
                                    if y["occupied"] == True:
                                        print("You are unable to move to this spot.")
                                        MoveAction.move(w)
                                    else:
                                        if x < 2 and w >= 2:
                                            w -= 2
                                        elif x >= 2:
                                            x -= 2
                                        else:
                                            print("You don't have enough action point and/or command points to do this action.")
                                            MoveAction.move(w)

                                        gametiles.tiles[y]["occupied"] = False
                                        gametiles.tiles[b]["occupied"] = True

                                        y = gametiles[b]
                                else:
                                    print("You are unable to move in this direction.")
                                    MoveAction.move(w)  
                    elif z == "south":
                        for b in gametiles.tiles:
                            for c in gametiles.tiles[b]["connected to"]:
                                direction_find = gametiles.tiles[b]["connected to"].get(c)
                                if direction_find == "north":
                                    if gametiles.tiles[b]["occupied"] == True:
                                        print("You are unable to move to this spot")
                                        MoveAction.move(w)
                                    else:
                                        if x < 2 and w >= 2:
                                            w -= 2
                                        elif x >= 2:
                                            x -=2
                                        else:
                                            print("You don't have enough action points and/or command points to do this action.")
                                            MoveAction.move(w)

                                        gametiles.tiles[y]["occupied"] = False
                                        gametiles.tiles[b]["occupied"] = True 

                                        y = gametiles[b]
                                else:
                                    print("You are unable to move in this direction.")
                                    MoveAction.move(w)
                    elif z == "east":
                            for b in gametiles.tiles:
                                for c in gametiles.tiles[b]["connected to"]:
                                    direction_find = gametiles.tiles[b]["connected to"].get(c)
                                    if direction_find == "west":
                                        if gametiles.tiles[b]["occupied"] == True:
                                            print("You are unable to move to this spot.")
                                            MoveAction.move(w)
                                        else:
                                            if x < 2 and w >= 2:
                                                w -= 2
                                            elif x >= 2:
                                                x -= 2
                                            else:
                                                print("You don't have enough action points and/or command points to do this action.")
                                                MoveAction.move(w)

                                            gametiles.tiles[y]["occupied"] = False
                                            gametiles.tiles[b]["occupied"] = True

                                            y = gametiles[b]
                                    else:
                                        print("You are unable to move in this direction.")
                                        MoveAction.move(w)
                    elif z == "west":
                        for b in gametiles.tiles:
                            for c in gametiles.tiles[b]["connected to"]:
                                direction_find = gametiles.tiles[b]["connected to"].get(c)
                                if direction_find == "west":
                                    if gametiles.tiles[b]["occupied"] == True:
                                        print("You are unable to move to this spot.")
                                        MoveAction.move(w)
                                    else:
                                        if x < 2 and w >= 2:
                                            w -= 2
                                        elif x >= 2:
                                            x -= 2
                                        else:
                                            print("You don't have enough action points and/or command points to do this action.")
                                            MoveAction.move()

                                        gametiles.tiles[y]["occupied"] = False
                                        gametiles.tiles[b]["occupied"] = True

                                        y = gametiles[MoveAction.backwards]
                                else:
                                    print("You are unable to move in this direction.")
                                    MoveAction.move(w)

            MoveAction.move(w)

        elif backwards_move > w + x:
            print("You do not have enough action points to move this far.")
            MoveAction.move(w)

    def turn_left(x, y, z):
        #print(z)
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
                MoveAction.move(x)
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
                MoveAction.move(x)
        else:
            print("You do not have enough action points/command points to complete this action.")
            MoveAction.move(x)

        #print(z)
        MoveAction.move(x)

    def turn_right(x, y, z):
        #print(z)
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
                MoveAction.move(x)
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
                MoveAction.move(x)
        else:
            print("You do not have enough action points/command points to complete this action.")
            MoveAction.move(x)
        
        #print(z)
        MoveAction.move(x)

    def move_other_term(command_pts):
        MoveAction.move(command_pts)

    def choose_other_action():
        SpaceMarineTurn.turn_menu()
        exit

class Attack():
    def attack():
        print("Which terminator would you like to attack with?")

        for i in squad.squad:
            if squad.squad[i]["action points"] > 0 and squad.squad[i]["alive"] == True:
                print(i)

        print("Cancel")

        attack_with = input("> ")

        for j in squad.squad:
            #print(j)
            if attack_with == j:
                #print(attack_with)
                print("How would you like to Attack?")

                if squad.squad[j]["weapon loadout"] == "Storm Bolter and Powerfist":
                    print("Storm Bolter")
                    print("Powerfist")
                    print("Cancel")

                    attack_choice = input("> ")

                    if attack_choice == "Storm Bolter":
                        Attack.ranged_combat(SpaceMarineTurn.command_points,
                                    squad.squad[j]["action points"],
                                    squad.squad[j]["current_place"],
                                    squad.squad[j]["direction"],
                                    squad.squad[j]["alive"],
                                    attack_choice)
                    elif attack_choice == "Powerfist":
                        Attack.close_combat(SpaceMarineTurn.command_points,
                                        squad.squad[j]["action points"],
                                        squad.squad[j]["current_place"],
                                        squad.squad[j]["direction"],
                                        squad.squad[j]["alive"],
                                        attack_choice)
                    elif attack_choice == "Cancel":
                        Attack.attack()
                    else:
                        print("You entered an invalid command, please try again.")
                        Attack.attack()
                elif squad.squad[j]["weapon loadout"] == "Power Sword and Storm Bolter":
                    print("Storm Bolter")
                    print("Power Sword")
                    print("Cancel")

                    attack_choice = input("> ")

                    if attack_choice == "Storm Bolter":
                        Attack.ranged_combat(SpaceMarineTurn.command_points,
                                    squad.squad[j]["action points"],
                                    squad.squad[j]["current_place"],
                                    squad.squad[j]["direction"],
                                    squad.squad[j]["alive"],
                                    attack_choice)
                    elif attack_choice == "Power Sword":
                        Attack.close_combat(SpaceMarineTurn.command_points,
                                        squad.squad[j]["action points"],
                                        squad.squad[j]["current_place"],
                                        squad.squad[j]["direction"],
                                        squad.squad[j]["alive"],
                                        attack_choice)
                    elif attack_choice == "Cancel":
                        Attack.attack()
                    else:
                        print("You entered an invalid command, please try again.")
                        Attack.attack()
                elif squad.squad[j]["weapon loadout"] == "Thunder Hammer and Storm Shield":
                    print("Thunder Hammer")
                    print("Cancel")

                    attack_choice = input("> ")

                    if attack_choice == "Thunder Hammer":
                        Attack.close_combat(SpaceMarineTurn.command_points,
                                        squad.squad[j]["action points"],
                                        squad.squad[j]["current_place"],
                                        squad.squad[j]["direction"],
                                        squad.squad[j]["alive"],
                                        attack_choice)
                    elif attack_choice == "Cancel":
                        Attack.attack()
                    else:
                        print("You entered an invalid command, please try again.")
                        Attack.attack()
                elif squad.squad[j]["weapon loadout"] == "Lightning Claws":
                    print("Lightning Claws")
                    print("Cancel")

                    attack_choice = input("> ")

                    if attack_choice == "Lightning Claws":
                        Attack.close_combat(SpaceMarineTurn.command_points,
                                        squad.squad[j]["action points"],
                                        squad.squad[j]["current_place"],
                                        squad.squad[j]["direction"],
                                        squad.squad[j]["alive"],
                                        attack_choice)
                    elif attack_choice == "Cancel":
                        Attack.attack()
                    else:
                        print("You entered an invalid command, please try again.")
                        Attack.attack()
                elif squad.squad[j]["weapon loadout"] == "Storm Bolter and Chainfist":
                    print("Storm Bolter")
                    print("Chainfist")
                    print("Cancel")

                    attack_choice = input("> ")

                    if attack_choice == "Storm Bolter":
                        Attack.ranged_combat(SpaceMarineTurn.command_points,
                                    squad.squad[j]["action points"],
                                    squad.squad[j]["current_place"],
                                    squad.squad[j]["direction"],
                                    squad.squad[j]["alive"],
                                    attack_choice)
                    elif attack_choice == "Chainfist":
                        Attack.close_combat(SpaceMarineTurn.command_points,
                                        squad.squad[j]["action points"],
                                        squad.squad[j]["current_place"],
                                        squad.squad[j]["direction"],
                                        squad.squad[j]["alive"],
                                        attack_choice)
                    elif attack_choice == "Cancel":
                        Attack.attack()
                    else:
                        print("You entered an invalid command, please try again.")
                        Attack.attack()
                elif squad.squad[j]["weapon loadout"] == "Storm Bolter and Power Axe":
                    print("Storm Bolter")
                    print("Power Axe")
                    print("Cancel")

                    attack_choice = input("> ")

                    if attack_choice == "Storm Bolter":
                        Attack.ranged_combat(SpaceMarineTurn.command_points,
                                    squad.squad[j]["action points"],
                                    squad.squad[j]["current_place"],
                                    squad.squad[j]["direction"],
                                    squad.squad[j]["alive"],
                                    attack_choice)
                    elif attack_choice == "Power Axe":
                        Attack.close_combat(SpaceMarineTurn.command_points,
                                        squad.squad[j]["action points"],
                                        squad.squad[j]["current_place"],
                                        squad.squad[j]["direction"],
                                        squad.squad[j]["alive"],
                                        attack_choice)
                    elif attack_choice == "Cancel":
                        Attack.attack()
                    else:
                        print("You entered an invalid command, please try again.")
                        Attack.attack()
                elif squad.squad[j]["weapon loadout"] == "Assault Cannon and Powerfist":
                    print("Assault Cannon")
                    print("Powerfist")
                    print("Cancel")

                    attack_choice = input("> ")

                    if attack_choice == "Assault Cannon":
                        Attack.ranged_combat(SpaceMarineTurn.command_points,
                                    squad.squad[j]["action points"],
                                    squad.squad[j]["current_place"],
                                    squad.squad[j]["direction"],
                                    squad.squad[j]["alive"],
                                    attack_choice,
                                    squad.squad[j]["clip size"])
                    elif attack_choice == "Powerfist":
                        Attack.close_combat(SpaceMarineTurn.command_points,
                                        squad.squad[j]["action points"],
                                        squad.squad[j]["current_place"],
                                        squad.squad[j]["direction"],
                                        squad.squad[j]["alive"],
                                        attack_choice)
                    elif attack_choice == "Cancel":
                        Attack.attack()
                    else:
                        print("You entered an invalid command, please try again.")
                        Attack.attack()
                elif squad.squad[j]["weapon loadout"] == "Heavy Flamer and Powerfist":
                    print("Heavy Flamer")
                    print("Powerfist")
                    print("Cancel")

                    attack_choice = input("> ")

                    if attack_choice == "Heavy Flamer":
                        Attack.ranged_combat(SpaceMarineTurn.command_points,
                                    squad.squad[j]["action points"],
                                    squad.squad[j]["current_place"],
                                    squad.squad[j]["direction"],
                                    squad.squad[j]["alive"],
                                    attack_choice,
                                    squad.squad[j]["clip size"])
                    elif attack_choice == "Powerfist":
                        Attack.close_combat(SpaceMarineTurn.command_points,
                                        squad.squad[j]["action points"],
                                        squad.squad[j]["current_place"],
                                        squad.squad[j]["direction"],
                                        squad.squad[j]["alive"],
                                        attack_choice)
                    elif attack_choice == "Cancel":
                        Attack.attack()
                    else:
                        print("You entered an invalid command, please try again.")
                        Attack.attack()
                elif squad.squad[j]["weapon loadout"] == "Cyclone Missile Launcher, Storm Bolter and Powerfist":
                    print("Storm Bolter")
                    print("Cyclone Missile Launcher")
                    print("Powerfist")
                    print("Cancel")

                    attack_choice = input("> ")

                    if attack_choice == "Storm Bolter":
                        Attack.ranged_combat(SpaceMarineTurn.command_points,
                                    squad.squad[j]["action points"],
                                    squad.squad[j]["current_place"],
                                    squad.squad[j]["direction"],
                                    squad.squad[j]["alive"],
                                    attack_choice)
                    elif attack_choice == "Cyclone Missile Launcher":
                        Attack.ranged_combat(SpaceMarineTurn.command_points,
                                    squad.squad[j]["action points"],
                                    squad.squad[j]["current_place"],
                                    squad.squad[j]["direction"],
                                    squad.squad[j]["alive"],
                                    attack_choice,
                                    squad.squad[j]["clip size"])
                    elif attack_choice == "Powerfist":
                        Attack.close_combat(SpaceMarineTurn.command_points,
                                        squad.squad[j]["action points"],
                                        squad.squad[j]["current_place"],
                                        squad.squad[j]["direction"],
                                        squad.squad[j]["alive"],
                                        attack_choice)
                    elif attack_choice == "Cancel":
                        Attack.attack()
                    else:
                        print("You entered and invalid command, please try again.")
                        Attack.attack()
                elif squad.squad[j]["weapon loadout"] == "Storm Bolter and Power Maul":
                    print("Storm Bolter")
                    print("Power Maul")
                    print("Cancel")

                    attack_choice = input("> ")

                    if attack_choice == "Storm Bolter":
                        Attack.ranged_combat(SpaceMarineTurn.command_points,
                                    squad.squad[j]["action points"],
                                    squad.squad[j]["current_place"],
                                    squad.squad[j]["direction"],
                                    squad.squad[j]["alive"],
                                    attack_choice)
                    elif attack_choice == "Power Maul":
                        Attack.close_combat(SpaceMarineTurn.command_points,
                                        squad.squad[j]["action points"],
                                        squad.squad[j]["current_place"],
                                        squad.squad[j]["direction"],
                                        squad.squad[j]["alive"],
                                        attack_choice)
                    elif attack_choice == "Cancel":
                        Attack.attack()
                    else:
                        print("You entered an invalid command, please try again.")
            elif attack_with == "Cancel":
                SpaceMarineTurn.turn_menu()
            else:
                print("Invalid Selection. Please try again.")
                SpaceMarineTurn.turn_menu()

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
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[0][x]])
                                        elif f == "Assault Cannon":
                                            if squad.squad.g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[0][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[0][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g>= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[0][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad.squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[0][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "east":
                    for x in range(0, 8, 1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[1][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "west":
                    for x in range(8, 15, 1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[1][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                e,
                                                                f)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print("There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "ll5":
                if d == "north":
                    for x in range(1, 15, 1):
                        if linesight.line_of_sight[4][x] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                            if gametiles.tiles[linesight.line_of_sight[4][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[4][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "east":
                    for x in range(2, -1, -1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[1][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "west":
                    for x in range(2, 15, 1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[1][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack() 
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "lr5":
                if d == "north":
                    for x in range(1, 15, 1):
                        if linesight.line_of_sight[5][x] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                            if gametiles.tiles[linesight.line_of_sight[5][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[5][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[5][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[5][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[5][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                                    elif x < 0:
                                        print(
                                            "There is not here for you to fire upon.")
                                        Attack.attack()
                elif d == "east":
                    for x in range(12, -1, -1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[1][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "west":
                    for x in range(13, 15, 1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[1][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "ll5":
                if d == "north":
                    for x in range(1, 15, 1):
                        if linesight.line_of_sight[4][x] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                            if gametiles.tiles[linesight.line_of_sight[4][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[4][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                                    elif x < 0:
                                        print(
                                            "There is not here for you to fire upon.")
                                        Attack.attack()
                elif d == "east":
                    for x in range(13, 15, 1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[1][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "west":
                    for x in range(12, -1, -1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[1][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "g3":
                if d == "south":
                    for x in range(1, 3, 1):
                        if linesight.line_of_sight[2][x] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                            if gametiles.tiles[linesight.line_of_sight[2][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[2][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[2][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[2][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[2][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "east":
                    for x in range(1, 15, 1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[1][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "g7":
                if d == "south":
                    for x in range(1, 3, 1):
                        if linesight.line_of_sight[2][x] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                            if gametiles.tiles[linesight.line_of_sight[2][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[2][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[2][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[2][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[2][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "west":
                    for x in range(13, -1, -1):
                        if linesight.line_of_sight[1][x] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                            if gametiles.tiles[linesight.line_of_sight[1][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[1][x]])
                                        elif f == "Assault Cannon":
                                            if g:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[1][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "l6":
                if d == "south":
                    for x in range(5, -1, -1):
                        if linesight.line_of_sight[4][x] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                            if gametiles.tiles[linesight.line_of_sight[4][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[4][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "north":
                    for x in range(7, 14, 1):
                        if linesight.line_of_sight[4][x] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                            if gametiles.tiles[linesight.line_of_sight[4][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[4][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "east":
                    for x in range(1, 10, 1):
                        if linesight.line_of_sight[6][x] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                            if gametiles.tiles[linesight.line_of_sight[6][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[6][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[6][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[6][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[6][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "r6":
                if d == "south":
                    for x in range(5, -1, -1):
                        if linesight.line_of_sight[5][x] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                            if gametiles.tiles[linesight.line_of_sight[5][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[5][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[5][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[5][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[5][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "north":
                    for x in range(7, 14, 1):
                        if linesight.line_of_sight[5][x] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                            if gametiles.tiles[linesight.line_of_sight[5][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[5][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[5][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[5][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[5][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad.squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "west":
                    for x in range(9, -1, -1):
                        if linesight.line_of_sight[6][x] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                            if gametiles.tiles[linesight.line_of_sight[6][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[6][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[6][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[6][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[6][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "c4":
                if d == "south":
                    for x in range(1, -1, -1):
                        if linesight.line_of_sight[7][x] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                            if gametiles.tiles[linesight.line_of_sight[7][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[7][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[7][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[7][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[7][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "north":
                    for x in range(3, 5, 1):
                        if linesight.line_of_sight[7][x] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                            if gametiles.tiles[linesight.line_of_sight[7][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[7][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[7][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[7][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[7][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "east":
                    for x in range(6, 10, 1):
                        if linesight.line_of_sight[6][x] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                            if gametiles.tiles[linesight.line_of_sight[6][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[6][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[6][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[6][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[6][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "west":
                    for x in range(4, -1, -1):
                        if linesight.line_of_sight[6][x] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                            if gametiles.tiles[linesight.line_of_sight[6][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[6][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[6][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[6][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[6][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "c2":
                if d == "north":
                    for x in range(1, 5, 1):
                        if linesight.line_of_sight[7][x] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                            if gametiles.tiles[linesight.line_of_sight[7][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[7][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[7][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[7][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[7][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "east":
                    for x in range(3, 5, 1):
                        if linesight.line_of_sight[8][x] == gametiles.tiles[linesight.line_of_sight[8][x]]:
                            if gametiles.tiles[linesight.line_of_sight[8][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[8][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[8][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[8][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[8][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "west":
                    for x in range(1, -1, -1):
                        if linesight.line_of_sight[8][x] == gametiles.tiles[linesight.line_of_sight[8][x]]:
                            if gametiles.tiles[linesight.line_of_sight[8][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[8][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[8][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[8][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missle Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[8][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "c6":
                if d == "south":
                    for x in range(3, -1, -1):
                        if linesight.line_of_sight[7][x] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                            if gametiles.tiles[linesight.line_of_sight[7][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[7][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[7][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[7][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[7][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "east":
                    for x in range(3, 5, 1):
                        if linesight.line_of_sight[9][x] == gametiles.tiles[linesight.line_of_sight[9][x]]:
                            if gametiles.tiles[linesight.line_of_sight[9][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[9][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[9][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[9][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[9][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "west":
                    for x in range(2, -1, -1):
                        if linesight.line_of_sight[9][x] == gametiles.tiles[linesight.line_of_sight[9][x]]:
                            if gametiles.tiles[linesight.line_of_sight[9][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[9][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[9][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[9][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[9][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "c7":
                if d == "north":
                    for x in range(1, 6, 1):
                        if linesight.line_of_sight[10][x] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                            if gametiles.tiles[linesight.line_of_sight[10][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[10][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[10][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[10][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[10][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "east":
                    for x in range(3, 5, 1):
                        if linesight.line_of_sight[11][x] == gametiles.tiles[linesight.line_of_sight[11][x]]:
                            if gametiles.tiles[linesight.line_of_sight[9][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[11][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[11][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[11][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[11][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "west":
                    for x in range(1, -1, -1):
                        if linesight.line_of_sight[11][x] == gametiles.tiles[linesight.line_of_sight[11][x]]:
                            if gametiles.tiles[linesight.line_of_sight[9][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[11][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[11][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[11][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[11][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "l13":
                if d == "south":
                    for x in range(12, -1, -1):
                        if linesight.line_of_sight[4][x] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                            if gametiles.tiles[linesight.line_of_sight[4][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[4][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                    RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[4][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad.squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "east":
                    for x in range(1, 11, 1):
                        if linesight.line_of_sight[13][x] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                            if gametiles.tiles[linesight.line_of_sight[13][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[13][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[13][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[13][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[13][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "r13":
                if d == "south":
                    for x in range(12, -1, -1):
                        if linesight.line_of_sight[5][x] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                            if gametiles.tiles[linesight.line_of_sight[5][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[5][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[5][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[5][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[5][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "west":
                    for x in range(9, -1, -1):
                        if linesight.line_of_sight[13][x] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                            if gametiles.tiles[linesight.line_of_sight[13][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[13][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[13][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[13][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[13][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "c10":
                if d == "south":
                    for x in range(2, -1, -1):
                        if linesight.line_of_sight[10][x] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                            if gametiles.tiles[linesight.line_of_sight[10][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[10][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[10][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[10][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[10][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "north":
                    for x in range(4, 6, 1):
                        if linesight.line_of_sight[10][x] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                            if gametiles.tiles[linesight.line_of_sight[10][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[10][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[10][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[10][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[10][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "east":
                    for x in range(6, 11, 1):
                        if linesight.line_of_sight[13][x] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                            if gametiles.tiles[linesight.line_of_sight[13][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[13][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[13][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[13][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[13][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "west":
                    for x in range(4, -1, -1):
                        if linesight.line_of_sight[13][x] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                            if gametiles.tiles[linesight.line_of_sight[13][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[13][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[13][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[13][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[13][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
            elif c == "c12":
                if d == "south":
                    for x in range(4, -1, -1):
                        if linesight.line_of_sight[10][x] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                            if gametiles.tiles[linesight.line_of_sight[10][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[10][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[10][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[10][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[10][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "east":
                    for x in range(3, 5, 1):
                        if linesight.line_of_sight[12][x] == gametiles.tiles[linesight.line_of_sight[12][x]]:
                            if gametiles.tiles[linesight.line_of_sight[12][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[12][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[12][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[12][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[12][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
                elif d == "west":
                    for x in range(1, -1, -1):
                        if linesight.line_of_sight[12][x] == gametiles.tiles[linesight.line_of_sight[12][x]]:
                            if gametiles.tiles[linesight.line_of_sight[12][x]]["occupied"] == True:
                                for y in genestealers.genestealers:
                                    if genestealers.genestealers[y]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][x]]:
                                        if f == "Storm Bolter":
                                            RangedWeapons.bolter_fire(a,
                                                        b,
                                                        genestealers.genestealers[y]["alive"],
                                                        gametiles.tiles[linesight.line_of_sight[12][x]])
                                        elif f == "Assault Cannon":
                                            if g >= 1:
                                                RangedWeapons.assault_cannon(a,
                                                                b,
                                                                genestealers.genestealers[y]["alive"],
                                                                gametiles.tiles[linesight.line_of_sight[12][x]],
                                                                e,
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Heavy Flamer":
                                            if g >= 1:
                                                RangedWeapons.heavy_flamer(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[12][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                        elif f == "Cyclone Missile Launcher":
                                            if g >= 1:
                                                RangedWeapons.cyclone_missle(a,
                                                                b,
                                                                genestealers.genestealers,
                                                                gametiles.tiles[linesight.line_of_sight[12][x]],
                                                                g)
                                            else:
                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                Attack.attack()
                                    elif y == len(genestealers.genestealers):
                                        for z in squad.squad:
                                            if squad.squad[z]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][x]]:
                                                print(
                                                    "You can't fire on your own men.")
                                                Attack.attack()
                                            elif z == len(squad.squad):
                                                print(
                                                    "There is nothing here for you to fire upon.")
                                                Attack.attack()
                            elif x < 0:
                                print("There is not here for you to fire upon.")
                                Attack.attack()
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
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[0][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[0][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[0][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[0][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[0][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                elif d == "north":
                                    for z in range(y + 1, -1, n):
                                        if linesight.line_of_sight[0][z] == gametiles.tiles[linesight.line_of_sight[0][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[0][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[0][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[0][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[0][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[0][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[0][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[0][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                else:
                                    print("You cannot fire in this direction.")
                                    Attack.attack()
                            elif linesight.line_of_sight[x] == "lower hall":
                                if d == "east":
                                    for z in range(y + 1, 15, o):
                                        if linesight.line_of_sight[1][z] == gametiles.tiles[linesight.line_of_sight[1][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[1][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[1][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[1][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[1][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[1][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                elif d == "west":
                                    for z in range(y + 1, -1, n):
                                        if linesight.line_of_sight[1][z] == gametiles.tiles[linesight.line_of_sight[1][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[1][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[1][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[1][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[1][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[1][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[1][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                else:
                                    print("You cannot fire in this direction.")
                                    Attack.attack()
                            elif linesight.line_of_sight[x] == "lower left genestealer entrance":
                                if d == "north":
                                    for z in range(y + 1, 3, o):
                                        if linesight.line_of_sight[2][z] == gametiles.tiles[linesight.line_of_sight[2][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[2][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[2][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[2][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[2][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if a >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[2][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                elif d == "south":
                                    for z in range(y + 1, -1, n):
                                        if linesight.line_of_sight[2][z] == gametiles.tiles[linesight.line_of_sight[2][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[2][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[2][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[2][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[2][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[2][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[2][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                else:
                                    print("You cannot fire in this direction.")
                                    Attack.attack()
                            elif linesight.line_of_sight[x] == "lower right genestealer entrance":
                                if d == "north":
                                    for z in range(y + 1, 3, o):
                                        if linesight.line_of_sight[3][z] == gametiles.tiles[linesight.line_of_sight[3][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[3][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[3][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[3][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[3][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[3][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[3][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[3][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                elif d == "south":
                                    for z in range(y + 1, -1, n):
                                        if linesight.line_of_sight[3][z] == gametiles.tiles[linesight.line_of_sight[3][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[3][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[3][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[3][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[3][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[3][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[3][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[3][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                else:
                                    print("You cannot fire in this direction.")
                                    Attack.attack()
                            elif linesight.line_of_sight[x] == "left hallway":
                                if d == "north":
                                    for z in range(y + 1, 14, o):
                                        if linesight.line_of_sight[4][z] == gametiles.tiles[linesight.line_of_sight[4][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[4][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[4][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[4][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[4][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[4][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                elif d == "south":
                                    for z in range(y + 1, -1, -1):
                                        if linesight.line_of_sight[4][z] == gametiles.tiles[linesight.line_of_sight[4][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[4][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[4][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[4][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[4][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[4][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[4][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                else:
                                    print("You cannot fire in this direction.")
                                    Attack.attack()
                            elif linesight.line_of_sight[x] == "right hallway":
                                if d == "north":
                                    for z in range(y + 1, 14, o):
                                        if linesight.line_of_sight[5][z] == gametiles.tiles[linesight.line_of_sight[5][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[5][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[5][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[5][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[5][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[5][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                elif d == "south":
                                    for z in range(y + 1, -1, n):
                                        if linesight.line_of_sight[5][z] == gametiles.tiles[linesight.line_of_sight[5][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[5][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[5][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[5][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[5][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[5][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[5][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                else:
                                    print("You cannot fire in this direction.")
                                    Attack.attack()
                            elif linesight.line_of_sight[x] == "center hall":
                                if d == "east":
                                    for z in range(y + 1, 11, o):
                                        if linesight.line_of_sight[6][z] == gametiles.tiles[linesight.line_of_sight[6][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[6][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[6][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[6][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[6][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[6][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                elif d == "west":
                                    for z in range(y + 1, -1, n):
                                        if linesight.line_of_sight[6][z] == gametiles.tiles[linesight.line_of_sight[6][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[6][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[6][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[6][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[6][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[6][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[6][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                else:
                                    print("You cannot fire in this direction.")
                                    Attack.attack()
                            elif linesight.line_of_sight[x] == "lower middle hall":
                                if d == "north":
                                    for z in range(y + 1, 5, o):
                                        if linesight.line_of_sight[7][z] == gametiles.tiles[linesight.line_of_sight[7][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[7][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[7][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[7][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[7][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[7][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                elif d == "south":
                                    for z in range(y + 1, -1, n):
                                        if linesight.line_of_sight[7][z] == gametiles.tiles[linesight.line_of_sight[7][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[7][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[7][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[7][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[7][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[7][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[7][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                else:
                                    print("You cannot fire in this direction.")
                                    Attack.attack()
                            elif linesight.line_of_sight[x] == "lower middle genestealer entrance":
                                if d == "east":
                                    for z in range(y + 1, 5, o):
                                        if linesight.line_of_sight[8][z] == gametiles.tiles[linesight.line_of_sight[8][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[8][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[8][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[8][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[8][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[8][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                elif d == "west":
                                    for z in range(y + 1, -1, n):
                                        for z in range(y + 1, 5, o):
                                            if linesight.line_of_sight[8][z] == gametiles.tiles[linesight.line_of_sight[8][z]]:
                                                if gametiles.tiles[linesight.line_of_sight[8][z]]["occupied"] == True:
                                                    for g in genestealers.genestealers:
                                                        if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][z]]:
                                                            if f == "Storm Bolter":
                                                                RangedWeapons.bolter_fire(a,
                                                                            b,
                                                                            genestealers.genestealers[g]["alive"],
                                                                            gametiles.tiles[linesight.line_of_sight[8][z]])
                                                            elif f == "Assault Cannon":
                                                                if g >= 1:
                                                                    RangedWeapons.assault_cannon(a,
                                                                                    b,
                                                                                    genestealers.genestealers[g]["alive"],
                                                                                    gametiles.tiles[linesight.line_of_sight[8][z]],
                                                                                    e,
                                                                                    g)
                                                                else:
                                                                    print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                    Attack.attack()
                                                            elif f == "Heavy Flamer":
                                                                if g >= 1:
                                                                    RangedWeapons.heavy_flamer(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[8][z]],
                                                                                g)
                                                                else:
                                                                    print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                    Attack.attack()
                                                            elif f == "Cyclone Missile Launcher":
                                                                if g >= 1:
                                                                    RangedWeapons.cyclone_missle(a,
                                                                                    b,
                                                                                    genestealers.genestealers,
                                                                                    gametiles.tiles[linesight.line_of_sight[8][z]],
                                                                                    g)
                                                                else:
                                                                    print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                    Attack.attack()
                                                        elif g == len(genestealers.genestealers):
                                                            for h in squad.squad:
                                                                if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[8][z]]:
                                                                    print(
                                                                        "You can't fire on your own men.")
                                                                    Attack.attack()
                                else:
                                    print("You cannot fire in this direction.")
                                    Attack.attack()
                            elif linesight.line_of_sight[x] == "upper middle genestealer entrance":
                                if d == "east":
                                    for z in range(y + 1, 5, o):
                                        if linesight.line_of_sight[9][z] == gametiles.tiles[linesight.line_of_sight[9][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[9][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[9][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[9][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                            b,
                                                                            genestealers.genestealers,
                                                                            gametiles.tiles[linesight.line_of_sight[9][z]],
                                                                            g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[9][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                elif d == "west":
                                    for z in range(y + 1, -1, n):
                                        if linesight.line_of_sight[9][z] == gametiles.tiles[linesight.line_of_sight[9][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[9][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[9][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[9][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[9][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[9][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[9][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                else:
                                    print("You cannot fire in this direction.")
                                    Attack.attack()
                            elif linesight.line_of_sight[x] == "upper middle hall":
                                if d == "north":
                                    for z in range(y + 1, 6, o):
                                        if linesight.line_of_sight[10][z] == gametiles.tiles[linesight.line_of_sight[10][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[10][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[10][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[10][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[10][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[10][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                elif d == "south":
                                    for z in range(y + 1, -1, n):
                                        if linesight.line_of_sight[10][z] == gametiles.tiles[linesight.line_of_sight[10][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[10][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[10][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[10][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[10][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[10][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[10][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                else:
                                    print("You cannot fire in this direction.")
                                    Attack.attack()
                            elif linesight.line_of_sight[x] == "lower top genestealer entrance":
                                if d == "east":
                                    for z in range(y + 1, 5, o):
                                        if linesight.line_of_sight[11][z] == gametiles.tiles[linesight.line_of_sight[11][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[11][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[11][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[11][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[11][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[11][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                elif d == "west":
                                    for z in range(y + 1, -1, n):
                                        if linesight.line_of_sight[11][z] == gametiles.tiles[linesight.line_of_sight[11][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[11][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[11][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[11][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[11][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[11][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[11][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                else:
                                    print("You cannot fire in this direction.")
                                    Attack.attack()
                            elif linesight.line_of_sight[x] == "upper top genestealer entrance":
                                if d == "east":
                                    for z in range(y + 1, 5, o):
                                        if linesight.line_of_sight[12][z] == gametiles.tiles[linesight.line_of_sight[12][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[12][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[12][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[12][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[12][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[12][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                elif d == "west":
                                    for z in range(y + 1, -1, n):
                                        if linesight.line_of_sight[12][z] == gametiles.tiles[linesight.line_of_sight[12][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[12][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[12][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[12][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[12][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[12][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[12][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                else:
                                    print("You cannot fire in this direction.")
                                    Attack.attack()
                            elif linesight.line_of_sight[x] == "upper hall":
                                if d == "east":
                                    for z in range(y + 1, 11, o):
                                        if linesight.line_of_sight[13][z] == gametiles.tiles[linesight.line_of_sight[13][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[13][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[13][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[13][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[13][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[13][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                elif d == "west":
                                    for z in range(y + 1, -1, n):
                                        if linesight.line_of_sight[13][z] == gametiles.tiles[linesight.line_of_sight[13][z]]:
                                            if gametiles.tiles[linesight.line_of_sight[13][z]]["occupied"] == True:
                                                for g in genestealers.genestealers:
                                                    if genestealers.genestealers[g]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][z]]:
                                                        if f == "Storm Bolter":
                                                            RangedWeapons.bolter_fire(a,
                                                                        b,
                                                                        genestealers.genestealers[g]["alive"],
                                                                        gametiles.tiles[linesight.line_of_sight[13][z]])
                                                        elif f == "Assault Cannon":
                                                            if g >= 1:
                                                                RangedWeapons.assault_cannon(a,
                                                                                b,
                                                                                genestealers.genestealers[g]["alive"],
                                                                                gametiles.tiles[linesight.line_of_sight[13][z]],
                                                                                e,
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Heavy Flamer":
                                                            if g >= 1:
                                                                RangedWeapons.heavy_flamer(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[13][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                        elif f == "Cyclone Missile Launcher":
                                                            if g >= 1:
                                                                RangedWeapons.cyclone_missle(a,
                                                                                b,
                                                                                genestealers.genestealers,
                                                                                gametiles.tiles[linesight.line_of_sight[13][z]],
                                                                                g)
                                                            else:
                                                                print("Your weapon is out of ammunition. You need to reload before you can fire again.")
                                                                Attack.attack()
                                                    elif g == len(genestealers.genestealers):
                                                        for h in squad.squad:
                                                            if squad.squad[h]["current_place"] == gametiles.tiles[linesight.line_of_sight[13][z]]:
                                                                print(
                                                                    "You can't fire on your own men.")
                                                                Attack.attack()
                                else:
                                    print("You cannot fire in this direction.")
                                    Attack.attack()
        else:
            print("You don't have enough action points to complete this action.")
            Attack.attack()

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
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Power Sword":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                RangedWeapons.parry(spacemarine_roll)

                                                if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                    e = False
                                                    gametiles.tiles["occupied"] = False
                                                    print("The attacking terminator has perished in combat.")
                                                    SpaceMarineTurn.lose_cond()
                                                    SpaceMarineTurn.turn_menu()
                                                elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                    genestealers.genestealers[z]["alive"] == False
                                                    gametiles.tiles[y]["occupied"] == False
                                                    print(
                                                        "The attacking terminator has sucessfully slain the xenos filth.")
                                                    Attack.attack()
                                                else:
                                                    print(
                                                        "There was a draw in combat")
                                                    Attack.attack()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Thunder Hammer":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
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
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[2] < spacemarine_rolls[1]:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Chainfist":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Power Axe":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Power Maul":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        else:
                                            print(
                                                "You entered an invalid weapon type, please try again.")
                                            Attack.attack()

                                        Attack.attack()
                                    elif genestealers.genestealers[z]["direction"] == "south" and d == "north":
                                        if f == "Powerfist":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Power Sword":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                RangedWeapons.parry(spacemarine_roll)

                                                if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                    e = False
                                                    gametiles.tiles["occupied"] = False
                                                    print("The attacking terminator has perished in combat.")
                                                    SpaceMarineTurn.lose_cond()
                                                    SpaceMarineTurn.turn_menu()
                                                elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                    genestealers.genestealers[z]["alive"] == False
                                                    gametiles.tiles[y]["occupied"] == False
                                                    print(
                                                        "The attacking terminator has sucessfully slain the xenos filth.")
                                                    Attack.attack()
                                                else:
                                                    print(
                                                        "There was a draw in combat")
                                                    Attack.attack()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Thunder Hammer":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
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
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[2] < spacemarine_rolls[1]:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Chainfist":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Power Axe":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Power Maul":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        else:
                                            print(
                                                "You entered an invalid weapon type, please try again.")
                                            Attack.attack()

                                        Attack.attack()
                                    elif genestealers.genestealers[z]["direction"] == "east" and d == "west":
                                        if f == "Powerfist":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Power Sword":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                RangedWeapons.parry(spacemarine_roll)

                                                if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                    e = False
                                                    gametiles.tiles["occupied"] = False
                                                    print("The attacking terminator has perished in combat.")
                                                    SpaceMarineTurn.lose_cond()
                                                    SpaceMarineTurn.turn_menu()
                                                elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                    genestealers.genestealers[z]["alive"] == False
                                                    gametiles.tiles[y]["occupied"] == False
                                                    print(
                                                        "The attacking terminator has sucessfully slain the xenos filth.")
                                                    Attack.attack()
                                                else:
                                                    print(
                                                        "There was a draw in combat")
                                                    Attack.attack()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Thunder Hammer":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
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
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[2] < spacemarine_rolls[1]:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Chainfist":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Power Axe":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Power Maul":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        else:
                                            print(
                                                "You entered an invalid weapon type, please try again.")
                                            Attack.attack()

                                        Attack.attack()
                                    elif genestealers.genestealers[z]["direction"] == "west" and d == "east":
                                        if f == "Powerfist":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Power Sword":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                RangedWeapons.parry(spacemarine_roll)

                                                if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                    e = False
                                                    gametiles.tiles["occupied"] = False
                                                    print("The attacking terminator has perished in combat.")
                                                    SpaceMarineTurn.lose_cond()
                                                    SpaceMarineTurn.turn_menu()
                                                elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                    genestealers.genestealers[z]["alive"] == False
                                                    gametiles.tiles[y]["occupied"] == False
                                                    print(
                                                        "The attacking terminator has sucessfully slain the xenos filth.")
                                                    Attack.attack()
                                                else:
                                                    print(
                                                        "There was a draw in combat")
                                                    Attack.attack()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Thunder Hammer":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
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
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[2] < spacemarine_rolls[1]:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Chainfist":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Power Axe":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        elif f == "Power Maul":
                                            spacemarine_roll = randint(1, 6)
                                            genestealer_rolls = {
                                                randint(1, 6), randint(1, 6), randint(1, 6)}

                                            if genestealer_rolls[0] > spacemarine_roll or genestealer_rolls[1] > spacemarine_roll or genestealer_rolls[2] > spacemarine_roll:
                                                e = False
                                                gametiles.tiles["occupied"] = False
                                                print("The attacking terminator has perished in combat.")
                                                SpaceMarineTurn.lose_cond()
                                                SpaceMarineTurn.turn_menu()
                                            elif genestealer_rolls[0] < spacemarine_roll or genestealer_rolls[1] < spacemarine_roll or genestealer_rolls[2] < spacemarine_roll:
                                                genestealers.genestealers[z]["alive"] == False
                                                gametiles.tiles[y]["occupied"] == False
                                                print(
                                                    "The attacking terminator has sucessfully slain the xenos filth.")
                                                Attack.attack()
                                            else:
                                                print("There was a draw in combat")
                                                Attack.attack()
                                        else:
                                            print(
                                                "You entered an invalid weapon type, please try again.")
                                            Attack.attack()

                                        Attack.attack()
                                elif z >= len(genestealers.genestealers):
                                    print(
                                        "There is no foe that you can Attack.attack at your current_place.")
                                    Attack.attack()
        else:
            print("You don't have enough action points and/or command points to complete this action.")
            Attack.attack()

class RangedWeapons():
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
            RangedWeapons.parry(x)

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
            Attack.attack()
        else:
            print("Your shot missed its target.")
            Attack.attack()

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
            Attack.attack()
        elif assault_shot_1 == assault_shot_2 and assault_shot_2 == assault_shot_3:
            e = False
            print("The terminator's assault cannon malfunctioned resulting in instant death.")
            SpaceMarineTurn.lose_cond()
            Attack.attack()
        else:
            print("The assault cannon volly missed its target.")
            Attack.attack()

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
        
        Attack.attack()

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
        Attack.attack()

new_game = Openingscene()
new_game.enter()