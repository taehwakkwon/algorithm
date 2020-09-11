import sys
sys.stdin = open('input.txt')
import time
start = time.time()
from collections import deque
def bfs(v):
    visited = [0] + [1]*(1<<11)
    queue = deque([(0,v)])
    while queue:
        c, v = queue.popleft()
        if v == k:
            return c
        for i in range(v.bit_length() - 1):
            comp = v ^ (1 << i)
            if comp < 1 << 11 and visited[comp] == 1:
                queue.append((c + 1, comp))
                visited[comp] = 0
        if v + 1 < 1 << 11 and visited[v + 1] == 1:
            queue.append((c + 1, v + 1))
            visited[v + 1] = 0
        if v - 1 >= 0 and visited[v - 1] == 1:
            queue.append((c + 1, v - 1))
            visited[v - 1] = 0


l = int(input(),base=2)
k = int(input(),base=2)
print(bfs(l))






print(time.time()-start)
#보수
#1더하기
#1빼기
