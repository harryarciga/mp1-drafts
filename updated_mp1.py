import os
import subprocess
import sys
import time
from argparse import ArgumentParser
from mp1_classes import Moves, Board


def main(): 
    """Handles the interaction with the player."""
    parser = ArgumentParser()
    parser.add_argument('stage_file')
    args = parser.parse_args()

    grid, num_moves, points = load_level(args.stage_file)
    prev_moves = []

    while num_moves > 0 and (any('🥚' in row for row in grid) and
        any('🪹' in row for row in grid)):
            clear_screen()
            display_grid(grid)
            print(f"Previous moves: {''.join(prev_moves)}")
            print(f"===============\nTo see the Top 3 high scores (leaderboard) for this grid, you may click the \'H\' key on your keyboard. Note that the high scores will not be shown if the input is \'RHL\', \'LH\', or any variants where \'H\' is together with other symbols in the input.\n===============")
            print(f"Remaining moves: {num_moves}")
            print(f"Points: {points}")

            directions = input("Enter move/s: ")
            match directions:
                case 'H' | 'h':
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
    print(f"Points: {points + (num_moves) * 2}")
    

def load_level(filename): 
    """Reads and takes the values located in the .in file.

    Keyword arguments:
        filename -- the filename of a level, containing the grid,
                    and the number of moves

    Returns:
        grid -- a list containing the characters of the grid
        num_moves -- an int denoting the remaining moves of the player
        int -- the current points of the player
    """

    with open(filename, encoding="utf-8") as file:
        num_rows = int(file.readline().strip())
        num_moves = int(file.readline().strip())
        grid = [list(file.readline().strip()) for _ in range(num_rows)]
    return grid, num_moves, 0


def display_grid(grid: list): 
    """Displays the grid."""
    for row in grid:
        print(''.join(row))


def clear_screen(): 
    """Clears the terminal."""
    if sys.stdout.isatty():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run([clear_cmd])


def separate_moves(args: list) -> list: 
    """Takes correct inputs and discards incorrect ones.

    Keyword argument:
        args -- a list denoting the inputs of the player

    Returns:
        list -- a filtered list, containing only valid moves
    """
    if isinstance(args, str):
        return [move.lower() for move in args if move.lower() in 'lrfb']
    else:
        return []


def get_leaderboard_scores(filename): 
    """Reads the leaderboard related to the file opened in the terminal.

    Keyword argument:
        filename -- the filename of the leaderboard

    Returns:
        first -- an int, denoting the highest score
        second -- an int, the second highest score
        third -- an int, the third highest score
        None -- if the file is not read
    """
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


def apply_move(grid: list, move: str, points: int) -> tuple[list, int]:
    """Links the inputs to the movement within the grid.

    Keyword arguments:
        grid -- a list containing the characters in the grid
        move -- a str, dictates the direction
        points -- an int, the player's current score

    Returns:
        list -- a list, showing the updated grid
        int -- an int, showing the updated score
    """
    match move:
        case Moves.LEFTWARD:
            grid, points = tilt_grid(grid, points, 0, -1)
        case Moves.RIGHTWARD:
            grid, points = tilt_grid(grid, points, 0, 1)
        case Moves.FORWARD:
            grid, points = tilt_grid(grid, points, -1, 0)
        case Moves.BACKWARD:
            grid, points = tilt_grid(grid, points, 1, 0)
    return grid, points


def tilt_grid(grid: list, points: int, dx: int, dy: int) -> tuple[list, int]:  
    """Determines the type of movement each egg will undergo.

    Keyword arguments:
        grid -- a list, denoting the present state of the grid
        points -- an int, denoting the player's present score
        dx -- an int, dictating if the movement should be left or right
        dy -- an int, dictating if the movement should be up or down

    Returns:
        grid -- a list, showing the updated grid
        points -- an int, showing the updated score
    """
    num_rows = len(grid)
    num_cols = len(grid[0])
    moved = True

    while moved:  
        moved = False
        new_grid = [row[:] for row in grid]  
        if dx == 0: 
            for r in range(num_rows):
                row = ''.join(grid[r])
                if dy == -1: 
                    shift_row, r_moved, update_points = step_shift_eggs(row, 
                                                                        points, 
                                                                        'left')
                elif dy == 1: 
                    shift_row, r_moved, update_points = step_shift_eggs(row, 
                                                                        points, 
                                                                        'right')

                new_grid[r] = list(shift_row)
                points = update_points
                moved = moved or r_moved
        elif dy == 0: 
            columns = [''.join([grid[r][c] 
                        for r in range(num_rows)]) 
                        for c in range(num_cols)]
            shifted_columns = []
            for col in columns:
                if dx == -1:  
                    shift_col, c_moved, update_points = step_shift_eggs(col, 
                                                                        points, 
                                                                        'left')
                elif dx == 1:  
                    shift_col, c_moved, update_points = step_shift_eggs(col, 
                                                                        points, 
                                                                        'right')

                shifted_columns.append(shift_col)
                points = update_points
                moved = moved or c_moved
            for c in range(num_cols):
                for r in range(num_rows):
                    new_grid[r][c] = shifted_columns[c][r]
        if moved:
            clear_screen()
            display_grid(new_grid)
            time.sleep(0.3)  
        grid = [row[:] for row in new_grid] 

    return grid, points


def step_shift_eggs(
        line: str, points: int, direction: str) -> tuple[str, bool, int]: 
    """This function shifts the position of the egg from left
    to right, depending on the dictated direction.

    Keyword arguments:
        line -- a str, denoting a line containing the chars of the grid
        points -- an int, denoting the player's current score
        direction -- a str, dictating if the movement is left or right

    Returns:
        str -- denoting the updated line after the movement
        bool -- is True if the egg moved, and False otherwise
        int -- denoting the updated score
    """
    line_list = list(line)
    moved = False

    match direction:   
        case 'left':
            for i in range(1, len(line_list)):
                if line_list[i] == '🥚':
                    match line_list[i - 1]:
                        case Board.PAN:
                            line_list[i] = Board.GRASS
                            moved = True
                            points -= 5
                        case Board.EMPTYNEST:
                            line_list[i - 1] = Board.FULLNEST
                            line_list[i] = Board.GRASS
                            moved = True
                            points += 10
                        case Board.GRASS:
                            line_list[i - 1] = line_list[i]  
                            line_list[i] = Board.GRASS
                            moved = True
        case 'right':
            for i in range(len(line_list) - 2, -1, -1):
                if line_list[i] == '🥚':
                    match line_list[i + 1]:
                        case Board.PAN:
                            line_list[i] = Board.GRASS
                            moved = True
                            points -= 5
                        case Board.EMPTYNEST:
                            line_list[i + 1] = Board.FULLNEST
                            line_list[i] = Board.GRASS
                            moved = True
                            points += 10
                        case Board.GRASS:
                            line_list[i + 1] = line_list[i] 
                            line_list[i] = Board.GRASS
                            moved = True

    return ''.join(line_list), moved, points


def change_leaderboard(filename, new_score):
    """Updates the leaderboard.
    
    Keyword arguments:
        filename -- the filename of the leaderboard
        new_score -- an int, denoting the score to be put on the board
    """
    first_score, second_score, third_score = get_leaderboard_scores(filename)
    scores = [first_score, second_score, third_score, new_score]
    scores = sorted(scores, reverse=True)[:3]
    with open('hs_mp1_' + filename, 'w', encoding="utf-8") as file:
        for score in scores:
            file.write(f"{score}\n")


if __name__ == "__main__":
    main()

