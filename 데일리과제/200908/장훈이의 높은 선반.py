import sys
sys.stdin = open('input.txt')


def dfs(v, sum):
    global M
    if b <= sum <= M:
        M = sum
    if sum >= M or v >= n:
        return
    else:
        dfs(v + 1, sum + s[v])
        dfs(v + 1, sum)


T = int(input())
for t in range(1, T + 1):
    n, b = map(int, input().split())
    M = float('inf')
    s = list(map(int, input().split()))
    dfs(0, 0)
    print('#%d %d'%(t, M - b))