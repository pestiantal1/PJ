class Ajto:
    def __init__(self, tipus, meret):
        self.tipus = tipus
        self.meret = meret
        self.nyitva = False
    
    def kinyit(self):
        if self.nyitva:
            print('Az ajtó már nyitva')
        else:
            self.nyitva = True
    
    def mekkora(self):
        return print(f"az ajtó mérete {self.meret} méter")

ajto = Ajto('fa', '2x1')
ajto.kinyit()
ajto.kinyit()
print('Az ajtó nyitva:', ajto.nyitva)
ajto.mekkora()