import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(v):
    cnt = 0
    queue = deque([(cnt, v)])
    visit = {}
    visit[v] = 0
    while queue:
        c, v = queue.popleft()
        for i in range(n - k + 1):
            tmp = v[i:i+k]
            tmp = v[:i] + tmp[::-1] + v[i+k:]
            if ''.join(tmp) not in visit:
                queue.append((c + 1, tmp[:]))
                visit[tmp] = c + 1
    print(visit)


n, k = map(int, input().split())
numbers = ''.join(list(input().split()))
sorted_numbers = ''.join(sorted(numbers))
if sorted_numbers == numbers:
    print(0)
else:
    res = bfs(numbers)
    if res == None:
        print(-1)
    else:
        print(res)