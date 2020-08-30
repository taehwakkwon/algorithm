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
            if board[i][j] >= 1 and (i,j) not in bishop:
                bishop.append((i,j))
                for dr, dc in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    new_r, new_c = i + dr, j + dc
                    while 0 <= new_r < n and 0 <= new_c < n:
                        board[new_r][new_c] -= 1
                        new_r += dr
                        new_c += dc
                dfs()
                bishop.remove((i,j))
                for dr, dc in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    new_r, new_c = i + dr, j + dc
                    while 0 <= new_r < n and 0 <= new_c < n:
                        board[new_r][new_c] += 1
                        new_r += dr
                        new_c += dc
    return

def dfs(v):
    for i in range(v + 1):
        if board[n - v - 1 + i][i] >= 1 and (n - v - 1 + i, i) not in bishop:
            bishop.append((n - v - 1 + i, i))
            for dr, dc in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                new_r, new_c = v + dr, i + dc
                while 0 <= new_r < n and 0 <= new_c < n:
                    board[new_r][new_c] -= 1
                    new_r += dr
                    new_c += dc
                dfs(v + 1)





M = 0
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
bishop = []
dfs()
print(M)
print(time.time()-start)

