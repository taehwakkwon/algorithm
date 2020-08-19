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
    cnt = 0
    while queue:
        v = queue.popleft()
        if cnt > 1000:
            return(-1)
        if v == sorted_numbers or sorted_numbers in queue:
            print(cnt, len(queue))
            return cnt
        cnt += 1
        for i in range(n - k + 1):
            v[i:i+k] = v[i:i+k][::-1]
            print(v, cnt)
            queue.append(copy.deepcopy(v))


res = []
m = float('inf')
n, k = map(int, input().split())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)
print(bfs(numbers))
#dfs(0, numbers, 0)