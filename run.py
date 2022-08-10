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

number_of_moves = 0 # Variable of number of moves used to not let players exceed the number of valid moves.

def valid_number():
    """
    Foundation ensures that a number greater than 9 is not used and fixing the bug.
    """
    global choice
    while choice -1 >= 10:
        print("\nInvalid number! Check a valid number on the Grid.\n")
        print_grid(grid)
        choice = int(input("\nPlayer, make your choice \n"))


while True: 
    """
    Game logic, request for Player input, generate a random choice for the CPU, 
    print the symbol at the chosen location and update the grid.
    """
    choice = int(input("\nPlayer, make your choice "))
    valid_number()
    while grid[choice -1] != "_":
        print("\nCheck the Grid. Invalid option!\n")
        print_grid(grid)
        choice = int(input("\nPlayer, make your choice \n"))
        valid_number()

    grid[choice - 1] = "X"
    number_of_moves += 1
    winner = check_winner(grid, "X")
    if winner !=0:
        break

    if number_of_moves == 9:
        break
    print_grid(grid)

    computer_choice = random.randint(1, 9)
    while grid[computer_choice -1] != "_":
        computer_choice = random.randint(1, 9)

    grid[computer_choice - 1] = "O"
    number_of_moves += 1
    winner = check_winner(grid, "O")

    print_grid(grid)

if winner == 1:
    print("Congrats! You win")
elif winner == 2:
   print("Sorry, you lost")
else:
   print("Draw! No one won")

print_grid(grid)