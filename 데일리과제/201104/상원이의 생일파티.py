import sys
sys.stdin = open('input.txt')

from collections import defaultdict
def dfs(node, depth):
    global cnt
    if depth > 2:
        return
    else:
        for next_node in graph.get(node,[]):
            if visited[next_node] == 0:
                visited[next_node] = 1
                cnt += 1

                dfs(next_node, depth+1)


from collections import defaultdict
T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    cnt = 0

    bf = graph[1][:]
    for i in bf[:]:
        bf.extend(graph.get(i,[]))
    bf = set(bf)
    if 1 in bf:
        bf.remove(1)
    print('#%d %d' % (t, len(bf)))
