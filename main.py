import random
import datetime
import chess
import chess.engine 
# pip3 install python-chess

"""
Chaira and Glory

https://python-chess.readthedocs.io/en/latest/
https://python-chess.readthedocs.io/en/latest/_modules/chess/engine.html
"""

def init_set():
    print('=====================================================\n\t\t\tCSC 290 Chess Bot V.01 by Chaira and Glory\t\t\t\n=====================================================')
    print('Time:', datetime.datetime.now())
    comp = ''
    while(comp not in ['w', 'b', 'white', 'black', 'wh', 'bl']):
        comp = input('Computer Player? (w=white/b=black): ')
    # starting_pos = input('Starting FEN position? (hit ENTER for standard starting position): ')
    if 'b' in comp:
        print('You are playing as BLACK. The computer will start first.\n')
    elif 'w' in comp:
        print('You are playing as WHITE. Please begin the first move.\n')
    print('\n')
    return comp

"""
def init_board():
    # Black pieces are lower case, white pieces are upper case.
    return [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]
"""

def update_board(board):
    print(board)
    # print('    a   b   c   d   e   f   g   h')
    # for row in range(8):
    #     print(f'{8 - row} |', end=' ')
    #     for col in range(8):
    #         print(f'{board[row][col]} |', end=' ')
    #     print(f'{8 - row}')
    #     if row < 7:
    #         print('  ---------------------------------')
    # print('    a   b   c   d   e   f   g   h\n')

def get_computer_move(board):
    legal_moves = list(board.legal_moves)
    if legal_moves:
        return random.choice(legal_moves)
    
def move(comp, board, turn):
    if turn == 0:
        move_choice = get_computer_move(board)
        if move_choice:
            board.push(move_choice)
            print(f"Computer moved: {move_choice}")
    else:
        move_choice = None
        while move_choice not in board.legal_moves:
            user_input = input('Enter your move (eg. e2e4): ')
            # if user_input == 'quit':
            #         return 
            # else:
            #     continue
            # for now just control C terminal
            try:
                move_choice = chess.Move.from_uci(user_input)
            except:
                print("Invalid format, please use standard notation like e2e4")
            if move_choice not in board.legal_moves:
                print("Sorry, you can't make that move. Please enter a different move.")
        board.push(move_choice)
        print(f"You moved: {move_choice}")
        # reminder to print when a move removes an opponent piece
    
"""
def move_piece(board, move_choice, colour):
    src = move_choice[:2]
    dest = move_choice[2:]

    srcc = ord(src[0]) - ord('a')
    # print('srcc: ', srcc)
    srcr = 8-int(src[1])
    # print('srcr: ', srcr)

    destc = ord(dest[0]) - ord('a')
    destr = 8-int(dest[1])
    # print('drcr: ', destr)
    # print('drcr: ', destc)

    # print('debug: ', board[srcr][srcc]) 

    board[destr][destc] = board[srcr][srcc]
    board[srcr][srcc] = ' '

    print(colour.upper(), ' moved from', src, ' to', dest, '\n')
    update_board(board)



def move(comp, board, turn):
    if turn == 0: 
        if 'w' in comp:
            move_piece(board, 'e2e4', 'w')
        else:
            move_piece(board, 'e7e5', 'b')
    else:
        move_choice = ''
        while len(move_choice) != 4:
            move_choice = input('Enter move: (eg. f2f4): ')
        move_piece(board, move_choice, 'w' if 'b' in comp else 'b')

"""

def main():
    comp = init_set()
    # board = init_board()
    board = chess.Board()

    # print(board[0][0]) # debug

    update_board(board) # initial board

    checkmate = False
    # turn tracker:
    if 'b' in comp:
        i=0
    else:
        i=1

    # while(not checkmate):
    while(not board.is_game_over()):
        turn = i%2
        move(comp, board, turn)
        update_board(board)

        if board.is_checkmate():
            print("Checkmate")
        elif board.is_stalemate():
            print("Stalemate (tie)")

        i+=1

if __name__ == '__main__':
    main()

    """"
    extra:
        - more clear movement ('White Queen moved c3 to c7)
        - see list of 'taken' pieces
        - make board more clear. UI graphics?
        - potential bug -- won't let my pawn take opp. Queen (screenshotted)
    """