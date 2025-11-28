#!/bin/bash

echo "Подготовка к записи asciinema..."
echo "Эта запись продемонстрирует:"
echo "!!! Запуск игры"
echo "!!! Перемещение между комнатами"
echo "!!! Команды look и inventory"
echo "!!! Взятие предметов"
echo "!!! Решение загадки"
echo "!!! Использование предметов"
echo "!!! Условие победы"
echo ""

echo "Начинаем запись через 3 секунды..."
sleep 3

# Записываем asciinema
asciinema rec treasure_labyrinth_perfect.cast -c "./demo_robust.sh"

echo ""
echo "Запись сохранена в treasure_labyrinth_perfect.cast"
echo "Для загрузки выполните: asciinema upload treasure_labyrinth_perfect.cast"
