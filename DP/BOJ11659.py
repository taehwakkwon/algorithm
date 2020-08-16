import sys
sys.stdin = open('input.txt','r')

import sys

n,m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [0]*n
dp[0] = numbers[0]
for i in range(1,len(numbers)):
    dp[i] = numbers[i]+dp[i-1]
for i in range(m):
    i,j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(dp[j-1])
    else:
        print(dp[j-1]-dp[i-2])