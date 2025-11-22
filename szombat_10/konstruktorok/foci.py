class Focista:
    def __init__(self, nev, meccs, golok):
        self.nev = nev
        self.meccs = meccs
        self.golok = golok
        
    def atlag_gol(self):
        return self.golok / self.meccs
    
    def meccs_jatszas(self):
        self.meccs += 1
        
    def gol_loves(self, db):
        self.golok += db
    
# adatok felvétele
focistak = {
    'Aladár': Focista('Aladár', 4, 3),
    'Béla':   Focista('Béla', 3, 1),
    'Csanád': Focista('Csanád', 1, 3)
}


for nev, focista in focistak.items():
    print(f"{focista.nev} meccsen meccsenkénti átlagos gólok száma: {focista.atlag_gol()}")

# következő meccs
focistak['Aladár'].meccs_jatszas()
focistak['Aladár'].gol_loves(2)
focistak['Béla'].meccs_jatszas()
focistak['Béla'].gol_loves(1)
focistak['Csanád'].meccs_jatszas()

# szótár bejárása és statisztika kiírása
# Aladár meccsenkénti átlagos gólok száma: 1.0
# Béla meccsenkénti átlagos gólok száma: 0.5
# Csanád meccsenkénti átlagos gólok száma: 1.5


for nev, focista in focistak.items():
    print(f"{focista.nev} meccsen meccsenkénti átlagos gólok száma: {focista.atlag_gol()}")