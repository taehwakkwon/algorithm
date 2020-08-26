import sys
sys.stdin = open('input.txt')

import sys
sys.setrecursionlimit(10**7)
def dfs(y,x):
    global res
    if (y, x) == end:
        res = 1
    else:
        for dy, dx in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_y, new_x = y + dy, x + dx
            while 0 <= new_y < 16 and 0 <= new_x < 16 and maze[new_y][new_x] != 1:
                maze[new_y][new_x] = 1
                dfs(new_y,new_x)


T = 10
for t in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    res = 0
    for i in range(16):
        if 2 in maze[i]:
            start = (i, maze[i].index(2))
        if 3 in maze[i]:
            end = (i, maze[i].index(3))
    dfs(start[0],start[1])
    print('#%d %d'%(t, res))

