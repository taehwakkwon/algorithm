import sys
sys.stdin = open('../now/input.txt')

#상어 > 물고기: 잡아먹
#상어 >= 물고기: 이동가능
#먹을 수 있는게 없음 엄마한테 도움 : 끝
#먹을 수 있는 물고기 중 가장 가까운놈, 여럿이면 가장 왼쪽의 물고기
from collections import deque
def bfs(queue, cnt):
    global time_save, fishes, had, size
    next_queue = deque([])
    eatable = []
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and size >= board[nr][nc] and visited[nr][nc] == 0:
                next_queue.append((nr,nc))
                visited[nr][nc] = 1
                if 0 < board[nr][nc] < size:
                    eatable.append((nr,nc))
    if next_queue:
        if eatable:
            r, c = min(eatable)
            had += 1
            if had == size:
                size += 1
                had = 0

            del fishes[(r, c)]

            board[r][c] = 0
            time_save = cnt + 1
            for i in range(n):
                for j in range(n):
                    visited[i][j] = 0
            visited[r][c] = 1
            bfs(deque([(r,c)]), cnt + 1)

        elif fishes and min(fishes.values()) < size:
            bfs(next_queue, cnt + 1)



time_save = 0
n = int(input())
size = 2
fishes = {}
had = 0
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            baby_shark = (i,j)
            board[i][j] = 0
            visited[i][j] = 1
        elif board[i][j] != 0:
            fishes[(i,j)] = board[i][j]

if not fishes:
    print(0)
else:
    queue = deque([baby_shark])
    bfs(queue,0)
    print(time_save)