import pygame
import sys
from pygame.locals import KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_f, K_b, K_l, K_r, QUIT, K_DELETE

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 768
FPS = 60

game_light = pygame.image.load('images/game_light.png')
game_dark = pygame.image.load('images/game_dark.png')
win_light = pygame.image.load('images/win_light.png')
win_dark = pygame.image.load('images/win_dark.png')
lose_light = pygame.image.load('images/lose_light.png')
lose_dark = pygame.image.load('images/lose_dark.png')

def load_assets():
    assets = {
        "egg": pygame.image.load("assets/egg.png"),
        "nest": pygame.image.load("assets/nest.png"),
        "full_nest": pygame.image.load("assets/full_nest.png"),
        "frying_pan": pygame.image.load("assets/frying_pan.png"),
        "grass": pygame.image.load("assets/grass.png"),
        "wall": pygame.image.load("assets/wall.png")
    }
    for key, image in assets.items():
        assets[key] = pygame.transform.scale(image, (81, 81))
    return assets

def display_grid(screen, grid, assets):
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            x, y = col_idx * 27, row_idx * 27
            if cell == '🥚':
                screen.blit(assets['egg'], (x, y))
            elif cell == '🪹':
                screen.blit(assets['nest'], (x, y))
            elif cell == '🪺':
                screen.blit(assets['full_nest'], (x, y))
            elif cell == '🍳':
                screen.blit(assets['frying_pan'], (x, y))
            elif cell == '🟩':
                screen.blit(assets['grass'], (x, y))
            else:
                screen.blit(assets['wall'], (x, y))


def load_level(filename):
    with open(filename, encoding="utf-8") as file:
        num_rows = int(file.readline().strip())
        num_moves = int(file.readline().strip())
        grid = [list(file.readline().strip()) for _ in range(num_rows)]
    return grid, num_moves, 0


def apply_move(grid, move, points):
    prev_grid = [row[:] for row in grid]  
    if move == 'l':
        grid, points = tilt_grid(grid, points, dx=0, dy=-1)
    elif move == 'r':
        grid, points = tilt_grid(grid, points, dx=0, dy=1)
    elif move == 'f':
        grid, points = tilt_grid(grid, points, dx=-1, dy=0)
    elif move == 'b':
        grid, points = tilt_grid(grid, points, dx=1, dy=0)
    

    if grid != prev_grid:
        return grid, points, True  
    
    return grid, points, False  


def tilt_grid(grid, points, dx, dy):
    num_rows = len(grid)
    num_cols = len(grid[0])
    moved = True

    while moved:
        moved = False
        new_grid = [row[:] for row in grid]

        if dx == 0 and dy != 0:  
            for r in range(num_rows):
                row = ''.join(grid[r])
                if dy == -1: 
                    shifted_row, row_moved, updated_points = step_shift_eggs_with_rules(row, points, 'left')
                elif dy == 1:
                    shifted_row, row_moved, updated_points = step_shift_eggs_with_rules(row, points, 'right')
                new_grid[r] = list(shifted_row)
                points = updated_points
                moved = moved or row_moved

        elif dy == 0 and dx != 0:  # Vertical movement
            columns = [''.join([grid[r][c] for r in range(num_rows)]) for c in range(num_cols)]
            shifted_columns = []
            for col in columns:
                if dx == -1:  # Up
                    shifted_col, col_moved, updated_points = step_shift_eggs_with_rules(col, points, 'left')
                elif dx == 1:  # Down
                    shifted_col, col_moved, updated_points = step_shift_eggs_with_rules(col, points, 'right')
                shifted_columns.append(shifted_col)
                points = updated_points
                moved = moved or col_moved

            for c in range(num_cols):
                for r in range(num_rows):
                    new_grid[r][c] = shifted_columns[c][r]

        grid = [row[:] for row in new_grid]
    return grid, points

def step_shift_eggs_with_rules(line, points, direction):
    grass = '🟩'
    frying_pan = '🍳'
    nest = '🪹'
    full_nest = '🪺'
    line_list = list(line)
    moved = False

    if direction == 'left':
        for i in range(1, len(line_list)):
            if line_list[i] == '🥚':
                if line_list[i - 1] == frying_pan: 
                    line_list[i] = grass
                    moved = True
                    points -= 5
                elif line_list[i - 1] == nest: 
                    line_list[i - 1] = full_nest
                    line_list[i] = grass
                    moved = True
                    points += 10
                elif line_list[i - 1] == grass: 
                    line_list[i - 1], line_list[i] = line_list[i], grass
                    moved = True

    elif direction == 'right':
        for i in range(len(line_list) - 2, -1, -1):
            if line_list[i] == '🥚':
                if line_list[i + 1] == frying_pan: 
                    line_list[i] = grass
                    moved = True
                    points -= 5
                elif line_list[i + 1] == nest:
                    line_list[i + 1] = full_nest
                    line_list[i] = grass
                    moved = True
                    points += 10
                elif line_list[i + 1] == grass: 
                    line_list[i + 1], line_list[i] = line_list[i], grass
                    moved = True

    return ''.join(line_list), moved, points

def is_game_over(grid):
    empty_nests = sum(row.count('🪹') for row in grid)
    eggs = sum(row.count('🥚') for row in grid)
    return empty_nests == 0 or eggs == 0

def check_if_win_or_lose(grid):
    empty_nests = sum(row.count('🪹') for row in grid)
    if empty_nests == 0:
        return True
    else:
        return False

def start_gui_with_level(filename, mode="light"):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Egg Roll")
    clock = pygame.time.Clock()

    # Load assets
    assets = load_assets()

    click = False

    grid, num_moves, points = load_level(filename)
    prev_moves = []

    
    while num_moves > 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                valid_move = False
                if event.key == K_DELETE:
                    start_gui_with_level(filename, mode)
                elif event.key == K_UP or event.key == K_f:
                    grid, points, valid_move = apply_move(grid, 'f', points)
                    if valid_move:
                        prev_moves.append('F')
                elif event.key == K_DOWN or event.key == K_b:
                    grid, points, valid_move = apply_move(grid, 'b', points)
                    if valid_move:
                        prev_moves.append('B')
                elif event.key == K_LEFT or event.key == K_l:
                    grid, points, valid_move = apply_move(grid, 'l', points)
                    if valid_move:
                        prev_moves.append('L')
                elif event.key == K_RIGHT or event.key == K_r:
                    grid, points, valid_move = apply_move(grid, 'r', points)
                    if valid_move:
                        prev_moves.append('R')
                if valid_move:
                    num_moves -= 1


        # Draw everything
        if mode == "light":
            screen.blit(game_light, (0, 0))
        else:
            screen.blit(game_dark, (0, 0))
        display_grid(screen, grid, assets)

        # Display additional game info
        font = pygame.font.Font(None, 36)
        #print(prev_moves)
        if prev_moves == []:
            pass
        else:
            prev_moves_text = font.render(f"{''.join(prev_moves)}", True, (121,78,7))
            screen.blit(prev_moves_text, (315,583))
        moves_text = font.render(f"{num_moves}", True, (121, 78, 7))
        screen.blit(moves_text, (315,623))
        points_text = font.render(f"{points}", True, (121, 78, 7))
        screen.blit(points_text, (315, 668))


        #print(points)
        if is_game_over(grid):
            if check_if_win_or_lose(grid) == True and mode == "light":
                screen.blit(win_light,(0,0))
            elif check_if_win_or_lose(grid) == False and mode == "light":
                screen.blit(lose_light,(0,0))
            elif check_if_win_or_lose(grid) == True and mode == "dark":
                screen.blit(win_dark,(0,0))
            else:
                screen.blit(lose_dark,(0,0))
            display_grid(screen,grid,assets)

            if len(''.join(prev_moves)) == 1:
                points = (sum(row.count('🪺') for row in grid)) * 10
                prev_moves_text = font.render(f"{''.join(prev_moves)}", True, (121,78,7))
                moves_text = font.render(f"{num_moves}", True, (121, 78, 7))
                points_text = font.render(f"{points + num_moves * 2}", True, (121, 78, 7))
                screen.blit(prev_moves_text, (315,583))
                screen.blit(moves_text, (315,623))
                screen.blit(points_text, (315, 668))

            else:
                prev_moves_text = font.render(f"{''.join(prev_moves)}", True, (121,78,7))
                moves_text = font.render(f"{num_moves}", True, (121, 78, 7))
                points_text = font.render(f"{points + num_moves * 2}", True, (121, 78, 7))
                screen.blit(prev_moves_text, (315,583))
                screen.blit(moves_text, (315,623))
                screen.blit(points_text, (315, 668))


        pygame.display.flip()
        clock.tick(FPS)


    pygame.quit()
    sys.exit()
