class GenerationManager:
    """Manages the full generation cycle and grid updates"""
    
    def __init__(self, grid, cell_state_manager):
        self.grid = grid
        self.cell_state_manager = cell_state_manager
        self.generation_count = 0
    
    def next_generation(self):
        """Update the entire grid to the next generation"""
        # Calculate all next states first (to avoid modifying grid during calculation)
        next_states = []
        for row in range(self.grid.height):
            row_states = []
            for col in range(self.grid.width):
                next_state = self.cell_state_manager.calculate_next_state(row, col)
                row_states.append(next_state)
            next_states.append(row_states)
        
        # Apply all the new states
        for row in range(self.grid.height):
            for col in range(self.grid.width):
                self.grid.set_cell_state(row, col, next_states[row][col])
        
        self.generation_count += 1
    
    def reset_generation_count(self):
        """Reset the generation counter"""
        self.generation_count = 0