# import sys
# sys.stdin = open('sample_input.txt')


def solve(n):
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = 2 * solve(n - 2) + solve(n-1)
        return dp[n]


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    dp = [1, 3, 5] + [0]*(n//10)
    print('#%d %d' %(tc, solve(n//10 - 1)))

