from constants import COMMANDS


def parse_command(user_input):
    words = user_input.lower().strip().split()
    if not words:
        return None, None

    command_word = words[0]
    argument = " ".join(words[1:]) if len(words) > 1 else None

    for command_type, aliases in COMMANDS.items():
        if command_word in aliases:
            return command_type, argument

    return None, None


def display_welcome():
    from constants import GAME_DESCRIPTION, GAME_TITLE

    print(f"=== {GAME_TITLE} ===")
    print(GAME_DESCRIPTION)
    print("\nYour goal: Find the treasure and escape through the fountain!")
    print("Type 'help' for available commands.\n")


def display_help():
    print("\n=== HELP ===")
    print("go <direction> - Move in a direction (north, south, east, west)")
    print("look - Examine the current room")
    print("take <item> - Pick up an item")
    print("use <item> - Use an item from inventory")
    print("inventory - Show your items")
    print("solve <answer> - Answer a riddle")
    print("quit - Exit the game")
    print("\nWin conditions:")
    print("- Solve the riddle in the library to get the key")
    print("- Use the key at the fountain to escape")
    print("\nBe careful of traps and manage your health!\n")
