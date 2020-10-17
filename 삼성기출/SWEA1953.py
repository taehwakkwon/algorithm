import sys
sys.stdin = open('../now/input.txt')

from collections import deque
move = [(0,1),(1,0),(0,-1),(-1,0)] #우하좌상
left = [1,3,6,7]
right = [1,3,4,5]
up = [1,2,4,7]
down = [1,2,5,6]
def bfs(queue, cnt):
    next_queue = deque([])
    if cnt >= l:
        return
    while queue:
        r,c = queue.popleft()
        if board[r][c] in right:
            dr, dc = move[0]  # 오른쪽으로 뚤린거 r,c
            nr, nc = r + dr, c + dc
            # 왼쪽으로 뚫린거
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and board[nr][nc] in left:
                next_queue.append((nr, nc))
                visited[nr][nc] = 1
        if board[r][c] in down:
            dr, dc = move[1]  # 위쪽으로 뚤린거 r,c
            nr, nc = r + dr, c + dc
            # 아래쪽으로 뚫린거
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and board[nr][nc] in up:
                next_queue.append((nr, nc))
                visited[nr][nc] = 1
        if board[r][c] in left:
            dr, dc = move[2]  # 왼쪽으로 뚤린거 r,c
            nr, nc = r + dr, c + dc
            # 오른쪽으로 뚫린거
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and board[nr][nc] in right:
                next_queue.append((nr, nc))
                visited[nr][nc] = 1
        if board[r][c] in up: #아래쪽으로 뜷린거
            dr, dc = move[3]  # 오른쪽으로 뚤린거 r,c
            nr, nc = r + dr, c + dc
            # 왼쪽으로 뚫린거
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and board[nr][nc] in down:
                next_queue.append((nr, nc))
                visited[nr][nc] = 1
    # for pp in visited:
    #     print(pp)
    # print()
    if next_queue:
        bfs(next_queue,cnt + 1)


T = int(input())
for t in range(1, T + 1 ):
    n, m, r, c, l = map(int, input().split())
    #세로, 가로 (맨홀위치), 소요된 시간
    board = [list(map(int, input().split())) for _ in range(n)]
    queue = deque([(r, c)])
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    bfs(queue,1)
    count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1:
                count += 1
    print('#%d %d'%(t,count))

