import sys
sys.stdin = open('input.txt')


import sys
n = int(input())
board = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 1
l = int(input())
move = []
r = c = 0
for _ in range(l):
    a, b = input().split()
    move.append((int(a),b))
move = move[::-1]
dr, dc = 0, 1
t = 0
a, b = move.pop()
flag = True
while True:
    print(r, c, dr, dc, b, t, move)
    if flag and a < t:
        if (dr,dc) == ((1,0) or (-1,0)):
            if b == 'D':
                dr *= -1
                dc *= -1
                dr, dc = dc ,dr
            else:
                dr, dc = dc, dr
        else:
            if b == 'L':
                dr *= -1
                dc *= -1
                dr, dc = dc, dr
            else:
                dr, dc = dc, dr
        if move:
            a, b = move.pop()
        else:
            flag = False

    else:
        if 0 <= r + dr < n and 0 <= c + dc < n:
            r += dr
            c += dc
            t += 1
        else:
            print(t + 1)
            sys.exit()