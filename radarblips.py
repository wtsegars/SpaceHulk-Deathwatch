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
                else:
                    blip["current_location"] = b[tile_choice]
                    c[b[tile_choice]]["occupied"] = True
                    blips[f"Blip{a}"]["current_location"] = c[b[tile_choice]
                    blips[f"Blip{a}"]["hidden"] = True
                    blips[f"Blip{a}"]["action_points"] = 6
                    blip.clear()
                    a -= 1
            elif b[tile_choice] == "g5":
                if c["g6"]["occupied"] == True or c["g7"]["occupied"] == True:
                    for x in d:
                        if d[x]["current_place"] == "g6" or d[x]["current_place"] == "g7":
                            if d[x]["direction"] != "south":
                                blip["current_location"] = b[tile_choice]
                                c[b[tile_choice]]["occupied"] = True
                                blips[f"Blip{a}"]["current_location"] = c[b[tile_choice]
                                blips[f"Blip{a}"]["hidden"] = True
                                blips[f"Blip{a}"]["action_points"] = 6
                                blip.clear()
                                a -= 1
                else:
                    blip["current_location"] = b[tile_choice]
                    c[b[tile_choice]]["occupied"] = True
                    blips[f"Blip{a}"]["current_location"] = c[b[tile_choice]
                    blips[f"Blip{a}"]["hidden"] = True
                    blips[f"Blip{a}"]["action_points"] = 6
                    blip.clear()
                    a -= 1
            elif b[tile_choice] == "g9":
                if c["g10"]["occupied"] == True or c["c2"]["occupied"] == True or c["g12"]["occupied"] == True or c["g11"]["occupied"] == True:
                    for x in d:
                        if d[x]["current_place"] == "g10" or d[x]["current_place"] == "c2" or d[x]["current_place"] == "g12" or d[x]["current_place"] == "g11":
                            if d[x]["direction"] != "west":
                                blip["current_location"] = b[tile_choice]
                                c[b[tile_choice]]["occupied"] = True
                                blips[f"Blip{a}"]["current_location"] = c[b[tile_choice]
                                blips[f"Blip{a}"]["hidden"] = True
                                blips[f"Blip{a}"]["action_points"] = 6
                                blip.clear()
                                a -= 1
                else:
                    blip["current_location"] = b[tile_choice]
                    c[b[tile_choice]]["occupied"] = True
                    blips[f"Blip{a}"]["current_location"] = c[b[tile_choice]
                    blips[f"Blip{a}"]["hidden"] = True
                    blips[f"Blip{a}"]["action_points"] = 6
                    blip.clear()
                    a -= 1
            elif b[tile_choice] == "g11":
                if c["g12"]["occupied"] == True or c["c2"]["occupied"] == True or c["g10"]["occupied"] == True or c["g9"]["occupied"] == True:
                    for x in d:
                        if d[x]["current_place"] == "g12" or d[x]["current_place"] == "c2" or d[x]["current_place"] == "g10" or d[]["current_place"] == "g9":
                            if d[x]["direction"] != "east":
                                blip["current_location"] = b[tile_choice]
                                c[b[tile_choice]]["occupied"] = True
                                blips[f"Blip{a}"]["current_location"] = c[b[tile_choice]
                                blips[f"Blip{a}"]["hidden"] = True
                                blips[f"Blip{a}"]["action_points"] = 6
                                blip.clear()
                                a -= 1
                else:
                    blip["current_location"] = b[tile_choice]
                    c[b[tile_choice]]["occupied"] = True
                    blips[f"Blip{a}"]["current_location"] = c[b[tile_choice]
                    blips[f"Blip{a}"]["hidden"] = True
                    blips[f"Blip{a}"]["action_points"] = 6
                    blip.clear()
                    a -= 1