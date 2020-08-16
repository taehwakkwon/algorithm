import sys
sys.stdin = open('input.txt')

def solve(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    if dp[n]:
        return dp[n]
    else:
        dp[n] = solve(n-1) + solve(n-2)
        return dp[n]

n = int(input())
dp = [0]*(n+1)
dp[:3] = [0,1,1]
print(solve(n))
