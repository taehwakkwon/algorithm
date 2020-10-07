import sys
sys.stdin = open('input.txt')

from collections import deque
from itertools import combinations
def bfs(queue):
    global m
    cnt = mm
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            if 0 <= r + dr < n and 0 <= c + dc < n and board[r+dr][c+dc] != 1 and visited[r+dr][c+dc] == 0:
                dis[r+dr][c+dc] = dis[r][c] + 1
                visited[r+dr][c+dc] = 1
                queue.append((r+dr,c+dc))
                cnt += 1
    if cnt == clean:
        M = 0
        for i in range(n):
            for j in range(n):
                if (i,j) not in virus:
                    M = max(M,dis[i][j])
        m = min(m, M)


n, mm = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus = set([])
clean = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.add((i,j))
        if board[i][j] != 1:
            clean += 1
comb = list(combinations(virus, mm))
m = 100
for com in comb:
    visited = [[0]*n for _ in range(n)]
    dis = [[0] * n for _ in range(n)]
    for r, c in com:
        visited[r][c] = 1
    com = deque(com)
    bfs(com)

if m == 100:
    print(-1)
else:
    print(m)