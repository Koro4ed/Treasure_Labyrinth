import random

from constants import RANDOM_EVENTS, ROOMS, TRAP_DAMAGE


def move_player(current_room, direction, player):
    if direction in ROOMS[current_room]["exits"]:
        new_room = ROOMS[current_room]["exits"][direction]
        player["room"] = new_room
        trigger_random_event(player)
        check_trap(new_room, player)
        return True
    return False


def look_around(current_room):
    room_info = ROOMS[current_room]
    description = room_info["description"]
    exits = ", ".join(room_info["exits"].keys())
    items = ", ".join(room_info["items"]) if room_info["items"] else "none"

    result = f"{description}\n"
    result += f"Exits: {exits}\n"
    result += f"Items: {items}\n"

    if "riddle" in room_info:
        result += "There is a riddle here waiting to be solved!\n"

    return result


def take_item(current_room, item_name, player):
    room_items = ROOMS[current_room]["items"]
    if item_name in room_items:
        room_items.remove(item_name)
        player["inventory"].append(item_name)
        return True
    return False


def use_item(item_name, player, current_room):
    if item_name in player["inventory"]:
        if item_name == "potion":
            player["health"] = min(player["health"] + 20, 100)
            player["inventory"].remove(item_name)
            return (
                f"You drink the potion and restore 20 health! "
                f"Current health: {player['health']}"
            )
        elif item_name == "key" and current_room == "fountain":
            player["game_over"] = True
            player["victory"] = True
            return (
                "You use the golden key at the fountain! A portal opens and "
                "you escape the labyrinth! VICTORY!"
            )
        elif item_name == "torch":
            return "The torch illuminates dark corners, but reveals nothing new."
        elif item_name == "sword":
            return "You swing the sword. It feels powerful in your hands."
        else:
            return f"You use the {item_name}, but nothing special happens."
    return f"You don't have {item_name} in your inventory."


def solve_riddle(current_room, answer, player):
    room_info = ROOMS[current_room]
    if "riddle" in room_info:
        riddle = room_info["riddle"]
        if answer.lower() == riddle["answer"].lower():
            reward = riddle["reward"]
            player["inventory"].append(reward)
            del room_info["riddle"]
            return f"Correct! The riddle is solved. You receive: {reward}"
        else:
            return "Wrong answer! Try again."
    return "There is no riddle to solve here."


def show_inventory(player):
    if player["inventory"]:
        return "Inventory: " + ", ".join(player["inventory"])
    return "Your inventory is empty."


def trigger_random_event(player):
    if random.random() < 0.3:
        event = random.choice(RANDOM_EVENTS)
        print(f"\n*** {event} ***\n")


def check_trap(room, player):
    room_info = ROOMS[room]
    if room_info.get("trap", False) and random.random() < 0.5:
        player["health"] -= TRAP_DAMAGE
        print(
            f"\n*** TRAP! You take {TRAP_DAMAGE} damage! "
            f"Health: {player['health']} ***\n"
        )
        if player["health"] <= 0:
            player["game_over"] = True
            print("You have been defeated by the labyrinth's traps!")
