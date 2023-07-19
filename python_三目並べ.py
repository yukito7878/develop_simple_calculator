OPEN = 0
FIRST = 1
SECOND = 2
DRAW = 3

turn = 1
board = [[0,0,0], [0,0,0],[0,0,0]]

def show_turn():
    if turn == FIRST:
        return('先手')
    elif turn == SECOND:
        return('後手')
    else:
        return('手番の値が不適切です')
        
def init_turn():
    global turn
    turn = 1

def change_turn():
    global turn
    if turn == FIRST:
        turn = SECOND
    elif turn == SECOND:
        turn = FIRST

def show_board():
    s = ' :0 1 2\n---------\n'
    for i in range(3):
        s = s + str(i) + ':'
        for j in range(3):
            cell = ''
            if board[i][j] == OPEN:
                cell = ' '
            elif board[i][j] == FIRST:
                cell = '0'
            elif board[i][j] == SECOND:
                cell = 'x'
            else:
                cell = '?'
            s = s + cell + ' '
        s = s + '\n'
    return s

def init_board():
    for i in range(3):
        for j in range(3):
            board[i][j] = OPEN

def examine_board(i, j):
    return board[i][j]

def set_board(i, j, t):
    if (i>=0) and (i<3) and (j>=0) and (j<3):
        if (t == FIRST) or (t == SECOND):
            if examine_board(i, j) == 0:
                board[i][j] = t
                return 'OK'
            else:
                return 'Not empty'
        else:
            return 'illegal turn'
    else:
        return 'illegal slot'


def check_board_horizontal(t):
    for i in range(3):
        if (board[i][0] == t) and (board[i][1] == t) and (board[i][2] == t):
            return True
    return False

def check_board_vertical(t):
    for j in range(3):
        if (board[0][j] == t) and (board[1][j] == t) and (board[2][j] == t):
            return True
    return False

def check_board_diagonal(t):
    if (board[0][0] == t) and (board[1][1] == t) and (board[2][2] == t):
        return True
    return False

def check_board_inverse_diagonal(t):
    if (board[0][2] == t) and (board[1][1] == t) and (board[2][0] == t):
        return True
    return False

def is_win_simple(t):
    if check_board_horizontal(t):
        return True
    if check_board_vertical(t):
        return True
    if check_board_diagonal(t):
        return True
    if check_board_inverse_diagonal(t):
        return True
    return False

def is_win_actual(t):
    if not is_win_simple(t):
        return False
    if t == FIRST:
        if is_win_simple(SECOND):
            False
    elif t == SECOND:
        if is_win_simple(FIRST):
            False
    return True

def is_full():
    for i in range(3):
        for j in range(3):
            if board[i][j] == OPEN:
                return False
    return True

def is_draw():
    if is_win_simple(FIRST):
        return False
    if is_win_simple(SECOND):
        return False
    if not is_full():
        return False
    return True

def replay_log(log):
    init_board()
    init_turn()
    print(show_board())
    for m in log:
        if len(m) == 2:
            print(show_turn(), 'の番です')
            print(set_board(m[0], m[1], turn))
            print(show_board())
            print('IS WIN', turn, ': ', is_win_actual(turn))
            change_turn()
        else:
            print('REULT IN LOG: ', m[0])
    print('IS WIN FIRST: ', is_win_actual(FIRST))
    print('IS WIN SECOND: ', is_win_actual(SECOND))
    print('IS DRAW: ', is_draw())

def play():
    init_board()
    print(show_board())
    #log = []
    while True:
        print(show_turn(), 'の番です')
        while(True): 
            row = int(input('行を選択してください: '))
            column = int(input('列を入力してください: '))
            result = set_board(row, column, turn)
            if result == 'OK':
                print(show_board())
                break
            print(set_board(row, column, turn))
            
            print('不適切な入力です。再度入力してください: ')
        
        print(show_board())
        if is_draw():
            print('引き分けです')
            break
        if is_win_actual(turn):
            print(show_turn(), 'の勝ちです')
            break
        change_turn()
    change_turn()
    play()
    #if len(log)>0:
     #   replay_log(log)
    #else:
     #   print('棋譜は作成されていません　')
        
if __name__ == '__main__':
    print('三目並べ')
    
play()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
                
                
                
                
                
                
                
                
                