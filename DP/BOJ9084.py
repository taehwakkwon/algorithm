import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(m + 1):
            if dp[j] > 0 and j + coins[i] <= m:
                dp[j + coins[i]] += dp[j]
    print(dp[m])


