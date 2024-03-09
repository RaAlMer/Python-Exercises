from random import randrange

PLAYER_O = 'O'
PLAYER_X = 'X'

initial_board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

def display_board(board):
    # The function takes a parameter containing the current state of the board
    # and displays it on the console.    
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

def enter_move(board):
    # The function takes the current state of the board and asks the user about their move,  
    # checks the input, and updates the board according to the user's decision.
    display_board(board)
    movement = int(input('Input your movement: '))
    if movement not in range(1, 10):
        print('Input a number between 1 and 9')
        movement = int(input('Input your movement: '))
    while divmod(movement - 1, 3) not in make_list_of_free_fields(board):
        print('That square is not empty')
        movement = int(input('Choose another one: '))
    if movement <= 3:
        board[0][movement - 1] = PLAYER_O
    elif movement <= 6:
        movement %= 4
        board[1][movement] = PLAYER_O
    else:
        movement %= 7
        board[2][movement] = PLAYER_O

def make_list_of_free_fields(board):
    # The function examines the board and builds a list of all empty squares.
    # The list is composed of tuples, where each tuple is a pair of numbers indicating the row and column.
    empty_positions = [(row, col) for row in range(3) for col in range(3) if board[row][col] not in [PLAYER_X, PLAYER_O]]
    return empty_positions

def victory_for(board, sign):
    # The function analyzes the status of the board to check 
    # if the player using 'O's or 'X's has won the game.
    # Assuming board is a 3x3 list and sign is the player's sign
    for row in range(3):
        for col in range(3):
            if col + 2 < 3 and board[row][col] == sign and board[row][col + 1] == sign and board[row][col + 2] == sign:
                print('You won!: ', sign)
                return True
            if row + 2 < 3 and board[row][col] == sign and board[row + 1][col] == sign and board[row + 2][col] == sign:
                print('You won!: ', sign)
                return True
            if row == 0 and col == 0 and board[row][col] == sign and board[row + 1][col + 1] == sign and board[row + 2][col + 2] == sign:
                print('You won!: ', sign)
                return True
            if row == 0 and col == 2 and board[row][col] == sign and board[row + 1][col - 1] == sign and board[row + 2][col - 2] == sign:
                print('You won!: ', sign)
                return True
    return False
            
def draw_move(board):
    # The function draws the machine's move and updates the board.
    movement_machine = randrange(10)
    while divmod(movement_machine - 1, 3) not in make_list_of_free_fields(board):
        movement_machine = randrange(10)
    if movement_machine <= 3:
        board[0][movement_machine - 1] = PLAYER_X
    elif movement_machine <= 6:
        movement_machine %= 4
        board[1][movement_machine] = PLAYER_X
    else:
        movement_machine %= 7
        board[2][movement_machine] = PLAYER_X

def main(board):
    display_board(board)
    board[1][1] = PLAYER_X
    while True:
        enter_move(board)
        if victory_for(board, PLAYER_O):
            break
        elif not make_list_of_free_fields(board):
            print('Draw!')
            break
        draw_move(board)
        display_board(board)
        if victory_for(board, PLAYER_X):
            break
        elif not make_list_of_free_fields(board):
            print('Draw!')
            break
    display_board(board)
    
if __name__ == "__main__":
    main(initial_board)
