# https://app.makerslab.hu/courses/pj-y2/lessons/a-pickle-modul/topic/kozos-feladatok-28/quizzes/1-2-feladat-mentes-pickle-modullal

import os
import random
import sys
import pickle

# Függvények
def jatek_mentes(adatok):
  with open("mentes.txt", "wb") as f:
    pickle.dump(adatok, f)

def jatek_betoltes():
  adatok = None
  
  if os.path.exists("mentes.txt"):
    with open("mentes.txt", "rb") as f:
      adatok = pickle.load(f)
  else:
    print("Nincs korábbi játék elmentve.")
      
  return adatok

def korabbi_mentes_torlese():
  if os.path.exists("mentes.txt"):
    os.remove("mentes.txt")

def uj_jatek():
  adatok = {
    "megfejtés": random.randint(1, 100),
    "tippek": []
  }
  return adatok
  
# Főprogram
adatok = None

if input("Szeretnéd betölteni a legutóbbi játékot? (i/n) ") == "i":
  adatok = jatek_betoltes()

if adatok == None:
  adatok = uj_jatek()

while len(adatok["tippek"]) == 0 or adatok["tippek"][-1] != adatok["megfejtés"]:
  # Tipp validálása
  tipp = input("Tippelj egy számot 1 és 100 között: ")

  if tipp == "x":
    sys.exit(0) # Kilépés "x" beírására
  
  if not tipp.isdigit():
    print("A tippnek számnak kell lennie!")
    continue
    
  tipp = int(tipp)

  if tipp < 1 or tipp > 100:
    print("A tipped 1 és 100 között kell, hogy legyen!")
    continue
  elif tipp in adatok["tippek"]:
    print("Ezt a számot már tippelted!")
    continue

  # Tipp elmentése
  adatok["tippek"].append(tipp)

  # Eltaláltuk-e a megfejtést
  if tipp < adatok["megfejtés"]:
    print("Nagyobbat!")
  elif tipp > adatok["megfejtés"]:
    print("Kisebbet!")
  else:
    print("Gratulálok, eltaláltad a megfejtést!")

  # Játék mentése/nyert játék esetén korábbi mentés törlése
  if tipp != adatok["megfejtés"]:
    jatek_mentes(adatok)
  else:
    korabbi_mentes_torlese()