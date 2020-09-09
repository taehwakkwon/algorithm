import sys
sys.stdin = open('input.txt')

def dfs(v,s,i):
    global res
    if visited[i][0] == 1 and visited[i][1] >= v:
        return
    if visited[s][0] == 0:
        visited[s][0] = 1
        visited[s][1] = v
    if s > i or v == n:
        return
    else:
        dfs(v + 1, s + score[v], i)
        dfs(v + 1, s, i)


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    score = list(map(int, input().split()))
    visited = [[0, 0] for _ in range(sum(score) + 1)]
    cnt = 0
    for i in range(sum(score) + 1):
        res = 0
        dfs(0, 0, i)
        if res:
            cnt += 1
    s = 0
    for i in range(len(visited)):
        s += visited[i][0]
    print('#%d %d' %(t,s))