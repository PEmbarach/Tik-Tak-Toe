import random

print("Welcome to Tik-Tok-Toe Game")

print("_ _ _")
print("_ _ _")
print("_ _ _")
print("\n")

print("1 2 3")
print("4 5 6")
print("7 8 9")
print("\n")

def print_grid(grid):
    """
    This function is a function that creates the number of spaces and formats the grid.    
    """
    print("\nGrid Status\n")
    for index in range (len(grid)):
        print(grid[index], end=" ")
        if index == 2 or index == 5 or index == 8:
            print (" ")

grid = ["_"] * 9 # Set number of spaces in the grid

def check_winner(grid, player):
    """
    This function checks for a winner
    """

    # Check lines
    if grid[0] == player and grid[1] == player and grid[2] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[3] == player and grid[4] == player and grid[5] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[6] == player and grid[7] == player and grid[8] == player:
        if player == "X":
            return 1
        else:
            return 2

    # Check Columns
    if grid[0] == player and grid[3] == player and grid[6] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[1] == player and grid[4] == player and grid[7] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[2] == player and grid[5] == player and grid[8] == player:
        if player == "X":
            return 1
        else:
            return 2

    # Check Diagonals
    if grid[0] == player and grid[4] == player and grid[8] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[2] == player and grid[4] == player and grid[6] == player:
        if player == "X":
            return 1
        else:
            return 2

    return 0
