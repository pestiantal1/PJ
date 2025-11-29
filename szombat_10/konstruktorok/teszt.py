class Csilivili_osztály:
    '''
    Egy egyszerű példa, hogyan lehet Pythonban attribútumokat és metódusokat definiálni. 
    
    Attribútumok:
    csillogo (bool): Megadja, hogy az objektum csillogó-e. Alapértelmezetten: True.
    villogo (bool): Meghatározza, hogy az objektum villog-e. Alapértelmezetten: True.
    hasznos (bool): Jelzi, hogy az objektum hasznos-e. Alapértelmezetten: False.
    '''

    def __init__(self, csillogo=True, villogo=True, hasznos=False):
        '''
        Inicializálja az osztály egy példányát a megadott értékekkel.

        Paraméterek:
        csillogo (bool, opcionális): Beállítja a csillogás tulajdonságát. Alapértelmezett: True.
        villogo (bool, opcionális): Beállítja a villogás tulajdonságát. Alapértelmezett: True.
        hasznos (bool, opcionális): Beállítja, hogy az objektum hasznos-e. Alapértelmezett: False.
        '''
        self.csillogo = csillogo
        self.villogo = villogo
        self.hasznos = hasznos
        
    def __str__(self):
        '''
        Visszaad egy szöveges reprezentációt az objektum jelenlegi állapotáról.

        Visszatérési érték:
        str: Az objektum attribútumainak szöveges formája, pl. `csillogo:True villogo:True hasznos:False`.
        '''
        return f'csillogo:{self.csillogo} villogo:{self.villogo} hasznos:{self.hasznos}'