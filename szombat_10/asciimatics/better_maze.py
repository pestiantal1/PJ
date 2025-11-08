from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
import sys
import random

MAZE = [
    "####################",
    "#..................#",
    "#.####.####.####.#.#",
    "#.#..#.#..#.#....#.#",
    "#.#..#.#..#.#.####.#",
    "#....#....#.#......#",
    "#.#########.#.####.#",
    "#.#.........#....#.#",
    "#.#.#######.####.#.#",
    "#...#.......#....#.#",
    "#.###.#####.#.####.#",
    "#.#...#...#.#......#",
    "#.#.###.#.#.#######.",
    "#.......#..........#",
    "####################"
]

PLAYER_CHAR = 'P'
ITEM_CHAR = 'X'
WALL_CHAR = '#'
EMPTY_CHAR = '.'

player_pos = [1, 1]
item_positions = []
collected_items = 0
total_items = 5  # Ennyi kincset kell összegyűjteni

def initialize_items(maze, count):
    """Véletlenszerűen elhelyez kincseket üres cellákra"""
    items = []
    empty_cells = []
    
    # Üres cellák gyűjtése
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == EMPTY_CHAR and [y, x] != player_pos:
                empty_cells.append([y, x])
    
    # Véletlenszerű kincsek elhelyezése
    if len(empty_cells) >= count:
        items = random.sample(empty_cells, count)
    
    return items

def draw_cell(screen, char, pos):
    screen.print_at(char, pos[1], pos[0])

def move_player(key, player_pos, maze):
    new_pos = player_pos[:]
    if key in ('w', 'W'):  # Fel
        new_pos[0] -= 1
    elif key in ('s', 'S'):  # Le
        new_pos[0] += 1
    elif key in ('a', 'A'):  # Balra
        new_pos[1] -= 1
    elif key in ('d', 'D'):  # Jobbra
        new_pos[1] += 1

    # Ha falba ütközne a játékos, ne engedjük a mozgást
    if maze[new_pos[0]][new_pos[1]] != WALL_CHAR:
        return new_pos
    return player_pos

def game(screen: Screen):
    global player_pos, item_positions, collected_items
    
    # Kincsek inicializálása
    item_positions = initialize_items(MAZE, total_items)
    collected_items = 0

    # Pálya kirajzolása
    for y, row in enumerate(MAZE):
        for x, char in enumerate(row):
            screen.print_at(char, x, y)

    # Játékos és kincsek kirajzolása
    draw_cell(screen, PLAYER_CHAR, player_pos)
    for item_pos in item_positions:
        draw_cell(screen, ITEM_CHAR, item_pos)
    
    # Státusz kiírása
    screen.print_at(f"Kincsek: {collected_items}/{total_items}", 0, len(MAZE) + 1)
    screen.refresh()

    while True:
        event = screen.get_event()
        if isinstance(event, KeyboardEvent):
            key = chr(event.key_code)
            if key in ('q', 'Q'):  # Kilépés
                sys.exit(0)

            new_pos = move_player(key, player_pos, MAZE)

            if new_pos != player_pos:
                # Régi pozíció törlése
                draw_cell(screen, MAZE[player_pos[0]][player_pos[1]], player_pos)

                # Új pozíció rajzolása
                draw_cell(screen, PLAYER_CHAR, new_pos)
                
                player_pos = new_pos

                # Kincs felvétele
                if player_pos in item_positions:
                    item_positions.remove(player_pos)
                    collected_items += 1
                    screen.print_at(f"Kincsek: {collected_items}/{total_items}", 0, len(MAZE) + 1)
                
                screen.refresh()

            # Győzelem ellenőrzése
            if collected_items == total_items:
                screen.clear()
                screen.print_at("Gratulálok! Összeszedtél minden kincset!", 0, 0)
                screen.print_at("Nyomd meg a Q-t a kilépéshez.", 0, 1)
                screen.refresh()
                while True:
                    event = screen.get_event()
                    if isinstance(event, KeyboardEvent) and chr(event.key_code) in ('q', 'Q'):
                        sys.exit(0)


Screen.wrapper(game)