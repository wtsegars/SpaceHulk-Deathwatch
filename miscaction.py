from textwrap import dedent

def other_action():
    print("What would you like to do?")
    print(dedent("""
            Reload,
            Toggle Door,
            Overwatch,
            Clear Jam
            """))