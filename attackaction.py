from random import randint
import squad

def attack():
    print("Which terminator would you like to attack with?")

    for i in squad.squad:
        if squad[i]["action points"] > 0 and squad[i]["alive"] == True:
            print(squad[i])

    print("Cancel")

    attack_with = input("> ")

    for j in squad.squad:
        if attack_with == squad[i]:
            print("How would you like to attack?")

            if squad[i]["weapon loadout"] == "Storm Bolter and Powerfist":
                print("Storm Bolter")
                print("Powerfist")
                print("Cancel")

                attack_choice = input("> ")

                if attack_choice == "Storm Bolter":
                    ranged_combat()
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
                    ranged_combat()
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
                    ranged_combat()
                elif attack_choice == "Chainfist":
                    close_combat()
                elif attack_choice == "Cancel":
                    attack()
                else:
                    print("You entered an invalid command, please try again.")
                    attack()

def ranged_combat():

def close_combat():