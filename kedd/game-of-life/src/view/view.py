class View:
    def __init__(self, model):
        self.model = model

    def render(self):
        state = self.model.get_state()
        for row in state:
            print(' '.join(['█' if cell else ' ' for cell in row]))
        print()

    def handle_input(self):
        user_input = input("Enter command (start/stop/quit): ")
        self.model.process_input(user_input)