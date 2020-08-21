import sys
sys.stdin = open('input.txt')
import sys
n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(k + 1 + max(coins))]
dp[0] = 1
for i in range(n):
    for j in range(k + 1):
        dp[j + coins[i]] += dp[j]
print(dp[k])


'''
import sys
def dfs(v, s, li):
    global cnt
    if li in res:
        return
    if s == k:
        cnt += 1
        res.append(li[:])
        return
    if v >= n or s > k:
        return
    else:
        for idx, i in enumerate(range(0, k + 1, coins[v])):
            dfs(v + 1, s + i,li+[coins[v]]*idx )

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
res = []
cnt = 0
dfs(0, 0, [])
print(cnt)
print(time.time()-start)
#0.004019021987915039


import sys
def dfs(v, s):
    global cnt
    if s == k:
        cnt += 1
        return
    if v >= n or s > k:
        return
    else:
        for i in range(0, k + 1, coins[v]):
            dfs(v + 1, s + i)

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
cnt = 0
dfs(0, 0)
print(cnt)
print(time.time()-start)

import sys
n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(k + 1 + max(coins))]
dp[0] = 1
for i in range(n):
    for j in range(k + 1):
        dp[j + coins[i]] += dp[j]
print(dp[k])
'''