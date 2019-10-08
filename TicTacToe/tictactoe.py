list_of_winners = []

class Gameboard(object):
    def __init__(self, board):
        self.board = board
    def get(self):
        return self.board

def row_check(board, row_number):
    list_of_unique_members_of_row = []
    for i in range (0,len(board[0])):
        if board[row_number][i] not in list_of_unique_members_of_row:
            list_of_unique_members_of_row.append(board[row_number][i])

    if len(list_of_unique_members_of_row) == 1:
        if list_of_unique_members_of_row[0] not in list_of_winners:
            list_of_winners.append(list_of_unique_members_of_row[0])

def column_check(board, column_number):
    list_of_unique_members_of_column = []
    for i in range(0, len(board[0])):
        if board[i][column_number] not in list_of_unique_members_of_column:
            list_of_unique_members_of_column.append(board[i][column_number])

    if len(list_of_unique_members_of_column) == 1:
        if list_of_unique_members_of_column[0] not in list_of_winners:
            list_of_winners.append(list_of_unique_members_of_column[0])

def diagonal_check_top_left_to_bottom_right(board):
    list_of_unique_members_of_diagonal = []
    for i in range(0, len(board[0])):
        if board[i][i] not in list_of_unique_members_of_diagonal:
            list_of_unique_members_of_diagonal.append(board[i][i])

    if len(list_of_unique_members_of_diagonal) == 1:
        if list_of_unique_members_of_diagonal[0] not in list_of_winners:
            list_of_winners.append(list_of_unique_members_of_diagonal[0])

def diagonal_check_bottom_left_to_top_right(board):
    list_of_unique_members_of_diagonal = []
    for i in range(0, len(board[0])):
        if board[i][(len(board)-i-1)] not in list_of_unique_members_of_diagonal:
            list_of_unique_members_of_diagonal.append(board[i][(len(board)-i-1)])

    if len(list_of_unique_members_of_diagonal) == 1:
        if list_of_unique_members_of_diagonal[0] not in list_of_winners:
            list_of_winners.append(list_of_unique_members_of_diagonal[0])

def __main__(input_matrix):

    game_board = Gameboard(input_matrix)

    for i in range(0, len(game_board.get()[0])):
        row_check(game_board.get(), i)

    for i in range(0, len(game_board.get()[0])):
        column_check(game_board.get(), i)

    diagonal_check_top_left_to_bottom_right(game_board.get())

    diagonal_check_bottom_left_to_top_right(game_board.get())

    # Is it a tie?
    if list_of_winners == []:
        print("It's a tie!")
        return "tie"

    elif len(list_of_winners) == 1:
        print("Player " + str(list_of_winners[0]) + " won!")
        return list_of_winners

    else:
        print("More than one player won! I think there's something wrong with the input.")
        return None

__main__([[4,3,3,5],
          [7,2,5,5],
          [2,5,4,2],
          [5,3,3,4]])