from Property import *
from Player import *
import random

def init_players():
    # Játékosok számának megadása (legalább 2)
    no_players = int(input("Hány játékos játszik? (min. 2)"))
    while no_players < 2:
        print("Legalább 2 játékos szükséges!")
        no_players = int(input("Hány játékos játszik? (min. 2)"))


    # Nevek megadása
    players = []
    for i in range(no_players):
        name = input(f'{i+1}. játékos neve: ')
        players.append(Player(name=name))
    
    # Visszatérés a játékosok listájával
    return players

def makeBoard(board_size):
    # játék tábla generálása: az ingatlanok ára legyen 1000 és 6000 közötti random érték,
    #  a belépési díj az ár harmada, egész számként.
    properties = []
    for i in range(board_size): # CSERÉLD LE A TÁBLA MÉRETÉRE
        rand_price = random.randint(1000, 6000)
        fee_price = rand_price // 3
        properties.append(Property(id=i, price=rand_price, fee=fee_price))

    # visszatér a mezők listájával
    return properties

def next_roll():
    return random.randint(1, 6)

# A játéktábla kiírásáért felelős függvény (nem kell módosítani)
def displayBoard(board):
    if len(board) % 4 != 0:
        return
    
    size = len(board)
    screen = []

    # Top
    screen.append('   ')
    for col in range(int(size/4)+1):
        screen.append(f'{str(int(size/2+col+1)).zfill(2)} ')
    screen.append('\n   ')

    # Mid
    cells = int(size / 4) + 1
    for row in range(cells):
        if row == cells - 1:
            screen.append('   ')
        for col in range(cells):
            if row == 0:
                screen.append(printCell(board[int(size / 2 + col)]))
            elif row < cells - 1: # 0 < row < cells-1
                if col == 0:
                    cellIdx = int(size / 2 - row)
                    screen.append(f'{str(cellIdx + 1).zfill(2)} {printCell(board[cellIdx])} ')
                elif col < cells - 1: # 0 < col < cells-1 
                    screen.append('   ')
                else: # col == cells-1
                    cellIdx = int(size / 4 * 3 + row)
                    screen.append(f'\b{printCell(board[cellIdx])}\b {str(cellIdx + 1).zfill(2)} ')
            else: # row == cells-1
                screen.append(printCell(board[int(size / 4 - col)]))
        screen.append('\n')
 
    # Bottom
    screen.append('   ')
    for col in range(int(size/4)+1):
        screen.append(f'{str(int(size/4-col+1)).zfill(2)} ')

    print('\nA mezők tulajdonosai:\n' + ''.join(screen))

def printCell(property):
    if property.owner is None:
        return '## '
    else:
        return f'{property.owner.name[0:2]} '