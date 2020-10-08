#a, b 사이 거리, c, a 사이 거리, 3개 중 중간값
import sys
from collections import Counter, defaultdict
sys.setrecursionlimit(10**7)
def solution(n, edges):
    def find_deepest(node,s):
        if node in graph:
            for value in graph[node]:
                if dis[value] == -1:
                    dis[value] = s
                    find_deepest(value, s+1)

    graph = defaultdict(list)

    for i in range(len(edges)):
        graph[edges[i][0]].append(edges[i][1])
        graph[edges[i][1]].append(edges[i][0])
    node = edges[0][1]
    dis = [-1]*(n+1)
    dis[node] = 0
    find_deepest(node,0)
    M = max(dis)
    node = dis.index(M)
    dis = [-1]*(n+1)
    dis[node] = 0
    find_deepest(node,1)
    cnter = Counter(dis)
    M = max(dis)
    if cnter[M] == 1:
        return M - 1
    else:
        return M

print(solution(4,[[1,2],[2,3],[3,4]]))
print(solution(5,[[1,5],[2,5],[3,5],[4,5]]))


