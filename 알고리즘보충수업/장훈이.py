import sys
sys.stdin = open('input.txt')


def dfs(v, s):
    global m
    if s >= b:
        if m > s:
            m = s
    if m <= s or v == n:
        return
    else:
        dfs(v + 1, s + h[v])
        dfs(v + 1, s)


T = int(input())
for t in range(1, T + 1):
    n, b = map(int, input().split())
    m = float('inf')
    h = list(map(int ,input().split()))
    dfs(0, 0)

    print('#%d %d' %(t, m - b))