import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(v):
    global pre_length, res
    queue = deque([(0,v)])
    visited = [v]
    while queue:
        c, v = queue.popleft()
        for nxt in dic.get(v, []):
            if nxt not in visited:
                visited.append(nxt)
                queue.append((c+1, nxt))
        if pre_length < len(visited):
            pre_length = len(visited)
            res = max(queue)


T = 10
for t in range(1, T + 1):
    length, start = map(int, input().split())
    tmp = list(map(int, input().split()))
    dic = {}
    pre_length = 0
    res = 0
    #board = [[0]*(M + 1) for _ in range(M + 1)]
    for i in range(0, len(tmp), 2):
        dic[tmp[i]] = dic.get(tmp[i], []) + [tmp[i+1]]
    bfs(start)
    print('#%d' %t, res[1])