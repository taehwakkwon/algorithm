import sys
sys.stdin = open('input.txt')

import sys
from collections import deque
def bfs(i):
    queue = deque([i])
    while queue:
        v = queue.popleft()
        if v in dic:
            for value in dic[v]:
                if visited[value] == 0:
                    visited[value] = 1
                    queue.append(value)


n, m = map(int, sys.stdin.readline().split())
dic = { i:[] for i in range(1,n+1)}
visited = [0]*(n+1)
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    dic[u] = dic.get(u,[]) + [v]
    dic[v] = dic.get(v, []) + [u]
cnt = 0
for i in range(1,n+1):
    if visited[i] == 0 and i in dic:
        visited[i] = 1
        bfs(i)
        cnt += 1
print(cnt)

