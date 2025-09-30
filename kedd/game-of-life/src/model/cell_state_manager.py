class CellStateManager:
    """Handles the core rules logic for cell state transitions"""
    
    def __init__(self, grid):
        self.grid = grid
    
    def calculate_next_state(self, row, col):
        """Calculate the next state of a cell based on Conway's rules"""
        current_state = self.grid.get_cell_state(row, col)
        live_neighbors = self.grid.count_live_neighbors(row, col)
        
        if current_state == 1:  # Cell is alive
            # Underpopulation: fewer than 2 neighbors -> dies
            if live_neighbors < 2:
                return 0
            # Survival: 2 or 3 neighbors -> survives
            elif live_neighbors in [2, 3]:
                return 1
            # Overcrowding: more than 3 neighbors -> dies
            else:
                return 0
        else:  # Cell is dead
            # Reproduction: exactly 3 neighbors -> becomes alive
            if live_neighbors == 3:
                return 1
            else:
                return 0