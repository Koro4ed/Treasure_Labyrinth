# Treasure Labyrinth

A text-based adventure game where you explore a mysterious labyrinth, solve riddles, and find treasure!

## Description

Navigate through rooms, collect items, solve puzzles, and avoid traps to find the treasure and escape the labyrinth.

## Installation

1. Ensure you have Python 3.8+ installed
2. Install Poetry: `pip install poetry`
3. Clone the repository: `git clone https://github.com/Koro4ed/Treasure_Labyrinth.git`
4. Navigate to the project directory: `cd Treasure_Labyrinth`
5. Install dependencies: `make install`

## How to Play

Run the game: `poetry run treasure-labyrinth`

### Commands:
- `go <direction>` - Move north, south, east, or west
- `look` - Examine the current room
- `take <item>` - Pick up an item
- `use <item>` - Use an item from your inventory
- `inventory` - Check your inventory
- `solve <answer>` - Solve a riddle
- `quit` - Exit the game
- `help` - Show available commands

### Win Conditions:
- Find the riddle in the library and solve it to get the key
- Use the key at the fountain to escape and win!

## Development

- Install project: `make project`
- Run linter: `make lint`
- Build package: `make build`

## Gameplay Recording

https://asciinema.org/connect/f852f1fe-2184-4163-8280-ded9f7c4950f

