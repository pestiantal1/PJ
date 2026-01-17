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
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
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
    
def draw_x(width):
    # bal fel -> jobb le
    pygame.draw.line(screen, RED, (0,0), (SCREEN_WIDTH, SCREEN_HEIGHT), width)
    
    # bal le -> jobb fel
    pygame.draw.line(screen, RED, (0,SCREEN_HEIGHT), (SCREEN_WIDTH, 0), width)
    
    
def draw_squares(length, width):
    pygame.draw.rect(screen, BLUE, pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, length, length), width)
    pygame.draw.rect(screen, BLUE, pygame.Rect(SCREEN_WIDTH // 2 - length, SCREEN_HEIGHT // 2, length, length), width)
    pygame.draw.rect(screen, BLUE, pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - length, length, length), width)
    pygame.draw.rect(screen, BLUE, pygame.Rect(SCREEN_WIDTH // 2- length, SCREEN_HEIGHT // 2 - length, length, length), width)
    
        
def draw_player(length, width):
    pontok = [
        (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - length),
        # (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
        (SCREEN_WIDTH // 2 + length, SCREEN_HEIGHT // 2 + length),
        (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
        (SCREEN_WIDTH // 2 - length, SCREEN_HEIGHT // 2 + length)
    ]
    
    pygame.draw.polygon(screen, GREEN, pontok, width)
    
def main():

    # Rajzolási parancsok kiadása
    screen.fill(BACKGROUNG_COLOR) # háttér beállítása
    
    # draw_points(7)
    draw_x(2)
    
    # 
    draw_squares(50, 1)
    draw_player(50, 1)

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