import game
import gametiles

blips = {
    
}

def blip_deployment(a, b, c, d):
    while a > 0:
        blip = {}
        tile_choice = randint(0, 9)
        
        if c[b[tile_choice]]["occupied"] == False:
            blip["current_location"] = b[tile_choice]
            c[b[tile_choice]]["occupied"] = True
            blips[f"Blip{a}"]["current_location"] = c[b[tile_choice]
            blip.clear()
            a -= 1