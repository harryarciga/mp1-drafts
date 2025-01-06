import os
import subprocess
import sys
import time
from argparse import ArgumentParser

def main(): #Handles the interaction with the player
    parser = ArgumentParser()
    parser.add_argument('stage_file')
    args = parser.parse_args()

    grid, num_moves, points = load_level(args.stage_file)
    prev_moves = []


    while num_moves > 0 and (any('🥚' in row for row in grid) and any('🪹' in row for row in grid)):
        clear_screen()
        display_grid(grid)
        #print(type(args.stage_file))
        print(f"===============\nTo see the Top 3 high scores (leaderboard) for this grid, you may click the \'H\' key on your keyboard. Note that the high scores will not be shown if the input is \'RHL\', \'LH\', or any variants where \'H\' is together with other symbols in the input.\n===============")
        print(f"Previous moves: {''.join(prev_moves)}")
        print(f"Remaining moves: {num_moves}")
        print(f"Points: {points}")

        directions = input("Enter move/s: ")
        if directions == "H" or directions == "h":
            first_score, second_score, third_score = get_leaderboard_scores(args.stage_file)
            print(f"""===============\nLeaderboard for this level:\n
    1st: {first_score}
    2nd: {second_score}
    3rd: {third_score}
            """)
            input("Press any key to return to the game.")
            
        valid_moves = separate_moves(directions)
        for move in valid_moves:
            if num_moves == 0:
                break
            grid, points = apply_move(grid, move, points)
            move_conversion = {"f": "↑", "b": "↓", "l": "←", "r": "→"}
            prev_moves.append(move_conversion[move])
            num_moves -= 1

    clear_screen()
    display_grid(grid)
    print(f"Previous moves: {''.join(prev_moves)}")
    print(f"Remaining moves: {num_moves}")
    if any('🪹' in row for row in grid):
        print(f"Points: {points}")
    else:
        points = points + (num_moves) * 2
        print(f"Points: {points}")
    change_leaderboard(args.stage_file, points)
    

def load_level(filename): #Reads the information located in the .in file
    with open(filename, encoding="utf-8") as file:
        num_rows = int(file.readline().strip())
        num_moves = int(file.readline().strip())
        grid = [list(file.readline().strip()) for _ in range(num_rows)]
    return grid, num_moves, 0

def display_grid(grid): #Displays the grid
    for row in grid:
        print(''.join(row))

def clear_screen(): #Clears the screen
    if sys.stdout.isatty():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run([clear_cmd])

def separate_moves(args): #Accepts valid moves and discards irrelevant inputs
    if isinstance(args, str):
        return [move.lower() for move in args if move.lower() in 'lrfb']
    else:
        return []

def get_leaderboard_scores(filename): #This reads the leaderboard related to the file opened in the terminal
    leaderboard_file = 'hs_mp1_' + filename
    try:
        with open(leaderboard_file, encoding="utf-8") as file:
            first = int(file.readline().strip())
            second = int(file.readline().strip())
            third = int(file.readline().strip())
        return first, second, third
    except (ValueError, FileNotFoundError) as e:
        print(f"Cannot read the leaderboard file: {e}")
        return
  
def apply_move(grid, move, points): #Links the egg's movements within the grid to the inputs
    if move == 'l':
        grid, points = tilt_grid(grid, points, dx=0, dy=-1)
    elif move == 'r':
        grid, points = tilt_grid(grid, points, dx=0, dy=1)
    elif move == 'f':
        grid, points = tilt_grid(grid, points, dx=-1, dy=0)
    elif move == 'b':
        grid, points = tilt_grid(grid, points, dx=1, dy=0)
    return grid, points

def tilt_grid(grid, points, dx, dy): #Handles the two kinds of movements in the grid: from row to row, and from column to column
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

        elif dy == 0 and dx != 0: 
            columns = [''.join([grid[r][c] for r in range(num_rows)]) for c in range(num_cols)]
            shifted_columns = []
            for col in columns:
                if dx == -1:  
                    shifted_col, col_moved, updated_points = step_shift_eggs_with_rules(col, points, 'left')
                elif dx == 1:  
                    shifted_col, col_moved, updated_points = step_shift_eggs_with_rules(col, points, 'right')
                shifted_columns.append(shifted_col)
                points = updated_points
                moved = moved or col_moved

            for c in range(num_cols):
                for r in range(num_rows):
                    new_grid[r][c] = shifted_columns[c][r]

        if moved:
            clear_screen()
            display_grid(new_grid)
            time.sleep(0.3)  

        grid = [row[:] for row in new_grid] 

    return grid, points

def step_shift_eggs_with_rules(line, points, direction): #Moves the egg from left to right within the grid
    empty_char = '🟩' 
    frying_pan = '🍳'
    nest = '🪹'
    full_nest = '🪺'
    line_list = list(line)
    moved = False

    if direction == 'left':
        for i in range(1, len(line_list)):
            if line_list[i] == '🥚':
                if line_list[i - 1] == frying_pan: 
                    line_list[i] = empty_char
                    moved = True
                    points -= 5
                elif line_list[i - 1] == nest: 
                    line_list[i - 1] = full_nest
                    line_list[i] = empty_char
                    moved = True
                    points += 10
                elif line_list[i - 1] == empty_char: 
                    line_list[i - 1], line_list[i] = line_list[i], empty_char
                    moved = True

    elif direction == 'right':
        for i in range(len(line_list) - 2, -1, -1):
            if line_list[i] == '🥚':
                if line_list[i + 1] == frying_pan: 
                    line_list[i] = empty_char
                    moved = True
                    points -= 5
                elif line_list[i + 1] == nest:
                    line_list[i + 1] = full_nest
                    line_list[i] = empty_char
                    moved = True
                    points += 10
                elif line_list[i + 1] == empty_char: 
                    line_list[i + 1], line_list[i] = line_list[i], empty_char
                    moved = True

    return ''.join(line_list), moved, points

def change_leaderboard(filename, new_score):
    first_score, second_score, third_score = get_leaderboard_scores(filename)
    scores = [first_score, second_score, third_score, new_score]
    scores = sorted(scores, reverse=True)[:3]
    with open('hs_mp1_' + filename, 'w', encoding="utf-8") as file:
        for score in scores:
            file.write(f"{score}\n")


if __name__ == "__main__":
    main()
