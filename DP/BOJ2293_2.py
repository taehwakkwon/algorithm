import sys
sys.stdin = open('input.txt')

import sys
n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(k + 1)]
dp[0] = 1
for i in range(n):
    for j in range(k + 1):
        if dp[j] > 0 and j + coins[i] <= k:
            dp[j + coins[i]] += dp[j]
print(dp[k])


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k + 1)]
dp[0] = 1
for i in range(n):
    for j in range(k + 1):
        if dp[j] > 0 and j + coins[i] <= k:
            if dp[j] > 0 and j + coins[i] <= k:
                dp[j + coins[i]] += dp[j]
print(dp[k])



