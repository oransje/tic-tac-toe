MIN_MOVES_WIN = 5
MAX_MOVES = 9

def run(moves, current_board, char):
    if moves < MIN_MOVES_WIN:
        return False

    for i in range(0, 9, 3):
        if current_board[i] == current_board[i+1] == current_board[i+2] == char:
            print(char + ' WINS')
            return True
    
    for i in range(0, 3):
        if current_board[i] == current_board[i+3] == current_board[i+6] == char:
            print(char + ' WINS')
            return True

    if current_board[0] == current_board[4] == current_board[8] == char:
        print(char + ' WINS')
        return True

    if current_board[2] == current_board[4] == current_board[6] == char:
        print(char + ' WINS')
        return True
                
    if moves == MAX_MOVES:
        print('Tie! No one wins')
        return False

    return False
