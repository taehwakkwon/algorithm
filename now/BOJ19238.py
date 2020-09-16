import sys
import time
sys.stdin = open('input.txt')

start = time.time()

import sys
sys.setrecursionlimit(10**7)
from collections import deque
def bfs(queue):
    global fuel, dis
    arrive = []
    next_queue = deque([])
    while queue:
        r, c = queue.popleft()
        if (r,c) in passengers:
            arrive.append((r,c))
        else:
            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < n and 0 <= new_c < n and board[new_r][new_c] == 0 and dis[new_r][new_c] > dis[r][c] + 1:
                    dis[new_r][new_c] = dis[r][c] + 1
                    next_queue.append((new_r,new_c))
                    if (new_r, new_c) in passengers:
                        arrive.append((new_r,new_c))
    if arrive:
        arrive = min(sorted(arrive))
        fuel -= dis[arrive[0]][arrive[1]]
        if fuel <= 0:
            print(-1)
            sys.exit()
        r,c = find_destination(arrive)
        next_queue = deque([(r,c)])

    if next_queue:
        bfs(next_queue)
    elif not passengers:
        print(fuel)
        sys.exit()
    else:
        print(-1)
        sys.exit()

def set_zero(dis):
    for i in range(n):
        for j in range(n):
            dis[i][j] = float('inf')
    return dis

def find_destination(arrive):
    global fuel, dis
    q = deque([arrive])
    dis = set_zero(dis)
    dis[arrive[0]][arrive[1]] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < n and 0 <= new_c < n and board[new_r][new_c] == 0 and dis[new_r][new_c] > dis[r][c] + 1:
                dis[new_r][new_c] = dis[r][c] + 1
                if (new_r,new_c) == passengers[(arrive[0],arrive[1])]:

                    del passengers[(arrive[0],arrive[1])]

                    if fuel < dis[new_r][new_c]:
                        print(-1)
                        sys.exit()
                    fuel += dis[new_r][new_c]
                    dis[new_r][new_c] = dis[arrive[0]][arrive[1]] = 0
                    dis = set_zero(dis)
                    dis[new_r][new_c] = 0
                    return (new_r, new_c)
                q.append((new_r, new_c))
    else:
        print(-1)
        sys.exit()


n, m, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dis = [[float('inf')]*n for _ in range(n)]

r,c = map(int, input().split())
dis[r-1][c-1] = 0

passengers = {}
for i in range(1, m+1):
    d,e,f,g = map(int, input().split())
    passengers[(d-1,e-1)] = (f-1,g-1)

queue = deque([(r-1,c-1)])
bfs(queue)


'''
400칸

400명

'''