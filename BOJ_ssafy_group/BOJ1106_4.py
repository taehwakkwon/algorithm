import sys
sys.stdin = open('input.txt')

import time

start = time.time()
MAX = 2000
c, n = map(int,input().split())
dp = [float('inf')]*(MAX+1)
dp[0] = 0
for i in range(n):
    cost, tourist = map(int, input().split())
    for j in range(tourist, MAX):
        dp[j] = min(dp[j], dp[j - tourist] + cost)

print(min(dp[c:]))

print(time.time()-start)