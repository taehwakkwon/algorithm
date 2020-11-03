import sys
sys.stdin = open('input.txt')

def dfs(v, battery, cnt):
    global m
    if battery < 0 or m <= cnt:
        return
    if v == n:
        m = min(m, cnt)
    else:
        dfs(v + 1, battery - 1, cnt)
        dfs(v + 1, batteries[v] - 1, cnt + 1)



T = int(input())
for t in range(1, T+1):
    batteries = list(map(int, input().split()))
    n = batteries[0]
    batteries[0] = 0
    m = float('inf')
    dfs(1, 0, 0)
    print('#%d %d' %(t, m-1))
