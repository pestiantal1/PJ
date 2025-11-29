class Kaptar:
    def __init__(self, oldal=3, db=45):
        self.oldal = oldal
        self.db = db
    
    def terulet(self):
        return int(self.oldal * 2.6)
    
    def felulet(self):
        return self.terulet() * self.db
    
    def __str__(self):
        return f'oldal: {oldal}, darab: {db}'

sima_kaptar = Kaptar()
sim_kap_fel = sima_kaptar.felulet()
print(f"Sima kaptár felülete: {sim_kap_fel}")

oldal = int(input("Másik kaptár hatszögeinek oldalhossza:"))
db = int(input("Másik kaptár hatszögeinek darabszáma:"))
masik_kaptar = Kaptar()
masik_kaptar.oldal = oldal
masik_kaptar.db = db
print(f"Kaptár felülete: {masik_kaptar.felulet()}")