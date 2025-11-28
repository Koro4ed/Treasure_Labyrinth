#!/bin/bash

# Создаем файл с командами
cat > game_commands.txt << 'EOF'
look
go east
look
take scroll
inventory
solve echo
inventory
go west
go north
look
go up
go east
look
take herb
inventory
use herb
go north
look
use key
EOF

echo "=== Treasure Labyrinth Complete Demo ==="
echo ""

# Запускаем игру с командами из файла
cat game_commands.txt | poetry run python main.py

echo ""
echo "=== Demo Finished ==="

# Удаляем временный файл
rm -f game_commands.txt
