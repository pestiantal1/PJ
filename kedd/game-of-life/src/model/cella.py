
class Cella:
    def __init__(self, alive=False):
        self.alive = alive
        self.neighbor_count = 0
    
    def set_neighbor_count(self, count):
        """Beállítja a szomszédok számát"""
        self.neighbor_count = count
    
    def next_generation(self):
        """Kiszámítja, hogy él-e a következő generációban Conway szabályai alapján"""
        if self.alive:
            # Élő cella túlél, ha 2 vagy 3 szomszédja van
            return self.neighbor_count == 2 or self.neighbor_count == 3
        else:
            # Halott cella életre kel, ha pontosan 3 szomszédja van
            return self.neighbor_count == 3
    
    def is_alive(self):
        return self.alive
    
    def set_alive(self, alive):
        self.alive = alive