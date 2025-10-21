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
bg_trees_back = pygame.image.load("bg-trees-back.png")
bg_trees_middle = pygame.image.load("bg-trees-middle.png")
bg_trees_front = pygame.image.load("bg-trees-front.png")
bear_surf = pygame.image.load("bear.png")

def main():

    running = True
    
    # Medve pozíció és mozgás változók
    offset = 0
    bear_pos = SCREEN_WIDTH // 2

    # Game loop
    while running:
        # Esemény kezelés
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    offset = -5
                elif event.key == pygame.K_RIGHT:
                    offset = 5
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    offset = 0

        # Medve pozíció frissítése
        bear_pos += offset
        
        # Medve pozíció korlátozása a képernyő szélein
        if bear_pos < 0:
            bear_pos = 0
        elif bear_pos > SCREEN_WIDTH:
            bear_pos = SCREEN_WIDTH

        # Elemek kirajzolása (hátulról előre)
        screen.fill(WHITE)
        
        # Háttér rétegek
        screen.blit(bg_sky, (0, 0))
        screen.blit(bg_trees_back, (0, 0))
        screen.blit(bg_trees_middle, (0, 0))
        
        # Medve kirajzolása
        bear_rect = bear_surf.get_rect(midbottom=(bear_pos, SCREEN_HEIGHT))
        screen.blit(bear_surf, bear_rect)
        
        # Előtér fa réteg (medve előtt)
        screen.blit(bg_trees_front, (0, 0))

        # Képernyő frissítése
        pygame.display.flip()

        # FPS korlátozás
        clock.tick(FPS)

    # Kilépés
    pygame.quit()

# Projekt belépési pontja
if __name__ == "__main__":
    main()