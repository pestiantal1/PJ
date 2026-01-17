from utils import *
from Player import Player
from Property import Property


STARTING_MONEY = 10000
MONEY_PER_CIRCLE = 2000
BOARD_SIZE = 16 # 4-gyel osztható legyen

def main():
    
    # Játékosok létrehozása
    players = init_players()
    for player in players:
        player.money = STARTING_MONEY
        player.properties = []
        player.place = 0
    
    # Pálya létrehozása
    board = makeBoard(BOARD_SIZE)


    # Game loop
    round = 0
    while len(players) > 1:
        # Soron levő játékos nevének kiírása és dobás
        soron_levo_jatekos = round % len(players)
        print(f"{players[soron_levo_jatekos].name} van soron.")
        
        
        # Dobás kiértékelése, azaz léptetés a táblán (kiírni, hogy hányas mezőre érkezett a játékos)
        dobott_szam = next_roll()
        players[soron_levo_jatekos].step(dobott_szam, BOARD_SIZE, MONEY_PER_CIRCLE)
        
        print(f"Pénzed: {players[soron_levo_jatekos].money}. Dobásod: {dobott_szam}.")
        print(f"Ezzel a {players[soron_levo_jatekos].place + 1}. mezőre léptél.")
        
        # Mező kiértékelése
        if board[players[soron_levo_jatekos].place].owner is None:
            # Mező még üres -> játékos döntése
            players[soron_levo_jatekos].decision(board[players[soron_levo_jatekos].place])
            
            
        # Mezőt a soron levő játékos birtokolja -> tájékoztatjuk erről a játékost, de nem történik semmi
        elif board[players[soron_levo_jatekos].place].owner is players[soron_levo_jatekos]:
            print("Ez a mező már a tiéd!")
        
        # Valaki már birtokolja a telket -> díjat kell fizetni a soron levő játékosnak
        else: 
            print(f"A mező {board[players[soron_levo_jatekos].place].owner.name} tulajdonában áll.")
            print(f"Fizetsz neki ennyit: {board[players[soron_levo_jatekos].place].fee}.")
            board[players[soron_levo_jatekos].place].pay_fee(players[soron_levo_jatekos])

        # Kör végén kiesett-e a játékos (játékos pénze < 0), egyébként írjuk ki a megmaradt pénzt 
        if players[soron_levo_jatekos].money < 0:
            print(f"{players[soron_levo_jatekos].name} kiesett a játékból!")
            players[soron_levo_jatekos].eliminated()
            players.remove(players[soron_levo_jatekos])
        else:
            print(f"Maradt pénzed a köröd végén: {players[soron_levo_jatekos].money}.")

        # játéktábla megjelenítése: meilyik mezőt ki birtokolja
        displayBoard(board)
        
        # kovetkező kör előkészítése
        input()
        round += 1

    # Nyertes
    print(f"{players[0].name} nyert!")

# A program belépési pontja, a main() függvény
if __name__ == '__main__':
    main()