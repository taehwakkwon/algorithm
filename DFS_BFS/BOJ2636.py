import sys
sys.stdin = open('../now/input.txt')

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
from collections import deque
def bfs(queue,t,cnt):
    next_queue = deque([])
    new_cnt = 0
    while queue:
        rr, cc = queue.popleft()
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_r, new_c = rr + dr, cc + dc
            if 0 <= new_r < r + 2 and 0 <= new_c < c + 2 and visited[new_r][new_c] == 0:
                if board[new_r][new_c] == 0:
                    queue.append((new_r,new_c))
                    visited[new_r][new_c] = 1
                else:
                    board[new_r][new_c] = 0
                    visited[new_r][new_c] = 1
                    next_queue.append((new_r,new_c))
                    new_cnt += 1
    if next_queue:
        bfs(next_queue,t+1,new_cnt)
    else:
        print(t)
        print(cnt)



r, c = map(int, input().split())
visited = [[0] * (c + 2) for _ in range(r + 2)]

board = [[0]*(c+2)]
for i in range(r):
    board.append([0]+list(map(int, input().split()))+[0])
board.append([0]*(c+2))

bfs(deque([(0, 0)]),0,0)