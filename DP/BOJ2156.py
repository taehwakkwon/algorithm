import sys
sys.stdin = open('input.txt')

n = int(input())
wine = [int(input()) for _ in range(n)]
if n <= 2:
    print(sum(wine))
else:
    dp = [0]*(10002)
    dp[:3] = [wine[0], wine[0] + wine[1], max(wine[0] + wine[1], wine[0] + wine[2], wine[1], wine[2])]
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i] + wine[i-1])
    print(dp[n-1])