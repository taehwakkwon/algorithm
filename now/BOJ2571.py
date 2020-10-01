import sys
sys.stdin = open('input.txt')

MAX = 101
n = int(input())
board = [[0]*MAX for _ in range(MAX)]
line = []
for i in range(n):
    a, b = map(int, input().split())
    for j in range(10):
        line.extend([(a,b+j),(a+j,b),(a+9-j,b+9),(a+9,b+9-j)])
        for k in range(10):
            board[a+j][b+k] = 1
for i in range(MAX):



for r in board:
    print(*r)