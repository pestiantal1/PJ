import os
import random
import sys
import pickle

def mentes(adatok):
    """A mentés lement bemeneti adatokat a mentes.txt fájlba, a pickle.dumb metódussal

    Args:
        adatok (list): Ezek a lementendő adatok listás formában
    """
    with open("mentes.txt", "wb") as f:
        pickle.dump(adatok, f)

def betoltes():
    """Betölti az adatokat a mentes.txt fájlból

    Returns:
        list: Ez a mentes.txt-ben tárolt lista
    """
    adatok = []
    if os.path.exists("mentes.txt"):
        with open("mentes.txt", "rb") as f:
            adatok = pickle.load(f)
    else:
        print("Nincsenek korábbi kincsek elmentve.")
    return adatok

def hozzaadas(lista):
    kincs = input("Add meg a kincs nevét: ").strip()
    if not kincs:
        print("A kincs neve nem lehet üres.")
        return lista

    lista.append(kincs)
    mentes(lista)
    print(f"'{kincs}' hozzáadva a kincsesládához.")
    return lista

def kiiras(lista):
    if not lista:
        print("A kincsesláda üres.")
    else:
        print("\n--- Kincsek a ládában ---")
        for i, kincs in enumerate(lista, 1):
            print(f"{i}. {kincs}")
        print("--------------------------")

def torles(lista):
    if not lista:
        print("Nincs mit törölni, a láda üres.")
        return lista

    kiiras(lista)
    try:
        index = int(input("Add meg a törlendő kincs sorszámát: "))
        if index < 1 or index > len(lista):
            print("Érvénytelen sorszám.")
            return lista
        torolt = lista.pop(index - 1)
        mentes(lista)
        print(f"'{torolt}' törölve a kincsesládából.")
    except ValueError:
        print("Csak számot adhatsz meg.")
    return lista


kincsek = betoltes()

while True:
    print("\nKINCSESLÁDA PROGRAM")
    print("1. Kincs hozzáadása")
    print("2. Kincs törlése")
    print("3. Kincsek megtekintése")
    print("0. Kilépés")

    opt = input("Válassz egy opciót: ")

    if not opt.isdigit():
        print("Számot válassz!")
        continue

    opt = int(opt)

    if opt < 0 or opt > 3:
        print("Nincs ilyen opció!")
        continue

    if opt == 0:
        print("Kilépés...")
        sys.exit(0)
    elif opt == 1:
        kincsek = hozzaadas(kincsek)
    elif opt == 2:
        kincsek = torles(kincsek)
    elif opt == 3:
        kiiras(kincsek)
