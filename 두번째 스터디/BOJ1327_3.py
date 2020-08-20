import copy
from collections import deque
def bfs(v):
    queue = deque([v])
    next_queue = deque([])
    cnt = 0
    visit = [v]
    while queue:
        if sorted_numbers in queue:
            return cnt
        v = queue.popleft()
        for i in range(n - k + 1):
            tmp = v[:]
            tmp[i:i+k] = tmp[i:i+k][::-1]
            if tmp not in visit:
                next_queue.append(copy.deepcopy(tmp))
                visit.append(copy.deepcopy(tmp))
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