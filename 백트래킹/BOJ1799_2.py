import sys
sys.stdin = open('input.txt')

import time
start = time.time()
def dfs():
    global M
    if M < len(bishop):
        M = len(bishop)
    for i in range(n):
        for j in range(n):
            if board[(i,j)] >= 1 and (i,j) not in bishop:
                bishop.add((i,j))
                for dr, dc in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    new_r, new_c = i + dr, j + dc
                    while 0 <= new_r < n and 0 <= new_c < n:
                        board[(new_r,new_c)] -= 1
                        new_r += dr
                        new_c += dc
                dfs()
                bishop.pop()
                for dr, dc in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    new_r, new_c = i + dr, j + dc
                    while 0 <= new_r < n and 0 <= new_c < n:
                        board[(new_r, new_c)] += 1
                        new_r += dr
                        new_c += dc
    return


M = 0
n = int(input())
board = {}
tmp = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        board[(i,j)] = tmp[i][j]
bishop = set([])
dfs()
print(M)
print(time.time()-start)