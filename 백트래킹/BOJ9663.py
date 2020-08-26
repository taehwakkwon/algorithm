import time
import sys
sys.setrecursionlimit(10 ** 7)

def dfs(s):
    global cnt
    if s == N:
        cnt += 1
    else:
        for i in range(N):
            if board[s][i] == 0:
                board[s][i] = 1
                for dy, dx in move:
                    new_y, new_x = s + dy, i + dx
                    while 0 <= new_y < N and 0 <= new_x < N:
                        board[new_y][new_x] -= 1
                        new_y += dy
                        new_x += dx
                dfs(s + 1)
                board[s][i] = 0
                for dy, dx in move:
                    new_y, new_x = s + dy, i + dx
                    while 0 <= new_y < N and 0 <= new_x < N:
                        board[new_y][new_x] += 1
                        new_y += dy
                        new_x += dx


for p in range(16):
    start = time.time()
    move = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    cnt = 0
    N = p
    board = [[0]*N for _ in range(N)]
    dfs(0)
    print(cnt)
    print(p, time.time() - start)