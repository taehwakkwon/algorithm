import sys
sys.stdin = open('input.txt')


import sys
c, r = map(int, input().split())
k = int(input())
if k > c*r:
    print(0)
else:
    board = [[0]*c for _ in range(r)]
    start = (r-1, 0)
    total = c*r
    cnt = 1
    y, x = r, 0
    while total - cnt >= 0:
        for dy, dx in [(-1,0),(0,1),(1,0),(0,-1)]:
            while 0 <= y + dy < r and 0 <= x + dx < c and board[y+dy][x+dx] == 0:
                board[y+dy][x+dx] = cnt
                cnt += 1
                y += dy
                x += dx

    for i in range(len(board)):
        if k in board[i]:
            print(board[i].index(k) + 1, r - i)
            break
