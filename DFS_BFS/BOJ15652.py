import sys
sys.stdin = open('input.txt')

def dfs(v):
    if v == M:
        print(' '.join(map(str,res)))
    else:
        for i in range(1, N + 1):
            if res[v-1] <= i:
                res[v] = i
                dfs(v + 1)
                res[v] = 0

N, M = map(int,input().split())
res = [0]*M
dfs(0)