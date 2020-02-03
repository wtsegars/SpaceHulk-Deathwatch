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
            elif b[tile_choice] == "g13":
                if c["g14"]["occupied"] == True or c["c6"]["occupied"] == True or c["g16"]["occupied"] == True or c["g15"]["occupied"] == True:
                    for x in d:
                        if d[x]["current_place"] == "g14" or d[x]["current_place"] == "c6" or d[x]["current_place"] == "g16" or d[x]["current_place"] == "g15":
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
            elif b[tile_choice] == "g15":
                if c["g16"]["occupied"] == True or c["c6"]["occupied"] == True or c["g14"]["occupied"] == True or c["g13"]["occupied"] == True:
                    for x in d:
                        if d[x]["current_place"] == "g16" or d[x]["current_place"] == "c6" or d[x]["current_place"] == True or d[x]["current_place"] == "g14" or d[x]["current_place"] == "g13":
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
            elif b[tile_choice] == "g17":
                if c["g18"]["occupied"] == True or c["c7"]["occupied"] == True or c["g20"]["occupied"] == True or c["g20"]["occupied"] == True or c["g19"]["occupied"] == True:
                    for x in d:
                        if d[x]["current_place"] == "g18" or d[x]["current_place"] == "c7" or d[x]["current_place"] == "g20" or d[x]["current_place"] == "g19":
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
            elif b[tile_choice] == "g19":
                if c["g20"]["occupied"] == True or c["c7"]["occupied"] == True or c["g18"]["occupied"] == True or c["g17"]["occupied"] == True:
                    for x in d:
                        if d[x]["current_place"] == "g20" or d[x]["current_place"] == "c7" or d[x]["current_place"] == "g18" or d[x]["current_place"] == "g17":
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