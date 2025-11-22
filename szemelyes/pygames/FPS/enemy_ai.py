import math
from sprite_animator import SpriteAnimator, create_enemy_frame_data
import os

TILE_SIZE = 100

class Enemy:
    def __init__(self, x, y, speed=1.5):
        self.x = x
        self.y = y
        self.speed = speed
        self.active = True
        
        # Animation setup
        self.animator = None
        self.anim_timer = 0.0
        self.frame_duration = 0.15  # Time between walk frames
        self.current_sprite = None
        
        # Load animation
        self._load_animation()
    
    def _load_animation(self):
        """Load the enemy sprite animation"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            sprite_path = os.path.join(script_dir, 'res/textures', 'enemy_sheet.png')
            
            frame_data = create_enemy_frame_data()
            self.animator = SpriteAnimator(sprite_path, frame_data, scale=2.0)
            self.current_sprite = self.animator.frames[0][0]
            print("✓ Enemy 8-directional animation loaded!")
        except Exception as e:
            print(f"✗ Error loading enemy animation: {e}")
    
    def update(self, player, game_map, dt=0.016):
        """Update enemy position and animation"""
        if not self.active:
            return 999999
        
        # Calculate direction to player
        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.sqrt(dx * dx + dy * dy)
        
        if distance > 0:
            # Normalize and move towards player
            dx /= distance
            dy /= distance
            
            new_x = self.x + dx * self.speed
            new_y = self.y + dy * self.speed
            
            # Check collision with walls
            map_x = int(new_x / TILE_SIZE)
            map_y = int(new_y / TILE_SIZE)
            
            if 0 <= map_x < len(game_map[0]) and 0 <= map_y < len(game_map):
                if game_map[map_y][map_x] == 0:
                    self.x = new_x
                    self.y = new_y
        
        # Update animation
        if self.animator:
            self.anim_timer += dt
            if self.anim_timer >= self.frame_duration:
                self.anim_timer = 0.0
                self.animator.next_frame()
        
        return distance
    
    def get_sprite(self, player):
        """Get current sprite frame based on player viewing angle"""
        if not self.animator:
            return self.current_sprite
        
        # Calculate angle from player to enemy
        dx = self.x - player.x
        dy = self.y - player.y
        angle_to_enemy = math.atan2(dy, dx)
        
        # Get appropriate direction sprite
        direction = self.animator.get_direction_index(angle_to_enemy, player.angle)
        frame_index = self.animator.current_frame
        
        return self.animator.get_frame(direction, frame_index)
    
    def get_distance_to(self, x, y):
        """Calculate distance to a point"""
        dx = x - self.x
        dy = y - self.y
        return math.sqrt(dx * dx + dy * dy)
    
    def to_dict(self):
        """Convert to dictionary for rendering"""
        return {
            'x': self.x,
            'y': self.y,
            'speed': self.speed,
            'active': self.active
        }

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def add_enemy(self, x, y, speed=1.5):
        """Add a new enemy"""
        enemy = Enemy(x, y, speed)
        self.enemies.append(enemy)
        return enemy
    
    def update_all(self, player, game_map, dt=0.016):
        """Update all enemies"""
        for enemy in self.enemies:
            enemy.update(player, game_map, dt)
    
    def check_collision_with_player(self, player, damage_radius=40):
        """Check if any enemy is touching the player"""
        for enemy in self.enemies:
            if not enemy.active:
                continue
            
            distance = enemy.get_distance_to(player.x, player.y)
            if distance < damage_radius:
                return True, enemy
        
        return False, None
    
    def get_active_enemies(self):
        """Get list of active enemies as dictionaries"""
        return [enemy.to_dict() for enemy in self.enemies if enemy.active]
    
    def get_all_enemies(self):
        """Get all enemies"""
        return self.enemies