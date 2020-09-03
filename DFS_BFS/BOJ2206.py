import sys
sys.stdin = open('input.txt')

import time
start = time.time()

import sys
from collections import deque
def bfs(v):
    queue = deque([v])
    visited[0][0] = 1
    while queue:
        flag, r, c = queue.popleft()
        if (r,c) == (n-1, m-1):
            return visited[r][c]
        for dr, dc in [(0,1),(1,0), (0,-1), (-1,0)]:
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < n and 0 <= new_c < m:
                print(new_r, new_c, flag)
                if board[new_r][new_c] == 0 and visited[new_r][new_c] == 0:
                    visited[new_r][new_c] = visited[r][c] + 1
                    queue.append((flag, new_r, new_c))
                elif flag and board[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                    visited[new_r][new_c] = visited[r][c] + 1
                    queue.append((False, new_r, new_c))
    return -1


n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
# n, m = 1000, 1000
# board = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
print(bfs((True,0,0)))
print(time.time() - start)
