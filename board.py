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

winning_combination = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
player1_winner = False
player2_winner = False

def check_winner():
    if any(sorted(player1_postions) == combo for combo in winning_combination):
        global player1_winner
        player1_winner = True
        print("Player 1 is the winner")
    elif any(sorted(player2_postions) == combo for combo in winning_combination):
        global player2_winner
        player2_winner = True
        print("Player 2 is the winner")
    return player1_winner, player2_winner

def player_inputs():
    player1_input = int(input("Player 1, please enter number (1-9): "))
    if player1_input > 0 and player1_input < 10 and type(grid[int(player1_input) - 1]) != str:
        player1_postions.append(player1_input)
        grid[int(player1_input) - 1] = "X"
        print_grid()
        check_winner()
        if player1_winner == True:
            return
    else:
        print("Not a valid Number or Postion is already taken")

    player2_input = int(input("Player 2, please enter number (1-9): "))
    if player2_input > 0 and player2_input < 10 and type(grid[int(player2_input) - 1]) != str:
        player2_postions.append(player2_input)
        grid[int(player2_input) - 1] = "O"
        print_grid()
        check_winner()
    else:
        print("Not a valid Number or Postion is already taken")


while player1_winner == False and player2_winner == False:
    player_inputs()





