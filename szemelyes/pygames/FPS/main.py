import pygame
import math
import sys
import os
from enemy_ai import EnemyManager
from gun import Gun, draw_gun

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FOV = math.pi / 3  # 60 degrees
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH  # One ray per pixel for smooth walls
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
TEXTURE_SIZE = 64  # Size of texture images

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (220, 0, 0)
BLUE = (0, 0, 220)
GREEN = (0, 220, 0)
DARK_GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)

# Map (1 = wall, 0 = empty)
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

TILE_SIZE = 100

# Collectibles - list of [x, y, collected]
collectibles = [
    {'x': 250, 'y': 150, 'collected': False},
    {'x': 450, 'y': 350, 'collected': False},
    {'x': 550, 'y': 550, 'collected': False},
]

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 3
        self.rotation_speed = 0.05
        self.money = 0  # Track collected money
        self.health = 100  # Player health
        self.last_damage_time = 0  # For damage cooldown

    def move(self, keys):
        new_x, new_y = self.x, self.y
        
        # Forward/Backward
        if keys[pygame.K_w]:
            new_x += math.cos(self.angle) * self.speed
            new_y += math.sin(self.angle) * self.speed
        if keys[pygame.K_s]:
            new_x -= math.cos(self.angle) * self.speed
            new_y -= math.sin(self.angle) * self.speed
        
        # Strafe left/right
        if keys[pygame.K_a]:
            new_x += math.cos(self.angle - math.pi/2) * self.speed
            new_y += math.sin(self.angle - math.pi/2) * self.speed
        if keys[pygame.K_d]:
            new_x += math.cos(self.angle + math.pi/2) * self.speed
            new_y += math.sin(self.angle + math.pi/2) * self.speed
        
        # Check collision
        map_x = int(new_x / TILE_SIZE)
        map_y = int(new_y / TILE_SIZE)
        
        if 0 <= map_x < len(MAP[0]) and 0 <= map_y < len(MAP):
            if MAP[map_y][map_x] == 0:
                self.x = new_x
                self.y = new_y
        
        # Rotation
        if keys[pygame.K_LEFT]:
            self.angle -= self.rotation_speed
        if keys[pygame.K_RIGHT]:
            self.angle += self.rotation_speed
    
    def check_collectibles(self):
        """Check if player is close enough to collect money"""
        for item in collectibles:
            if not item['collected']:
                dx = self.x - item['x']
                dy = self.y - item['y']
                distance = math.sqrt(dx * dx + dy * dy)
                if distance < 30:  # Collection radius
                    item['collected'] = True
                    self.money += 1
                    print(f"Collected money! Total: ${self.money}")

    def take_damage(self, amount, current_time):
        """Take damage with cooldown"""
        if current_time - self.last_damage_time > 1000:
            self.health -= amount
            self.last_damage_time = current_time
            print(f"Granny hit you! Health: {self.health}")
            
            if self.health <= 0:
                print("Game Over!")
                return True
        return False

def create_default_texture(color):
    """Create a simple checkered texture"""
    texture = pygame.Surface((TEXTURE_SIZE, TEXTURE_SIZE))
    for y in range(TEXTURE_SIZE):
        for x in range(TEXTURE_SIZE):
            if (x // 8 + y // 8) % 2:
                texture.set_at((x, y), color)
            else:
                darker = tuple(max(0, c - 50) for c in color)
                texture.set_at((x, y), darker)
    return texture

def create_default_money():
    """Create a simple money sprite"""
    sprite = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.circle(sprite, YELLOW, (16, 16), 15)
    pygame.draw.circle(sprite, (200, 200, 0), (16, 16), 15, 2)
    font = pygame.font.Font(None, 24)
    text = font.render("$", True, (100, 100, 0))
    sprite.blit(text, (10, 8))
    return sprite

def load_texture():
    """Load wall texture after display is initialized"""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        texture_path = os.path.join(script_dir, 'res/textures', 'wall.png')
        print(f"Attempting to load texture from: {texture_path}")
        wall_tex = pygame.image.load(texture_path).convert()
        wall_tex = pygame.transform.scale(wall_tex, (TEXTURE_SIZE, TEXTURE_SIZE))
        print("✓ Texture loaded successfully!")
        return wall_tex
    except FileNotFoundError as e:
        print(f"✗ File not found: {e}")
        print(f"Script location: {os.path.dirname(os.path.abspath(__file__))}")
        print("Using default brown brick texture")
        return create_default_texture((150, 75, 0))
    except Exception as e:
        print(f"✗ Error loading texture: {e}")
        print("Using default brown brick texture")
        return create_default_texture((150, 75, 0))

def load_money_sprite():
    """Load money sprite"""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        sprite_path = os.path.join(script_dir, 'res/textures', 'money.png')
        print(f"Attempting to load money sprite from: {sprite_path}")
        money_spr = pygame.image.load(sprite_path).convert_alpha()
        money_spr = pygame.transform.scale(money_spr, (32, 32))
        print("✓ Money sprite loaded successfully!")
        return money_spr
    except FileNotFoundError as e:
        print(f"✗ Money sprite not found: {e}")
        print("Using default yellow coin")
        return create_default_money()
    except Exception as e:
        print(f"✗ Error loading money sprite: {e}")
        print("Using default yellow coin")
        return create_default_money()

def load_music():
    """Load and play background music"""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        music_path = os.path.join(script_dir, 'res/sounds', 'music.wav')
        print(f"Attempting to load music from: {music_path}")
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.5)  # Set volume to 50%
        pygame.mixer.music.play(-1)  # Loop indefinitely (-1)
        print("✓ Music loaded and playing!")
    except FileNotFoundError as e:
        print(f"✗ Music file not found: {e}")
    except Exception as e:
        print(f"✗ Error loading music: {e}")

def cast_ray(player, angle):
    sin_a = math.sin(angle)
    cos_a = math.cos(angle)
    
    # Check horizontal grid lines
    depth_hor = float('inf')
    tex_hor = 0
    if abs(sin_a) > 0.001:
        y_step = TILE_SIZE if sin_a > 0 else -TILE_SIZE
        y = (player.y // TILE_SIZE) * TILE_SIZE + (TILE_SIZE if sin_a > 0 else 0)
        
        for _ in range(20):
            depth = (y - player.y) / sin_a
            if depth < 0 or depth > MAX_DEPTH:
                break
            x = player.x + depth * cos_a
            
            map_x = int(x / TILE_SIZE)
            map_y = int(y / TILE_SIZE) - (0 if sin_a > 0 else 1)
            
            if 0 <= map_y < len(MAP) and 0 <= map_x < len(MAP[0]):
                if MAP[map_y][map_x] == 1:
                    depth_hor = depth
                    tex_hor = x % TILE_SIZE  # Texture offset
                    break
            y += y_step
    
    # Check vertical grid lines
    depth_vert = float('inf')
    tex_vert = 0
    if abs(cos_a) > 0.001:
        x_step = TILE_SIZE if cos_a > 0 else -TILE_SIZE
        x = (player.x // TILE_SIZE) * TILE_SIZE + (TILE_SIZE if cos_a > 0 else 0)
        
        for _ in range(20):
            depth = (x - player.x) / cos_a
            if depth < 0 or depth > MAX_DEPTH:
                break
            y = player.y + depth * sin_a
            
            map_x = int(x / TILE_SIZE) - (0 if cos_a > 0 else 1)
            map_y = int(y / TILE_SIZE)
            
            if 0 <= map_y < len(MAP) and 0 <= map_x < len(MAP[0]):
                if MAP[map_y][map_x] == 1:
                    depth_vert = depth
                    tex_vert = y % TILE_SIZE  # Texture offset
                    break
            x += x_step
    
    if depth_vert < depth_hor:
        return depth_vert, True, tex_vert
    return depth_hor, False, tex_hor

def render_3d(screen, player):
    # Draw ceiling and floor
    pygame.draw.rect(screen, DARK_GRAY, (0, 0, WIDTH, HEIGHT // 2))
    pygame.draw.rect(screen, GRAY, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))
    
    # Depth buffer to track wall distances for each column
    depth_buffer = []
    
    # Cast one ray per pixel column
    for x in range(WIDTH):
        angle = player.angle - HALF_FOV + (x / WIDTH) * FOV
        depth, is_vertical, tex_offset = cast_ray(player, angle)
        
        # Fix fisheye effect
        depth *= math.cos(player.angle - angle)
        depth = max(depth, 0.1)
        
        # Store depth for sprite occlusion
        depth_buffer.append(depth)
        
        # Calculate wall height
        wall_height = min(int(TILE_SIZE * HEIGHT / depth), HEIGHT * 2)
        
        # Calculate texture column to sample
        tex_x = int((tex_offset / TILE_SIZE) * TEXTURE_SIZE)
        tex_x = max(0, min(TEXTURE_SIZE - 1, tex_x))
        
        # Get the texture column and scale it to wall height
        texture_column = pygame.Surface((1, TEXTURE_SIZE))
        texture_column.blit(wall_texture, (0, 0), (tex_x, 0, 1, TEXTURE_SIZE))
        
        # Scale to wall height
        scaled_column = pygame.transform.scale(texture_column, (1, wall_height))
        
        # Apply distance shading
        shade = max(0, min(255, 255 - int(depth * 0.3)))
        if not is_vertical:
            shade = int(shade * 0.7)  # Darker for horizontal walls
        
        # Create shading surface
        shade_surface = pygame.Surface((1, wall_height))
        shade_surface.fill((shade, shade, shade))
        scaled_column.blit(shade_surface, (0, 0), special_flags=pygame.BLEND_MULT)
        
        # Draw the textured wall slice
        screen.blit(scaled_column, (x, HEIGHT // 2 - wall_height // 2))
    
    return depth_buffer

def render_sprites(screen, player, money_sprite, depth_buffer, enemy_manager):
    """Render collectible sprites and enemies in 3D view with depth checking"""
    sprites_to_draw = []
    
    # Add collectibles
    for item in collectibles:
        if item['collected']:
            continue
        
        dx = item['x'] - player.x
        dy = item['y'] - player.y
        
        distance = math.sqrt(dx * dx + dy * dy)
        angle_to_sprite = math.atan2(dy, dx)
        
        angle_diff = angle_to_sprite - player.angle
        
        while angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        while angle_diff < -math.pi:
            angle_diff += 2 * math.pi
        
        if abs(angle_diff) < HALF_FOV and distance > 0:
            screen_x = (angle_diff / FOV + 0.5) * WIDTH
            sprite_height = min(int(TILE_SIZE * HEIGHT / distance), HEIGHT)
            sprite_width = sprite_height
            
            sprites_to_draw.append({
                'type': 'money',
                'sprite': money_sprite,
                'distance': distance,
                'screen_x': screen_x,
                'height': sprite_height,
                'width': sprite_width
            })
    
    # Add enemies with directional animated sprites
    for enemy in enemy_manager.get_all_enemies():
        if not enemy.active:
            continue
        
        dx = enemy.x - player.x
        dy = enemy.y - player.y
        
        distance = math.sqrt(dx * dx + dy * dy)
        angle_to_sprite = math.atan2(dy, dx)
        angle_diff = angle_to_sprite - player.angle
        
        while angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        while angle_diff < -math.pi:
            angle_diff += 2 * math.pi
        
        if abs(angle_diff) < HALF_FOV and distance > 0:
            screen_x = (angle_diff / FOV + 0.5) * WIDTH
            sprite_height = min(int(TILE_SIZE * HEIGHT / distance), HEIGHT)
            sprite_width = sprite_height
            
            # Get directional sprite based on player view angle
            enemy_sprite = enemy.get_sprite(player)
            if enemy_sprite:
                sprites_to_draw.append({
                    'type': 'enemy',
                    'sprite': enemy_sprite,
                    'distance': distance,
                    'screen_x': screen_x,
                    'height': sprite_height,
                    'width': sprite_width
                })
    
    # Sort sprites by distance (furthest first)
    sprites_to_draw.sort(key=lambda s: s['distance'], reverse=True)
    
    # Draw sprites with depth testing
    for sprite_data in sprites_to_draw:
        scaled_sprite = pygame.transform.scale(sprite_data['sprite'], 
                                               (sprite_data['width'], sprite_data['height']))
        
        shade = max(50, min(255, 255 - int(sprite_data['distance'] * 0.3)))
        shade_surface = pygame.Surface(scaled_sprite.get_size())
        shade_surface.fill((shade, shade, shade))
        scaled_sprite.blit(shade_surface, (0, 0), special_flags=pygame.BLEND_MULT)
        
        sprite_x = int(sprite_data['screen_x'] - sprite_data['width'] / 2)
        sprite_y = int(HEIGHT / 2 - sprite_data['height'] / 2)
        
        for x_offset in range(sprite_data['width']):
            screen_col = sprite_x + x_offset
            
            if 0 <= screen_col < WIDTH:
                if sprite_data['distance'] < depth_buffer[screen_col]:
                    sprite_column = pygame.Surface((1, sprite_data['height']), pygame.SRCALPHA)
                    sprite_column.blit(scaled_sprite, (0, 0), (x_offset, 0, 1, sprite_data['height']))
                    screen.blit(sprite_column, (screen_col, sprite_y))


def draw_minimap(screen, player, enemy_manager):
    minimap_scale = 3
    minimap_offset_x, minimap_offset_y = 10, 10
    
    # Draw map
    for y, row in enumerate(MAP):
        for x, tile in enumerate(row):
            color = WHITE if tile else BLACK
            pygame.draw.rect(screen, color,
                           (minimap_offset_x + x * minimap_scale,
                            minimap_offset_y + y * minimap_scale,
                            minimap_scale, minimap_scale))
    
    # Draw collectibles on minimap
    for item in collectibles:
        if not item['collected']:
            mini_x = minimap_offset_x + int(item['x'] / TILE_SIZE * minimap_scale)
            mini_y = minimap_offset_y + int(item['y'] / TILE_SIZE * minimap_scale)
            pygame.draw.circle(screen, YELLOW, (mini_x, mini_y), 2)
    
    # Draw enemies on minimap
    for enemy in enemy_manager.get_all_enemies():
        if enemy.active:
            mini_x = minimap_offset_x + int(enemy.x / TILE_SIZE * minimap_scale)
            mini_y = minimap_offset_y + int(enemy.y / TILE_SIZE * minimap_scale)
            pygame.draw.circle(screen, RED, (mini_x, mini_y), 2)
    
    # Draw player
    player_x = minimap_offset_x + int(player.x / TILE_SIZE * minimap_scale)
    player_y = minimap_offset_y + int(player.y / TILE_SIZE * minimap_scale)
    pygame.draw.circle(screen, GREEN, (player_x, player_y), 3)
    
    # Draw direction line
    line_length = 10
    end_x = player_x + int(math.cos(player.angle) * line_length)
    end_y = player_y + int(math.sin(player.angle) * line_length)
    pygame.draw.line(screen, GREEN, (player_x, player_y), (end_x, end_y), 2)

def create_default_granny():
    """Create a simple granny sprite"""
    sprite = pygame.Surface((32, 32), pygame.SRCALPHA)
    # Head
    pygame.draw.circle(sprite, (255, 200, 180), (16, 12), 10)
    # Gray hair
    pygame.draw.circle(sprite, (150, 150, 150), (16, 10), 10, 3)
    # Body
    pygame.draw.rect(sprite, (100, 100, 200), (8, 18, 16, 14))
    # Eyes
    pygame.draw.circle(sprite, (0, 0, 0), (12, 12), 2)
    pygame.draw.circle(sprite, (0, 0, 0), (20, 12), 2)
    return sprite

def load_granny_sprite():
    """Load granny sprite"""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        sprite_path = os.path.join(script_dir, 'res/textures', 'granny.png')
        print(f"Attempting to load granny sprite from: {sprite_path}")
        granny_spr = pygame.image.load(sprite_path).convert_alpha()
        granny_spr = pygame.transform.scale(granny_spr, (32, 32))
        print("✓ Granny sprite loaded successfully!")
        return granny_spr
    except FileNotFoundError as e:
        print(f"✗ Granny sprite not found: {e}")
        print("Using default granny sprite")
        return create_default_granny()
    except Exception as e:
        print(f"✗ Error loading granny sprite: {e}")
        print("Using default granny sprite")
        return create_default_granny()

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Doom-style FPS")
    clock = pygame.time.Clock()
    
    global wall_texture
    wall_texture = load_texture()
    
    money_sprite = load_money_sprite()
    
    load_music()
    
    player = Player(TILE_SIZE * 1.5, TILE_SIZE * 1.5)
    
    # Initialize gun
    gun = Gun()
    
    enemy_manager = EnemyManager()
    enemy_manager.add_enemy(400, 200, speed=1.5)
    enemy_manager.add_enemy(600, 500, speed=1.0)
    
    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # Delta time in seconds
        current_time = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_m:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                        print("Music paused")
                    else:
                        pygame.mixer.music.unpause()
                        print("Music resumed")
                # Shooting with spacebar
                if event.key == pygame.K_SPACE:
                    if gun.shoot():
                        print("BANG!")
                        # TODO: Add bullet/raycast hit detection here
        
        keys = pygame.key.get_pressed()
        player.move(keys)
        player.check_collectibles()
        
        # Update gun animation
        gun.update(dt)
        
        # Update enemies with delta time
        enemy_manager.update_all(player, MAP, dt)
        
        collision, enemy = enemy_manager.check_collision_with_player(player)
        if collision:
            game_over = player.take_damage(10, current_time)
            if game_over:
                running = False
        
        screen.fill(BLACK)
        depth_buffer = render_3d(screen, player)
        render_sprites(screen, player, money_sprite, depth_buffer, enemy_manager)
        
        # Draw gun on top of 3D view
        draw_gun(screen, gun, WIDTH, HEIGHT)
        
        draw_minimap(screen, player, enemy_manager)
        
        font = pygame.font.Font(None, 36)
        fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, WHITE)
        money_text = font.render(f"Money: ${player.money}", True, YELLOW)
        health_text = font.render(f"Health: {player.health}", True, RED if player.health < 30 else WHITE)
        
        # Add ammo counter
        ammo_text = font.render(f"Ready" if gun.can_shoot() else "Reloading...", True, WHITE)
        
        screen.blit(fps_text, (WIDTH - 150, 10))
        screen.blit(money_text, (10, HEIGHT - 50))
        screen.blit(health_text, (10, HEIGHT - 90))
        screen.blit(ammo_text, (WIDTH - 200, HEIGHT - 50))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()