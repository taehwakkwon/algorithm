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
    s = time.time()
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                for age in list(trees[i][j].keys()):
                    cnt = min(board[i][j]//age, trees[i][j][age])
                    board[i][j] -= cnt * age
                    trees[i][j][age + 1] += cnt
                    board[i][j] += (trees[i][j][age] - cnt)*age//2
                    del trees[i][j][age]
    print(time.time()-s)

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
                        trees[nx][ny][1] += c


n, m, k = map(int, input().split())
board = [[5] * n for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(n)]

trees = [[defaultdict(int) for _ in range(n)] for _ in range(n)]

for i in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1][z] += 1


for i in range(k):
    aged()
    breeding()

cnt = 0
for i in range(n):
    for j in range(n):
        for age in trees[i][j]:
            cnt += trees[i][j][age]

print(cnt)
print(trees)
print(time.time()-start)