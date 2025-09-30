import pygame
from model import (
    Grid, 
    CellStateManager, 
    GenerationManager, 
    InputManager, 
    DrawManager, 
    GameController
)

# Initialize Pygame
# Csak ezután tudjuk elkezdeni használni a pygame parancsokat
pygame.init()

# Konstans értékek felvétele
# Game of Life specifikus konstansok
GRID_WIDTH = 80   # rács szélessége (cellák száma)
GRID_HEIGHT = 45  # rács magassága (cellák száma)
CELL_SIZE = 10    # egy cella mérete pixelben

# Képernyő méretei
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE + 100  # +100 a UI-nak

# Színek
# A színeket, amiket használunk érdemes így megadni,
# hogy a kód későbbi része olvashatóbb legyen
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = BLACK

# Kép frissítési sebesség
FPS = 60  # Smooth input handling
GENERATION_FPS = 5  # Generációk másodpercenként
clock = pygame.time.Clock()

# Képernyő létrehozása
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

class GameOfLife:
    """Main entry point that initializes all components"""
    
    def __init__(self):
        self.screen = screen
        
        # Initialize all components following the architecture
        self.grid = Grid(GRID_WIDTH, GRID_HEIGHT)
        self.cell_state_manager = CellStateManager(self.grid)
        self.generation_manager = GenerationManager(self.grid, self.cell_state_manager)
        self.input_manager = InputManager(self.grid, CELL_SIZE)
        self.draw_manager = DrawManager(self.screen, self.grid, CELL_SIZE)
        self.game_controller = GameController(
            self.generation_manager,
            self.input_manager,
            self.draw_manager,
            fps=GENERATION_FPS
        )
    
    def start(self):
        """Start the game"""
        print("Conway's Game of Life")
        print("Vezérlés:")
        print("- Space: Pause/Resume szimuláció")
        print("- R: Rács véletlenszerűsítése")
        print("- C: Rács törlése")
        print("- Egér kattintás: Cella állapotának váltása")
        print("- Ablak bezárása: kilépés")
        
        # Start with a randomized grid
        self.grid.randomize()
        
        # Start the main game loop
        try:
            self.game_controller.run()
        finally:
            pygame.quit()

def main():
    """Főprogram belépési pontja"""
    game = GameOfLife()
    game.start()

# Projekt belépési pontja
if __name__ == "__main__":
    main()