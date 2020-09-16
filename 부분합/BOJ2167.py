import sys
sys.stdin = open('input.txt')
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
sum_board = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1,m+1):
        sum_board[i][j] = board[i-1][j-1] + sum_board[i][j-1] + sum_board[i-1][j] - sum_board[i-1][j-1]

k = int(input())
for i in range(k):
    s = 0
    a, b, c, d = map(int ,input().split())
    print(sum_board[c][d] + sum_board[a-1][b-1] - sum_board[a-1][d] - sum_board[c][b-1])


