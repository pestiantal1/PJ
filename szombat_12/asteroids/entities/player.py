import pygame
import math

class Player:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.angle = 0
        self.size = 30
        self.speed = 0
        self.vel_x = 0
        self.vel_y = 0
    
    def rotate_left(self):
        self.angle += 5
        
    def rotate_right(self):
        self.angle -= 5    
        
    def thrust(self):
        angle_rad = math.radians(self.angle)
        self.vel_x += math.cos(angle_rad) * 0.1
        self.vel_y += -math.sin(angle_rad) * 0.1
    
    def update(self, width, height):
        self.x += self.vel_x
        self.y += self.vel_y
        
        self.x %= width
        self.y %= height
        
        self.vel_x *= 0.99
        self.vel_y *= 0.99
        
    def draw(self, surface):
        angle_rad = math.radians(self.angle)
        tip = (
            self.x + math.cos(angle_rad) * self.size,
            self.y - math.sin(angle_rad) * self.size
        )
        left = (
            self.x + math.cos(angle_rad + math.radians(140)) * self.size * 0.6,
            self.y - math.sin(angle_rad + math.radians(140)) * self.size * 0.6,
        )
        right = (
            self.x + math.cos(angle_rad - math.radians(140)) * self.size * 0.6,
            self.y - math.sin(angle_rad - math.radians(140)) * self.size * 0.6,
        )
        
        pygame.draw.polygon(surface, (255,255,255), [tip,left,right], 2)