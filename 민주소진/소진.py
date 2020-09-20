import sys
sys.stdin = open('input.txt')

#bfs 구현
def bfs(q):
    visited = []
    Q = []
    Q.append(q)
    visited.append(q)
    #방문 표시 #큐에 삽입
    while Q:
        n = Q.pop(0)
        #인접행렬
        for w in range(N+1):
            if Board[n][w] == 1 and w not in visited:
                Q.append(w)
                visited.append(w)
    return visited

#dfs 구현
def dfs(v):
    stack = []
    visited[v] = 1
    stack.append(v)
    result.append(v)
    while stack:
        current = stack.pop(-1)
        visited[current] = 1
        for neighbor in range(N+1):
            if Board[current][neighbor] == 1 and visited[neighbor] == 0:
                stack.append(neighbor)
                print(len(stack))
                result.append(neighbor)
                break
        # else: # break에 걸리지 않음 : 현재노드에서 갈수 있는 노드가 없음
        #      stack.pop()
    return result

# 빈 인접행렬
N, M, V = map(int, input().split()) #N: 정점의 개수 #M: 간선개수 #V:탐색을 시작할 정점 번호 ㅉ
Board = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    x,y = map(int, input().split())
    Board[x][y] = Board[y][x] = 1
    visited = [0] * (N + 1)
    result = list()


#결과값
result1 = bfs(V)
print(*result1)

result2 = dfs(V)
print(*result2)