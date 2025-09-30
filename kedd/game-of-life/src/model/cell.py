class Cell:
    """Represents a single cell with alive/dead state"""
    
    def __init__(self, state=0):
        self._state = state  # 0 = dead, 1 = alive
    
    def get_state(self):
        """Get the current state of the cell"""
        return self._state
    
    def set_state(self, state):
        """Set the state of the cell (0 for dead, 1 for alive)"""
        self._state = 1 if state else 0
    
    def is_alive(self):
        """Check if the cell is alive"""
        return self._state == 1
    
    def toggle(self):
        """Toggle the cell state"""
        self._state = 1 - self._state