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
BACKGROUNG_COLOR = WHITE

# Képernyő létrehozása
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Teszt")

# Rajzolási parancs(ok) definiálása
def draw_points(radius):
    # pygame.draw.circle(screen, BLACK, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), radius, 5)
    # (0,0) pontba
    pygame.draw.circle(screen, BLACK, (0,0), radius)
    
    # (SCREEN_WIDTH, SCREEN_HEIGHT) pontba
    pygame.draw.circle(screen, BLACK, (SCREEN_WIDTH, SCREEN_HEIGHT), radius)
    
    # képernyő közepére
    pygame.draw.circle(screen, BLACK, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), radius)
    
    # bal alsó sarokba
    pygame.draw.circle(screen, BLACK, (0, SCREEN_HEIGHT), radius)
    
    # jobb felső sarokba
    pygame.draw.circle(screen, BLACK, (SCREEN_WIDTH, 0), radius)
    
    
def main():

    # Rajzolási parancsok kiadása
    screen.fill(BACKGROUNG_COLOR) # háttér beállítása
    
    draw_points(7)

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