import radarblips
import move
import game
import spacemarineturn

class GenestealerTurn():
    blips_to_deploy = 0

    def enter(turn_count):
        print("Genestealers are now moving.")
        print("(press enter to continue)")
        input('')
        turn_count += 1
        GenestealerTurn.blip_count()
        radarblips.RadarBlips.blip_deployment(GenestealerTurn.blips_to_deploy)
        move.GenestealerMove.genestealer_movement()

    def blip_count():
        if game.turn_count <= 2:
            GenestealerTurn.blips_to_deploy += 3
        elif 2 < game.turn_count <= 4:
            GenestealerTurn.blips_to_deploy += 2
        elif game.turn_count > 5:
            GenestealerTurn.blips_to_deploy += 1

    def end_turn():
        print("End of Genestealer turn.")
        print("(press enter to continue)")
        input('')
        return spacemarineturn.enter(game.turn_count)