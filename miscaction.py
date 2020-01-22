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
                    )
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

    def reload(a, b):
