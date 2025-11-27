GAME_TITLE = "Treasure Labyrinth"
GAME_DESCRIPTION = "Find the treasure and escape the labyrinth!"

ROOMS = {
    "start": {
        "description": "You are in a dark chamber. Torches flicker on the walls.",
        "exits": {"north": "hallway", "east": "library"},
        "items": ["torch"]
    },
    "hallway": {
        "description": "A long hallway stretches before you. Dust covers the floor.",
        "exits": {"south": "start", "west": "armory", "east": "garden"},
        "items": []
    },
    "library": {
        "description": "Bookshelves line the walls.An ancient tome lies open on a desk",
        "exits": {"west": "start", "north": "study"},
        "items": ["scroll"],
        "riddle": {
            "question": (
                "I speak without a mouth and hear without ears. I have no body, "
                "but I come alive with the wind. What am I?"
            ),
            "answer": "echo",
            "reward": "key"
        }
    },
    "armory": {
        "description": "Rusty weapons hang on the walls. A chest sits in the corner.",
        "exits": {"east": "hallway"},
        "items": ["sword"],
        "trap": True
    },
    "garden": {
        "description": "An overgrown garden with strange glowing plants.",
        "exits": {"west": "hallway", "north": "fountain"},
        "items": ["herb"]
    },
    "study": {
        "description": "A wizard's study with potions and strange instruments.",
        "exits": {"south": "library"},
        "items": ["potion"]
    },
    "fountain": {
        "description": "A magical fountain with shimmering water. This is the exit!",
        "exits": {"south": "garden"},
        "items": []
    }
}

COMMANDS = {
    "move": ["go", "move", "walk", "run"],
    "look": ["look", "examine", "view"],
    "take": ["take", "grab", "pick"],
    "use": ["use", "activate", "drink"],
    "inventory": ["inventory", "inv", "items"],
    "solve": ["solve", "answer", "riddle"],
    "quit": ["quit", "exit", "q"]
}

RANDOM_EVENTS = [
    "A bat flies past your head!",
    "You hear distant footsteps...",
    "The torches flicker ominously.",
    "A cold chill runs down your spine.",
    "You hear whispering from the shadows."
]

TRAP_DAMAGE = 10
PLAYER_MAX_HEALTH = 100
