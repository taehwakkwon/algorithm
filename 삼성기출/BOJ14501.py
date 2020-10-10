import sys
sys.stdin = open('../now/input.txt')

import sys
sys.setrecursionlimit(10**7)
def dfs(v, money):
    global M
    if v > n:
        return
    elif v == n:
        M = max(M, money)
    else:
        dfs(v + 1, money)
        dfs(v + schedule[v][0], money + schedule[v][1])

n = int(input())
schedule = [[0,0] for _ in range(n)]
for i in range(n):
    t, p = map(int,input().split())
    schedule[i][0] = t
    schedule[i][1] = p
M = 0
dfs(0,0)
print(M)