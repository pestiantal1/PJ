class Model:
    def __init__(self, grid):
        self.grid = grid
        self.is_running = False

    def start_simulation(self):
        self.is_running = True

    def stop_simulation(self):
        self.is_running = False

    def get_state(self):
        return [[cell.is_alive for cell in row] for row in self.grid.cells]

    def process_input(self, user_input):
        if user_input == 'start':
            self.start_simulation()
        elif user_input == 'stop':
            self.stop_simulation()