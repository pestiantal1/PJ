class Csempe:
    def terulet(self, oldal):
        return oldal * oldal

    def kerulet(self, oldal):
        return 4 * oldal


csempek = {}
csempe = Csempe()

while True:
    oldal_input = input("Add meg a csempe oldalhosszát:")
    
    if oldal_input == "":
        break
    
    try:
        oldal = int(oldal_input)
        
        if oldal in csempek:
            print(f"Ez már hozzá lett adva: {csempek[oldal]}")
        else:
            csempe_kerulet = csempe.kerulet(oldal)
            csempe_terulet = csempe.terulet(oldal)
            
            csempek[oldal] = (csempe_kerulet, csempe_terulet)
            
            print(f"{oldal} oldalhosszú csempe kerülete: {csempe_kerulet}")
            print(f"{oldal} oldalhosszú csempe területe: {csempe_terulet}")
    except ValueError:
        print("Kérlek, adj meg egy érvényes számot!")

print("\nA csempek szótár tartalma:")
print(csempek)