import sys
sys.stdin = open('input.txt')

def dfs(v):
    if v == M:
        print(' '.join(map(str, res)))
    else:
        for i in range(N):
            if ch[i] == 0:
                ch[i] = 1
                res[v] = numbers[i]
                dfs(v + 1)
                ch[i] = 0


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
res = [0]*M
ch = [0]*(N + 1)
dfs(0)