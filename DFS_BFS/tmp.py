import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

h, w = map(int, input().split())

miro = [[] for i in range(h)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(h):
    ss = input().strip()
    for s in ss:
        miro[i].append(int(s))

dist = [[[0, 0] for j in range(w)] for i in range(h)]

def bfs(y, x, wall):
    q = [[y, x, wall]]
    dist[y][x][wall] = 1
    while q:
        now = q.pop(0)
        for i in range(4):
            y, x, z = now
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < w and 0 <= ny < h:
                if miro[ny][nx] == 0 and dist[ny][nx][z] == 0:
                    dist[ny][nx][z] = dist[y][x][z] + 1
                    q.append([ny, nx, z])
                if z == 0 and miro[ny][nx] == 1 and dist[ny][nx][z + 1] == 0:
                    dist[ny][nx][z + 1] = dist[y][x][z] + 1
                    q.append([ny, nx, z + 1])
bfs(0, 0, 0)
ans = []
if dist[-1][-1][0] != 0 and dist[-1][-1][1] != 0:
    print(min(dist[-1][-1][0], dist[-1][-1][1]))
elif dist[-1][-1][0] != 0:
    print(dist[-1][-1][0])
elif dist[-1][-1][1] != 0:
    print(dist[-1][-1][1])
else:
    print(-1)