from random import randint
import weapons
import linesight
import squad

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
                    marine["overwatch"] = False
            else:
                print("The bolter shot missed its target.")
                if (roll_1 == roll_2):
                    print(f"{marine}'s bolter has jammed!")
                    marine["jammed"] = True
                    marine["overwatch"] = False
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

def check_for_overwatch(gs):
    for a in linesight.line_of_sight:
        for b in linesight.line_of_sight[a]:
            if (gs["current location"] == linesight.line_of_sight[a][b]):
                for c in linesight.line_of_sight[a]:
                    for d in squad.squad:
                        if (linesight.line_of_sight[a][c] == squad.squad[d]["current_place"]):
                            if (linesight[a] == linesight.line_of_sight[0] or linesight[a] == linesight.line_of_sight[2] or linesight[a] == linesight.line_of_sight[3] or linesight[a] == linesight.line_of_sight[4] or linesight[a] == linesight.line_of_sight[5] or linesight[a] == linesight.line_of_sight[7] or linesight[a] == linesight.line_of_sight[10]):
                                if (squad.squad[d]["direction"] == "north"):
                                    gs_index = linesight.line_of_sight[a].index(gs["current location"])
                                    for e in range(b, gs_index, 1):
                                        if (linesight.line_of_sight[a][e] == gs["current location"]):
                                            overwatch_fire(squad.squad[d], gs)
                                elif (squad.squad[d]["direction"] == "south"):
                                    gs_index = linesight[a].index(gs["current location"])
                                    for e in range(b, gs_index, -1):
                                        if (linesight.line_of_sight[a][e] == gs["current location"]):
                                            overwatch_fire(squad.squad[d], gs)
                            elif (linesight[c] == linesight.line_of_sight[1] or linesight[c] == linesight.line_of_sight[6] or linesight[c] == linesight.line_of_sight[8] or linesight[c] == linesight.line_of_sight[9] or linesight[c] == linesight.line_of_sight[11] or linesight[c] == linesight.line_of_sight[12] or linesight[c] == linesight.line_of_sight[13]):
                                if (squad.squad[d]["direction"] == "east"):
                                    gs_index = linesight.line_of_sight[a].index(gs["current location"])
                                    for e in range(b, gs_index, 1):
                                        if (linesight.line_of_sight[a][e] == gs["current location"]):
                                            overwatch_fire(squad.squad[d], gs)
                                elif (squad.squad[d]["direction"] == "west"):
                                    gs_index = linesight.line_of_sight[a].index(gs["current location"])
                                    for e in range(b, gs_index, -1):
                                        if (linesight.line_of_sight[a][e] == gs["current location"]):
                                            overwatch_fire(squad.squad[d], gs)