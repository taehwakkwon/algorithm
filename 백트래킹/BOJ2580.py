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


def dfs(zero):
    if zero == 0:
        for r in board:
            print(*r)
        sys.exit()
    else:
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for k in range(1,10):
                        # print(k)
                        # print(board[i])
                        # print(board_transposed[i])
                        # print(board_box[i//3][j//3])
                        if k not in board[i] and k not in board_transposed[j] and k not in board_box[i//3][j//3]:
                            board[i][j] = k
                            board_transposed[j][i] = k
                            board_box[i//3][j//3][i % 3 * 3 + j % 3] = k
                            dfs(zero - 1)
                            board[i][j] = 0
                            board_transposed[j][i] = 0
                            board_box[i // 3][j // 3][i % 3 * 3 + j % 3] = k


board = [list(map(int, input().split())) for _ in range(9)]
board_transposed = transpose(board)
board_box = make_box(board)
zero = 0
for i in range(9):
    zero += board[i].count(0)
dfs(zero)


'''
4 6 7 8 0 0 2 0 9
3 4 9 8 2 0 5 0 0
2 1 4 9 5 3 6 8 0
3 7 1 2 9 4 0 0 6
1 3 6 0 0 0 0 0 8
2 6 7 8 4 0 0 5 1
1 3 7 5 8 4 0 9 0
1 2 3 0 7 9 0 4 0
5 4 9 0 0 2 7 6 0

4 6 7 8 0 0 2 0 9
3 4 9 8 2 0 5 0 0
2 1 4 9 5 3 6 8 0
3 7 1 2 9 4 0 0 6
1 3 6 0 0 0 0 0 8
2 6 7 8 4 0 0 5 1
1 3 7 5 8 4 0 9 0
1 2 3 0 7 9 0 4 0
5 4 9 3 0 2 7 6 0

1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1
'''