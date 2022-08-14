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

break_line = [2, 5, 8]


def print_grid(grid):
    """
    This function is a function that creates
    the number of spaces and formats the grid.
    """
    print("\nGrid Status\n")
    for index in range(len(grid)):
        print(grid[index], end=" ")
        if index == break_line[0] or index == break_line[1]
        or index == break_line[2]:
            print (" ")

grid = ["_"] * 9  # Set number of spaces in the grid


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


def reset_grid():
    '''
    Resets the board if user wants to play again
    '''
    grid.clear()
    grid.extend(["_"] * 9)


def return_to_first_page():
    '''
    Asks the user if they want to play again or quit when the game ends
    '''
    print("Game Ended...\n")

    print("Enter '1' to play again.")
    print('Enter "Q" if you want to quit the game.')
    while True:
        make_a_choice = input().strip()
        if make_a_choice.lower() == 'q':
            print(f'Thank for playing the game.')
            quit()
        elif make_a_choice == '1':
            print(f'Welcome again.')
            reset_grid()
            play_game()

        else:
            print("Invalid selection. Please select '1' or 'q'")


def play_game():

    number_of_moves = 0  # Variable of number of moves used to not let players
    # exceed the number of valid moves.

    while True:
        """
        Game logic, request for Player input,
        generate a random choice for the CPU,
        print the symbol at the chosen location and update the grid.
        """
        while True:
            try:

                choice = int(input("\nPlayer, make your choice "))

                if choice in range(1, 10):
                    if grid[choice - 1] == "_":
                        grid[choice - 1] = choice - 1
                        break
                    else:
                        print("\nCheck the Grid. Invalid option!\n")
                        print_grid(grid)
                else:
                    print("\nCheck the Grid. Invalid option!\n")
                    print_grid(grid)
            except ValueError:
                print("\nCheck the Grid. Invalid option!\n")

        grid[choice - 1] = "X"
        number_of_moves += 1
        winner = check_winner(grid, "X")
        if winner != 0:
            break

        if number_of_moves == 9:
            break
        print_grid(grid)

        computer_choice = random.randint(1, 9)
        while grid[computer_choice - 1] != "_":
            computer_choice = random.randint(1, 9)

        grid[computer_choice - 1] = "O"
        number_of_moves += 1
        print_grid(grid)

        winner = check_winner(grid, "O")
        if winner != 0:
            break

        print_grid(grid)

    if winner == 1:
        print("Congrats! You win")
        return_to_first_page()
    elif winner == 2:
        print("Sorry, you lost")
        return_to_first_page()
    else:
        print("Draw! No one won")
        return_to_first_page()

    print_grid(grid)

play_game()
