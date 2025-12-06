class Player:
    def __init__(self, name, money=0, properties=[], place=0):
        self.name = name
        self.money = money
        self.properties = properties
        self.place = place
        
    def transaction(self, amount):
        self.money += amount
    
    def eliminated(self):
        for property in self.properties:
            property.owner = None
    
    def step(self, amount, board_length, money_per_cycle):
        self.place += amount
        if self.place >= board_length:
            print(f"{self.name} megkerülte a táblát! {money_per_cycle} Forintot kapott.")
            self.money += money_per_cycle
            self.place -= board_length
    
    def decision(self, property):
        print(f"{property.price} Forintba kerül a telek.")
        valasztas = input("Meg szeretnéd venni? (i/n)")
        if valasztas == "i":
            if self.money >= property.price:
                property.buy(self)
                self.properties.append(property)
            else:
                print("Nincs rá elég pénzed!")
        elif valasztas == "n":
            pass
        else:
            print("Hibás válasz")