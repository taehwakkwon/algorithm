import sys
sys.stdin = open('../now/input.txt')

import time
start = time.time()

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(2, n):
    if board[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]

for i in range(n):
    for j in range(2,n):
        if board[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][2] + dp[i-1][j][1]

        if board[i][j] == board[i][j-1] == board[i-1][j] == 0:
            dp[i][j][2] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]
print(sum(dp[n-1][n-1]))