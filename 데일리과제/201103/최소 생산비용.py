import sys
sys.stdin = open('input.txt')

def dfs(v,cost):
    global m
    if cost >= m:
        return
    if v == n:
        m = min(m, cost)
    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                dfs(v+1, cost + costs[v][i])
                check[i] = 0

T = int(input())
for t in range(1, T+1):
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    check = [0]*n
    m = float('inf')
    dfs(0, 0)
    print('#%d %d' %(t, m))
