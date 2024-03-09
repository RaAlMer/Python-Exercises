from random import randrange

PLAYER_O = 'O'
PLAYER_X = 'X'

def display_board(board):
    print('+-------+-------+-------+')
    for row in board:
        print('|       |       |       |')
        print(f'|   {row[0]}   |   {row[1]}   |   {row[2]}   |')
        print('|       |       |       |')
        print('+-------+-------+-------+')

def enter_move(board):
    display_board(board)
    while True:
        try:
            movement = int(input('Enter your move (1-9): '))
            if 1 <= movement <= 9 and divmod(movement - 1, 3) in make_list_of_free_fields(board):
                break
            else:
                print('Invalid move. Please choose a free position (1-9).')
        except ValueError:
            print('Invalid input. Please enter a number.')

    update_board(board, movement, PLAYER_O)

def update_board(board, move, player):
    row, col = divmod(move - 1, 3)
    board[row][col] = player

def make_list_of_free_fields(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ['X', 'O']]

def victory_for(board, sign):
    for row in range(3):
        if all(board[row][col] == sign for col in range(3)) or \
           all(board[col][row] == sign for col in range(3)):
            return True

    if all(board[i][i] == sign for i in range(3)) or \
       all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False

def draw_move(board):
    movement_machine = randrange(1, 10)
    while divmod(movement_machine - 1, 3) not in make_list_of_free_fields(board):
        movement_machine = randrange(1, 10)
    update_board(board, movement_machine, PLAYER_X)

def main():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    display_board(board)
    board[1][1] = PLAYER_X

    while True:
        enter_move(board)
        if victory_for(board, PLAYER_O):
            print('Congratulations! You won!')
            break
        elif not make_list_of_free_fields(board):
            print('It\'s a draw!')
            break

        draw_move(board)
        display_board(board)

        if victory_for(board, PLAYER_X):
            print('The machine won. Better luck next time!')
            break
        elif not make_list_of_free_fields(board):
            print('It\'s a draw!')
            break

    display_board(board)

if __name__ == "__main__":
    main()
