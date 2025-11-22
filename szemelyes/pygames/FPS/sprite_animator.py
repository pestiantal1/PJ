import pygame
import os
import math

class SpriteAnimator:
    """Handles 8-directional sprite sheet animation with 2 frames per direction"""
    def __init__(self, path, frame_data, scale=1.0):
        """
        path: Path to sprite sheet
        frame_data: List of (x, y, width, height) for each frame
        scale: Scale factor for the sprites
        """
        try:
            sheet = pygame.image.load(path).convert_alpha()
            print(f"✓ Loaded sprite sheet: {path}")
        except Exception as e:
            print(f"✗ Error loading sprite sheet: {e}")
            default_frame = pygame.Surface((32, 32), pygame.SRCALPHA)
            pygame.draw.circle(default_frame, (255, 0, 0), (16, 16), 15)
            self.frames = [[default_frame, default_frame] for _ in range(8)]
            return
        
        # Extract all 16 frames
        all_frames = []
        for x, y, w, h in frame_data:
            img = pygame.Surface((w, h), pygame.SRCALPHA)
            img.blit(sheet, (0, 0), (x, y, w, h))
            
            if scale != 1.0:
                new_w = int(w * scale)
                new_h = int(h * scale)
                img = pygame.transform.scale(img, (new_w, new_h))
            
            all_frames.append(img)
        
        # Organize into 8 directions with 2 frames each
        # Top row (0-7): first frame of each direction
        # Bottom row (8-15): second frame of each direction
        self.frames = []
        for i in range(8):
            self.frames.append([all_frames[i], all_frames[i + 8]])
        
        self.current_direction = 0
        self.current_frame = 0
    
    def get_direction_index(self, angle_to_enemy, player_angle):
        """
        Calculate which of 8 directions to show based on relative angle
        angle_to_enemy: angle from player to enemy (what we calculated in enemy_ai.py)
        player_angle: direction player is facing
        """
        # The relative angle should show which sprite direction to use
        # 0 = enemy facing player directly
        # We need to reverse the angle since we're looking FROM player TO enemy
        relative_angle = player_angle - angle_to_enemy
        
        # Normalize to 0-2π
        while relative_angle < 0:
            relative_angle += 2 * math.pi
        while relative_angle >= 2 * math.pi:
            relative_angle -= 2 * math.pi
        
        # Convert to 8 directions (each direction covers 45 degrees)
        # Offset by half a segment so direction 0 is centered
        direction = int((relative_angle + math.pi / 8) / (2 * math.pi / 8)) % 8
        return direction
    
    def get_frame(self, direction_index, frame_index=0):
        """Get specific frame for a direction"""
        return self.frames[direction_index][frame_index]
    
    def next_frame(self):
        """Toggle between the 2 animation frames"""
        self.current_frame = (self.current_frame + 1) % 2
        return self.frames[self.current_direction][self.current_frame]

def create_enemy_frame_data():
    """
    Frame data extracted from CSS sprite sheet
    Format: (x, y, width, height)
    """
    # Top row - first frame of each direction (0-7)
    top_row = [
        (1, 1, 34, 57),    # Direction 0
        (36, 1, 30, 56),   # Direction 1
        (67, 1, 43, 55),   # Direction 2
        (111, 1, 40, 54),  # Direction 3
        (152, 1, 30, 56),  # Direction 4
        (183, 1, 28, 55),  # Direction 5
        (212, 1, 43, 55),  # Direction 6
        (256, 0, 41, 56),  # Direction 7
    ]
    
    # Bottom row - second frame of each direction (8-15)
    bottom_row = [
        (1, 59, 33, 56),   # Direction 0 frame 2
        (35, 59, 29, 56),  # Direction 1 frame 2
        (65, 59, 38, 56),  # Direction 2 frame 2
        (104, 59, 33, 56), # Direction 3 frame 2
        (138, 59, 30, 56), # Direction 4 frame 2
        (169, 59, 29, 56), # Direction 5 frame 2
        (199, 59, 34, 56), # Direction 6 frame 2
        (234, 58, 33, 56), # Direction 7 frame 2
    ]
    
    return top_row + bottom_row