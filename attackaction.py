from random import randint
import squad
import game
import gametiles

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
                                    squad[j]["alive"])
                elif attack_choice == "Power Maul":
                    close_combat()
                elif attack_choice == "Cancel":
                    attack()
                else:
                    print("You entered an invalid command, please try again.")
        elif attack_with == "Cancel":
            game.SpaceMarineTurn.enter.turn_menu()

def ranged_combat(a, b, c, d, e):

def close_combat(a, b, c, d, e):
    if a >= 1 and b >= 1:
        for x in gametiles.tiles:
            if gametiles.tiles[x] == c:
                for y in gametiles.tiles[x]["connected to"]:
                    if gametiles.tiles[y]["occupied"] == True: