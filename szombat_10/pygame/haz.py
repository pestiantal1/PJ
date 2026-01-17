import pygame
import time

# Inicializálás
pygame.init()

# Képernyő méretek
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Színek
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
RED = (200, 0, 0)
BACKGROUND_COLOR = WHITE

# Képernyő létrehozása
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Házikó")

def draw_house():
    # Ház méretei
    house_size = 200
    roof_height = 100
    cx, cy = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

    # Négyzet (ház test)
    left = cx - house_size // 2
    top = cy - house_size // 2
    rect = pygame.Rect(left, top, house_size, house_size)
    pygame.draw.rect(screen, BROWN, rect)

    # Háromszög (tető)
    roof_points = [
        (left, top),  # bal felső
        (left + house_size, top),  # jobb felső
        (cx, top - roof_height)  # felső csúcs
    ]
    pygame.draw.polygon(screen, RED, roof_points)

def main():
    screen.fill(BACKGROUND_COLOR)
    draw_house()
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()

if __name__ == "__main__":
    main()