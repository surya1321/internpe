# Importing Module
import time

# Initialize the board
def initialize_board():
    board = [' ']*9
    return board

# Print the board
def print_board(board):
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

# Get player's move
def get_player_move(board, player):
    valid_move = False
    while not valid_move:
        move = input(f"{player}'s turn. Choose a position (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move)-1] == ' ':
            return int(move)-1
        else:
            print("Invalid move. Please try again.")

# Check if game is over
def is_game_over(board):
    # check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True, board[i]
    # check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True, board[i]
    # check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True, board[0]
    if board[2] == board[4] == board[6] != ' ':
        return True, board[2]
    # check tie
    if ' ' not in board:
        return True, 'Tie'
    return False, None

# Main game loop
def play_game():
    print("Welcome to Tic Tac Toe!")
    time.sleep(1)
    play_again = True
    while play_again:
        # initialize the board and other variables
        board = initialize_board()
        players = ['X', 'O']
        current_player = players[0]
        winner = False
        game_over = False
        # game loop
        while not game_over:
            print_board(board)
            move = get_player_move(board, current_player)
            board[move] = current_player
            game_over, winner = is_game_over(board)
            if game_over:
                if winner != 'Tie':
                    print_board(board)
                    print(f'Player {winner} wins!')
                else:
                    print_board(board)
                    print('It is a tie!')
            else:
                current_player = players[(players.index(current_player)+1)%2]
        # ask player if they want to play again
        play_again = input('Do you want to play again? (y/n)').lower() == 'y'
    print('Thanks for playing!')

# Start the game
play_game()