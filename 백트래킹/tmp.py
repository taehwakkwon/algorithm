import sys
sys.stdin = open('input.txt')
def transpose(board):
    new_board = []
    for i in range(9):
        tmp = []
        for j in range(9):
            tmp.append(board[j][i])
        new_board.append(tmp)
    return new_board

def make_box(board):
    new_box = []
    for i in range(0,9,3):
        tmp2 = []
        for j in range(0,9,3):
            tmp = []
            for p in range(3):
                for q in range(3):
                    tmp.append(board[i+p][j+q])
            tmp2.append(tmp)
        new_box.append(tmp2)
    return new_box
board = [list(map(int, input().split())) for _ in range(9)]
board_transposed = transpose(board)
board_box = make_box(board)
print(str(board_box))