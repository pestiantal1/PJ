import pygame
from enum import Enum

# Game_State enum
class Game_State(Enum):
    MENU = 1,
    PLAYING = 2,
    SCORES = 3

# Initialize Pygame
pygame.init()

# Képernyő méretei
SCREEN_WIDTH = 800 # szélesség
SCREEN_HEIGHT = 600 # magasság

# Színek
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#FONT_COLOR = pass

# font beállítás
font = pygame.font.Font(None, 36)  # alapértelmezett betűtípus, 36-os mérettel


# Kép frissítési sebesség
FPS = 30
clock = pygame.time.Clock()

# Képernyő létrehozása
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kattintós játék")

# Rajzolási parancs(ok) definiálása
def draw_menu(player_name):
    screen.fill(WHITE)
    
    text_surface = font.render("Gépeld be a neved:", True, BLACK)  # Szöveg renderelése fekete színnel
    screen.blit(text_surface, (SCREEN_WIDTH/2-100, 0))

    text_surface = font.render(player_name, True, BLACK)
    screen.blit(text_surface, (SCREEN_WIDTH/2-30, 30))


def draw_game(player_name, score):
    screen.fill(BLUE)
    
    text_surface = font.render(player_name, True, BLACK)  # Szöveg renderelése fekete színnel
    screen.blit(text_surface, (10,10))

    text_surface = font.render(str(score), True, BLACK)
    screen.blit(text_surface, (10, 50))
    
    
def draw_scores(scores):
    """
    Kirajzolja a ponttáblát a képernyőre
    """
    screen.fill(GREEN)

def draw_points(point_list):
    """
    Kirajzolja a pontokat a listában megadott helyekre
    """
    pass

def draw_triangles(point_list):
    """
    Kirajzolja a pontok listájából a háromszögeket.
    Ha pontok száma < 3 nem csinál semmit
    Ügyeljünk az utolsó pontokra, hogyha nem 3-mal osztható a pont lista koordinátái
    """
    counter = 0
    
    if len(point_list) < 3:
        return
    
    for i in range(0, len(point_list) - (len(point_list) % 3), 3):
        triangle_points = [
            point_list[i],
            point_list[i+1],
            point_list[i+2]
        ]
        pygame.draw.polygon(screen, BLACK, triangle_points, 1)
    
    
# Segédfüggvények
def move_points(point_list, offset):
    """
    Megváltoztatja az összes pont koordinátáját az offset ( list(x,y) ) mértékével.
    Visszatér az új pontlistával
    """
    pass

def calculate_score(triangle_coords):
    """
    Visszatér a képernyőn lévő pontok számával
    """
    pass

def modify_direction(key, direction, speed):
    """
    Leírást lásd 2. lecke Nehéz része
    """
    pass

def main():
    # Változók előkészítése
    running = True
    
    game_state = Game_State.MENU
    
    player_name = ""
    score = 0
    scores = []
    
    click_points = []
    
    
    # Game loop
    while running:
        print(game_state) # debug
        
        # Esemény kezelés
        for event in pygame.event.get():
            # folyamatosan figyelt események
            if event.type == pygame.QUIT: # X-re kattintás a jobb felső sarokban
                running = False

            # menüben figyelt események
            if game_state == Game_State.MENU:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # print("enter")
                        #ITT GO TO PLAYING STATE
                        game_state = Game_State.PLAYING
                        
                    else:
                        # print(event.dict["unicode"])
                        #APPEND TO PLAYER NAME
                        player_name += (event.dict["unicode"])
            # játék közben figyelt események
            if game_state == Game_State.PLAYING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = Game_State.SCORES
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score += 1
                    # print(event.dict["pos"])
                    click_points.append(event.dict["pos"])
            
            
            # scores közben figyelt események
            if game_state == Game_State.SCORES:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_state = Game_State.MENU
            
            pass
                # score növelése


                # kilépés a játékból, score elmentése és változók kezdő helyzetbe állítása
                

                # pontok mozgatásával kapcsolatos események                


            # játék vége állapotból átkerülés a menü állapotba
            pass

        # Rajzolási parancsok kiadása, játékállapottól függően
        if game_state == Game_State.MENU:
            draw_menu(player_name)
        if game_state == Game_State.PLAYING:
            draw_game(player_name, score)
            draw_triangles(click_points)
        if game_state == Game_State.SCORES:
            draw_scores(scores) 
        # Képernyő frissítése
        pygame.display.flip()

        # FPS alkalmazása
        clock.tick(FPS)

    # Kilépés
    pygame.quit()

# Projekt belépési pontja
if __name__ == "__main__":
    main()