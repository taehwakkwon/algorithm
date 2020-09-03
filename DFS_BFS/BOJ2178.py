import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(v = (1,0,0)):
    global res
    visited = [v]
    queue = deque([v])
    while queue:
        s, r, c = queue.popleft()
        if (r, c) == (n - 1, m - 1):
            res = s
            return
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < n and 0 <= new_c < m and board[new_r][new_c] == 1:
                board[new_r][new_c] = 0
                queue.append((s + 1, new_r, new_c))


n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
res = 0
bfs()
print(res)
