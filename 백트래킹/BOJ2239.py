import sys
sys.stdin = open('input.txt')

import time
start = time.time()

import sys
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


def dfs():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for k in range(1,10):
                    if k not in board[i] and k not in board_box[i//3][j//3] and k not in board_transposed[j]:
                        board[i][j] = k
                        board_transposed[j][i] = k
                        board_box[i//3][j//3][i % 3 * 3 + j % 3] = k
                        dfs()
                        board[i][j] = 0
                        board_transposed[j][i] = 0
                        board_box[i // 3][j // 3][i % 3 * 3 + j % 3] = 0
                return
    for r in board:
        print(''.join(map(str,r)))
    sys.exit()

if __name__ == "__main__":
    board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]
    board_transposed = transpose(board)
    board_box = make_box(board)
    dfs()

    print(time.time() - start)

