import random

class Cell:
    """
    Egy cella a négyzetrácson, ami számon tartja a szomszédai számát és hogy életbe van-e.
    Képes meghatározni a következő generációban életben lesz-e vagy nem
    """
    def __init__(self):
        self.isAlive = False
        self.neighbors_count = 0
    
    def set_alive(self, alive):
        """Beállítja a cella állapotát"""
        self.isAlive = alive
    
    def set_neighbors_count(self, count):
        """Beállítja a szomszédok számát"""
        self.neighbors_count = count
    
    def next(self):
        """
        Lépteti a cellát a következő generációba: kiszámolja a szomszédai száma alapján, hogy mi lesz a sorsa
        Visszatér 1-el ha életben van, 0-val ha nem él
        """
        if self.isAlive:
            # Élő cella szabályai
            if self.neighbors_count < 2:  # Alulnépesedés
                return 0
            elif self.neighbors_count in [2, 3]:  # Túlélés
                return 1
            else:  # Túlnépesedés (neighbors_count > 3)
                return 0
        else:
            # Halott cella szabályai
            if self.neighbors_count == 3:  # Újraszületés
                return 1
            else:
                return 0
    
    def get_color(self):
        """
        Visszatér egy RGB kóddal: fekete, ha él és fehér ha nem
        """
        return (0, 0, 0) if self.isAlive else (255, 255, 255)

class Grid:
    """
    Reprezentálja a négyzetrácsot, amin a szimuláció fut egy listák listájaként,
    számon tartja a populációt, iterációk számát és a négyzetrács méretét.
    Frissíti a cellák szomszédainak számát és lépteti a szimulációt
    Számon tartja hányadik generációban vagyunk.
    Beállítja az előkészítő fázisban a cellák állapotát.
    """
    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h
        self.cells = [[Cell() for _ in range(w)] for _ in range(h)]
        self.population = 0
        self.iterations = 0
    
    def turn_cell_alive(self, i: int, j: int):
        """
        Életre kelti az (i,j) pozícióban lévő cellát
        """
        if 0 <= i < self.height and 0 <= j < self.width:
            if not self.cells[i][j].isAlive:
                self.cells[i][j].set_alive(True)
                self.population += 1
    
    def turn_cell_dead(self, i: int, j: int):
        """
        Halottra állítja az (i,j) pozícióban lévő cellát
        """
        if 0 <= i < self.height and 0 <= j < self.width:
            if self.cells[i][j].isAlive:
                self.cells[i][j].set_alive(False)
                self.population -= 1
    
    def _count_neighbors(self, i: int, j: int):
        """Megszámolja az élő szomszédokat egy adott pozíció körül"""
        count = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:  # Saját maga kihagyása
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < self.height and 0 <= nj < self.width:
                    if self.cells[ni][nj].isAlive:
                        count += 1
        return count
    
    def next(self):
        """
        Léptet 1 generációt a szimuláción
        """
        # Szomszédok kiszámítása minden cellára
        for i in range(self.height):
            for j in range(self.width):
                neighbors = self._count_neighbors(i, j)
                self.cells[i][j].neighbors_count = neighbors
        
        # Cellák frissítése az előbb kiszámított szomszéd adatok alapján
        new_population = 0
        for i in range(self.height):
            for j in range(self.width):
                new_state = self.cells[i][j].next()
                self.cells[i][j].set_alive(bool(new_state))
                if new_state:
                    new_population += 1
        
        self.population = new_population
        self.iterations += 1
    
    def get_cell_color(self, i: int, j: int):
        """
        Visszatér az (i,j) pozícióban megtalálható színével
        """
        if 0 <= i < self.height and 0 <= j < self.width:
            return self.cells[i][j].get_color()
        return (255, 255, 255)  # Fehér alapértelmezett szín
    
    def reset(self):
        """
        Letörli a rácsot és visszaállítja a populációt 0-ra
        """
        for i in range(self.height):
            for j in range(self.width):
                self.cells[i][j].set_alive(False)
        self.population = 0
        self.iterations = 0
    
    def randomize(self):
        """Véletlenszerűsíti a rácsot"""
        self.reset()
        for i in range(self.height):
            for j in range(self.width):
                if random.random() < 0.3:  # 30% esély az életben maradásra
                    self.turn_cell_alive(i, j)

class Model:
    """
    Összefoglalja a modelt
    Tartalmazza a rácsot és azt, hogy a szimuláció fut-e.
    Kezeli az előkészítő kattintásokat és a szimuláció futtatását
    """
    def __init__(self, w, h, cell_size=10):
        self.grid = Grid(w, h)
        self.is_running = False
        self.placing_cells = True  # True = cellát rak le, False = cellát szed fel
        self.cell_size = cell_size
    
    def mousedown(self, x, y, mouse_buttons_down):
        """
        Kezeli az egér lenyomást.
        Kiszűri, ha érvénytelen kattintás történik
        (éppen fut szimuláció vagy kintre kattintás a játéktérről).
        Eldönti, hogy éppen lerak vagy felszed a játékos cellákat és frissíti ez alapján a rácsot.
        """
        # Ha fut a szimuláció, nem engedélyezünk kattintást
        if self.is_running:
            return
        
        # Koordináták átváltása rács koordinátákra
        grid_x = x // self.cell_size
        grid_y = y // self.cell_size
        
        # Határok ellenőrzése
        if (0 <= grid_y < self.grid.height and 
            0 <= grid_x < self.grid.width):
            
            # Bal egérgomb: cella lerakás/felvétel váltogatása
            if 1 in mouse_buttons_down:  # Bal egérgomb
                cell_is_alive = self.grid.cells[grid_y][grid_x].isAlive
                
                if cell_is_alive:
                    self.grid.turn_cell_dead(grid_y, grid_x)
                    self.placing_cells = False
                else:
                    self.grid.turn_cell_alive(grid_y, grid_x)
                    self.placing_cells = True
    
    def start_stop_simulation(self):
        """
        Megállítja vagy elindítja a szimulációt
        """
        self.is_running = not self.is_running
    
    def reset(self):
        """
        Ha a szimuláció nem fut visszaállítja a változókat kezdő állapotba
        """
        if not self.is_running:
            self.grid.reset()
    
    def get_population(self):
        """
        Visszaadja a jelenlegi populációt
        """
        return self.grid.population
    
    def get_iterations(self):
        """
        Visszaadja hányadik iterációban vagyunk
        """
        return self.grid.iterations
    
    def next(self):
        """
        Lépteti a szimulációt, ha nincs több élő cella leállítja 
        """
        if self.is_running:
            self.grid.next()
            
            # Ha nincs több élő cella, leállítjuk a szimulációt
            if self.grid.population == 0:
                self.is_running = False
    
    def step(self):
        """
        Léptet 1-et a szimuláción, ha éppen nem fut és van élő cella a rácson
        """
        if not self.is_running and self.grid.population > 0:
            self.grid.next()
    
    def get_cell_color(self, i, j):
        """
        Visszaadja a paraméterként megadott cella színét
        """
        return self.grid.get_cell_color(i, j)
    
    # def randomize(self):
    #     """Véletlenszerűsíti a rácsot, ha nem fut a szimuláció"""
    #     if not self.is_running:
    #         self.grid.randomize()