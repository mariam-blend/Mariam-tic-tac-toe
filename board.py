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

player1_positions = []
player2_positions = []

winning_combination = ([1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7])

winner = False

def check_winner(player_positions: list[int], player: str):
    for x in winning_combination:
        if set(x).issubset(set(player_positions)):
            print(f"{player} is the winner")
            return True
    return False

def check_inputs(player_input: int):
    return int(player_input) > 0 and player_input < 10 and type(grid[int(player_input) - 1]) != str



def player_inputs(player: str, player_positions: list[int], symbol: str):
    loop_player = False
    valid_input = False
    while loop_player == False: 
        player_input = int(input(f"{player} please enter number (1-9): "))
        valid_input = check_inputs(player_input)
        if valid_input:
            player_positions.append(player_input)
            grid[int(player_input) - 1] = symbol
            print_grid()
            global winner
            winner = check_winner(player_positions, player)
            loop_player = True
            if winner == True:
                return
        else:
            print("Not a valid Number or Postion is already taken")



while winner == False:
    player_inputs('Player 1', player1_positions, 'X')
    player_inputs('Player 2', player2_positions, 'O')
    





