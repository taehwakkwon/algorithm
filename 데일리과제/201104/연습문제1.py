from collections import defaultdict
def dfs(v):
    if v > n:
        return
    else:
        for next_node in graph.get(v,[]):
            if visited[next_node] == 0:
                visited[next_node] = 1
                print(next_node, end=' ')
                dfs(next_node)

n, m = 7, 8#map(int, input().split())
infos = list(map(int, '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'.split())) #list(map(int, input().split()))
graph = defaultdict(list)
for i in range(0, 2*m, 2):
    a, b = infos[i:i+2]
    graph[a].append(b)
    graph[b].append(a)
visited = [0]*(n+1)
visited[1] = 1
print(1, end=' ')
dfs(1)