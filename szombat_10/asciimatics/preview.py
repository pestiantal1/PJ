from asciimatics.screen import Screen
import time

def hello(screen: Screen):
    text = 'Hello, World!'
    # Számítsuk ki a középső pozíciót, levonva a szöveg hosszának felét
    x = screen.width // 2 - len(text) // 2
    y = screen.height // 2
    
    screen.print_at(text, x, y)
    screen.refresh()
    time.sleep(10)

# Indítsuk el a programot
Screen.wrapper(hello)