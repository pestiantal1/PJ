import pygame
import sys
from entities.player import Player
from entities.bullet import Bullet
from entities.asteroid import Asteroid
from core.utils import spawn_asteroids
from core.state import GameState
from roguelite.run_data import RunData
from roguelite.upgrades import UpgradeManager
from ui.game_over_screen import GameOverScreen
from ui.hud import HUD
from ui.upgrade_screen import UpgradeScreen

WIDTH, HEIGHT = 1280, 720
FPS = 60

SCORE_VALUES = {
    "large": 20,
    "medium": 50,
    "small": 100,
}

def check_collision(obj1, obj2, radius1, radius2):
    dx = obj1.x - obj2.x
    dy = obj1.y - obj2.y
    distance = (dx ** 2 + dy ** 2) ** 0.5
    return distance < (radius1 + radius2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Asteroids Roguelite")
    clock = pygame.time.Clock()

    # Game state
    game_state = GameState()
    run_data = RunData()
    upgrade_manager = UpgradeManager()
    
    # Entities
    player = Player(WIDTH // 2, HEIGHT // 2)
    bullets = []
    shoot_cooldown = 0
    
    asteroids = spawn_asteroids(5, WIDTH, HEIGHT, avoid_pos=(player.x, player.y), avoid_radius=200)

    # UI
    game_over_screen = GameOverScreen(WIDTH, HEIGHT)
    hud = HUD(WIDTH, HEIGHT)
    upgrade_screen = UpgradeScreen(WIDTH, HEIGHT)

    running = True
    showing_upgrades = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_state.game_over:
                    # Restart game
                    game_state.reset()
                    run_data.reset()
                    upgrade_manager.reset()
                    player = Player(WIDTH // 2, HEIGHT // 2)
                    bullets = []
                    shoot_cooldown = 0
                    asteroids = spawn_asteroids(5, WIDTH, HEIGHT, avoid_pos=(player.x, player.y), avoid_radius=200)
                    hud.reset()
                    showing_upgrades = False
                
                # Handle upgrade selection
                if showing_upgrades:
                    selected_upgrade = upgrade_screen.handle_input(event)
                    if selected_upgrade:
                        upgrade_manager.apply_upgrade(selected_upgrade, player, game_state)
                        run_data.record_upgrade(selected_upgrade.name)
                        showing_upgrades = False
        
        if not game_state.game_over and not showing_upgrades:
            # --- HUD ---
            hud.update_time()
            
            # --- Controls ---
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player.rotate_left()
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player.rotate_right()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                player.thrust()
            if keys[pygame.K_SPACE] and shoot_cooldown == 0:
                bullets.append(Bullet(player.x, player.y, player.angle))
                base_cooldown = 10
                fire_rate_reduction = getattr(player, 'fire_rate_bonus', 0)
                shoot_cooldown = max(3, base_cooldown - fire_rate_reduction)
                run_data.record_shot()

            # --- Update game state ---
            player.update(WIDTH, HEIGHT)
            for bullet in bullets[:]:
                bullet.update(WIDTH, HEIGHT)
                if bullet.lifetime <= 0:
                    bullets.remove(bullet)
            if shoot_cooldown > 0:
                shoot_cooldown -= 1
            for asteroid in asteroids:
                asteroid.update(WIDTH, HEIGHT)

            # --- Player-Asteroid Collision ---
            for asteroid in asteroids:
                if check_collision(player, asteroid, player.size * 0.5, asteroid.radius):
                    game_state.game_over = True
                    break
            
            # --- Bullet-Asteroid Collision ---
            bullets_to_remove = []
            asteroids_to_remove = []
            asteroids_to_add = []
            
            for bullet in bullets:
                for asteroid in asteroids:
                    if check_collision(bullet, asteroid, bullet.radius, asteroid.radius):
                        if bullet not in bullets_to_remove:
                            bullets_to_remove.append(bullet)
                        if asteroid not in asteroids_to_remove:
                            asteroids_to_remove.append(asteroid)
                            asteroids_to_add.extend(asteroid.split())
                            
                            # Add score and check for level up
                            points = SCORE_VALUES[asteroid.size]
                            leveled_up = game_state.add_score(points)
                            
                            # Track stats
                            run_data.record_asteroid_kill(asteroid.size)
                            run_data.update_max_level(game_state.level)
                            
                            # Show upgrade screen on level up
                            if leveled_up:
                                upgrades = upgrade_manager.get_random_upgrades(3)
                                if upgrades:
                                    upgrade_screen.set_upgrades(upgrades)
                                    showing_upgrades = True
                        break
            
            # Remove bullets and asteroids that collided
            for bullet in bullets_to_remove:
                bullets.remove(bullet)
            for asteroid in asteroids_to_remove:
                asteroids.remove(asteroid)
            # Add new asteroids from splits
            asteroids.extend(asteroids_to_add)
            
            # Spawn more asteroids periodically based on level
            if len(asteroids) == 0:
                num_new_asteroids = min(5 + game_state.level // 5, 15)
                asteroids = spawn_asteroids(num_new_asteroids, WIDTH, HEIGHT, avoid_pos=(player.x, player.y), avoid_radius=200)

        # --- Drawing ---
        screen.fill((0, 0, 0))
        
        if not game_state.game_over:
            player.draw(screen)
            for bullet in bullets:
                bullet.draw(screen)
            for asteroid in asteroids:
                asteroid.draw(screen)
            hud.draw(screen, game_state)
            
            # Draw upgrade screen if showing
            if showing_upgrades:
                upgrade_screen.draw(screen)
        else:
            # Draw game over screen
            game_over_screen.draw(screen)
        
        pygame.display.flip()

        # --- Cap framerate ---
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()