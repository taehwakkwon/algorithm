import sys
sys.stdin = open('../발표/자리배정.txt')

import sys
c, r = map(int, input().split())
k = int(input())
if k == 1:
    print(1, 1)
elif k > c*r:
    print(0)
else:
    board = [[0]*c for _ in range(r)]
    total = c*r
    cnt = 1
    y, x = -1, 0

    while total - cnt >= 0:
        for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            while 0 <= y + dy < r and 0 <= x + dx < c and board[y+dy][x+dx] == 0:
                board[y+dy][x+dx] = cnt
                if cnt == k:
                    print(x + dx + 1, y + dy + 1)
                    sys.exit()
                cnt += 1
                y += dy
                x += dx
