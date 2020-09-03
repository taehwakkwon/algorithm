import sys
sys.stdin = open('input.txt')
import sys
from collections import deque
def bfs(v):
    queue = deque([v])
    while queue:
        flag, r, c = queue.popleft()
        if (r,c) == (n-1, m-1):
            res = [visited[r][c][0], visited[r][c][1]]
            if 0 in res:
                res.remove(0)
            return min(res) + 1
        for dr, dc in [(0,1),(1,0), (0,-1), (-1,0)]:
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < n and 0 <= new_c < m:
                if board[new_r][new_c] == 0 and visited[new_r][new_c][flag] == 0:
                    visited[new_r][new_c][flag] = visited[r][c][flag] + 1
                    queue.append((flag, new_r, new_c))
                if flag == 0 and board[new_r][new_c] == 1 and visited[new_r][new_c][flag + 1] == 0:
                    visited[new_r][new_c][flag + 1] = visited[r][c][flag] + 1
                    queue.append((flag + 1, new_r, new_c))
    return -1


n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[[0,0] for _ in range(m)] for i in range(n)]
print(bfs((0,0,0)))