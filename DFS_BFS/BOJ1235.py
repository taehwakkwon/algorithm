import sys
sys.stdin = open('../now/input.txt')

import sys
from collections import deque
def bfs(key):
    queue = deque([key])
    visited = [False] * (n+1)
    visited[key] = True
    cnt = 0
    while queue:
        v = queue.popleft()
        if v in dic:
            for key in dic[v]:
                if visited[key] == False:
                    visited[key] = True
                    cnt += 1
                    queue.append(key)
    return cnt


n, m = map(int ,sys.stdin.readline().split())
dic = {}
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dic[b] = dic.get(b,[]) + [a]
M = 0
res = {}
for key in range(1,n+1):
    tmp = bfs(key)
    if M <= tmp:
        res[key] = tmp
        M = tmp

res = sorted(res.items(), key = lambda x:x[1], reverse=True)
M = res[0][1]
for key, value in res:
    if value != M:
        break
    print(key, end = ' ')