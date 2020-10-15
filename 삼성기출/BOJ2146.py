import sys
sys.stdin = open('../now/input.txt')

import sys
sys.setrecursionlimit(10**7)
from collections import deque
move = [(0,1),(1,0),(0,-1),(-1,0)]
def coloring(r,c):
    for dr, dc in [(0,0)] + move:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and colored[nr][nc] == 0 and board[nr][nc] == 1:
            colored[nr][nc] = color
            coloring(nr,nc)

def bfs(queue,cnt):
    global m
    next_queue = deque([])
    if cnt >= m:
        return

    while queue:
        r, c = queue.popleft()

        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if colored[nr][nc] == now_color:
                    continue
                else:
                    if colored[r][c] != 0:
                        m = min(m, cnt)
                        return
                    next_queue.append((nr, nc))
    if next_queue:
        bfs(next_queue, cnt + 1)


n = int(input())
board = [list(map(int ,input().split())) for _ in range(n)]
colored = [[0]*n for _ in range(n)]
color = 0
m = 2*n
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and colored[i][j] == 0:
            color += 1
            coloring(i,j)
for i in range(n):
    for j in range(n):
        if colored[i][j] != 0:
            now_color = colored[i][j]
            queue = deque([])
            queue.append((i, j))
            bfs(queue,0)
print(m - 1)
