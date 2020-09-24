import sys
sys.stdin = open('input.txt')

import sys
def dfs(v,s):
    global M
    if v == n:
        if s > M:
            M = s
    else:
        if v in dic:
            for key in dic[v]:
                dfs(key, s + 1)

n, m = map(int ,sys.stdin.readline().split())
dic = {}
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dic[b] = dic.get(b,[]) + [a]
M = 0
res = {}
for key in range(1,n+1):

res = sorted(res.items(), key = lambda x:x[1], reverse=True)
M = res[0][1]
for key, value in res:
    if value != M:
        break
    print(key, end = ' ')