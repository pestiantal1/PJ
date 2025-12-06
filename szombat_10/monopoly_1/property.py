class Property:
    def __init__(self, id, price, fee, owner=None):
        self.id = id
        self.price = price
        self.fee = fee
        self.owner = owner
        
    def buy(self, player):
        print(f"{player.place+1}. mező a tiéd!")
        self.owner = player
        player.transaction(-self.price)
        
    def pay_fee(self, paying_player):
        paying_player.transaction(-self.fee)
        self.owner.transaction(self.fee)