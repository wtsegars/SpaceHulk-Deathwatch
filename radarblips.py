import game
import gametiles
import squad
import genestealers
from random import randint

genestealer_count = 1

blips = {
    
}

def blip_deployment(a, b):
    while a > 0:
        tile_choice = randint(0, 9)
        deploy_tile = ""
        
        if tile_choice == 1:
            deploy_tile = "g1"
        elif tile_choice == 2:
            deploy_tile = "g5"
        elif tile_choice == 3:
            deploy_tile = "g9"
        elif tile_choice == 4:
            deploy_tile = "g11"
        elif tile_choice == 5:
            deploy_tile = "g19"
        elif tile_choice == 6:
            deploy_tile = "g17"
        elif tile_choice == 7:
            deploy_tile = "g23"
        elif tile_choice == 8:
            deploy_tile = "g21"

        if gametiles[deploy_tile]["occupied"] == True:
            blip_deployment(game.GeneStealerTurn.blips_to_deploy, squad.squad)
        elif gametiles[deploy_tile]["occupied"] == False:
            gametiles[deploy_tile]["occupied"] = True
            blips[f"blip {a}"]["current location"] = deploy_tile
            blips[f"blip {a}"]["action points"] = 6
            a -= 1

def blip_reveal(a, b):
    blip_num = randint(0, 3)
    new_genestealer = {}
    if (blip_num == 1):
        new_genestealer["current location"] = blips[a]["current location"]
        new_genestealer["action points"] = blips[a]["action points"]
        if (b == "north"):
            new_genestealer["direction"] = "south"
        elif (b == "south"):
            new_genestealer["direction"] = "north"
        elif (b == "west"):
            new_genestealer["direction"] = "east"
        elif (b == "east"):
            new_genestealer["direction"] = "west"
        genestealers[f"Genestealer {genestealer_count}"] = new_genestealer

        new_genestealer.clear()
        genestealer_count += 1
    elif (blip_num == 2):
        for g in range(1, 3):
            new_genestealer["current location"] = blips[a]["current location"]
            new_genestealer["action points"] = blips[a]["action points"]
            if (b == "north"):
                new_genestealer["direction"] = "south"
            elif (b == "south"):
                new_genestealer["direction"] = "north"
            elif (b == "west"):
                new_genestealer["direction"] = "east"
            elif (b == "east"):
                new_genestealer["direction"] = "west"
            genestealers[f"Genestealer {genestealer_count}"] = new_genestealer

            new_genestealer.clear()
            genestealer_count += 1
    elif (blip_num == 3):
        for g in range(1, 4):
            new_genestealer["current location"] = blips[a]["current location"]
            new_genestealer["action points"] = blips[a]["action points"]
            if (b == "north"):
                new_genestealer["direction"] = "south"
            elif (b == "south"):
                new_genestealer["direction"] = "north"
            elif (b == "west"):
                new_genestealer["direction"] = "east"
            elif (b == "east"):
                new_genestealer["direction"] = "west"
            genestealers[f"Genestealer {genestealer_count}"] = new_genestealer

            new_genestealer.clear()
            genestealer_count += 1