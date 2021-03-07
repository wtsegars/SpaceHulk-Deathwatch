import game
import attackaction
import radarblips
import genestealers
import gametiles
import linesight
import squad

def genestealer_movement():
    for x in radarblips: #looping through radar blips
        while radarblips[x]["action points"] > 0:
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
                                        tracker1 == gametiles(radarblips[x]["current location"]["connected to"][0])["connected to"][0]
                                        c1 += 1

                                        if (tracker2 != None):
                                            tracker2 == gametiles(radarblips[x]["current location"]["connected to"][1])["connected to"][1]
                                            c2 += 1

                                        if (tracker3 != None):
                                            tracker3 == gametiles(radarblips[x]["current location"]["connected to"][2])["connected to"][2]
                                            c3 += 1

                                        if (tracker4 != None):
                                            tracker4 == gametiles(radarblips[x]["current location"]["connected to"][3])["connected to"][3]
                                            c4 += 1

                                    if (tracker1 == squad[y]["current_place"]):
                                        if (gametiles(radarblips[x]["current location"]["connected to"][0])["occupied"] != True):
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
                                                    attackaction.close_combat(game.command_points,
                                                                                squad[d]["action points"],
                                                                                squad[d]["current_place"],
                                                                                squad[d]["direction"],
                                                                                squad[d]["alive"],
                                                                                squad[d]["weapon loadout"])
                                                    break