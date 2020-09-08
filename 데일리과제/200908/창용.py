import sys
sys.stdin = open('input.txt')

def dfs(v):
    for i in range(1, n + 1):
        if i in dic[v] and visit[i] == 0:
            visit[v] = visit[i] = 1
            dfs(i)



T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    dic = {i : [] for i in range(1, n + 1)}
    for i in range(m):
        a, b = map(int, input().split())
        dic[a].append(b)
        dic[b].append(a)

    cnt = 0
    visit = [0]*(n+1)
    for i in range(1, n + 1):
        if visit[i] == 0:
            dfs(i)
            cnt += 1
    print('#%d %d'%(t, cnt))
