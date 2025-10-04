import pygame

class GameOverScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font_large = pygame.font.Font(None, 74)
        self.font_medium = pygame.font.Font(None, 36)
    
    def draw(self, screen):
        """Draw the game over screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # Game Over text
        text = self.font_large.render("GAME OVER", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(text, text_rect)
        
        # Restart instruction
        restart_text = self.font_medium.render("Press R to Restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 60))
        screen.blit(restart_text, restart_rect)