import random

def main():
    print('Welcome to Tic Tac Toe game')
    (player1_marker, player2_marker) = player_input()  # choosing marker for each Player (X or O)

    while True:
        board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']  # creating a board list to store markers
        mark = choose_first()    # mark will store a current player move (X or O), but first move is selected randomly
        while game_on(board, mark):
            print('\n' * 100)
            display_board(board)
            if mark == 'X':
                # Player 1 turn
                print('Player 1')
                player_choice(board, player1_marker)
                print('\n' * 100)
                display_board(board)
                if win_check(board, mark):
                    print('Player 1 won!')
                    for i in range(1, 10):
                        if board[i] == ' ':
                            board[i] = 'X'
                    break
                mark = 'O'
            if mark == 'O':
                # Player 2 Turn.
                print('Player 2')
                player_choice(board, player2_marker)
                print('\n' * 100)
                display_board(board)
                if win_check(board, mark):
                    print('Player 2 won!')
                    for i in range(1, 10):
                        if board[i] == ' ':
                            board[i] = 'O'
                    break
                mark = 'X'
        if not replay(board):
            break

def player_input():
    marker = ''
    # Keep asking Player 1 input to choose X or O
    # Once chosen Player 2 assign opposite marker
    while marker != 'X' and marker != 'O':
        marker = input('Player1, choose X or O: ')
    player1_marker = marker

    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'
    return (player1_marker, player2_marker)

def choose_first():
    return random.choice(['X', 'O'])

def place_marker(board, marker, position):
    # depending on Player's marker, the position number marker will go into the list
    board[position] = marker

def player_choice(board, marker):
    position = int(input('Please enter a number '))

    if space_check(board, position):
        place_marker(board, marker, position)

# displaying a board game using board list
def display_board(board):
    print(board[7]+'|'+board[8] + '|' + board[9])
    print('-----')
    print(board[4]+'|'+board[5] + '|' + board[6])
    print('-----')
    print(board[1]+'|'+board[2] + '|' + board[3])

def full_board_check(board):
    count = 0
    for i in range(1, 10):
        if board[i] == ' ':
            count += 1
    if count > 0:
        return False
    else:
        return True

def space_check(board, position):
    return board[position] == ' '

def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False

def game_on(board, mark):
    if not full_board_check(board) or not win_check(board, mark):
        return True
    else:
        return False

def replay(board):
    ask_replay = input('Do you want to play again? Yes or No? ')
    if ask_replay == 'Yes':
        for i in range(1, 10):
            board[i] == ' '
        return True
    else:
        return False

if __name__ == '__main__':
    main()