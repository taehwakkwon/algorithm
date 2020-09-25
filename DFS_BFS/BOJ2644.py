import sys
sys.stdin = open('../now/input.txt')

from collections import deque
def bfs():
    queue = deque([(0, s)])
    visited = [0]*(n + 1)
    while queue:
        c, v = queue.popleft()
        if v in dic:
            for value in dic[v]:
                if visited[value] == 0:
                    if value == e:
                        return c + 1
                    queue.append((c+1, value))
                    visited[value] = 1
    return -1

n = int(input())
s, e = map(int ,input().split())
dic = {}
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    dic[x] = dic.get(x,[]) + [y]
    dic[y] = dic.get(y, []) + [x]
print(bfs())