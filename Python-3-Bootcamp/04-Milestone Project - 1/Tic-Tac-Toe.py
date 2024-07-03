import random
from os import system

def create_board(board):
    system('cls')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def player_choice():
    mark = ''

    while not (mark == 'X' or mark == 'O'):
        system('cls')
        mark = input('Player 1, X or O? ').upper()

    if mark == 'X':
        return(mark, 'O')
    else:
        return(mark, 'X')

def place_mark(board, mark, loc):
    board[loc] = mark

def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[7] == mark and board[8] == mark and board[9] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal up-left to bot-right
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal up-right to bot-left

def first_turn():
    if random.randint(0, 1)  == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def empty(board, loc):
    return board[loc]  == ' '

def full_board(board):
    for i in range(1, 10):
        if empty(board, i):
            return False
    return True

def restart():
    return input('Restart the game? (Y/N) ').lower() == 'y'

def player_move(board):
    loc = 0

    while loc not in range(1,9) or not empty(board, loc):
        loc = int(input('Make your move! (1-9) '))

    return loc

print('Tic Tac Toe')

while True:
    board = [' '] * 10
    player1, player2 = player_choice()
    turn = first_turn()
    print(turn + ' have the first turn!')

    start = input('Start the game? (Y/N) ')

    if start.lower() == 'y':
        game = True
    else:
        game = False

    while game:
        if turn == 'Player 1':
            create_board(board)
            location = player_move(board)
            place_mark(board, player1, location)

            if win_check(board, player1):
                create_board(board)
                print('Player 1 has won the game!')
                game = False
            else:
                if full_board(board):
                    create_board(board)
                    print('It\'s a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            create_board(board)
            location = player_move(board)
            place_mark(board, player2, location)

            if win_check(board, player2):
                create_board(board)
                print('Player 2 has won the game!')
                game = False
            else:
                if full_board(board):
                    create_board(board)
                    print('It\'s a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not restart():
        break