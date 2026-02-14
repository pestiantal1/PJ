import pygame
from enum import Enum
import pickle
import json

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
    
    title_text = "Név és pont"
    title_surface = font.render(title_text, True, BLACK)
    title_width, _ = font.size(title_text)
    screen.blit(title_surface, ((SCREEN_WIDTH - title_width) / 2, 20))
    
    ctr = 1
    for name, score in scores.items():
        score_text = f"{name} - {score}"
        score_surface = font.render(score_text, True, BLACK)
        score_width, _ = font.size(score_text)
        screen.blit(score_surface, ((SCREEN_WIDTH - score_width) / 2, 20 + ctr * 40))  # Centered score
        ctr += 1

def draw_points(point_list):
    """
    Kirajzolja a pontokat a listában megadott helyekre
    """
    for i in range(len(point_list)):
        pygame.draw.circle(screen, BLACK, point_list[i], 5)
    

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
    

def save_scores(adatok):
    try:
        with open("scores.txt", "xb") as f:
            pickle.dump({}, f)
    except FileExistsError:
        pass
    
    with open("scores.txt", "wb") as f:
        pickle.dump(adatok, f)
    
def load_scores():
    try:
        with open("scores.txt", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

# Segédfüggvények
def move_points(point_list, offset, speed):
    """
    Megváltoztatja az összes pont koordinátáját az offset ( list(x,y) ) mértékével.
    Visszatér az új pontlistával
    """
    new_points = []
    for point in point_list:
        new_x = point[0] + offset[0] * speed
        new_y = point[1] + offset[1] * speed
        new_points.append((new_x, new_y))
    return new_points

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
    
    scores = load_scores()
    
    click_points = []

    direction = [0,0]

    speed = 1
    
    # Game loop
    while running:
        # print(game_state) # debug
        print(speed)
        # print(scores)
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
                        #frisstine a scores szotarat
                        if player_name in scores:
                            if score > scores[player_name]:
                                scores[player_name] = score
                        else:
                            scores[player_name] = score
                        save_scores(scores)
                        
                    elif event.key == pygame.K_UP:
                        direction[0] = -1
                    elif event.key == pygame.K_DOWN:
                        direction[0] = 1
                    elif event.key == pygame.K_LEFT:
                        direction[1] = -1
                    elif event.key == pygame.K_RIGHT:
                        direction[1] = 1
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction[0] = 0
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        direction[1] = 0
                    
                        
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    score += 1
                    # print(event.dict["pos"])
                    # pygame.mouse.get_pos()
                    click_points.append(event.dict["pos"])
            
            
                if event.type == pygame.MOUSEWHEEL:
                    speed += event.y
                    
                    if speed < 1:
                        speed = 1
                    if speed > 100:
                        speed = 100
                        
            # scores közben figyelt események
            if game_state == Game_State.SCORES:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        score = 0
                        player_name = ""
                        click_points = []
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
            
            if direction[0] != 0 or direction[1] != 0:
                offset = (direction[1], direction[0])
                click_points = move_points(click_points, offset, speed)
            
            draw_game(player_name, score)
            draw_triangles(click_points)
            draw_points(click_points)
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