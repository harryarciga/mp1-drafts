import os
import subprocess
import sys
import time

def clear_screen(): #to clear the terminal after every input
    if sys.stdout.isatty():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run([clear_cmd])

def first_grid_setup(row, col): #basic set-up, to control size of grid
    grid = []
    d = []
    for i in range(row):
        if i == 0 or i == max(range(row)):
            grid.append(['#'] * col)
        else:
            grid.append(['.'] * col)
        grid[i][0] = '#'
        grid[i][-1] = '#'

    for m in grid:
        d.append(m)
    return d

# print(first_grid_setup(4, 9))

def grid_added_elements(row, col): #to add any more element to the grid (PRINT THIS!)
    grid = first_grid_setup(row, col)
    d = []
    #first grid
    # grid[3][7], grid[2][7] = '#', '#' #extra walls
    # grid[2][2], grid[2][4], grid[2][6], grid[2][8], grid[2][10], grid[2][12] = 'P', 'P', 'P', 'P', 'P', 'P' #pans
    grid[1][1], grid[1][2] = 'O', 'O'
    grid[2][6], grid[2][7] = 'P', 'P'
    # grid[1][3], grid[1][11], grid[3][1], grid[3][6], grid[3][8], grid[3][13] = 'O', 'O', 'O', 'O', 'O', 'O' #nests
    for m in grid:
        d.append(m)
    return d

# print(grid_added_elements(4, 9))

def separate_moves(args): #to throw away any unnecessary input, to accept multiple inputs at once
    moves = 'LBFRlbfr'
    s = []
    for arg in args:
        if arg in moves:
            s.append(arg)
    return s

def actual_moves(args): #appends the direction to which the eggs would be rolling
    d = []
    moves = separate_moves(args)
    directions = '↑←↓→'
    for move in moves:
        if move == 'L' or move == 'l':
            d.append(directions[1])
        elif move == 'B' or move == 'b':
            d.append(directions[2])
        elif move == 'F' or move == 'f':
            d.append(directions[0])
        elif move == 'R' or move == 'r':
            d.append(directions[3])
    return "".join(d)

def egg_coords(row, col): #to get the original coords of the eggs
    # return [(2, 3), (2, 5), (2, 9), (2, 11), (3, 3), (3, 11)] #change at any time
    return [(1, 6), (1, 7)]

def egg_movements(args, row, col, grid): #updates the coords of the eggs
    grid = grid_added_elements(row, col)
    coords = egg_coords(row, col)
    updated = []

    for r, c in coords:
        if args == 'B' or args == 'b':
            while grid[r - 1][c] != '#' and grid[r - 1][c] != '0':
                r -= 1
            updated.append((r, c))
            # else:
            #     updated.append((r, c))
            # updated.append((r, c))
        if args == 'F' or args == 'f':
            while grid[r + 1][c] != '#' and grid[r - 1][c] != '0':
                r += 1
            updated.append((r, c))
            # else:
            #     updated.append((r, c))
        if args == 'L' or args == 'l':
            while grid[r][c - 1] != '#' and grid[r - 1][c] != '0':    
                c -= 1
            updated.append((r, c))
            # else:
            #     updated.append((r, c))
        if args == 'R' or args == 'r':
            while grid[r][c + 1] != '#' and grid[r - 1][c] != '0':
                c += 1
            updated.append((r, c))
            # else:
            #     updated.append((r, c))

    return updated

# print(egg_movements('L', 4, 9))

def first_level():
    row = 4
    col = 9
    grid = grid_added_elements(row, col)
    coords = egg_coords(row, col)
    count = 5

    for r, c in coords:
        grid[r][c] = '0'

    while count != 0:
        for m in grid:
            print(''.join(m))
        inp = input('try this mf: ')
        time.sleep(0.09)
        coords = egg_movements(inp, row, col, grid)
        print(coords)
        for r, c in coords:
            grid[r][c] = '0'
        count -= 1
        clear_screen()

    # for m in grid:
    #     print(''.join(m))

# first_level()

def compiled_elements():
    inps = ''
    count = 5
    print(grid_added_elements(5, 15))
    print('Remaining move/s: ' + str(count))
    print('Previous move/s: ' + inps)
    while count != 0:
        x = input('Enter move/s here: ')
        clear_screen()
        count -= len(actual_moves(str(x)))
        inps += actual_moves(str(x))
        for m in grid_added_elements(5, 15):
            print(''.join(m))
        print('Remaining move/s: ' + str(count))
        print('Previous move/s: ' + inps)

