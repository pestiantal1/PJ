import pygame

class InputManager:
    """Handles user input events"""
    
    def __init__(self, grid, cell_size):
        self.grid = grid
        self.cell_size = cell_size
    
    def handle_mouse_click(self, pos):
        """Handle mouse click to toggle cell state"""
        x, y = pos
        col = x // self.cell_size
        row = y // self.cell_size
        
        if 0 <= row < self.grid.height and 0 <= col < self.grid.width:
            self.grid.toggle_cell(row, col)
    
    def handle_events(self):
        """Handle all pygame events and return action flags"""
        actions = {
            'quit': False,
            'pause_toggle': False,
            'randomize': False,
            'clear': False
        }
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                actions['quit'] = True
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    actions['pause_toggle'] = True
                elif event.key == pygame.K_r:
                    actions['randomize'] = True
                elif event.key == pygame.K_c:
                    actions['clear'] = True
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.handle_mouse_click(event.pos)
        
        return actions