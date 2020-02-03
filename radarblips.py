import game
import gametiles

blips = {
    
}

def blip_deployment(a, b, c, d):
    while a > 0:
        blip = {}
        tile_choice = randint(0, 9)
        
        if c[b[tile_choice]]["occupied"] == False:
            if b[tile_choice] == "g1":
                if c["g3"]["occupied"] == True or c["g2"]["occupied"] == True:
                    for x in d:
                        if d[x]["current_place"] == c["g3"] or d[x]["current_place"] == c["g2"]:
                            if d[x]["direction"] != "south":
                                blip["current_location"] = b[tile_choice]
                                c[b[tile_choice]]["occupied"] = True
                                blips[f"Blip{a}"]["current_location"] = c[b[tile_choice]
                                blips[f"Blip{a}"]["hidden"] = True
                                blips[f"Blip{a}"]["action_points"] = 6
                                blip.clear()
                                a -= 1