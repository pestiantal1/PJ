import pygame
import sys

# Import directly from the standalone model.py file using a specific import
import importlib.util
import os

# Get the path to model.py (standalone file)
model_path = os.path.join(os.path.dirname(__file__), 'model.py')
spec = importlib.util.spec_from_file_location("model_module", model_path)
model_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model_module)

Model = model_module.Model

# Initialize Pygame
pygame.init()

# Konstans értékek felvétele
GRID_WIDTH = 80   # rács szélessége (cellák száma)
GRID_HEIGHT = 45  # rács magassága (cellák száma)
CELL_SIZE = 10    # egy cella mérete pixelben

# Képernyő méretei
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE + 100  # +100 a UI-nak

# Színek
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Kép frissítési sebesség
FPS = 60
GENERATION_FPS = 5

# Képernyő létrehozása
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()

# Font inicializálás
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

def draw_grid(model):
    """Rajzolja ki a rácsot és a cellákat"""
    # Cellák rajzolása
    for i in range(model.grid.height):
        for j in range(model.grid.width):
            color = model.get_cell_color(i, j)
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)
    
    # Rácsvonalak rajzolása
    for i in range(model.grid.height + 1):
        pygame.draw.line(screen, GRAY, (0, i * CELL_SIZE), (SCREEN_WIDTH, i * CELL_SIZE))
    for j in range(model.grid.width + 1):
        pygame.draw.line(screen, GRAY, (j * CELL_SIZE, 0), (j * CELL_SIZE, model.grid.height * CELL_SIZE))

def draw_ui(model):
    """Rajzolja ki a felhasználói felületet"""
    ui_y = GRID_HEIGHT * CELL_SIZE + 10
    
    # Generáció és populáció
    gen_text = font.render(f"Generáció: {model.get_iterations()}", True, WHITE)
    pop_text = font.render(f"Populáció: {model.get_population()}", True, WHITE)
    
    screen.blit(gen_text, (10, ui_y))
    screen.blit(pop_text, (10, ui_y + 40))
    
    # Státusz
    status = "FUTÁS" if model.is_running else "MEGÁLLÍTVA"
    status_text = font.render(f"Státusz: {status}", True, WHITE)
    screen.blit(status_text, (300, ui_y))
    
    # Vezérlés leírása
    controls = [
        "SPACE: Start/Stop",
        "R: Véletlenszerűsítés",
        "C: Törlés",
        "S: Egy lépés",
        "Egér: Cella váltás"
    ]
    
    for i, control in enumerate(controls):
        control_text = small_font.render(control, True, WHITE)
        screen.blit(control_text, (500, ui_y + i * 20))

def main():
    """Főprogram belépési pontja"""
    model = Model(GRID_WIDTH, GRID_HEIGHT, CELL_SIZE)
    
    # Időzítés a generációk automatikus frissítéséhez
    last_generation_update = 0
    generation_interval = 1000 // GENERATION_FPS  # milliszekundum
    
    print("Conway's Game of Life")
    print("Vezérlés:")
    print("- SPACE: Szimuláció indítása/megállítása")
    print("- R: Rács véletlenszerűsítése")
    print("- C: Rács törlése")
    print("- S: Egy lépés előre (ha megállítva)")
    print("- Egér bal gomb: Cella állapotának váltása")
    
    running = True
    while running:
        current_time = pygame.time.get_ticks()
        
        # Események kezelése
        mouse_buttons = pygame.mouse.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    model.start_stop_simulation()
                elif event.key == pygame.K_r:
                    model.randomize()
                elif event.key == pygame.K_c:
                    model.reset()
                elif event.key == pygame.K_s:
                    model.step()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bal egérgomb
                    x, y = pygame.mouse.get_pos()
                    model.mousedown(x, y, [1])  # [1] = bal egérgomb lenyomva
        
        # Automatikus generáció frissítés
        if model.is_running and (current_time - last_generation_update) >= generation_interval:
            model.next()
            last_generation_update = current_time
        
        # Rajzolás
        screen.fill(BLACK)
        draw_grid(model)
        draw_ui(model)
        pygame.display.flip()
        
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()