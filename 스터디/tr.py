import time
startss = time.time()

import sys
import collections

sys.stdin = open("input.txt", 'r')

def start(h):
    rtn = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] and area[i][j] < h and not visited[i][j]:
                rtn += bfs(i, j, h)
    return rtn

def bfs(i, j, h):
    q = collections.deque()
    pos = [[i, j]]
    q.append([i, j])
    visited[i][j] = True
    flag = False
    while q:
        i, j = q.popleft()
        for a in range(4):
            ni, nj = i+di[a], j+dj[a]
            if 0 <= ni < N and 0 <= nj < M and area[ni][nj]!=0:
                if not visited[ni][nj]:
                    if area[ni][nj] < h:
                        visited[ni][nj] = True
                        pos.append([ni, nj])
                        q.append([ni, nj])
            else:
                flag = True

    if flag:
        return 0
    else:
        water = 0
        for i, j in pos:
            area[i][j] += 1
            water += 1
        return water

N, M = map(int, input().split())
area = [list(map(int, list(input()))) for _ in range(N)]
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
result = 0
for h in range(1, 10):
    visited = [[False] * M for _ in range(N)]
    result += start(h)
print(result)
print(time.time()-startss)
