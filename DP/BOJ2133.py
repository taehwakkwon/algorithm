import sys
#sys.stdin = open('input.txt')


def solve(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n == 2:
        return 3
    if dp[n] != 0:
        return dp[n]
    dp[n] = solve(n - 2)*3 + 2
    return dp[n]

dp = [0]*31
print(solve(int(input())))


#n = 2 : 3
#n = 4 : 11