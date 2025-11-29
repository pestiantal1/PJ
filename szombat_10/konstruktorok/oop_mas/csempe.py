# 1.) OOP NELKUL
# def terulet(oldal):
#     return oldal * oldal
    
# def kerulet(oldal):
#     return 4 * oldal

# darab = int(input("Hány darab csempéd van?"))
# oldal = int(input("Mekkora a csempék oldalhossza (cm-ben)?"))
# fal_meret = int(input("Mekkora a fal mérete (cm^2-ben)?"))

# osszes_terulet = darab * terulet(oldal)
# osszes_kerulet = darab * kerulet(oldal)
# lefedi = osszes_terulet >= fal_meret

# print(f"Lefedik a csempék a falat: {lefedi}")
# print(f"A csempék kerülete összesen: {osszes_kerulet} cm")

#2.)OOP
class Csempe():
    oldal = 0
    
    def terulet(self):
       return self.oldal * self.oldal
   
    def kerulet(self):
        return 4 * self.oldal
    
csempe = Csempe()

darab = int(input("Hány darab csempéd van?"))
oldal = int(input("Mekkora a csempék oldalhossza (cm-ben)?"))
fal_meret = int(input("Mekkora a fal mérete (cm^2-ben)?"))

csempe.oldal = oldal

osszes_terulet = darab * csempe.terulet()
osszes_kerulet = darab * csempe.kerulet()
lefedi = osszes_terulet >= fal_meret

print(f"Lefedik a csempék a falat: {lefedi}")
print(f"A csempék kerülete összesen: {osszes_kerulet} cm")