import sys
sys.stdin = open('input.txt')

def dfs(v):
    global cnt
    cnt += 1
    for i in range(2):
        if tree[v][i] != 0:
            dfs(tree[v][i])


T = int(input())
for t in range(1, T + 1):
    e, n = map(int, input().split())
    tree = [[0]*2 for _ in range(e+2)]
    info = list(map(int, input().split()))
    cnt = 0
    for i in range(0, len(info), 2):
        if tree[info[i]][0] == 0:
            tree[info[i]][0] = info[i + 1]
        else:
            tree[info[i]][1] = info[i + 1]
    dfs(n)
    print('#%d %d' %(t,cnt))