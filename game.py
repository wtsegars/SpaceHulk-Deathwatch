from sys import exit
from random import randint
from textwrap import dedent
import chapters
import squad
import weapons
import gametiles
import genestealers
import movement
import attackaction
import miscaction
import gamemap
import radarblips
import genestealermove

turn_count = 0
        
class Openingscene():
    def enter(self):
        print(dedent("""
                Welcome to Space Hulk Deathwatch, a console-based game that
                is based on the classic Games Workshop game, Space Hulk. This, 
                along with many other games that are created by Game Workshop,
                is based in the Warhammer 40,000 universe.
                """))

        print(dedent("""
                This game is set inside of a space hulk (hence the name), which
                is a floating mass of ships that have been fused together while
                being lost in the warp. Sometimes these space hulks will appear
                in realspace and, from time to time, the superhuman Adeptus 
                Astartes (space marines) will send a squad or two into these
                space hulks to cleanse them of alien life, find lost relics and
                technologies from the past, or any number of other reasons.
                """))

        print(dedent("""
                The Deathwatch are an elite chaper of the space marines that are
                made up from veteran marines from various chapers from all across
                the Imperium of Man. The Deathwatch acts as the chamber militant 
                (military branch) for the Ordo Xenos branch of the Inquisition (
                secret police that help keep the Imperium stable). Your goal is 
                to try and get your squad out of the space hulk before they are 
                overrun by genestealers (a form of Tyranid that are commonly found
                on board of space hulks).
                """))

        return SquadSelect().enter()

class SquadSelect():
    heavy_count = 0

    def enter(self):
        print(dedent("""
                Below is where you can select your squad of five marines from a 
                pre-selected list of chapters. The first marine you select will
                be the squad's sergent while the rest are standard marines. Choose
                wisely because some chapters will have advantages over others.
                """))
        SquadSelect.chapter_select()
        SquadSelect.weapon_select()
        Squadplacement.enter(self)
        SpaceMarineTurn.enter(self, turn_count)

    def chapter_select():
        print("Below is a list of available chapters, choose wisely...")
        print()
        
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
                        else:
                            squad.squad[y]["weapon loadout"] = wpn_input
            
                if squad.squad[y]["weapon loadout"] == None:
                    print("An invalid weapon loadout was selected, please select another.")
                    SquadSelect.weapon_select()
            else:
                continue

class Squadplacement():
    order = ["first", "second", "third", "fourth", "fifth"]

    def enter(self):
        print("Select the order in which your squad is to be deployed:")
        print()
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
                        continue
                else:
                    continue
                        
    def place_loop(term, start_place):
        if start_place == "first":
            term["current_place"] = "s5"
            Squadplacement.order.remove("first")
        elif start_place == "second":
            term["current_place"] = "s4"
            Squadplacement.order.remove("second")
        elif start_place == "third":
            term["current_place"] = "s3"
            Squadplacement.order.remove("third")
        elif start_place == "fourth":
            term["current_place"] = "s4"
            Squadplacement.order.remove("fourth")
        else:
            term["current_place"] = "s1"
            Squadplacement.order.remove("fifth")

class SpaceMarineTurn():
    command_points = randint(1, 7)

    def enter(turn_count):
        turn_count +=1
        print("It is now the space marines' turn.")
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
            movement.Movement.move()
        elif menu_choice == "Attack":
            attackaction.Attack.attack()
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
        return SpaceMarineTurn.enter(turn_count)

new_game = Openingscene()
new_game.enter()