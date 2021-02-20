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

def blip_reveal(a, b, c):
    blips.pop(a)
    blip_num = randint(0, 3)
    new_genestealer = {}
    if (blip_num == 1):
        new_genestealer["current location"] = 