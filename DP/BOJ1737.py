import sys


mod=1000**6
pi=3.14159265359
dp=[[None]*400 for i in range(1001)]
def pib(n,p):
    if 0<=n-p*pi<=pi: return 1
    if dp[n][p]!=None: return dp[n][p]
    dp[n][p]=(pib(n-1,p)+pib(n,p+1))%mod
    return dp[n][p]
print(pib(int(input()),0))
print(dp)




import math
def solve(n):
    if n <= math.pi:
        return 1
    elif n in dp:
        return dp[n]
    else:
        dp[n] = (solve(n - 1) + solve(n - math.pi))%1000000000000000000
        return dp[n]


dp = {}
print(solve(int(input())))
