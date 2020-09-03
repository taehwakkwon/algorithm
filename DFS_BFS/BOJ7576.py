import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(v):
    queue = deque(v)
    while queue:
        s, r, c = queue.popleft()
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < n and 0 <= new_c < m and boxes[new_r][new_c] == 0:
                boxes[new_r][new_c] = 1
                queue.append((s + 1, new_r, new_c))
    for i in range(n):
        if 0 in boxes[i]:
            print(-1)
            return
    else:
        print(s)


if __name__ == "__main__":
    m, n = map(int, input().split())
    boxes = [list(map(int, input().split())) for _ in range(n)]
    start = []
    for i in range(n):
        for j in range(m):
            if boxes[i][j] == 1:
                start.append((0, i,j))
    bfs(start)

