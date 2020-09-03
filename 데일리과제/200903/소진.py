import sys
sys.stdin = open("input.txt", "r")
def bfs():
    queue = []
    queue.append((s, 0))
    visited = [0]*(v+1)
    visited[s] = 1
    while queue:
        now, length = queue.pop(0)
        for q in range(v+1):
            if ta[now][q] == 1 and not visited[q]:
                if q == g:
                    return length+1
                queue.append((q, length+1))
                visited[now] = 1
    return 0
t = int(input())
for tc in range(1,t+1):
    v, e = map(int,input().split())
    node = [list(map(int,input().split())) for _ in range(e)]
    ta = [[0] * (v+1) for _ in range(v+1)]
    s, g = map(int, input().split())
    while node:
        x, y = node.pop(0)
        ta[x][y] = ta[y][x] = 1
    result = bfs()
    print('#%d %d' %(tc, result))
#
#
# # 반복구조의 bfs
# from collections import deque
# def bfs():
#     # 시작점 찾고,
#     global queue, res
#     r = 0
#     c = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:
#                 r, c = i, j
#                 break
#
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#
#     visited = [[0] * N for _ in range(N)]
#     queue = deque(list())
#     queue.append((r, c, 0))
#     while queue:
#         # 시작점으로부터 위치정보를 얻어올 때는
#         # 현재 위치 받을 때 같이 받아와야함.
#         cr, cc, length = queue.popleft()
#         visited[cr][cc] = 1
#
#         for i in range(4):
#             nr = cr + dr[i]
#             nc = cc + dc[i]
#             # 범위 내에 있으며, 방문하지 않았으면
#             if 0 <= nr < N and 0 <= nc < N and (arr[nr][nc] == 0 or arr[nr][nc] == 3) and not visited[nr][nc]:
#                 if arr[nr][nc] == 0:
#                     queue.append((nr, nc, length + 1))
#                 elif arr[nr][nc] == 3:
#                     return length
#     return 0
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     res = 0
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     result = bfs()
#     print("#{} {}".format(tc, result))