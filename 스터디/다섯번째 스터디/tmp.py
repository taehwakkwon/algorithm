import sys
sys.stdin = open('input.txt')

def check(min_y, min_x,max_y, max_x):
    for y in range(min_y,max_y+1):
        for x in range(min_x,max_x+1):
            if board[y][x] == 0:
                return False
    return True

MAX = 101
n = int(input())
points = []
dr = [1,0,-1,0]
dc = [0,1,0,-1]
x1 = y1 = 101
x2 = y2 = 0
for i in range(n):
    a, b = map(int, input().split())
    x1 = min(a, x1)
    y1 = min(b, y1)
    x2 = max(a, x2)
    y2 = max(b, y2)
    points.append((a,b))
board = [[0]*(x2+10 - x1) for _ in range(y2 + 10 - y1)]
r = y2 + 10 - y1
c = x2 + 10 - x1
# row_filter = [[0]*(x2+10 - x1) for _ in range(y2 + 10 - y1)]
# col_filter = [[0]*(x2+10 - x1) for _ in range(y2 + 10 - y1)]


for a, b in points:
    for i in range(10):
        for j in range(10):
            board[b+j-y1][a+i-x1] = 1

num = 0
for j in range(c):
    for i in range(1, r):
        if board[i][j] != 0:
            board[i][j] += board[i-1][j]
for r in board:
    print(*r)