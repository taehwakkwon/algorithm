import sys

# sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10 ** 6)
n = int(input())
dp = [0]*(n+1)
for i in range(2,n+1):
    dp[i] = dp[i - 1] + 1
    if not i % 3 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
    if not i % 2 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
print(dp[n])
