import attackaction
import radarblips
import genestealers
import gametiles
import linesight
import squad

#a = radarblips.blips
#b = genestealers.genestealers
#c = gametiles.tiles
#d = linesight.line_of_sight
#e = squad.squad

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
                                if (squad[y]["current_place"] == linesight[z][a]):
                                    tracker1 == gametiles(squad[y]["current_place"])