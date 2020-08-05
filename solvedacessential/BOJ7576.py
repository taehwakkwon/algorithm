import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(graph, start_node):
    visited = []
    need_visit = deque([])

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited