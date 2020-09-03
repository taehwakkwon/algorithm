import sys
sys.stdin = open("sample_input.txt", "r")

def dfs(v, s):
    global m
    if s > m:
        return
    if v == n:
        if s < m:
            m = s
    else:
        for c in range(n):
            if visited[c] == 0:
                visited[c] = 1
                dfs(v + 1, s + board[v][c])
                visited[c] = 0
T = int(input())
for t in range(1, 1 + T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    m = float('inf')
    dfs(0, 0)
    print('#%d'%t, m)