import game
import gametiles
from random import randint

blips = {
    
}

def blip_deployment(a, b, c, d):
    while a > 0:
        blip = {}
        tile_choice = randint(0, 9)
        
        