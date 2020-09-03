import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(v):
    global res
    queue = deque([v])
    while queue:
        c, y, x = queue.popleft()
        if (y, x) == end:
            if res > c:
                res = c
            return
        for dy, dx in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_y, new_x = y + dy, x + dx
            while 0 <= new_y < n and 0 <= new_x < n and maze[new_y][new_x] != 1 and visited[new_y][new_x] == 0:
                visited[new_y][new_x] = 1
                queue.append((c + 1, new_y, new_x))
    return


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    res = float('inf')
    for i in range(n):
        if 2 in maze[i]:
            start = (i, maze[i].index(2))
        if 3 in maze[i]:
            end = (i, maze[i].index(3))
    bfs((-1,start[0],start[1]))
    if res == float('inf'):
        print('#%d %d'%(t, 0))
    else:
        print('#%d %d'%(t, res))