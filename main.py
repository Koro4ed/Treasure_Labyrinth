from player_actions import (
    look_around,
    move_player,
    show_inventory,
    solve_riddle,
    take_item,
    use_item,
)
from utils import display_help, display_welcome, parse_command


def initialize_player():
    return {
        "room": "start",
        "inventory": [],
        "health": 100,
        "game_over": False,
        "victory": False
    }

def process_command(command_type, argument, player):
    current_room = player["room"]

    if command_type == "move":
        if argument:
            if move_player(current_room, argument, player):
                print(f"You move {argument}.")
                print(look_around(player["room"]))
            else:
                print(f"You cannot go {argument} from here.")
        else:
            print("Please specify a direction.")

    elif command_type == "look":
        print(look_around(current_room))

    elif command_type == "take":
        if argument:
            if take_item(current_room, argument, player):
                print(f"You take the {argument}.")
            else:
                print(f"There is no {argument} here.")
        else:
            print("Please specify an item to take.")

    elif command_type == "use":
        if argument:
            result = use_item(argument, player, current_room)
            print(result)
        else:
            print("Please specify an item to use.")

    elif command_type == "inventory":
        print(show_inventory(player))

    elif command_type == "solve":
        if argument:
            result = solve_riddle(current_room, argument, player)
            print(result)
        else:
            print("Please provide an answer to the riddle.")

    elif command_type == "quit":
        player["game_over"] = True
        print("Thanks for playing!")

    else:
        print("Unknown command. Type 'help' for available commands.")

def main():
    player = initialize_player()
    display_welcome()
    print(look_around(player["room"]))

    while not player["game_over"]:
        try:
            user_input = input(f"\nHealth: {player['health']} > ").strip()

            if user_input.lower() == "help":
                display_help()
                continue

            command_type, argument = parse_command(user_input)

            if command_type is None:
                print("Unknown command. Type 'help' for available commands.")
                continue

            process_command(command_type, argument, player)

        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")
            break
        except EOFError:
            print("\n\nGame ended. Thanks for playing!")
            break

    if player.get("victory", False):
        print("\n🎉 Congratulations! You have won the game! 🎉")
    else:
        print("\nGame over. Better luck next time!")

if __name__ == "__main__":
    main()
