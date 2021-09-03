import gametiles
import squad
import genestealers
import linesight
import overwatchfire
from random import randint

class RadarBlips():
    genestealer_count = 0

    blips = {
        
    }

    def blip_deployment(a):
        while a > 0:
            blip = {
                f"blip {a}": {
                    "current location": None,
                    "action points": 0
                }
            }

            tile_choice = randint(1, 8)
            deploy_tile = ""

            print(tile_choice)
            
            if tile_choice == 1:
                deploy_tile += "g1"
            elif tile_choice == 2:
                deploy_tile += "g5"
            elif tile_choice == 3:
                deploy_tile += "g9"
            elif tile_choice == 4:
                deploy_tile += "g11"
            elif tile_choice == 5:
                deploy_tile += "g19"
            elif tile_choice == 6:
                deploy_tile += "g17"
            elif tile_choice == 7:
                deploy_tile += "g23"
            elif tile_choice == 8:
                deploy_tile += "g21"

            print(a)
            print(deploy_tile)
            #print(gametiles.tiles[deploy_tile])

            if gametiles.tiles[deploy_tile]["occupied"] == True:
                RadarBlips.blip_deployment(a)
            elif gametiles.tiles[deploy_tile]["occupied"] == False:
                gametiles.tiles[deploy_tile]["occupied"] = True
                blip[f"blip {a}"]["current location"] = deploy_tile
                blip[f"blip {a}"]["action points"] += 6
                RadarBlips.blips[f"blip {a}"] = {}
                RadarBlips.blips[f"blip {a}"]["current location"] = blip[f"blip {a}"]["current location"]
                RadarBlips.blips[f"blip {a}"]["action points"] = blip[f"blip {a}"]["action points"]
                a -= 1

    def blip_reveal(a, b, genestealer_count):
        blip_num = randint(0, 3)
        new_genestealer = {}
        if (blip_num == 1):
            new_genestealer["current location"] = RadarBlips.blips[a]["current location"]
            new_genestealer["action points"] = RadarBlips.blips[a]["action points"]
            if (b["direction"] == "north"):
                new_genestealer["direction"] = "south"
            elif (b["direction"] == "south"):
                new_genestealer["direction"] = "north"
            elif (b["direction"] == "west"):
                new_genestealer["direction"] = "east"
            elif (b["direction"] == "east"):
                new_genestealer["direction"] = "west"
            genestealers.genestealers[f"Genestealer {genestealer_count}"] = new_genestealer

            new_genestealer.clear()
            genestealer_count += 1

            if (b["overwatch"] == True):
                overwatchfire.overwatch_fire(b, genestealers[f"Genestealer {genestealer_count}"])
            
        elif (blip_num == 2):
            for g in range(1, 3):
                new_genestealer["current location"] = RadarBlips.blips[a]["current location"]
                new_genestealer["action points"] = RadarBlips.blips[a]["action points"]
                if (b["direction"] == "north"):
                    new_genestealer["direction"] = "south"
                elif (b["direction"] == "south"):
                    new_genestealer["direction"] = "north"
                elif (b["direction"] == "west"):
                    new_genestealer["direction"] = "east"
                elif (b["direction"] == "east"):
                    new_genestealer["direction"] = "west"
                genestealers.genestealers[f"Genestealer {genestealer_count}"] = new_genestealer

                new_genestealer.clear()
                genestealer_count += 1

                if (g == 1 and b["overwatch"] == True):
                    overwatchfire.overwatch_fire(b, genestealers[f"Genestealer {genestealer_count}"])

        elif (blip_num == 3):
            for g in range(1, 4):
                new_genestealer["current location"] = RadarBlips.blips[a]["current location"]
                new_genestealer["action points"] = RadarBlips.blips[a]["action points"]
                if (b["direction"] == "north"):
                    new_genestealer["direction"] = "south"
                elif (b["direction"] == "south"):
                    new_genestealer["direction"] = "north"
                elif (b["direction"] == "west"):
                    new_genestealer["direction"] = "east"
                elif (b["direction"] == "east"):
                    new_genestealer["direction"] = "west"
                genestealers.genestealers[f"Genestealer {genestealer_count}"] = new_genestealer

                new_genestealer.clear()
                genestealer_count += 1

                if (g == 1 and b["overwatch"] == True):
                    overwatchfire.overwatch_fire(b, genestealers[f"Genestealer {genestealer_count}"])

    def check_for_reveal(blip):
        for c in linesight.line_of_sight:
            for d in linesight.line_of_sight[c]:
                if gametiles(linesight.line_of_sight[c][d])["occupied"] == True:
                    for e in squad:
                        if squad[e]["current_place"] == gametiles(linesight[c][d]):
                            if linesight[c] == linesight.line_of_sight[0] or linesight[c] == linesight.line_of_sight[2] or linesight[c] == linesight.line_of_sight[3] or linesight[c] == linesight.line_of_sight[4] or linesight[c] == linesight.line_of_sight[5] or linesight[c] == linesight.line_of_sight[7] or linesight[c] == linesight.line_of_sight[10]:
                                if squad[e]["direction"] == "north":
                                    sm_index = linesight[c].index(squad[e]["current_place"])
                                    for f in range(d, sm_index, 1):
                                        if linesight[c][f] == blip["current location"]:
                                            RadarBlips.blip_reveal(blip, squad[e], RadarBlips.genestealer_count)
                                if squad[e]["direction"] == "south":
                                    sm_index = linesight[c].index(squad[e]["current_place"])
                                    for g in range(d, sm_index, -1):
                                        if linesight[c][g] == blip["current location"]:
                                            RadarBlips.blip_reveal(blip, squad[e], RadarBlips.genestealer_count)
                            elif linesight[c] == linesight.line_of_sight[1] or linesight[c] == linesight.line_of_sight[6] or linesight[c] == linesight.line_of_sight[8] or linesight[c] == linesight.line_of_sight[9] or linesight[c] == linesight.line_of_sight[11] or linesight[c] == linesight.line_of_sight[12] or linesight[c] == linesight.line_of_sight[13]:
                                if squad[e]["direction"] == "west":
                                    sm_index = linesight[c].index(squad[e]["current_place"])
                                    for h in range(d, sm_index, -1):
                                        if linesight[c][h] == blip["current location"]:
                                            RadarBlips.blip_reveal(blip, squad[e], RadarBlips.genestealer_count)
                                if squad[e]["direction"] == "east":
                                    sm_index = linesight[c].index(squad[e]["current_place"])
                                    for i in range(d, sm_index, 1):
                                        if linesight[c][i] == blip["current location"]:
                                            RadarBlips.blip_reveal(blip, squad[e], RadarBlips.genestealer_count)