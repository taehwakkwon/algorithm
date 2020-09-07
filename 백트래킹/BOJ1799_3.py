import sys
sys.stdin = open('input.txt')
import time

start = time.time()

def dfs(li):
    global M
    if M < len(bishop):
        M = len(bishop)
    for i in range(n):
        for j in range(n):
            if li[i][j] >= 1 and (i, j) not in bishop:
                bishop.append((i,j))
                for dr, dc in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    new_r, new_c = i + dr, j + dc
                    while 0 <= new_r < n and 0 <= new_c < n:
                        li[new_r][new_c] -= 1
                        new_r += dr
                        new_c += dc
                dfs(li)
                bishop.pop()
                for dr, dc in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    new_r, new_c = i + dr, j + dc
                    while 0 <= new_r < n and 0 <= new_c < n:
                        li[new_r][new_c] += 1
                        new_r += dr
                        new_c += dc


M = 0
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
black = [[0]*n for _ in range(n)]
white = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (i + j) % 2 and board[i][j] == 1:
            white[i][j] = 1
        if (i + j) % 2 == 0 and board[i][j] == 1:
            black[i][j] = 1
bishop = []

dfs(white)
cnt = M
M = 0
dfs(black)


print(M + cnt)
print(time.time()-start)