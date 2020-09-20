import sys
sys.stdin=open('input.txt')
board = [[0]*101 for _ in range(101)]
for i in range(4):
    a, b, c, d = map(int,input().split())
    for i in range(a, c):
        for j in range(b, d):
            board[i][j] = 1
s = 0
for r in board:
    s += sum(r)
print(s)