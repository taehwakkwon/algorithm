import sys
sys.stdin = open('sample_input.txt')

import sys
sys.setrecursionlimit(10**7)
def dfs(y,x,s):
    global res
    if (y, x) == end:
        if res > s:
            res = s
    else:
        for dy, dx in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_y, new_x = y + dy, x + dx
            while 0 <= new_y < 16 and 0 <= new_x < 16 and maze[new_y][new_x] != 1:
                maze[new_y][new_x] = 1
                dfs(new_y,new_x, s + 1)


T = 10
for t in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    res = float('inf')
    for i in range(16):
        if 2 in maze[i]:
            start = (i, maze[i].index(2))
        if 3 in maze[i]:
            end = (i, maze[i].index(3))
    dfs(start[0],start[1],0)
    if res == float('inf'):
        print('#%d %d'%(t, -1))
    else:
        print('#%d %d'%(t, res))