import random

class Kincses_lada:
    def __init__(self):
        self.kincs_erteke = random.randint(1, 100)
        self.kifosztott = False
    
    def kifosztas(self):
        """Ha a láda már üres: visszatér Hamissal, ha nem: a kifosztott attrib.-ot igazra állítja és visszatér Igazzal"""
        if self.kifosztott:
            return False
        else:
            self.kifosztott = True
            return True
    
    def ertek(self):
        """Visszatér a kincs értékével"""
        return self.kincs_erteke

# kalózok és aranyaiknak száma
kalozok = {
    'Jack': 0,
    'Bill': 0
}

# ládák generálása
ladak = []
for _ in range(6):
    ladak.append(Kincses_lada())

# Elosztás
for kor in range(1, 4):
    print(f'\n{kor}. kör')
    
    # Jack választ
    sikeres = False
    while not sikeres:
        valasztas = int(input('Jack, hányadik ládát szeretnéd kifosztani?\n>>>'))
        # Átváltás 0-indexre (felhasználó 1-6 között ad meg, de lista 0-5 indexű)
        lada_index = valasztas - 1
        
        if ladak[lada_index].kifosztas():
            ertek = ladak[lada_index].ertek()
            kalozok['Jack'] += ertek
            print(f'A láda értéke {ertek} arany')
            sikeres = True
        else:
            print('A ládát már kifosztották.')
    
    # Bill választ
    sikeres = False
    while not sikeres:
        valasztas = int(input('Bill, hányadik ládát szeretnéd kifosztani?\n>>>'))
        lada_index = valasztas - 1
        
        if ladak[lada_index].kifosztas():
            ertek = ladak[lada_index].ertek()
            kalozok['Bill'] += ertek
            print(f'A láda értéke {ertek} arany')
            sikeres = True
        else:
            print('A ládát már kifosztották.')

# Végeredmény: szótár bejárása
print('\nEredmény:')
for nev, vagyon in kalozok.items():
    print(f'{nev} vagyona: {vagyon} arany')