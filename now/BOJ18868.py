import sys
sys.stdin = open('input.txt')
#4, 2, 4, 4, 1
from collections import deque
#
dr = [0,1,0,-1]
dc = [1,0,-1,0]
moves = [0,
        [(0,),(1,),(2,),(3,)],
        [(0,2),(1,3)],
        [(0,1),(1,2),(2,3),(3,0)],
        [(0,1,2),(1,2,3),(2,3,0),(3,0,1)],
        [(0,1,2,3)]
        ]

def dfs(v):
    global M
    if v == len(cameras):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0 and watch[i][j] == 0:
                    cnt += 1

        M = min(M, cnt)
        return
    else:
        for move in moves[cameras[v][1]]:
            for d in move:
                r, c = cameras[v][0]
                while 0 <= r + dr[d] < n and 0 <= c + dc[d] < m and board[r + dr[d]][c + dc[d]] != 6:
                    r += dr[d]
                    c += dc[d]
                    watch[r][c] -= 1
            dfs(v+1)
            for d in move:
                r, c = cameras[v][0]
                while 0 <= r + dr[d] < n and 0 <= c + dc[d] < m and board[r + dr[d]][c + dc[d]] != 6:
                    r += dr[d]
                    c += dc[d]
                    watch[r][c] += 1

M = float('inf')
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
watch = [[0]*m for _ in range(n)]
cameras = []
for i in range(n):
    for j in range(m):
        if 0 < board[i][j] < 6:
            cameras.append(((i,j), board[i][j]))
dfs(0)
print(M)
