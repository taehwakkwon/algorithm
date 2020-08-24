import sys
sys.stdin = open('input.txt')

import sys
import copy
sys.setrecursionlimit(10**7)
def dfs(v, num_list, s):
    global m
    print(num_list, v, n - k, s)
    if sorted_numbers == num_list:
        if m > s:
            m = s
    if v > n - k:
        return
    else:
        for i in range(n - k + 1):
            num_list[i:i+k] = num_list[i:i+k][::-1]
            print(num_list)
            res.append(copy.deepcopy(num_list))
            dfs(v + i, num_list, s + 1)

import copy
from collections import deque
def bfs(v):
    queue = deque([v])
    next_queue = deque([])
    cnt = 0
    visit = {}
    visit[str(v)] = 0
    while queue:
        if sorted_numbers in queue:
            return cnt
        v = queue.popleft()
        for i in range(n - k + 1):
            tmp = v[:]
            tmp[i:i+k] = tmp[i:i+k][::-1]
            if str(tmp) not in visit:
                next_queue.append(copy.deepcopy(tmp))
                visit[str(tmp[:])] = 0
        if not queue:
            queue.extend(next_queue)
            next_queue = deque([])
            cnt += 1


n, k = map(int, input().split())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)
res = bfs(numbers)
if res == None:
    print(-1)
else:
    print(res)
#dfs(0, numbers, 0)