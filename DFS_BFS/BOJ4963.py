import sys
sys.stdin = open('input.txt')
import time
start = time.time()
import sys
sys.setrecursionlimit(10**6)
def dfs(i, j):
    for dr, dc in move:
        r, c = i, j
        r += dr
        c += dc
        if 0 <= c < w and 0 <= r < h and board[r][c] == 1:
            board[r][c] = 0
            dfs(r, c)


move = [(0,1),(1,1), (1,0),(1,-1), (0,-1),(-1,-1),(-1,0),(-1,1)]
while True:
    w, h = map(int, sys.stdin.readline().split())
    if (w, h) == (0, 0):
        break
    cnt = 0
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    for r in board:
        print(r)
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                cnt += 1
                board[i][j] = 0
                dfs(i,j)

    print(cnt)
print(time.time() - start)