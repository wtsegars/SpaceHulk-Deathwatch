import game
import attackaction
import radarblips
import genestealers
import gametiles
import linesight
import squad
import overwatchfire

def genestealer_movement():
    for x in radarblips.blips: #looping through radar blips
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0

        tracker1 = None
        tracker2 = None
        tracker3 = None
        tracker4 = None

        if (radarblips.blips[x]["current location"]):
            for y in squad:
                if (squad[y]["current_place"]):
                    for z in linesight.line_of_sight:
                        for a in linesight.line_of_sight[z]:
                            if (radarblips.blips[x]["current location"] == linesight.line_of_sight[z][a]):
                                tracker1 == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][0]
                                if (gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][1]):
                                    tracker2 == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][1]
                                if (gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][2]):
                                    tracker3 == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][2]
                                if (gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][3]):
                                    tracker4 == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][3]                                    

                                while (tracker1 != squad[y]["current_place"] or tracker2 != squad[y]["current_place"] or tracker3 != squad[y]["current_place"] or tracker4 != squad[y]["current_place"]):
                                    tracker1 = gametiles.tiles(radarblips.blips[x]["current location"]["connected to"][0])
                                    c1 += 1

                                    if (tracker2 != None):
                                        tracker2 = gametiles.tiles(radarblips.blips[x]["current location"]["connected to"][1])
                                        c2 += 1

                                    if (tracker3 != None):
                                        tracker3 = gametiles.tiles(radarblips.blips[x]["current location"]["connected to"][2])
                                        c3 += 1

                                    if (tracker4 != None):
                                        tracker4 = gametiles.tiles(radarblips.blips[x]["current location"]["connected to"][3])
                                        c4 += 1

                                if (tracker1 == squad[y]["current_place"]):
                                    if (gametiles.tiles(radarblips.blips[x]["current location"]["connected to"][0])["occupied"] != True):
                                        radarblips.check_for_reveal(radarblips.blips[x])
                                        radarblips.blips[x]["current location"] = gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][0]
                                        radarblips.blips[x]["action points"] -= 1
                                    else:
                                        for b in radarblips.blips:
                                            if (radarblips.blips[b] != radarblips.blips[x]):
                                                if (radarblips.blips[b]["current location"] == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][0]):
                                                    break
                                            
                                        for c in genestealers:
                                            if (genestealers[c]["current location"] == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][0]):
                                                break

                                        for d in squad:
                                            if (squad[d]["current_place"] == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][0]):
                                                if (radarblips.blips[x]["action points"] > 0):
                                                    while (radarblips.blips[x]["action points"] > 0 or squad[d]["alive"] == True):
                                                        attackaction.close_combat(game.command_points,
                                                                                    squad[d]["action points"],
                                                                                    squad[d]["current_place"],
                                                                                    squad[d]["direction"],
                                                                                    squad[d]["alive"],
                                                                                    squad[d]["weapon loadout"])
                                                    break
                                elif (tracker2 == squad[y]["current_place"]):
                                    if (gametiles.tiles(radarblips.blips[x]["current location"]["connected to"][1])["occupied"] != True):
                                        radarblips.check_for_reveal(radarblips.blips[x])
                                        radarblips.blips[x]["current location"] = gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][1]
                                        radarblips.blips[x]["action points"] -= 1
                                    else:
                                        for b in radarblips.blips:
                                            if (radarblips.blips[b] != radarblips.blips[x]):
                                                if (radarblips.blips[b]["current location"] == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][1]):
                                                    break
                                            
                                        for c in genestealers:
                                            if (genestealers[c]["current location"] == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][1]):
                                                break

                                        for d in squad:
                                            if (squad[d]["current_place"] == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][1]):
                                                if (radarblips.blips[x]["action points"] > 0):
                                                    while (radarblips.blips[x]["action points"] > 0 or squad[d]["alive"] == True):
                                                        attackaction.close_combat(game.command_points,
                                                                                    squad[d]["action points"],
                                                                                    squad[d]["current_place"],
                                                                                    squad[d]["direction"],
                                                                                    squad[d]["alive"],
                                                                                    squad[d]["weapon loadout"])
                                                    break
                                elif (tracker3 == squad[y]["current_place"]):
                                    if (gametiles.tiles(radarblips.blips[x]["current location"]["connected to"][2])["occupied"] != True):
                                        radarblips.check_for_reveal(radarblips.blips[x])
                                        radarblips.blips[x]["current location"] = gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][2]
                                        radarblips.blips[x]["action points"] -= 1
                                    else:
                                        for b in radarblips.blips:
                                            if (radarblips.blips[b] != radarblips.blips[x]):
                                                if (radarblips.blips[b]["current location"] == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][2]):
                                                    break
                                            
                                        for c in genestealers:
                                            if (genestealers[c]["current location"] == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][2]):
                                                break

                                        for d in squad:
                                            if (squad[d]["current_place"] == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][2]):
                                                if (radarblips.blips[x]["action points"] > 0):
                                                    while (radarblips.blips[x]["action points"] > 0 or squad[d]["alive"] == True):
                                                        attackaction.close_combat(game.command_points,
                                                                                    squad[d]["action points"],
                                                                                    squad[d]["current_place"],
                                                                                    squad[d]["direction"],
                                                                                    squad[d]["alive"],
                                                                                    squad[d]["weapon loadout"])
                                                    break
                                elif (tracker4 == squad[y]["current_place"]):
                                    if (gametiles.tiles(radarblips.blips[x]["current location"]["connected to"][3])["occupied"] != True):
                                        radarblips.check_for_reveal(radarblips.blips[x])
                                        radarblips.blips[x]["current location"] = gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][3]
                                        radarblips.blips[x]["action points"] -= 1
                                    else:
                                        for b in radarblips.blips:
                                            if (radarblips.blips[b] != radarblips.blips[x]):
                                                if (radarblips.blips[b]["current location"] == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][3]):
                                                    break
                                            
                                        for c in genestealers:
                                            if (genestealers[c]["current location"] == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][3]):
                                                break

                                        for d in squad:
                                            if (squad[d]["current_place"] == gametiles.tiles(radarblips.blips[x]["current location"])["connected to"][3]):
                                                if (radarblips.blips[x]["action points"] > 0):
                                                    while (radarblips.blips[x]["action points"] > 0 or squad[d]["alive"] == True):
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
                    for g in linesight.line_of_sight:
                        for h in linesight.line_of_sight[g]:
                            if (genestealers[e]["current location"] == linesight.line_of_sight[g][h]):
                                tracker1 = gametiles.tiles(genestealers[e]["current location"])["connected to"][0]
                                if (gametiles.tiles(genestealers[e]["current location"])["connected to"][1]):
                                    tracker2 = gametiles.tiles(genestealers[e]["current location"])["connected to"][1]
                                if (gametiles.tiles(genestealers[e]["current location"])["connected to"][2]):
                                    tracker3 = gametiles.tiles(genestealers[e]["current location"])["connected to"][2]
                                if (gametiles.tiles(genestealers[e]["current location"])["connected to"][3]):
                                    tracker4 = gametiles.tiles(genestealers[e]["current location"])["connected to"][3]

                                while (tracker1 != squad[f]["current_place"] or tracker2 != squad[f]["current_place"] or tracker3 != squad[f]["current_place"] or tracker4 != squad[f]["current_place"]):
                                    tracker1 = gametiles.tiles(genestealers[e]["current location"]["connected to"][0])
                                    c1 += 1

                                    if (tracker2 != None):
                                        tracker2 = gametiles.tiles(genestealers[e]["current location"]["connected to"][1])
                                        c2 += 1

                                    if (tracker3 != None):
                                        tracker3 = gametiles.tiles(genestealers[e]["current location"]["connected to"][2])
                                        c3 += 1

                                    if (tracker4 != None):
                                        tracker4 = gametiles.tiles(genestealers[e]["current location"]["connected to"][3])
                                        c4 += 1

                                if (tracker1 == squad[y]["current_place"]):
                                    if (gametiles.tiles(genestealers[e]["current location"]["connected to"][0])["occupied"] != True):
                                        genestealers[e]["current location"] = gametiles.tiles(genestealers[e]["current location"])["current location"][0]
                                        genestealers[e]["action points"] -= 1
                                        overwatchfire.check_for_overwatch(genestealers.genestealers[e])
                                        direction_change(genestealers[e], tracker1, gametiles.tiles(genestealers[e]["current location"])[0])
                                    else:
                                        for i in genestealers:
                                            if (genestealers[i] != genestealers[e]):
                                                if (genestealers[i]["current location"] == gametiles.tiles(genestealers[e]["current location"])["connected to"][0]):
                                                    break

                                        for j in radarblips.blips:
                                            if (radarblips.blips[j]["current location"] == gametiles.tiles(genestealers[e]["current location"])["connected to"][0]):
                                                break

                                        for k in squad:
                                            if (squad[k]["current_place"] == gametiles.tiles(genestealers[e]["current location"])["connected to"][0]):
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
                                    if (gametiles.tiles(genestealers[e]["current location"]["connected to"][1])["occupied"] != True):
                                        genestealers[e]["current location"] = gametiles.tiles(genestealers[e]["current location"])["current location"][1]
                                        genestealers[e]["action points"] -= 1
                                        overwatchfire.check_for_overwatch(genestealers.genestealers[e])
                                        direction_change(genestealers[e], tracker1, gametiles.tiles(genestealers[e]["current location"])[1])
                                    else:
                                        for i in genestealers:
                                            if (genestealers[i] != genestealers[e]):
                                                if (genestealers[i]["current location"] == gametiles.tiles(genestealers[e]["current location"])["connected to"][1]):
                                                    break

                                        for j in radarblips.blips:
                                            if (radarblips.blips[j]["current location"] == gametiles.tiles(genestealers[e]["current location"])["connected to"][1]):
                                                break

                                        for k in squad:
                                            if (squad[k]["current_place"] == gametiles.tiles(genestealers[e]["current location"])["connected to"][1]):
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
                                    if (gametiles.tiles(genestealers[e]["current location"]["connected to"][2])["occupied"] != True):
                                        genestealers[e]["current location"] = gametiles.tiles(genestealers[e]["current location"])["current location"][2]
                                        genestealers[e]["action points"] -= 1
                                        overwatchfire.check_for_overwatch(genestealers.genestealers[e])
                                        direction_change(genestealers[e], tracker1, gametiles.tiles(genestealers[e]["current location"])[2])
                                    else:
                                        for i in genestealers:
                                            if (genestealers[i] != genestealers[e]):
                                                if (genestealers[i]["current location"] == gametiles.tiles(genestealers[e]["current location"])["connected to"][2]):
                                                    break

                                        for j in radarblips.blips:
                                            if (radarblips.blips[j]["current location"] == gametiles.tiles(genestealers[e]["current location"])["connected to"][2]):
                                                break

                                        for k in squad:
                                            if (squad[k]["current_place"] == gametiles.tiles(genestealers[e]["current location"])["connected to"][2]):
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
                                    if (gametiles.tiles(genestealers[e]["current location"]["connected to"][3])["occupied"] != True):
                                        genestealers[e]["current location"] = gametiles.tiles(genestealers[e]["current location"])["current location"][3]
                                        genestealers[e]["action points"] -= 1
                                        overwatchfire.check_for_overwatch(genestealers.genestealers[e])
                                        direction_change(genestealers[e], tracker1, gametiles.tiles(genestealers[e]["current location"])[3])
                                    else:
                                        for i in genestealers:
                                            if (genestealers[i] != genestealers[e]):
                                                if (genestealers[i]["current location"] == gametiles.tiles(genestealers[e]["current location"])["connected to"][3]):
                                                    break

                                        for j in radarblips.blips:
                                            if (radarblips.blips[j]["current location"] == gametiles.tiles(genestealers[e]["current location"])["connected to"][3]):
                                                break

                                        for k in squad:
                                            if (squad[k]["current_place"] == gametiles.tiles(genestealers[e]["current location"])["connected to"][3]):
                                                if (genestealers[e]["action points"] > 0):
                                                    while (genestealers[e]["action points"] > 0 or squad[k]["alive"] == True):
                                                        attackaction.close_combat(game.command_points,
                                                                                    squad[k]["action points"],
                                                                                    squad[k]["current_place"],
                                                                                    squad[k]["direction"],
                                                                                    squad[k]["alive"],
                                                                                    squad[k]["weapon loadout"])
                                                    break

def direction_change(stealer, tracker, tile):
    turn = False
    for a in tile["connected to"]:
        if (tile["connected to"][a] == stealer["current direction"]):
            turn == False
            continue
        else:
            turn = True
    
    if (turn == True):
        if (tracker == gametiles.tiles(stealer["current location"]["connected to"][0])):
            stealer["direction"] = gametiles.tiles.get(tile[0])
            stealer["action points"] -= 1
            overwatchfire.check_for_overwatch(stealer)
        elif (tracker == gametiles.tiles(stealer["current location"]["connected to"][1])):
            stealer["direction"] = gametiles.tiles.get(tile[1])
            stealer["action points"] -= 1
            overwatchfire.check_for_overwatch(stealer)
        elif (tracker == gametiles.tiles(stealer["current location"]["connected to"][2])):
            stealer["direction"] = gametiles.tiles.get(tile[2])
            stealer["action points"] -= 1
            overwatchfire.check_for_overwatch(stealer)
        elif (tracker == gametiles.tiles(stealer["current location"]["connected to"][3])):
            stealer["direction"] = gametiles.tiles.get(tile[3])
            stealer["action points"] -= 1
            overwatchfire.check_for_overwatch(stealer)