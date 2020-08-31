import sys
sys.stdin = open('input.txt')
import time
start = time.time()

def dfs(start, v, s, cnt):
    global m
    if m < s:
        return
    if cnt == n:
        if board[v][start] != 0:
            s += board[v][start]
            if s < m:
                m = s
    else:
        for i in range(n):
            if board[v][i] != 0 and visited[i] == 0:
                visited[i] = 1
                dfs(start, i, s + board[v][i], cnt + 1)
                visited[i] = 0


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [0]*(n + 1)
m = float('inf')
for i in range(n):
    visited[i] = 1
    dfs(i, i,0, 1)
    visited[i] = 0
print(m)
print(time.time()-start)