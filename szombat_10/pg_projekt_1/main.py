import pygame
import time

# Initialize Pygame
# Csak ezután tudjuk elkezdeni használni a pygame parancsokat
pygame.init()

# Konstans értékek felvétele
# (pythonban ezeket csupa nagybetűvel szokás írni)

# Képernyő méretei
SCREEN_WIDTH = 800 # szélesség
SCREEN_HEIGHT = 600 # magasság

# Színek
# A színeket, amiket használunk érdemes így megadni,
# hogy a kód későbbi része olvashatóbb legyen
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BACKGROUNG_COLOR = WHITE

# Képernyő létrehozása
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Teszt")

font = pygame.font.Font(None, 36)  # alapértelmezett betűtípus, 36-os mérettel
text_surface = font.render("Hello pygame!", True, GREEN)  # Szöveg renderelése fekete színnel

    
def main():

    # Rajzolási parancsok kiadása
    screen.fill(BACKGROUNG_COLOR) # háttér beállítása

    screen.blit(text_surface, (50, 50))  # A szöveget a (50,50) koordinátára rajzoljuk ki


    # Képernyő frissítése 
    # (következő órán részletesebben foglalkozunk vele)
    pygame.display.flip()

    # Program megállítása, hogy lássuk amit rajzoltunk.
    time.sleep(5)

    # Kilépés
    pygame.quit()

# Projekt belépési pontja
if __name__ == "__main__":
    main()