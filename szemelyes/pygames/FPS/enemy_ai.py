import math

TILE_SIZE = 100

class Enemy:
    def __init__(self, x, y, speed=1.5):
        self.x = x
        self.y = y
        self.speed = speed
        self.active = True
    
    def update(self, player, game_map):
        """Update enemy position to chase player"""
        if not self.active:
            return
        
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
        
        return distance
    
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
    
    def update_all(self, player, game_map):
        """Update all enemies"""
        for enemy in self.enemies:
            enemy.update(player, game_map)
    
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
        """Get all enemies (for compatibility)"""
        return self.enemies