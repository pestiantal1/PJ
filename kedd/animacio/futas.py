import pygame
import os
import sys

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

# --- Sprite strip segédosztály ---
class SpriteStrip:
    def __init__(self, path, colorkey, number_of_images, width, height, scale=1.0):
        sheet = pygame.image.load(path)
        self.image_list = []
        self.counter = -1
        self.number_of_images = number_of_images
        
        # képek listájává alakítja a sheet-et
        for i in range(number_of_images):
            img = pygame.Surface((width, height)) # felület előkészítése
            img.blit(sheet, (0,0), (i*width, 0, width, height)) # kép ravetítése a felületre
            img = pygame.transform.scale_by(img, (scale, scale)) # átmérettezés
            img.set_colorkey(colorkey) # háttér átlátszóvá tétele
            self.image_list.append(img) # kész képkocka felvétele a listába

    def next_image(self):
        # visszaadja a következő képkockát
        self.counter = (self.counter + 1) % self.number_of_images
        return self.image_list[self.counter]

# Utility betöltés
def load_image(name, colorkey=None):
    path = os.path.join(os.path.dirname(__file__), name)
    if not os.path.exists(path):
        print(f"Hiányzó fájl: {path}")
        pygame.quit()
        sys.exit(1)
    img = pygame.image.load(path).convert_alpha()
    return img

def main():
    # Háttér betöltése és méretezése
    bg = load_image("bg-sky.png").convert()
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Spritecsík paraméterek
    FRAME_W, FRAME_H = 45, 40
    SCALE = 3
    FRAME_COUNT = 5

    # SpriteStrip-nek a fájl útvonalát adjuk át
    sprite_path = os.path.join(os.path.dirname(__file__), "running.png")
    COLORKEY = (255, 0, 255)
    animator = SpriteStrip(sprite_path, COLORKEY, FRAME_COUNT, FRAME_W, FRAME_H, scale=SCALE)

    frame_w_scaled = FRAME_W * SCALE
    frame_h_scaled = FRAME_H * SCALE

    # Kezdeti pozíció: bal alsó sarok
    x = 0
    y = SCREEN_HEIGHT - frame_h_scaled

    # Mozgás és animálás beállítások
    speed = 180  # px/sec, pozitív = jobbra
    anim_timer = 0.0
    frame_duration = 0.12  # másodpercenként váltás (anim sebesség)
    current_frame = animator.image_list[0]
    facing_right = True

    running = True

    while running:
        dt = clock.tick(FPS) / 1000.0  # delta time másodpercben

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Automatikus mozgás: gyorsulás nélkül állandó sebességgel
        x += speed * dt

        # Ütközés a falakkal: pattintás és irányváltás
        if x <= 0:
            x = 0
            speed = abs(speed)  # jobbra
            facing_right = True
        elif x >= SCREEN_WIDTH - frame_w_scaled:
            x = SCREEN_WIDTH - frame_w_scaled
            speed = -abs(speed)  # balra
            facing_right = False

        # Animáció váltása folyamatosan
        anim_timer += dt
        if anim_timer >= frame_duration:
            anim_timer = 0.0
            current_frame = animator.next_image()

        # Rajzolás
        screen.fill(BACKGROUNG_COLOR)
        screen.blit(bg, (0, 0))

        # Ha balra néz, tükrözzük a képet
        draw_frame = current_frame
        if not facing_right:
            draw_frame = pygame.transform.flip(current_frame, True, False)

        rect = draw_frame.get_rect()
        rect.bottomleft = (int(x), SCREEN_HEIGHT)
        screen.blit(draw_frame, rect)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()