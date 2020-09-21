import sys
sys.stdin = open('input.txt')

import sys
def dfs(v,s):
    global m
    if v > m:
        return
    if sum(ch) == N:
        m = min(s, m)
        return
    else:
        for value in dic[v]:
            if ch[value] == 0:
                ch[value] = 1
                dfs(v + 1, s + 1)
                ch[value] = 0


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, sys.stdin.readline().split())
    dic = {}
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        dic[a] = dic.get(a, []) + [b]
        dic[b] = dic.get(b, []) + [a]
    ch = [0]*(N+1)
    m = N
    for i in range(1, N + 1):
        dfs(i, 0)
    print(m-1)
