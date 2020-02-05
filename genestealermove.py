import attackaction
import radarblips
import genestealers
import gametiles
import linesight

def genestealer_movement(a, b, c, d):
    for x in a:
        while a[x]["action_points"] > 0:
            for y in d:
                for z in d[y]:
                    