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

def genestealer_movement(a, b, c, d, e):
    for x in a: #looping through radar blips
        while a[x]["action_points"] > 0:
            for y in d: #looping through line of sight to locate radar blips
                for z in d[y]: #looping through specicic tiles in each individual line of sight
                    if d[y][z] == a[x]["current_place"]:
                        for w in e: #looping through terminator squad
                            for v in d[y]: #looping through each individual tile in line of sight
                                if e[w]["current_place"] == d[y][v]:
                                    radarblips.blip_reveal(a[x])