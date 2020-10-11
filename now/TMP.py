import sys
sys.stdin=open('input.txt')

import time
start = time.time()

import sys
input = sys.stdin.readline
move = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def aged():
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                for p in range(len(trees[i][j])-1,-1,-1):
                    if board[i][j] >= trees[i][j][p]:
                        board[i][j] -= trees[i][j][p]
                        trees[i][j][p] += 1
                    else:
                        for q in range(p+1):
                            board[i][j] += (trees[i][j][q] // 2)
                        trees[i][j] = trees[i][j][p+1:]
                        break

def breeding():
    for i in range(n):
        for j in range(n):
            c = 0
            board[i][j] += a[i][j]
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    c += 1
            if c:
                for dx, dy in move:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        trees[nx][ny].extend([1]*c)


n, m, k = map(int, input().split())
board = [[5] * n for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(n)]

trees = [[[] for _ in range(n)] for _ in range(n)]
print(len(trees),len(trees[0]),len(trees[0][0]),trees[0][0])
for i in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

for i in range(k):
    breed = aged()
    breeding()

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(trees[i][j])

print(cnt)
print(trees)
print(time.time()-start)