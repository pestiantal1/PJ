from asciimatics.screen import Screen
import time

def spiral(screen: Screen):
    # Állítsuk a kurzort a (0, 0) pontra
    screen.move(0, 0)
    
    # Képernyő méretei - 1
    w = screen.width - 1
    h = screen.height - 1
    
    # Spirál pontjai
    points = [
        (0 * w // 5, 0 * h // 5),
        (5 * w // 5, 0 * h // 5),
        (5 * w // 5, 5 * h // 5),
        (0 * w // 5, 5 * h // 5),
        (0 * w // 5, 1 * h // 5),
        (4 * w // 5, 1 * h // 5),
        (4 * w // 5, 4 * h // 5),
        (1 * w // 5, 4 * h // 5),
        (1 * w // 5, 2 * h // 5),
        (3 * w // 5, 2 * h // 5),
        (3 * w // 5, 3 * h // 5)
    ]
    
    # Rajzoljuk ki a vonalakat
    for p in points:
        screen.draw(p[0], p[1])
    
    # Frissítsük a képernyőt
    screen.refresh()
    time.sleep(10)

# Indítsuk el a programot
Screen.wrapper(spiral)