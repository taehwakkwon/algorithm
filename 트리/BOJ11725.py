import sys
sys.stdin = open('input.txt')
import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def bfs():
    graph = defaultdict(int)
    visited = [0] * (n + 1)
    visited[:2] = [1,1]
    queue = deque([1])
    while queue:
        v = queue.popleft()
        if v in dic:
            for value in dic[v]:
                if visited[value] == 0:
                    visited[value] = 1
                    queue.append(value)
                    graph[value] = v
    return graph

n = int(input())
dic = defaultdict(list)
for i in range(n-1):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

graph = bfs()
for i in range(2,n+1):
    print(graph[i])
