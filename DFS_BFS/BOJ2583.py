import sys
sys.stdin = open('input.txt')


import sys
sys.setrecursionlimit(10**7)
def color(a, b, c, d):
    for i in range(b, d):
        for j in range(a, c):
            board[i][j] = 1
    return board


def dfs(i, j):
    global s
    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        r, c = i, j
        r += dr
        c += dc
        if 0 <= r < m and 0 <= c < n and board[r][c] == 0:
            board[r][c] = 1
            s += 1
            dfs(r, c)

m, n, k = map(int,sys.stdin.readline().split())
board = [[0]*n for _ in range(m)]
for i in range(k):
    a, b, c, d = map(int, sys.stdin.readline().split())
    board = color(a, b, c, d)
res = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            s = 1
            board[i][j] = 1
            dfs(i,j)
            res.append(s)
print(len(res))
print(*sorted(res))
