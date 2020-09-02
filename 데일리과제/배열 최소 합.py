#import sys
#sys.stdin = open('sample_input.txt')
def dfs(v, s):
    global m
    if s > m:
        return
    if v >= n:
        if s < m:
            m = s
        return
    else:
        for c in range(n):
            if row[c] == 0:
                row[c] = 1
                dfs(v + 1, s + board[v][c])
                row[c] = 0


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    row = [0]*n
    m = float('inf')
    dfs(0, 0)
    print('#%d %d' %(t, m))


