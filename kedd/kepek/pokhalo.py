import pygame
import time

# Initialize Pygame
pygame.init()

# Konstans értékek felvétele

# Képernyő méretei
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Színek

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUNG_COLOR = WHITE

# Képernyő létrehozása
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pókok a sarokokban")

# Rajzolási parancs definiálása
def draw_rect_corners(length):
    # Egyetlen Rect objektum létrehozása
    rect = pygame.Rect(0, 0, length, length)
    
    # Bal felső sarok
    rect.topleft = (0, 0)
    pygame.draw.rect(screen, BLACK, rect)
    
    # Jobb felső sarok
    rect.topright = (SCREEN_WIDTH, 0)
    pygame.draw.rect(screen, BLACK, rect)
    
    # Bal alsó sarok
    rect.bottomleft = (0, SCREEN_HEIGHT)
    pygame.draw.rect(screen, BLACK, rect)
    
    # Jobb alsó sarok
    rect.bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.draw.rect(screen, BLACK, rect)

def main():

    # Rajzolási parancsok kiadása
    screen.fill(BACKGROUNG_COLOR)
    draw_rect_corners(20)

    # Képernyő frissítése 
    pygame.display.flip()

    # Program megállítása, hogy lássuk amit rajzoltunk.
    time.sleep(10)

    # Kilépés
    pygame.quit()

# Projekt belépési pontja
if __name__ == "__main__":
    main()