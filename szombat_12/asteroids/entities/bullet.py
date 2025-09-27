import pygame
import math

class Bullet:
    def __init__(self, x, y, angle):
        speed = 12
        angle_rad = math.radians(angle)
        self.x = x
        self.y = y
        self.dx = math.cos(angle_rad) * speed
        self.dy = -math.sin(angle_rad) * speed
        self.radius = 3
        self.lifetime = 60
        
    def update(self, width, height):
        self.x += self.dx
        self.y += self.dy
        self.x %= width
        self.y %= height
        self.lifetime -= 1
        
    def draw(self, surface):
        pygame.draw.circle(surface, (255,255,0), (int(self.x), int(self.y)), self.radius)