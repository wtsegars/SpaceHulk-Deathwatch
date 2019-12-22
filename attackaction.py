from random import randint
import squad

def attack():
    print("Which terminator would you like to attack with?")

    for i in squad.squad:
        if squad[i]["action points"] > 0 and squad[i]["alive"] == True:
            print(squad[i])

    attack_with = input("> ")

    for j in squad.squad:
        if attack_with == squad[i]:
            print("How would you like to attack?")