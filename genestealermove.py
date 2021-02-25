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

def genestealer_movement(a, d, e):
    for x in a: #looping through radar blips
        while a[x]["action points"] > 0:
            if (a[x]["current location"]):
                