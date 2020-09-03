import sys
sys.stdin = open('../sample_input.txt')

from collections import deque
T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    for i in range(m):
        queue.append(queue.popleft())
    print('#%d %d' %(t, queue.popleft()))
