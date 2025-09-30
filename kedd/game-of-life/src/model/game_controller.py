import pygame
import time

class GameController:
    """Main game controller that orchestrates the game loop"""
    
    def __init__(self, generation_manager, input_manager, draw_manager, fps=5):
        self.generation_manager = generation_manager
        self.input_manager = input_manager
        self.draw_manager = draw_manager
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = True  # Start paused
        
        # Timing for automatic generation updates
        self.last_update = time.time()
        self.update_interval = 1.0 / fps  # seconds per frame
    
    def run(self):
        """Main game loop"""
        while self.running:
            current_time = time.time()
            
            # Handle input
            actions = self.input_manager.handle_events()
            
            if actions['quit']:
                self.running = False
            
            if actions['pause_toggle']:
                self.paused = not self.paused
            
            if actions['randomize']:
                self.generation_manager.grid.randomize()
                self.generation_manager.reset_generation_count()
            
            if actions['clear']:
                self.generation_manager.grid.clear()
                self.generation_manager.reset_generation_count()
            
            # Update generation if not paused and enough time has passed
            if not self.paused and (current_time - self.last_update) >= self.update_interval:
                self.generation_manager.next_generation()
                self.last_update = current_time
            
            # Render
            self.draw_manager.render(
                self.generation_manager.generation_count,
                self.paused
            )
            
            # Control frame rate
            self.clock.tick(60)  # 60 FPS for smooth input handling