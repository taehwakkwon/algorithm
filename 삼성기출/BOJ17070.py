import sys
sys.stdin = open('../now/input.txt')

import time
start = time.time()
move = {
    1: {1:[(0,1)],3:[(0,1),(1,0),(1,1)]},
    2: {2:[(1,0)],3:[(1,0),(1,1),(0,1)]},
    3: {1:[(0,1)],2:[(1,0)],3:[(1,0),(0,1),(1,1)]}
}
to = {
    1:(0,1),
    2:(1,0),
    3:(1,1)
}
def check(r,c,key1):
    for k in move[key1]:
        for dr, dc in move[key1][k]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                continue
            else:
                break
        else:
            queue.append((r+to[k][0],c+to[k][1], k))


from collections import deque
def bfs():
    global queue
    queue = deque([])
    queue.append((0,1,1))
    cnt = 0
    while queue:
        r, c, direc = queue.popleft()
        if (r,c) == (n-1,n-1):
            cnt += 1
        check(r,c,direc)
    return cnt


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
print(bfs())
print(time.time()-start)