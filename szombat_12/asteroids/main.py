import pygame
import sys
from entities.player import Player
from entities.bullet import Bullet
from entities.asteroid import Asteroid
from core.utils import spawn_asteroids

WIDTH, HEIGHT = 1280, 720
FPS = 60

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

    player = Player(WIDTH // 2, HEIGHT // 2)
    bullets = []
    shoot_cooldown = 0
    
    asteroids = spawn_asteroids(5, WIDTH, HEIGHT, avoid_pos=(player.x, player.y), avoid_radius=200)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
            shoot_cooldown = 10

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
                    break
        
        # Remove bullets and asteroids that collided
        for bullet in bullets_to_remove:
            bullets.remove(bullet)
        for asteroid in asteroids_to_remove:
            asteroids.remove(asteroid)
        # Add new asteroids from splits
        asteroids.extend(asteroids_to_add)

        # --- Drawing ---
        screen.fill((0, 0, 0))
        player.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for asteroid in asteroids:
            asteroid.draw(screen)
        pygame.display.flip()

        # --- Cap framerate ---
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()