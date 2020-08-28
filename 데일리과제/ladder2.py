import sys
sys.stdin = open('sample_input.txt')
def dfs(y, x, s, p):
    visited.append((y,x))
    if y == 99:
        dic[s] = p
        return s
    else:
        for dy, dx in move:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < 100 and 0 <= new_x < 100 and ladder[new_y][x + dx] == 1 and (new_y, new_x) not in visited:
                dfs(new_y, new_x, s + 1, p)
                return

from collections import deque
def bfs(v):
    queue = deque(v)
    for i in v:
        visited[i[:2]] = 1

    while queue:
        y, x, start_x = queue.popleft()
        visited[(y, x)] = 1
        for dy, dx in move:
            if 0 <= y + dy < 100 and 0 <= x + dx < 100 and ladder[y + dy][x + dx] == 1 and (y + dy, x + dx) not in visited:
                queue.append((y + dy, x + dx, start_x))
                if y + dy == 99:
                    return start_x




move = [(0, -1), (0, 1), (1, 0)]
T = 10
for tc in range(1, T + 1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    dic = {}
    start = []
    visited = {}
    for i in range(100):
        if ladder[0][i] == 1:
            start.append((0,i, i))
    print(bfs(start))