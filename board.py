# create grid
#a, b, c, d, e, f, g, h, i = 1, 2, 3, 4, 5, 6, 7, 8, 9
#grid =[a, b, c, d, e, f, g, h, i]
grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def print_grid():
    print(f"{grid[0]} | {grid[1]} | {grid[2]}")
    print("---------")
    print(f"{grid[3]} | {grid[4]} | {grid[5]}")
    print("---------")
    print(f"{grid[6]} | {grid[7]} | {grid[8]}")


def player_inputs():
    player1_input = input("Player 1, please enter number (1-9): ")
    grid[int(player1_input) - 1] = "X"
    print_grid()

    player2_input = input("Player 2, please enter number (1-9): ")
    grid[int(player2_input) - 1] = "O"
    print_grid()

player_inputs()