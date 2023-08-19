def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def make_move(board, player_symbol):
    while True:
        try:
            row = int(input('Enter row (0-2): '))
            col = int(input('Enter column (0-2): '))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == '':
                board[row][col] = player_symbol
                break
            else:
                print('Invalid move. Try again.')
        except ValueError:
            print('Invalid input. Please enter a number.')

def check_win(board, player_symbol):
    for row in board:
        if all(cell == player_symbol for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player_symbol for row in range(3)):
            return True
    if all(board[i][i] == player_symbol for i in range(3)) or \
       all(board[i][2 - i] == player_symbol for i in range(3)):
        return True
    return False

def check_tie(board):
    return all(cell != '' for row in board for cell in row)

def main():
    game_board = [['', '', ''], ['', '', ''], ['', '', '']]
    players = ['X', 'O']
    current_player = 0
    while True:
        print_board(game_board)
        player_symbol = players[current_player]
        make_move(game_board, player_symbol)
        if check_win(game_board, player_symbol):
            print_board(game_board)
            print(f'Player {player_symbol} wins!')
            break
        elif check_tie(game_board):
            print_board(game_board)
            print('It\'s a tie!')
            break
        current_player = (current_player + 1) % 2

if __name__ == '__main__':
    main()
