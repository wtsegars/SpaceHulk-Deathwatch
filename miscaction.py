from textwrap import dedent
import game
import squad

def other_action():
    print("Which terminator would you like to take action?")
    for x in squad:
        if squad[x]["action points"] > 0 and squad[x]["alive"] == True:
            print(squad[x])
    
    term_choice = input("> ")

    if term_choice == squad[x]:
        print("What would you like to do?")
        print(dedent("""
                Reload,
                Toggle Door,
                Overwatch,
                Clear Jam,
                Cancel
                """))

        action_choice = input("> ")

        if action_choice == "Reload":
            reload(game.command_points,
                    squad[x]["action points"],
                    squad[x]["clip_size"],
                    squad[x]["clip_num"],
                    squad[x]["weapon loadout"])
        elif action_choice == "Toggle Door":
            toggle_door()
        elif action_choice == "Overwatch":
            overwatch()
        elif action_choice == "Clear Jam":
            clear_jam()
        elif action_choice == "Cancel":
            game.SpaceMarineTurn.enter.turn_menu()
        else:
            print("You have entered an invalid command, please try again.")
            other_action()

def reload(a, b, c, d, e):
    if d == 0:
        print("You don't have any more clips to reload your weapon with.")
        other_action()

    if b >= 4:
        b -= 4
    else:
        diff = 4 - b

        b = 0
        a -= diff

    if e == "Assault Cannon and Powerfist":
        c = 10
        d -= 1
        print("Your assault cannon has been reloaded.")
        other_action()
    elif e == "Heavy Flamer and Powerfist":
        c = 10
        d -= 1
        print("Your heavy flamer has been reloaded.")
        other_action()
    else:
        print("Your don't have a weapon that needs to be reloaded")
        other_action()