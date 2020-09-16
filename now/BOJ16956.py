import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs():
    wolf_queue = deque(wolf)
    sheep_queue = deque(sheep)
    dis_wolf = [[0]*c for _ in range(r)]
    dis_sheep = [[0]*c for _ in range(r)]
    while wolf_queue and sheep_queue:
        w_r, w_c = wolf_queue.popleft()
        s_r, s_c = sheep_queue.popleft()
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_wr, new_wc = w_r + dr, w_c + dc
            new_sr, new_sc = s_r + dr, s_c + dc
            if 0 <= new_wr < r and 0 <= new_wc < c and dis_sheep[new_wr][new_wc] == 0:
                




r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
wolf = []
sheep = []
for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            sheep.append((i,j))
        elif board[i][j] == 'W':
            wolf.append((i,j))
if not wolf:
    print(1)
    for r in board:
        print(*r)
else:
    bfs()

