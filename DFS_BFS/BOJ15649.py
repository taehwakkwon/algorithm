import sys
sys.stdin = open('input.txt')
def dfs(v):
    if v == M:
        print(' '.join(map(str,res)))
    else:
        for i in range(1, N + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[v] = i
                dfs(v + 1)
                ch[i]=0

N, M = map(int, input().split())
ch = [0] * (N+1)
res = [0]*M
dfs(0)
