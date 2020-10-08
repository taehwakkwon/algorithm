from collections import defaultdict, Counter
answer = 0
node = 0
candi = []


def solution(n, edges):
    global answer, node, candi
    graph = defaultdict(list)
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    visited = [False for _ in range(n+1)]
    dfs(3, graph, 0, visited)  # 노드에서 가장 먼 점을 찾는다
    visited = [False for _ in range(n+1)]
    candi = []
    answer = 1
    dfs(node, graph, 0, visited)  # 그 가장 먼 점에서 탐색해서 먼 친구를 찾는다
    candi_cnter = Counter(candi)
    max_val = max(candi_cnter)
    ret = candi_cnter[max_val]
    return answer if ret >= 2 else answer-1
    # 거리 가장 먼 점이 여러개면 중간값은 최댓값
    # 거리 가장 먼 점이 한개면 중간값은 최댓값-1


def dfs(now, graph, cost, visited):
    global answer, node, candi
    if visited[now] == True:
        return
    visited[now] = True
    if (answer <= cost):
        answer = cost
        candi.append(cost)
        node = now
    for i in graph[now]:
        dfs(i, graph, cost+1, visited)

