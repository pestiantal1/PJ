import pygame

class UpgradeScreen:
    """Display upgrade choices when leveling up"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font_large = pygame.font.Font(None, 64)
        self.font_medium = pygame.font.Font(None, 42)
        self.font_small = pygame.font.Font(None, 32)
        self.upgrades = []
        self.selected_index = 0
    
    def set_upgrades(self, upgrades):
        """Set the upgrades to display"""
        self.upgrades = upgrades
        self.selected_index = 0
    
    def handle_input(self, event):
        """Handle keyboard input for selecting upgrades"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.selected_index = (self.selected_index - 1) % len(self.upgrades)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.selected_index = (self.selected_index + 1) % len(self.upgrades)
            elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                return self.upgrades[self.selected_index]
        return None
    
    def draw(self, screen):
        """Draw the upgrade selection screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # Title
        title = self.font_large.render("LEVEL UP!", True, (255, 215, 0))
        title_rect = title.get_rect(center=(self.width // 2, 100))
        screen.blit(title, title_rect)
        
        # Subtitle
        subtitle = self.font_small.render("Choose an Upgrade", True, (200, 200, 200))
        subtitle_rect = subtitle.get_rect(center=(self.width // 2, 160))
        screen.blit(subtitle, subtitle_rect)
        
        # Draw upgrade options
        start_y = 250
        spacing = 120
        
        for i, upgrade in enumerate(self.upgrades):
            is_selected = i == self.selected_index
            
            # Background box
            box_rect = pygame.Rect(self.width // 2 - 300, start_y + i * spacing - 10, 600, 100)
            box_color = (100, 100, 200) if is_selected else (50, 50, 50)
            pygame.draw.rect(screen, box_color, box_rect)
            pygame.draw.rect(screen, (255, 255, 255), box_rect, 3)
            
            # Upgrade name
            name_text = self.font_medium.render(upgrade.name, True, (255, 255, 255))
            name_rect = name_text.get_rect(center=(self.width // 2, start_y + i * spacing + 15))
            screen.blit(name_text, name_rect)
            
            # Upgrade description
            desc_text = self.font_small.render(upgrade.description, True, (200, 200, 200))
            desc_rect = desc_text.get_rect(center=(self.width // 2, start_y + i * spacing + 50))
            screen.blit(desc_text, desc_rect)
            
            # Stack indicator
            if upgrade.current_stacks > 0:
                stack_text = self.font_small.render(f"[{upgrade.current_stacks}/{upgrade.max_stacks}]", True, (255, 215, 0))
                stack_rect = stack_text.get_rect(topright=(box_rect.right - 10, box_rect.top + 10))
                screen.blit(stack_text, stack_rect)
        
        # Controls hint
        controls = self.font_small.render("↑/↓ to select  •  ENTER/SPACE to choose", True, (150, 150, 150))
        controls_rect = controls.get_rect(center=(self.width // 2, self.height - 50))
        screen.blit(controls, controls_rect)
