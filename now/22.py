import sys
sys.stdin = open('input.txt')
import time
start = time.time()
from collections import deque
def bfs(v):
    queue = deque([(0,v)])
    while queue:
        c, v = queue.popleft()

        if v == k:
            return c
        #보수
        b = bin(v)[2:]
        for i in range(1,len(b)):
            if b[i] == '1':
                queue.append((c + 1, int(b[:i] + '0' + b[i+1:], base=2)))
            else:
                queue.append((c + 1, int(b[:i] + '1' + b[i + 1:],base=2)))

        #더하기
        queue.append((c + 1,v + 1))

        #빼기
        if v > 0:
            queue.append((c + 1, v - 1))

l = int(input(), base = 2)
k = int(input(), base = 2)
print(bfs(l))
print(time.time()-start)