import sys
sys.stdin = open('../now/input.txt')

import sys
input = sys.stdin.readline
from collections import deque

move = [(0,1),(1,0),(0,-1),(-1,0)]
def bfs(y,x):
    global cnt, s
    queue = deque([(y,x)])
    while queue:
        y, x = queue.popleft()
        s += board[y][x]
        cnt += 1
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0 and l <= abs(board[y][x] - board[ny][nx]) <= r:
                visited[ny][nx] = idx
                queue.append((ny,nx))

def cal():
    for i in range(n):
        for j in range(n):
            board[i][j] = avg[visited[i][j]-1]


n,l,r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

MAX = n**2
for t in range(2001):
    visited = [[0] * n for _ in range(n)]
    idx = 0
    avg = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                idx += 1
                cnt,s = 0,0
                visited[i][j] = idx
                bfs(i,j)
                avg.append(s//cnt)
    if len(avg) == MAX:
        print(t)
        break
    cal()

