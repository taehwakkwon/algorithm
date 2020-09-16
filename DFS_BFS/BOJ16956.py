import sys
sys.stdin = open('../now/input.txt')

from collections import deque


import sys
y, x = map(int, input().split())
board = [list(input()) for _ in range(y)]
wolf = {}
sheep = {}
for i in range(y):
    for j in range(x):
        if board[i][j] == 'S':
            sheep[(i,j)] = 0
        elif board[i][j] == 'W':
            wolf[(i,j)] = 0

for r, c in wolf.keys():
    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        new_r, new_c = r + dr, c + dc
        if (new_r,new_c) in sheep:
            print(0)
            sys.exit()
        if (new_r,new_c) not in wolf and 0 <= new_r < y and 0 <= new_c < x:
            board[new_r][new_c] = 'D'
print(1)
for r in board:
    print(''.join(r))