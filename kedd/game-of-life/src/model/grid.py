import random
from .cell import Cell

class Grid:
    """Manages the 2D grid of cells and boundary logic"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell() for _ in range(width)] for _ in range(height)]
    
    def get_cell(self, row, col):
        """Get a cell at the specified position"""
        if 0 <= row < self.height and 0 <= col < self.width:
            return self.cells[row][col]
        return None
    
    def get_cell_state(self, row, col):
        """Get the state of a cell at the specified position"""
        cell = self.get_cell(row, col)
        return cell.get_state() if cell else 0
    
    def set_cell_state(self, row, col, state):
        """Set the state of a cell at the specified position"""
        cell = self.get_cell(row, col)
        if cell:
            cell.set_state(state)
    
    def toggle_cell(self, row, col):
        """Toggle the state of a cell at the specified position"""
        cell = self.get_cell(row, col)
        if cell:
            cell.toggle()
    
    def get_neighbors(self, row, col):
        """Get all 8 neighbors of a cell"""
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:  # Skip the cell itself
                    continue
                neighbor_row, neighbor_col = row + dr, col + dc
                if 0 <= neighbor_row < self.height and 0 <= neighbor_col < self.width:
                    neighbors.append(self.cells[neighbor_row][neighbor_col])
        return neighbors
    
    def count_live_neighbors(self, row, col):
        """Count the number of live neighbors around a cell"""
        neighbors = self.get_neighbors(row, col)
        return sum(neighbor.get_state() for neighbor in neighbors)
    
    def randomize(self):
        """Randomize the grid state"""
        for row in range(self.height):
            for col in range(self.width):
                self.cells[row][col].set_state(random.choice([0, 1]))
    
    def clear(self):
        """Clear all cells (set to dead)"""
        for row in range(self.height):
            for col in range(self.width):
                self.cells[row][col].set_state(0)