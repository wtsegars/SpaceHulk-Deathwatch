from random import randint
import squad
import game
import weapons

def overwatch_fire(marine, gs):
    if (marine["overwatch"] == True):
        roll_1 = randint(1, 7)
        roll_2 = randint(1, 7)
        roll_3 = randint(1, 7)

        if (marine["weapon loadout"] == weapons.weapon_loadout[0] or marine["weapon loadout"] == weapons.weapon_loadout[1] or marine["weapon loadout"] == weapons.weapon_loadout[4] or marine["weapon loadout"] == weapons.weapon_loadout[5] or marine["weapon loadout"] == weapons.weapon_loadout[8] or marine["weapon loadout"] == weapons.weapon_loadout[9]):
            if ((roll_1 == 5 or roll_1 == 6) and (roll_2 == 5 or roll_2 == 6)):
                print("Genestealer has been hit!")
                gs["alive"] = False
                if (roll_1 == roll_2):
                    print(f"{marine}'s bolter has jammed!")
                    marine["jammed"] = True
            else:
                print("The bolter shot missed its target.")
                if (roll_1 == roll_2):
                    print(f"{marine}'s bolter has jammed!")
                    marine["jammed"] = True
        elif (marine["weapon loadout"] == weapons.weapon_loadout[6]):
            if ((roll_1 == 4 or roll_1 == 5 or roll_1 == 6) and (roll_2 == 4 or roll_2 == 5 or roll_2 == 6) and (roll_3 == 4 or roll_3 == 5 or roll_3 == 6)):
                marine["clip_size"] -= 1
                print("Genestealer has been hit!")
                gs["alive"] = False
                if (roll_1 == roll_2 == roll_3):
                    marine["clip_size"] -= 1
                    print(f"{marine}'s assault cannon has malfunctioned!")
                    marine["alive"] = False
            else:
                print("The assault cannon missed its target.")
                marine["clip_size"] -= 1