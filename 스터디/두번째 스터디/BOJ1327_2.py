import sys
sys.stdin = open('input.txt')

from collections import deque
from copy import deepcopy
def bfs(v):
    queue = deque([v])
    next_queue = deque([v])
    cnt = 0
    while queue:
        if sorted_numbers in queue:
            return cnt
        v = queue.popleft()
        if v in visit:
            continue
        for i in range(n - k + 1):
            print(v[:i] + v[i:i+k][::-1] + v[i+k:])
            next_queue.append(deepcopy(v[:i] + v[i:i+k][::-1] + v[i+k:]))
            visit.append(deepcopy(v[:i] + v[i:i+k][::-1] + v[i+k:]))
        print(next_queue)
        if not queue:
            queue.extend(next_queue)
            next_queue = deque([])
            cnt += 1

visit = []
n, k = map(int, input().split())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)
res = bfs(numbers)
if res == None:
    print(-1)
else:
    print(res)