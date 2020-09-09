import sys
sys.stdin = open('input.txt')

def dfs(v):
    if v > n:
        return
    else:
        if str(2*v) in info[v][1:]:
            dfs(2*v)
        print(info[v][1], end = '')
        if str(2 * v + 1) in info[v][1:]:
            dfs(2*v+1)

T = 10
for t in range(1, T + 1):
    n = int(input())
    info = [[]]
    print('#%d' %t, end = ' ')
    for i in range(n):
        tmp = list(input().split())
        info.append(tmp)
    dfs(1)
    print()

