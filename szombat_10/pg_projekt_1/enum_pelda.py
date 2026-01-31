from enum import Enum

class Evszak(Enum):
    TAVASZ = 1
    NYAR = 2
    OSZ = 3
    TEL = 4

jelenlegi_evszak = Evszak.TAVASZ
print(type(Evszak))
print(type(Evszak.TAVASZ))
print(type(jelenlegi_evszak))
print("Most", jelenlegi_evszak.name, "van") # Most NYAR van
print("Az evszak azonosítója:", jelenlegi_evszak.value) # Az evszak azonosítója: 2

if jelenlegi_evszak == Evszak.NYAR:
    print("Juhé, itt a nyár")
    
if jelenlegi_evszak == Evszak.TAVASZ:
    print("Itt a tavasz!")