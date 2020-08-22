import sys
sys.stdin = open('input.txt')

import sys

cnt = 0
T = int(sys.stdin.readline())
k = int(sys.stdin.readline())
dp = [[0] * (k + 1) for i in range(T + 1)]
for i in range(1, k + 1):
    key, value = map(int, sys.stdin.readline().split())
    for j in range(key, min(key * value, k + 1), key):
        dp[j][i] = 1

dp[0][0] = 1
for i in range(T):
    for j in range(1, k + 1):
        if dp[i][j] > 0:
            