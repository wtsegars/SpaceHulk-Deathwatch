import attackaction
import radarblips
import genestealers
import gametiles
import linesight
import squad

def genestealer_movement(a, b, c, d, e):
    for x in a:
        while a[x]["action_points"] > 0:
            for y in d:
                for z in d[y]:
                    if d[y][z] == a[x]["current_place"]:
                        for w in e:
                            for v in d[y]:
                                if e[w]["current_place"] == d[y][v]:
                                    