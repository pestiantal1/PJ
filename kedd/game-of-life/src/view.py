import pygame
from model import Model # modell importálása

# Initialize Pygame
pygame.init()

# Képernyő méretei
WIDTH = 500
HEIGHT = 600
W = 20 # vízszintesen mennyi cella legyen
H = 24 # függőlegesen mennyi cella legyen
CELL_SIZE = WIDTH // W

# Színek
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (125, 125, 125)
BACKGROUND_COLOR = WHITE

# képfrissítési sebesség
FPS = 20
clock = pygame.time.Clock()

# Képernyő létrehozása
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway: Game of life")

# Betűtípus
font = pygame.font.Font(None, 36) 

# Állapot létrehozása
model = Model(W, H, CELL_SIZE)

def draw_grid():
    # Cellák kirajzolása
    for i in range(H):
        for j in range(W):
            color = model.get_cell_color(i, j)
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

    for i in range(H + 1):
        pygame.draw.line(screen, GREY, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))
    for i in range(W + 1):
        pygame.draw.line(screen, GREY, (j * CELL_SIZE, 0), (j * CELL_SIZE, H * CELL_SIZE))



def draw_info_panel(population, iteration):
    """Kirajzolja az információs panelt"""
    panel_y = H * CELL_SIZE + 10
    
    # Háttér törlése az info panel területén
    info_rect = pygame.Rect(0, H * CELL_SIZE, WIDTH, HEIGHT - H * CELL_SIZE)
    pygame.draw.rect(screen, BACKGROUND_COLOR, info_rect)
    
    # Populáció kiírása
    pop_text = font.render(f"Population: {population}", True, BLACK)
    screen.blit(pop_text, (10, panel_y))
    
    # Iteráció kiírása
    iter_text = font.render(f"Generation: {iteration}", True, BLACK)
    screen.blit(iter_text, (10, panel_y + 40))
    
    # Státusz kiírása
    status = "RUNNING" if model.is_running else "PAUSED"
    status_text = font.render(f"Status: {status}", True, BLACK)
    screen.blit(status_text, (10, panel_y + 80))
    

def main():

    # változók előkészítése a game loop-hoz:
    running = True
    show_info = True

    # Automatikus léptetés időzítése
    last_step_time = 0
    step_interval = 500

    # Game loop
    while running:
        current_time = pygame.time.get_ticks()
        
        # Esemény kezelés
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # kattintások kezelés
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bal egérgomb
                    x, y = pygame.mouse.get_pos()
                    model.mousedown(x, y, [1])
            
            # billentyűk kezelése
            elif event.type == pygame.KEYDOWN:
                # ENTER lenyomásra elindul vagy megáll a szimuláció
                if event.key == pygame.K_RETURN:
                    model.start_stop_simulation()
                
                # SPACE lenyomásra 1-et lép a szimuláció
                elif event.key == pygame.K_SPACE:
                    model.step()
                
                # "r" lenyomásra reset-elődik a játék
                elif event.key == pygame.K_r:
                    model.reset()
                
                # F1 lenyomásra info panel kirajzolása-eltüntetése
                elif event.key == pygame.K_F1:
                    show_info = not show_info
        
        # Modell automatikus léptetése, ha fut
        if model.is_running and (current_time - last_step_time) > step_interval:
            model.next()
            last_step_time = current_time
        
        # Játékállapot kirajzolása
        screen.fill(BACKGROUND_COLOR)
        draw_grid()

        # Infók kiírása, ha kell
        if show_info:
            draw_info_panel(model.get_population(), model.get_iterations())

        # Képernyő frissítése
        pygame.display.flip()

        # FPS korlátozás
        clock.tick(FPS)

    # Kilépés
    pygame.quit()

# Projekt belépési pontja
if __name__ == "__main__":
    main()