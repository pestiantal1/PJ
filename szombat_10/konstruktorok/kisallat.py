import datetime
class Allat:
    """ Állat osztály állatokhoz
    
    """
    
    def __init__(self, nev):
        """Konstruktor

        Args:
            nev (string): ez az állat neve
        """
        self.nev = nev
        self.ehseg = 0 #(Az állat éhsége, idővel folyamatosan növekszik, minimuma 0, kezdetben 0)
        self.boldogsag = 100 #(Az állat boldogsága, idővel folyamatosan csökken, maximuma 120, kezdetben 100)

    def etetes(self): # (50-nel csökkenti a ehseget)
        self.ehseg -= 50
        if self.ehseg < 0:
            self.ehseg = 0
 
    def jatek(self): #(30-cal növeli a boldogságot és 10-zel az éhséget)
        self.boldogsag += 30
        if self.boldogsag > 120:
            self.boldogsag = 120
        self.ehseg += 10
        
    def alvas(self): #(90-re állítja a boldogságot és 10-re az éhséget)
        self.boldogsag = 90
        self.ehseg = 10
        
    def allapot(self): #(Kiírja az állat jelenlegi boldogság és éhség szintjét)
        print(f'{self.nev} boldogsági szintje: {self.boldogsag}, éhség: {self.ehseg} ')
    
    def ido(self, eltelt): #(Változtatja az éhséget és a boldogságot eltelt egységgel)
        """_summary_

        Args:
            eltelt (int): eltelt ido masodpercben 
        """
        self.ehseg += eltelt
        self.boldogsag -= eltelt
        
        if self.boldogsag < 0:
            self.boldogsag = 0
            
    def __str__(self):
        return f'{self.nev} {self.ehseg} {self.boldogsag}'

# menü kiírása
def kiiras():
    """
    Kiirja a menü opcióit
    
    """
    print('1 - Etetés')
    print('2 - Játék')
    print('3 - Alvás')
    print('4 - Állapot lekérdezése')
    print('5 - Kilépés')

# állat létrehozása
nev = input('Mi legyen a háziállatod neve? ')
allat = Allat(nev)

# szimuláció futtatása
running = True
start = datetime.datetime.now()
while running:
    kiiras()
    allat.allapot()
    valasz = input(f'Mi legyen a kovetkező? ')

    now = datetime.datetime.now()
    eltelt = (now-start).seconds
    allat.ido(eltelt)
    start = now
    print(f'Eltelt {eltelt} mp.')

    if valasz == '1':
        allat.etetes()
    elif valasz == '2':
        allat.jatek()
    elif valasz == '3':
        allat.alvas()
    elif valasz == '4' or valasz == '':
        pass
    elif valasz == '5':
        running = False
    else:
        print('Egy számot adj meg 1 és 5 között.')
allat.allapot()