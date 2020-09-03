import sys
#sys.stdin = open('input.txt')


def solve(n):
    if n == 2:
        return 3
    if dp[n] != 0:
        return dp[n]
    dp[n] = (4*solve(n - 2) - solve(n-4))%1000000007
    return dp[n]


for i in range(0,101,2):
    n = i#int(input())
    dp = [1,0,3] + [0]*(n-2)

    if n % 2 or n == 0:
        print(0)
    else:
        print(solve(n))


#n = 2 : 3
#n = 4 : 11