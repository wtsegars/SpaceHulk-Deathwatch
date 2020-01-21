from textwrap import dedent
import game

def other_action():
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
        reload()
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