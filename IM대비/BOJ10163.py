import sys
sys.stdin = open('input.txt')

n = int(input())
board = [[0]*102 for _ in range(102)]
for i in range(1, n+1):
    a, b ,c ,d = map(int, input().split())
    for j in range(a,a + c):
        for k in range(b,b+d):
            board[j][k] = i
numbers = [0]*(n+1)
for r in board:
    for k in range(1,n+1):
        numbers[k] += r.count(k)
for i in range(1,n+1):
    print(numbers[i])