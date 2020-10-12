import sys
sys.stdin = open('input.txt')
import time

import time
start = time.time()

import sys
from collections import defaultdict
input = sys.stdin.readline
move = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def aged():
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                for age in list(trees[i][j].keys()):
                    cnt = min(board[i][j]//age, trees[i][j][age])
                    board[i][j] -= cnt * age
                    if age + 1 in trees[i][j]:
                        trees[i][j][age + 1] += cnt
                    else:
                        trees[i][j][age + 1] = cnt
                    board[i][j] += (trees[i][j][age] - cnt)*age//2
                    del trees[i][j][age]

def breeding():
    for i in range(n):
        for j in range(n):
            c = 0
            board[i][j] += a[i][j]
            for age in trees[i][j]:
                if age % 5 == 0:
                    c += trees[i][j][age]
            if c:
                for dx, dy in move:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if 1 in trees[nx][ny]:
                            trees[nx][ny][1] += c
                        else:
                            trees[nx][ny][1] = c


n, m, k = map(int, input().split())
board = [[5] * n for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(n)]

trees = [[{} for _ in range(n)] for _ in range(n)]
for i in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1][z] = 1
print(trees)


for i in range(k):
    aged()
    breeding()

cnt = 0
for i in range(n):
    for j in range(n):
        for age in trees[i][j]:
            cnt += trees[i][j][age]

print(cnt)
del trees[0][0][1000]
print(trees)

print(time.time()-start)