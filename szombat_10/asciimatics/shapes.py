from asciimatics.screen import Screen
import time
import math

def shapes(screen: Screen):
    w = screen.width - 1
    h = screen.height - 1
    
    # 1. Négyzet rajzolása (bal felső sarokban)
    screen.move(w // 6, h // 6)
    square_size = min(w, h) // 8
    square_points = [
        (w // 6 + square_size, h // 6),
        (w // 6 + square_size, h // 6 + square_size),
        (w // 6, h // 6 + square_size),
        (w // 6, h // 6)
    ]
    for p in square_points:
        screen.draw(p[0], p[1])
    
    # 2. Háromszög rajzolása (jobb felső sarokban)
    screen.move(4 * w // 6, h // 6)
    triangle_size = min(w, h) // 8
    triangle_points = [
        (4 * w // 6 + triangle_size // 2, h // 6 + triangle_size),
        (4 * w // 6 - triangle_size // 2, h // 6 + triangle_size),
        (4 * w // 6, h // 6)
    ]
    for p in triangle_points:
        screen.draw(p[0], p[1])
    
    # 3. Kör rajzolása (bal alsó sarokban)
    center_x = w // 6
    center_y = 4 * h // 6
    radius = min(w, h) // 10
    screen.move(center_x + radius, center_y)
    for angle in range(0, 361, 10):
        rad = math.radians(angle)
        x = int(center_x + radius * math.cos(rad))
        y = int(center_y + radius * math.sin(rad))
        screen.draw(x, y)
    
    # 4. Ház rajzolása (jobb alsó sarokban)
    base_x = 4 * w // 6
    base_y = 4 * h // 6
    house_size = min(w, h) // 10
    
    # Ház alapja (négyzet)
    screen.move(base_x, base_y)
    house_base = [
        (base_x + house_size, base_y),
        (base_x + house_size, base_y + house_size),
        (base_x, base_y + house_size),
        (base_x, base_y)
    ]
    for p in house_base:
        screen.draw(p[0], p[1])
    
    # Tető (háromszög)
    screen.move(base_x, base_y)
    roof = [
        (base_x + house_size // 2, base_y - house_size // 2),
        (base_x + house_size, base_y),
        (base_x, base_y)
    ]
    for p in roof:
        screen.draw(p[0], p[1])
    
    # Ajtó
    door_w = house_size // 4
    door_h = house_size // 2
    door_x = base_x + house_size // 2 - door_w // 2
    door_y = base_y + house_size
    screen.move(door_x, door_y)
    door = [
        (door_x + door_w, door_y),
        (door_x + door_w, door_y - door_h),
        (door_x, door_y - door_h),
        (door_x, door_y)
    ]
    for p in door:
        screen.draw(p[0], p[1])
    
    # Frissítsük a képernyőt
    screen.refresh()
    time.sleep(10)

# Indítsuk el a programot
Screen.wrapper(shapes)