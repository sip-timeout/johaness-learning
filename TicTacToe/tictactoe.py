list_of_winners_to_ensure_only_one_player_won = []

def column_check(player, column_number):
    global list_of_winners_to_ensure_only_one_player_won
    if game_board[0][column_number] == player and game_board[1][column_number] == player and game_board[2][column_number] == player:
        list_of_winners_to_ensure_only_one_player_won.append(player)

def row_check(player, row_number):
    global list_of_winners_to_ensure_only_one_player_won
    if game_board[row_number][0] == player and game_board[row_number][1] == player and game_board[row_number][2] == player:
        list_of_winners_to_ensure_only_one_player_won.append(player)

def diagonal_check(player):
    global list_of_winners_to_ensure_only_one_player_won
    if game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player or game_board[2][0] == player and game_board[1][1] == player and game_board[0][2] == player:
        list_of_winners_to_ensure_only_one_player_won.append(player)

def __main__(input_matrix):
    global game_board
    global list_of_winners_to_ensure_only_one_player_won

    game_board = input_matrix

    # Has anyone completed a row?
    for y in range(1,3):
        for x in range(3):
           row_check(y,x)

    # Has anyone completed a column?
    for y in range(1,3):
        for x in range(3):
            column_check(y,x)

    # Has anyone completed a diagonal?
    for y in range(1,3):
        diagonal_check(y)

    # Is it a tie?
    if list_of_winners_to_ensure_only_one_player_won == []:
        print("It's a tie!")
        return "tie"

    if len(list_of_winners_to_ensure_only_one_player_won) == 1:
        print("Player " + str(list_of_winners_to_ensure_only_one_player_won[0]) + " won!")
        return list_of_winners_to_ensure_only_one_player_won

    else:
        print("More than one player won! I think there's something wrong with the input.")
        return None

__main__([[1,2,1],[2,1,2],[2,2,1]])