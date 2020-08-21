import sys
sys.stdin = open('input.txt')

import sys
n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
dp = [float('inf') for _ in range(k + 1 + max(coins))]
for i in range(n):
    dp[coins[i]] = 1
    for j in range(k + 1):
        dp[j + coins[i]] = min(dp[j] + 1, dp[j + coins[i]])
if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])