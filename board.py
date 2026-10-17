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

player1_postions = []
player2_postions = []

winning_combination = [1,2,3]
player1_winner = False
player2_winner = False

def check_winner():
    if player1_postions == winning_combination:
        player1_winner = True
        print("Player 1 is the winner")
    elif player2_postions == winning_combination:
        player2_winner = True
        print("Player 2 is the winner")

def player_inputs():
    player1_input = int(input("Player 1, please enter number (1-9): "))
    if player1_input > 0 and player1_input < 10 and type(grid[int(player1_input) - 1]) != str:
        player1_postions.append(player1_input)
        grid[int(player1_input) - 1] = "X"
        check_winner()
        print_grid()
    else:
        print("Not a valid Number or Postion is already taken")

    player2_input = int(input("Player 2, please enter number (1-9): "))
    if player2_input > 0 and player2_input < 10 and type(grid[int(player2_input) - 1]) != str:
        player2_postions.append(player2_input)
        grid[int(player2_input) - 1] = "O"
        check_winner()
        print_grid()
    else:
        print("Not a valid Number or Postion is already taken")


while player1_winner == False and player2_winner == False:
    player_inputs()





