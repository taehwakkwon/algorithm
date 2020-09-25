import sys
sys.stdin = open('../now/input.txt')
from collections import deque
def bfs(y,x):
    global t_sheep, t_wolf
    queue = deque([(y,x)])
    sheep = wolf = 0
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(0,0), (0,1),(1,0),(0,-1),(-1,0)]:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < r and 0 <= new_x < c and board[new_y][new_x] != '#' and visited[new_y][new_x] == 0:
                if board[new_y][new_x] == 'k':
                    sheep += 1
                if board[new_y][new_x] == 'v':
                    wolf += 1
                queue.append((new_y,new_x))
                visited[new_y][new_x] = 1
    if sheep > wolf:
        t_sheep += sheep
    else:
        t_wolf += wolf


r,c = map(int, input().split())
t_sheep = t_wolf = 0
board = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if (board[i][j] == 'v' or board[i][j] == 'k') and visited[i][j] == 0:
            bfs(i,j)
print(t_sheep,t_wolf)