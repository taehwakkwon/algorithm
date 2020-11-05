import sys
sys.stdin = open('input.txt')

from collections import defaultdict, deque
def dfs(v):
    if v > n:
        return
    else:
        for node in graph.get(v,[]):
            if visited[node] == 0:
                visited[node] = 1
                dfs(node)

from collections import defaultdict, deque
def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for node in graph.get(v,[]):
            if visited[node] == 0:
                visited[node] = 1
                queue.append(node)


T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    votes = list(map(int, input().split()))
    visited = [0]*(n+1)
    graph = defaultdict(list)

    for i in range(0, m*2, 2):
        a, b = votes[i:i+2]
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    for i in range(1,n+1):
        if visited[i] == 0:
            visited[i] = 1
            # bfs(i)
            dfs(i)

            cnt += 1

    print('#%d %d' %(t, cnt))





