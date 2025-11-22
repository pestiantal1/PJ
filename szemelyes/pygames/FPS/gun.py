import pygame
import os

class Gun:
    """Handles gun sprite animation and shooting mechanics"""
    def __init__(self):
        self.frames = []
        self.current_frame = 0
        self.is_shooting = False
        self.anim_timer = 0.0
        self.frame_duration = 0.08  # 80ms per frame
        
        # Shooting cooldown
        self.shoot_cooldown = 0.0
        self.cooldown_duration = 0.5  # 500ms between shots
        
        self._load_gun_sprites()
    
    def _load_gun_sprites(self):
        """Load and extract gun animation frames from sprite sheet"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            sprite_path = os.path.join(script_dir, 'res/textures', 'PIST2.png')
            
            sheet = pygame.image.load(sprite_path).convert_alpha()
            print(f"✓ Loaded gun sprite sheet: {sprite_path}")
            
            # Sheet dimensions: 308px x 64px
            sheet_width = 308
            sheet_height = 64
            
            # Frame data: (x_percent, y_from_bottom_percent, width, height)
            frame_specs = [
                (5.981, 100, 40, 49),    # Frame 1
                (24.951, 100, 51, 57),   # Frame 2
                (48.713, 100, 55, 60),   # Frame 3 (muzzle flash)
                (73.308, 0, 42, 64),     # Frame 4 (recoil) - top aligned
                (96.449, 100, 40, 48),   # Frame 5
            ]
            
            # Extract each frame
            for x_percent, y_percent, w, h in frame_specs:
                # Calculate actual pixel positions
                x = int(sheet_width * (x_percent / 100))
                
                # y position depends on alignment
                if y_percent == 100:  # Bottom aligned
                    y = sheet_height - h
                else:  # Top aligned (y_percent == 0)
                    y = 0
                
                # Extract frame
                frame = pygame.Surface((w, h), pygame.SRCALPHA)
                frame.blit(sheet, (0, 0), (x, y, w, h))
                
                # Scale up (3x for better visibility)
                frame = pygame.transform.scale(frame, (w * 3, h * 3))
                
                self.frames.append(frame)
            
            print(f"✓ Gun animation loaded with {len(self.frames)} frames!")
            
        except Exception as e:
            print(f"✗ Error loading gun sprites: {e}")
            # Create default gun sprite
            default_frame = pygame.Surface((80, 100), pygame.SRCALPHA)
            pygame.draw.rect(default_frame, (100, 100, 100), (30, 40, 20, 40))
            pygame.draw.rect(default_frame, (150, 150, 150), (25, 20, 30, 25))
            self.frames = [default_frame]
    
    def update(self, dt):
        """Update gun animation and cooldown"""
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt
        
        if self.is_shooting:
            self.anim_timer += dt
            
            if self.anim_timer >= self.frame_duration:
                self.anim_timer = 0.0
                self.current_frame += 1
                
                if self.current_frame >= len(self.frames):
                    self.current_frame = 0
                    self.is_shooting = False
    
    def shoot(self):
        """Attempt to shoot the gun"""
        if not self.is_shooting and self.shoot_cooldown <= 0:
            self.is_shooting = True
            self.current_frame = 0
            self.anim_timer = 0.0
            self.shoot_cooldown = self.cooldown_duration
            return True
        return False
    
    def get_current_frame(self):
        """Get the current gun sprite frame"""
        if self.frames:
            return self.frames[self.current_frame]
        return None
    
    def can_shoot(self):
        """Check if gun is ready to shoot"""
        return not self.is_shooting and self.shoot_cooldown <= 0

def draw_gun(screen, gun, screen_width, screen_height):
    """Draw the gun centered at the bottom of the screen"""
    frame = gun.get_current_frame()
    if frame:
        # Get frame dimensions
        frame_rect = frame.get_rect()
        
        # Center horizontally, position at bottom with padding
        frame_rect.centerx = screen_width // 2
        frame_rect.bottom = screen_height - 20
        
        # Draw the gun
        screen.blit(frame, frame_rect)
        
        # Cooldown indicator (bottom left)
        if gun.shoot_cooldown > 0:
            cooldown_percent = gun.shoot_cooldown / gun.cooldown_duration
            bar_width = 100
            bar_height = 5
            bar_x = 20
            bar_y = screen_height - 10
            
            # Background
            pygame.draw.rect(screen, (50, 50, 50), 
                           (bar_x, bar_y, bar_width, bar_height))
            # Progress
            pygame.draw.rect(screen, (255, 200, 0), 
                           (bar_x, bar_y, int(bar_width * cooldown_percent), bar_height))