import sys
sys.stdin = open('input.txt')

sys.setrecursionlimit(10**8)
# def dfs(r,c,s, flag):
#     global res
#     if res < s:
#         return
#     if (r,c) == (n-1,m-1):
#         if res > s:
#             res = s
#         return
#     else:
#         for dr, dc in [(0,1),(1,0), (0,-1), (-1,0)]:
#             new_r = r + dr
#             new_c = c + dc
#             if 0 <= new_r < n and 0 <= new_c < m:
#                 if board[new_r][new_c] == 0 and visited[new_r][new_c] == 0:
#                     visited[new_r][new_c] = 1
#                     dfs(new_r, new_c, s + 1, flag)
#                     visited[new_r][new_c] = 0
#                 if board[new_r][new_c] == 1 and flag and visited[new_r][new_c] == 0:
#                     visited[new_r][new_c] = 1
#                     dfs(new_r, new_c, s + 1, False)
#                     visited[new_r][new_c] = 1

import time
start = time.time()

from collections import deque
def bfs(v):
    queue = deque([v])
    visited[0][0] = 1
    while queue:
        flag, cnt, r, c = queue.popleft()
        if (r,c) == (n-1, m-1):
            return cnt
        #visited[r][c] = 1
        for dr, dc in [(0,1),(1,0), (0,-1), (-1,0)]:
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < n and 0 <= new_c < m:
                if flag and board[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                    visited[new_r][new_c] = 1
                    queue.append((False, cnt + 1, new_r, new_c))

                elif board[new_r][new_c] == 0 and visited[new_r][new_c] == 0:
                    visited[new_r][new_c] = 1
                    queue.append((flag, cnt + 1, new_r, new_c))

    return -1

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
# n, m = 1000, 1000
# board = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
print(bfs((True,1,0,0)))

print(time.time() - start)
#dfs(0,0,1, True)
