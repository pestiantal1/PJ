import pygame
import random
import math

ASTEROID_SIZES = {
    "large": 60,
    "medium": 40,
    "small": 20
}

class Asteroid:
    def __init__(self, x, y, size="large"):
        self.x = x
        self.y = y
        self.size = size
        self.radius = ASTEROID_SIZES[size]
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, 3) if size == "large" else random.uniform(2, 4)
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed
        # Precompute random radii for each vertex
        self.vertex_offsets = [random.uniform(0.7, 1.2) for _ in range(12)]
        self.vertices = self.generate_vertices()

    def generate_vertices(self):
        points = []
        for i in range(12):
            angle = i * (2 * math.pi / 12)
            radius = self.radius * self.vertex_offsets[i]
            x = self.x + math.cos(angle) * radius
            y = self.y + math.sin(angle) * radius
            points.append((x, y))
        return points

    def update(self, width, height):
        self.x += self.dx
        self.y += self.dy
        self.x %= width
        self.y %= height
        self.vertices = self.generate_vertices()

    def draw(self, surface):
        pygame.draw.polygon(surface, (150, 150, 150), self.vertices, 2)
        
    def split(self):
        if self.size == "large":
            return [Asteroid(self.x, self.y, "medium"), Asteroid(self.x, self.y, "medium"),]
        if self.size == "medium":
            return [Asteroid(self.x, self.y, "small"), Asteroid(self.x, self.y, "small"),]
        else:
            return []