def how_to_play():
    print("~~~ TIC TAC TOE ~~~")
    print("How to play?")
    print("Enter the number of your cell")
    print("\t 1 | 2 | 3 ")
    print("\t---+---+---")
    print("\t 4 | 5 | 6 ")
    print("\t---+---+---")
    print("\t 7 | 8 | 9 ")
    print("Good luck!\n")


def print_grid(board):
    print(f"\t {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("\t---+---+---")
    print(f"\t {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("\t---+---+---")
    print(f"\t {board[2][0]} | {board[2][1]} | {board[2][2]} ")


def who_wins(board):
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None


def get_move(move):
    if move == 1:
        r, c = 0, 0
    elif move == 2:
        r, c = 0, 1
    elif move == 3:
        r, c = 0, 2
    elif move == 4:
        r, c = 1, 0
    elif move == 5:
        r, c = 1, 1
    elif move == 6:
        r, c = 1, 2
    elif move == 7:
        r, c = 2, 0
    elif move == 8:
        r, c = 2, 1
    elif move == 9:
        r, c = 2, 2
    moves = [r, c]
    return moves


def update_grid(board, row, column, last_player):
    board[row][column] = last_player
    return board


def cell_empty(board, row, column):
    if board[row][column] == " ":
        return True
    else:
        return False


if __name__ == "__main__":
    grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    to_continue = True
    MOVES = 0
    winner = who_wins(grid)
    player = "X"
    how_to_play()

    while to_continue:
        if (winner != None) or (MOVES == 9):
            to_continue = False
        else:
            MOVES += 1
            print(f"Player {player}, it's your turn")
            user_move = int(input("\tEnter the number of your cell > "))
            user_moves = get_move(user_move)
            while not cell_empty(grid, user_moves[0], user_moves[1]):
                print("The cell is not empty")
                user_move = int(input("\tEnter the number of your cell > "))
                user_moves = get_move(user_move)
            grid = update_grid(grid, user_moves[0], user_moves[1], player)
            print_grid(grid)
            player = "O" if player == "X" else "X"
            winner = who_wins(grid)
    if player != None:
        print(f"Player {winner} WINS!")
    else:
        print("Draw!")
