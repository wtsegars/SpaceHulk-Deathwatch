import game
import attackaction
import radarblips
import genestealers
import gametiles
import linesight
import squad
import overwatchfire

def genestealer_movement():
    for x in radarblips: #looping through radar blips
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0

        tracker1 = None
        tracker2 = None
        tracker3 = None
        tracker4 = None

        if (radarblips[x]["current location"]):
            for y in squad:
                if (squad[y]["current_place"]):
                    for z in linesight:
                        for a in linesight[z]:
                            if (radarblips[x]["current location"] == linesight[z][a]):
                                tracker1 == gametiles(radarblips[x]["current location"])["connected to"][0]
                                if (gametiles(radarblips[x]["current location"])["connected to"][1]):
                                    tracker2 == gametiles(radarblips[x]["current location"])["connected to"][1]
                                if (gametiles(radarblips[x]["current location"])["connected to"][2]):
                                    tracker3 == gametiles(radarblips[x]["current location"])["connected to"][2]
                                if (gametiles(radarblips[x]["current location"])["connected to"][3]):
                                    tracker4 == gametiles(radarblips[x]["current location"])["connected to"][3]                                    

                                while (tracker1 != squad[y]["current_place"] or tracker2 != squad[y]["current_place"] or tracker3 != squad[y]["current_place"] or tracker4 != squad[y]["current_place"]):
                                    tracker1 = gametiles(radarblips[x]["current location"]["connected to"][0])
                                    c1 += 1

                                    if (tracker2 != None):
                                        tracker2 = gametiles(radarblips[x]["current location"]["connected to"][1])
                                        c2 += 1

                                    if (tracker3 != None):
                                        tracker3 = gametiles(radarblips[x]["current location"]["connected to"][2])
                                        c3 += 1

                                    if (tracker4 != None):
                                        tracker4 = gametiles(radarblips[x]["current location"]["connected to"][3])
                                        c4 += 1

                                if (tracker1 == squad[y]["current_place"]):
                                    if (gametiles(radarblips[x]["current location"]["connected to"][0])["occupied"] != True):
                                        radarblips.check_for_reveal(radarblips[x])
                                        radarblips[x]["current location"] = gametiles(radarblips[x]["current location"])["connected to"][0]
                                        radarblips[x]["action points"] -= 1
                                    else:
                                        for b in radarblips:
                                            if (radarblips[b] != radarblips[x]):
                                                if (radarblips[b]["current location"] == gametiles(radarblips[x]["current location"])["connected to"][0]):
                                                    break
                                            
                                        for c in genestealers:
                                            if (genestealers[c]["current location"] == gametiles(radarblips[x]["current location"])["connected to"][0]):
                                                break

                                        for d in squad:
                                            if (squad[d]["current_place"] == gametiles(radarblips[x]["current location"])["connected to"][0]):
                                                if (radarblips[x]["action points"] > 0):
                                                    while (radarblips[x]["action points"] > 0 or squad[d]["alive"] == True):
                                                        attackaction.close_combat(game.command_points,
                                                                                    squad[d]["action points"],
                                                                                    squad[d]["current_place"],
                                                                                    squad[d]["direction"],
                                                                                    squad[d]["alive"],
                                                                                    squad[d]["weapon loadout"])
                                                    break
                                elif (tracker2 == squad[y]["current_place"]):
                                    if (gametiles(radarblips[x]["current location"]["connected to"][1])["occupied"] != True):
                                        radarblips.check_for_reveal(radarblips[x])
                                        radarblips[x]["current location"] = gametiles(radarblips[x]["current location"])["connected to"][1]
                                        radarblips[x]["action points"] -= 1
                                    else:
                                        for b in radarblips:
                                            if (radarblips[b] != radarblips[x]):
                                                if (radarblips[b]["current location"] == gametiles(radarblips[x]["current location"])["connected to"][1]):
                                                    break
                                            
                                        for c in genestealers:
                                            if (genestealers[c]["current location"] == gametiles(radarblips[x]["current location"])["connected to"][1]):
                                                break

                                        for d in squad:
                                            if (squad[d]["current_place"] == gametiles(radarblips[x]["current location"])["connected to"][1]):
                                                if (radarblips[x]["action points"] > 0):
                                                    while (radarblips[x]["action points"] > 0 or squad[d]["alive"] == True):
                                                        attackaction.close_combat(game.command_points,
                                                                                    squad[d]["action points"],
                                                                                    squad[d]["current_place"],
                                                                                    squad[d]["direction"],
                                                                                    squad[d]["alive"],
                                                                                    squad[d]["weapon loadout"])
                                                    break
                                elif (tracker3 == squad[y]["current_place"]):
                                    if (gametiles(radarblips[x]["current location"]["connected to"][2])["occupied"] != True):
                                        radarblips.check_for_reveal(radarblips[x])
                                        radarblips[x]["current location"] = gametiles(radarblips[x]["current location"])["connected to"][2]
                                        radarblips[x]["action points"] -= 1
                                    else:
                                        for b in radarblips:
                                            if (radarblips[b] != radarblips[x]):
                                                if (radarblips[b]["current location"] == gametiles(radarblips[x]["current location"])["connected to"][2]):
                                                    break
                                            
                                        for c in genestealers:
                                            if (genestealers[c]["current location"] == gametiles(radarblips[x]["current location"])["connected to"][2]):
                                                break

                                        for d in squad:
                                            if (squad[d]["current_place"] == gametiles(radarblips[x]["current location"])["connected to"][2]):
                                                if (radarblips[x]["action points"] > 0):
                                                    while (radarblips[x]["action points"] > 0 or squad[d]["alive"] == True):
                                                        attackaction.close_combat(game.command_points,
                                                                                    squad[d]["action points"],
                                                                                    squad[d]["current_place"],
                                                                                    squad[d]["direction"],
                                                                                    squad[d]["alive"],
                                                                                    squad[d]["weapon loadout"])
                                                    break
                                elif (tracker4 == squad[y]["current_place"]):
                                    if (gametiles(radarblips[x]["current location"]["connected to"][3])["occupied"] != True):
                                        radarblips.check_for_reveal(radarblips[x])
                                        radarblips[x]["current location"] = gametiles(radarblips[x]["current location"])["connected to"][3]
                                        radarblips[x]["action points"] -= 1
                                    else:
                                        for b in radarblips:
                                            if (radarblips[b] != radarblips[x]):
                                                if (radarblips[b]["current location"] == gametiles(radarblips[x]["current location"])["connected to"][3]):
                                                    break
                                            
                                        for c in genestealers:
                                            if (genestealers[c]["current location"] == gametiles(radarblips[x]["current location"])["connected to"][3]):
                                                break

                                        for d in squad:
                                            if (squad[d]["current_place"] == gametiles(radarblips[x]["current location"])["connected to"][3]):
                                                if (radarblips[x]["action points"] > 0):
                                                    while (radarblips[x]["action points"] > 0 or squad[d]["alive"] == True):
                                                        attackaction.close_combat(game.command_points,
                                                                                    squad[d]["action points"],
                                                                                    squad[d]["current_place"],
                                                                                    squad[d]["direction"],
                                                                                    squad[d]["alive"],
                                                                                    squad[d]["weapon loadout"])
                                                    break

    for e in genestealers:
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0

        tracker1 = None
        tracker2 = None
        tracker3 = None
        tracker4 = None

        if (genestealers[e]["current location"]):
            for f in squad:
                if (squad[f]["current_place"]):
                    for g in linesight:
                        for h in linesight:
                            if (genestealers[e]["current location"] == linesight[g][h]):
                                tracker1 = gametiles(genestealers[e]["current location"])["connected to"][0]
                                if (gametiles(genestealers[e]["current location"])["connected to"][1]):
                                    tracker2 = gametiles(genestealers[e]["current location"])["connected to"][1]
                                if (gametiles(genestealers[e]["current location"])["connected to"][2]):
                                    tracker3 = gametiles(genestealers[e]["current location"])["connected to"][2]
                                if (gametiles(genestealers[e]["current location"])["connected to"][3]):
                                    tracker4 = gametiles(genestealers[e]["current location"])["connected to"][3]

                                while (tracker1 != squad[f]["current_place"] or tracker2 != squad[f]["current_place"] or tracker3 != squad[f]["current_place"] or tracker4 != squad[f]["current_place"]):
                                    tracker1 = gametiles(genestealers[e]["current location"]["connected to"][0])
                                    c1 += 1

                                    if (tracker2 != None):
                                        tracker2 = gametiles(genestealers[e]["current location"]["connected to"][1])
                                        c2 += 1

                                    if (tracker3 != None):
                                        tracker3 = gametiles(genestealers[e]["current location"]["connected to"][2])
                                        c3 += 1

                                    if (tracker4 != None):
                                        tracker4 = gametiles(genestealers[e]["current location"]["connected to"][3])
                                        c4 += 1

                                if (tracker1 == squad[y]["current_place"]):
                                    if (gametiles(genestealers[e]["current location"]["connected to"][0])["occupied"] != True):
                                        genestealers[e]["current location"] = gametiles(genestealers[e]["current location"])["current location"][0]
                                        genestealers[e]["action points"] -= 1
                                    else:
                                        for i in genestealers:
                                            if (genestealers[i] != genestealers[e]):
                                                if (genestealers[i]["current location"] == gametiles(genestealers[e]["current location"])["connected to"][0]):
                                                    break

                                        for j in radarblips:
                                            if (radarblips[j]["current location"] == gametiles(genestealers[e]["current location"])["connected to"][0]):
                                                break

                                        for k in squad:
                                            if (squad[k]["current_place"] == gametiles(genestealers[e]["current location"])["connected to"][0]):
                                                if (genestealers[e]["action points"] > 0):
                                                    while (genestealers[e]["action points"] > 0 or squad[k]["alive"] == True):
                                                        attackaction.close_combat(game.command_points,
                                                                                    squad[k]["action points"],
                                                                                    squad[k]["current_place"],
                                                                                    squad[k]["direction"],
                                                                                    squad[k]["alive"],
                                                                                    squad[k]["weapon loadout"])
                                                    break
                                elif (tracker2 == squad[y]["current_place"]):
                                    if (gametiles(genestealers[e]["current location"]["connected to"][1])["occupied"] != True):
                                        genestealers[e]["current location"] = gametiles(genestealers[e]["current location"])["current location"][1]
                                        genestealers[e]["action points"] -= 1
                                    else:
                                        for i in genestealers:
                                            if (genestealers[i] != genestealers[e]):
                                                if (genestealers[i]["current location"] == gametiles(genestealers[e]["current location"])["connected to"][1]):
                                                    break

                                        for j in radarblips:
                                            if (radarblips[j]["current location"] == gametiles(genestealers[e]["current location"])["connected to"][1]):
                                                break

                                        for k in squad:
                                            if (squad[k]["current_place"] == gametiles(genestealers[e]["current location"])["connected to"][1]):
                                                if (genestealers[e]["action points"] > 0):
                                                    while (genestealers[e]["action points"] > 0 or squad[k]["alive"] == True):
                                                        attackaction.close_combat(game.command_points,
                                                                                    squad[k]["action points"],
                                                                                    squad[k]["current_place"],
                                                                                    squad[k]["direction"],
                                                                                    squad[k]["alive"],
                                                                                    squad[k]["weapon loadout"])
                                                    break
                                elif (tracker3 == squad[y]["current_place"]):
                                    if (gametiles(genestealers[e]["current location"]["connected to"][2])["occupied"] != True):
                                        genestealers[e]["current location"] = gametiles(genestealers[e]["current location"])["current location"][2]
                                        genestealers[e]["action points"] -= 1
                                    else:
                                        for i in genestealers:
                                            if (genestealers[i] != genestealers[e]):
                                                if (genestealers[i]["current location"] == gametiles(genestealers[e]["current location"])["connected to"][2]):
                                                    break

                                        for j in radarblips:
                                            if (radarblips[j]["current location"] == gametiles(genestealers[e]["current location"])["connected to"][2]):
                                                break

                                        for k in squad:
                                            if (squad[k]["current_place"] == gametiles(genestealers[e]["current location"])["connected to"][2]):
                                                if (genestealers[e]["action points"] > 0):
                                                    while (genestealers[e]["action points"] > 0 or squad[k]["alive"] == True):
                                                        attackaction.close_combat(game.command_points,
                                                                                    squad[k]["action points"],
                                                                                    squad[k]["current_place"],
                                                                                    squad[k]["direction"],
                                                                                    squad[k]["alive"],
                                                                                    squad[k]["weapon loadout"])
                                                    break
                                elif (tracker4 == squad[y]["current_place"]):
                                    if (gametiles(genestealers[e]["current location"]["connected to"][3])["occupied"] != True):
                                        genestealers[e]["current location"] = gametiles(genestealers[e]["current location"])["current location"][3]
                                        genestealers[e]["action points"] -= 1
                                    else:
                                        for i in genestealers:
                                            if (genestealers[i] != genestealers[e]):
                                                if (genestealers[i]["current location"] == gametiles(genestealers[e]["current location"])["connected to"][3]):
                                                    break

                                        for j in radarblips:
                                            if (radarblips[j]["current location"] == gametiles(genestealers[e]["current location"])["connected to"][3]):
                                                break

                                        for k in squad:
                                            if (squad[k]["current_place"] == gametiles(genestealers[e]["current location"])["connected to"][3]):
                                                if (genestealers[e]["action points"] > 0):
                                                    while (genestealers[e]["action points"] > 0 or squad[k]["alive"] == True):
                                                        attackaction.close_combat(game.command_points,
                                                                                    squad[k]["action points"],
                                                                                    squad[k]["current_place"],
                                                                                    squad[k]["direction"],
                                                                                    squad[k]["alive"],
                                                                                    squad[k]["weapon loadout"])
                                                    break