import sys

sys.stdin = open('input.txt')
import time
start = time.time()
import sys
sys.setrecursionlimit(10**7)
MAX = 2001
def dfs(v, t, money):
    global m
    if t >= c and t > 0 and m > money:
        m = money
    if v >= n or t >= c or money > m:
        return money
    else:
        dp[t] = min(dp[t], dfs(v, t + tourists[v], money + costs[v]),dfs(v + 1, t, money))


c, n = map(int,input().split())
costs = []
tourists = []
dp = [float('inf')]*MAX
for i in range(n):
    cost, tourist = map(int, input().split())
    costs.append(cost)
    tourists.append(tourist)
    dp[tourist] = cost
m = float('inf')
dfs(0,0,0)
print(dp)
print(m)
print(time.time() - start)