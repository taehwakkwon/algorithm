import sys
sys.stdin = open('input.txt')
def route(v,s,visit):
    global m
    if m < s:
        return
    if visit == n and v == 0:
        m = min(m, s)
    for idx in range(n):
        if v != idx and visited[idx] == 0:
            visited[idx] = 1
            route(idx, s + fields[v][idx],visit+1)
            visited[idx] = 0

T = int(input())
for t in range(1,T+1):
    n = int(input())
    fields = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    m = float('inf')
    route(0,0,0)
    print('#%d %d' %(t,m))
