import sys
sys.stdin = open('input.txt')
MAX = 101
n = int(input())
points = []
board = [[0]*MAX for _ in range(MAX)]
for i in range(n):
    a, b = map(int, input().split())
    for p in range(10):
        for q in range(10):
            board[a+p][b+q] = 1

for i in range(1, MAX):
    for j in range(MAX):
        if board[i][j] != 0:
            board[i][j] += board[i-1][j]

M = 100
for i in range(1, MAX):
    for j in range(MAX):
        h = 100
        for k in range(j, MAX):
            h = min(h, board[i][k])
            if h == 0:
                break
            M = max(M, h*(k - j + 1))
for r in board:
    print(*r)
print(M)