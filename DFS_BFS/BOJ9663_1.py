import sys
sys.stdin = open('input.txt')

from copy import deepcopy
def check(y, x):
    for dy, dx in move:
        new_y, new_x = y + dy, x + dx
        while  0 <= new_y < N and 0 <= new_x < N:
            if board[new_y][new_x] != 1:
                board[new_y][new_x] = -1
            else:
                return False, board
    else:
        return True, board

def dfs(y, x, s):
    if s == N:
        res.append(deepcopy(board))
    else:
        for i in range(N):
            for j in range(N):
                if board[i][j] == 0:
                    a, b = check(i,j)
                    if b:
                        board = deepcopy(a)






res = []
move = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
N = 4#int(input())
for i in range(N):
    for j in range(N):
        board = [[0] * N for _ in range(N)]
        if board[i][j] == 0:
