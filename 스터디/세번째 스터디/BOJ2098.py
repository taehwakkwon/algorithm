import sys
sys.stdin = open('input.txt')

import time
start = time.time()

def dfs(v):
    global cnt
    if v == n:
        cnt += 1
        return
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                res[v] = i
                dfs(v + 1)
                ch[i] = 0
                res[v] = 0


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [0]*(n + 1)
m = float('inf')
n = 16
ch = [0]*n
res = [0]*n
cnt = 0
dfs(0)
print(cnt)
print(m)
print(time.time()-start)