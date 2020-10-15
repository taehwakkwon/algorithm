import sys
sys.stdin=open('input.txt')

import time
start = time.time()
from collections import deque
import sys
sys.setrecursionlimit(10**7)
move = [(0,1),(1,0), (0,-1),(-1,0)]
def coloring(r,c):
    colored[r][c] = color
    for dr, dc in move:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and colored[nr][nc] == 0 and board[nr][nc] == 1:
            colored[nr][nc] = color
            coloring(nr,nc)

def bfs(r,c):
    queue = deque([])
    queue.append((0,r,c))
    visited = [[0]*n for _ in range(n)]
    while queue:
        cnt, r, c = queue.popleft()
        if colored[r][c] != 0 and colored[r][c] != now_color:
            return cnt
        if cnt - 1 >= m:
            return float('inf')
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if colored[nr][nc] == now_color or visited[nr][nc] == 1:
                    continue
                else:
                    visited[nr][nc] = 1
                    queue.append((cnt+1, nr, nc))
    return float('inf')


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
            m = min(m,bfs(i,j))
print(m-1)



print(time.time()-start)