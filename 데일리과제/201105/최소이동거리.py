from heapq import *
from collections import deque, defaultdict

T = int(input())
for t in range(1, T + 1):
    n, e = map(int, input().split())
    graph = defaultdict(list)
    for i in range(e):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    result = [0] + [float('inf')] * n
    queue = []
    heappush(queue, (0, 0))

    visited = [0] * (n + 1)

    cost = 0
    while queue:
        node, weight = heappop(queue)
        if visited[node]:
            continue
        visited[node] = 1
        for next_node, weight in graph.get(node, []):
            if result[next_node] >= result[node] + weight:
                result[next_node] = result[node] + weight
                heappush(queue, (next_node, weight))

    # print(result)
    print('#%d %d' % (t, result[n]))