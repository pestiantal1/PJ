import pygame

class DrawManager:
    """Handles all rendering using Pygame"""
    
    def __init__(self, screen, grid, cell_size=10):
        self.screen = screen
        self.grid = grid
        self.cell_size = cell_size
        
        # Colors
        self.DEAD_COLOR = (0, 0, 0)        # Black
        self.ALIVE_COLOR = (255, 255, 255) # White
        self.GRID_COLOR = (64, 64, 64)     # Dark gray
        self.TEXT_COLOR = (255, 255, 255)  # White
        
        # Font for UI text
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
    
    def draw_grid(self):
        """Draw the grid lines"""
        for row in range(self.grid.height + 1):
            y = row * self.cell_size
            pygame.draw.line(self.screen, self.GRID_COLOR, (0, y), (self.grid.width * self.cell_size, y))
        
        for col in range(self.grid.width + 1):
            x = col * self.cell_size
            pygame.draw.line(self.screen, self.GRID_COLOR, (x, 0), (x, self.grid.height * self.cell_size))
    
    def draw_cells(self):
        """Draw all cells based on their states"""
        for row in range(self.grid.height):
            for col in range(self.grid.width):
                cell = self.grid.get_cell(row, col)
                color = self.ALIVE_COLOR if cell.is_alive() else self.DEAD_COLOR
                
                rect = pygame.Rect(
                    col * self.cell_size + 1,
                    row * self.cell_size + 1,
                    self.cell_size - 1,
                    self.cell_size - 1
                )
                pygame.draw.rect(self.screen, color, rect)
    
    def draw_ui(self, generation_count, is_paused):
        """Draw UI elements like generation counter and status"""
        # Generation counter
        gen_text = self.font.render(f"Generation: {generation_count}", True, self.TEXT_COLOR)
        self.screen.blit(gen_text, (10, self.grid.height * self.cell_size + 10))
        
        # Pause status
        status = "PAUSED" if is_paused else "RUNNING"
        status_text = self.font.render(f"Status: {status}", True, self.TEXT_COLOR)
        self.screen.blit(status_text, (10, self.grid.height * self.cell_size + 50))
        
        # Instructions
        instructions = [
            "Space: Pause/Resume",
            "R: Randomize", 
            "C: Clear",
            "Click: Toggle cell"
        ]
        for i, instruction in enumerate(instructions):
            text = pygame.font.Font(None, 24).render(instruction, True, self.TEXT_COLOR)
            self.screen.blit(text, (300, self.grid.height * self.cell_size + 10 + i * 25))
    
    def render(self, generation_count, is_paused):
        """Main render method"""
        self.screen.fill(self.DEAD_COLOR)  # Clear screen
        self.draw_cells()
        self.draw_grid()
        self.draw_ui(generation_count, is_paused)
        pygame.display.flip()