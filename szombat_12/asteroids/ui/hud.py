import pygame
import time

class HUD:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 28)
        
        self.start_time = time.time()
        self.elapsed_time = 0
        
    def update_time(self):
        """Update the elapsed time"""
        self.elapsed_time = time.time() - self.start_time
        
    def format_time(self):
        """Format elapsed time as MM:SS"""
        minutes = int(self.elapsed_time // 60)
        seconds = int(self.elapsed_time % 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def reset(self):
        """Reset HUD to initial state"""
        self.start_time = time.time()
        self.elapsed_time = 0
        
    def draw(self, screen, game_state):
        """Draw the HUD elements"""
        # Score (top left)
        score_text = self.font_medium.render(f"Score: {game_state.score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))
        
        # Level (top center)
        level_text = self.font_medium.render(f"Level: {game_state.level}", True, (255, 255, 255))
        level_rect = level_text.get_rect(center=(self.width // 2, 35))
        screen.blit(level_text, level_rect)
        
        # Time (top right)
        time_text = self.font_medium.render(f"Time: {self.format_time()}", True, (255, 255, 255))
        time_rect = time_text.get_rect(topright=(self.width - 20, 20))
        screen.blit(time_text, time_rect)
        
        # XP Bar (below level)
        self._draw_xp_bar(screen, game_state)
    
    def _draw_xp_bar(self, screen, game_state):
        """Draw the XP progress bar"""
        bar_width = 300
        bar_height = 20
        bar_x = (self.width - bar_width) // 2
        bar_y = 70
        
        # Background
        pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))
        
        # XP Progress
        progress = game_state.xp / game_state.xp_to_next_level
        filled_width = int(bar_width * progress)
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, filled_width, bar_height))
        
        # Border
        pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height), 2)
        
        # XP Text
        xp_text = self.font_small.render(f"{game_state.xp}/{game_state.xp_to_next_level} XP", True, (255, 255, 255))
        xp_rect = xp_text.get_rect(center=(self.width // 2, bar_y + bar_height + 15))
        screen.blit(xp_text, xp_rect)

