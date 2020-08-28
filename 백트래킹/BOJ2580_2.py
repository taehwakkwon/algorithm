import sys
sys.stdin = open('input.txt')

import sys
def transpose(board):
    new_board = []
    for i in range(9):
        tmp = []
        for j in range(9):
            tmp.append(board[j][i])
        new_board.append(tmp)
    return new_board

def dfs(y, x):
    if y == 9:
        return
    else:
        for i in range(9):
            for j in range(9):
                cnt = [0] * 10
                for k in range(9):
                    if row_board[i][k] != 0 or col_board[i][k] != 0 or box_board[i//3*3 + j//3][k] != 0:
                        cnt[row_board[i][k]] += 1
                        cnt[col_board[i][k]] += 1
                        cnt[box_board[i][k]] += 1
                cnt[0] = -1
                row_board[i][j] = col_board[i][j] = box_board[i//3*3+j//3] 1
                cnt.index(0)


row_board = [list(map(int, input().split())) for _ in range(9)]
col_board = transpose(row_board)
box_board = []
for i in range(0,9,3):
    for j in range(0,9,3):
        tmp = []
        for k in range(3):
            for l in range(3):
                tmp.append(row_board[i + k][j + l])
        box_board.append(tmp)

print(box_board)