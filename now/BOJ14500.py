import sys
sys.stdin = open('input.txt')
#정사각형 겹치지 x
#모두 연결(변끼리)

import sys
input = sys.stdin.readline
moves = [[(0,0),(0,1),(0,2),(0,3)], [(0,0),(1,0),(2,0),(3,0)],
         [(0,0),(1,0),(0,1),(1,1)],
         [(0,0),(0,1),(0,2),(1,2)], [(0,0),(0,1),(0,2),(-1,2)],[(0,0),(0,1),(0,2),(1,0)],[(0,0),(0,1),(0,2),(-1,0)],[(0,0),(0,1),(1,0),(2,0)],[(0,0),(0,-1),(1,0),(2,0)],[(0,0),(2,1),(1,0),(2,0)],[(0,0),(1,0),(2,0),(2,-1)],
         [(0,0),(-1,0),(0,1),(1,1)],[(0,0),(-1,0),(0,-1),(1,-1)], [(0,0),(1,0),(1,1),(0,-1)], [(0,0),(-1,0),(-1,1),(0,-1)],
         [(0,0),(1,0),(0,-1),(0,1)],[(0,0),(-1,0),(0,-1),(0,1)], [(0,0),(1,0),(-1,0),(0,1)],[(0,0),(1,0),(-1,0),(0,-1)]
         ]

def check(r,c,move):
    s = 0
    for dr, dc in move:
        if 0 <= r + dr < n and 0 <= c + dc < m:
            s += board[r+dr][c+dc]
            continue
        else:
            return False
    return s

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s = 0
M = 0
for i in range(n):
    for j in range(m):
        for move in moves:
            s = check(i,j,move)
            if s:
                M = max(M, s)
                s = 0
print(M)
