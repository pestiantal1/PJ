import pygame
import time

# Initialize Pygame
pygame.init()

# Konstans értékek felvétele

# Képernyő méretei
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 470

# Színek
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUNG_COLOR = WHITE

# képfrissítési sebesség
FPS = 24
clock = pygame.time.Clock()

# Képernyő létrehozása
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Erdő")

# Kép(ek) betöltése
bg_sky = pygame.image.load("bg-sky.png")

def main():

    running = True

    # Game loop
    while running:
        # Esemény kezelés
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False           

        # Elemek kirajzolása
        screen.fill(WHITE)
        
        # Háttérkép kirajzolása
        screen.blit(bg_sky, (0, 0))

        # Képernyő frissítése
        pygame.display.flip()

        # FPS korlátozás
        clock.tick(FPS)

    # Kilépés
    pygame.quit()

# Projekt belépési pontja
if __name__ == "__main__":
    main()