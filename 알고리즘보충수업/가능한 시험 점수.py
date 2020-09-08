import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for i in range(len(v)):






T = int(input())
for t in range(1, T + 1):
    n = int(input())
    scores = list(map(int, input().split()))
    visited = [1] + [0]*(total - 1) + [1]
    for score in scores:
        visited[score] = 1
    total = sum(scores)

    print('#%d %d' %(t,s))