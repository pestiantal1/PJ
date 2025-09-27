import random
from entities.asteroid import Asteroid

def spawn_asteroids(num, width, heigth, avoid_pos=None, avoid_radius=100):
    asteroids = []
    for _ in range(num):
        while True:
            x = random.randint(0, width)
            y = random.randint(0, heigth)
            if avoid_pos:
                dist = ((x - avoid_pos[0]) ** 2 + (y - avoid_pos[1]) ** 2) ** 0.5
                if dist < avoid_radius:
                    continue
            asteroids.append(Asteroid(x,y))
            break
    return asteroids