import sys
sys.stdin = open('input.txt')

import sys
sys.setrecursionlimit(10**6)
def factorial(n):
    if n <= 1:
        return 1
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = n * factorial(n - 1)
        return dp[n]

n, k = map(int, input().split())
dp = [0] * (n + 1)
print((factorial(n)//(factorial(k) * factorial(n - k)))%10007)