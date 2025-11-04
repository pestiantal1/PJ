import pygame

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
pygame.display.set_caption("Animáció")

# Képek betöltése

def main():

    running = True

    # Game loop
    while running:
        # Esemény kezelés
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False           

        # Háttér kirajzolása
        
        # Animáció megjelenítése

        # Képernyő frissítése
        pygame.display.flip()

        # FPS korlátozás
        clock.tick(FPS)

    # Kilépés
    pygame.quit()

# Projekt belépési pontja
if __name__ == "__main__":
    main()