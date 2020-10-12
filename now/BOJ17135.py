import sys
sys.stdin = open('input.txt')
#10:25
#궁수 3명
#동시 공격, 거리 D 이하 가장 가까운 적(여럿이면 왼쪽)
import time
start = time.time()

import sys
sys.setrecursionlimit(10**7)
from collections import deque

def dfs(v,b,s):
    if s == 3:
        result.append(b)
    elif v == m or s > 3:
        return
    else:
        dfs(v + 1, b, s)
        dfs(v + 1, b | 1 << v, s + 1)


def bfs(queue):
    global kill
    # print(queue)
    while queue:
        cnt, r, c = queue.popleft()
        if cnt > d:
            continue
        if board[r][c] == 1:
            kill += 1
            board[r][c] = 0
            return
        for dr, dc in [(0,-1),(-1,0),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                queue.append((cnt + 1, nr, nc))


result = []
n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
army = {}
total = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            army[(i,j)] = 1
            total += 1
dfs(0,0,0)
M = 0
for com in result:
    kill = gone = 0
    while total > (kill + gone):
        for i in range(m):
            if com & 1 << i:
                queue = deque([])
                queue.append((1,n-1, i))
                bfs(queue)
        # for r in board:
        #     print(r)
        # print()
        for i in range(n-1,-1,-1):
            for j in range(m):
                if board[i][j] == 1:
                    board[i][j] = 0
                    if i + 1 < n:
                        board[i + 1][j] = 1
                    else:
                        gone += 1
    for r, c in army.keys():
        board[r][c] = 1

    M = max(M,kill)
print(M)

print(time.time()-start)