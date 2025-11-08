from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
import sys

MAZE = [
    "############",
    "#..........#",
    "#.########.#",
    "#..........#",
    "############"
]

PLAYER_CHAR = 'P'
ITEM_CHAR = 'X'
WALL_CHAR = '#'
EMPTY_CHAR = '.'

player_pos = [1, 1]
item_pos = [1, 10]

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
    global player_pos

    for y, row in enumerate(MAZE):
        for x, char in enumerate(row):
            screen.print_at(char, x, y)

    draw_cell(screen, PLAYER_CHAR, player_pos)
    draw_cell(screen, ITEM_CHAR, item_pos)
    screen.refresh()

    while True:
        event = screen.get_event()
        if isinstance(event, KeyboardEvent):
            key = chr(event.key_code)
            if key in ('q', 'Q'):  # Kilépés
                sys.exit(0)

            new_pos = move_player(key, player_pos, MAZE)

            if new_pos != player_pos:
                draw_cell(screen, MAZE[player_pos[0]][player_pos[1]], player_pos)

                draw_cell(screen, PLAYER_CHAR, new_pos)
                screen.refresh()

                player_pos = new_pos

            if player_pos == item_pos:
                screen.clear()
                screen.print_at("Megtaláltad a kincset! Nyomd meg a Q-t a kilépéshez.", 0, 0)
                screen.refresh()
                while True:
                    event = screen.get_event()
                    if isinstance(event, KeyboardEvent) and chr(event.key_code) in ('q', 'Q'):
                        sys.exit(0)


Screen.wrapper(game)