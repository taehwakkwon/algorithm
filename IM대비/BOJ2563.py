import sys
sys.stdin = open('input.txt')

n = int(input())
board = [[0]*100 for _ in range(100)]
for i in range(n):
    a, b = map(int, input().split())
    for p in range(a, a + 10):
        for q in range(b, b + 10):
            board[p][q] = 1

s = 0
for r in board:
    s += sum(r)
print(s)
