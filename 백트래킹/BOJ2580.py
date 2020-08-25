import sys
sys.stdin = open('input.txt')
def check(i, j):
    new_y, new_x = i, j
    for dy, dx in [(0, 1), (1, 0), (0, -1), (0, -1)]:
        while 0 <= new_y < 9 and 0 <= new_x < 9:
            if 


def solve(v):
    if v >= 9:
        return
    else:
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:


board = [list(map(int, input().split())) for _ in range(9)]

