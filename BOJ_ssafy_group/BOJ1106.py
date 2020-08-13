import sys
sys.stdin = open('input.txt')

MAX = 1000*100+1

c, n = map(int,input().split())
dp = [0]*(MAX+1)
for i in range(n):
    cost, tourist = map(int, input().split())
    dp[tourist] = cost

for i in range(c):
    if dp[i]:
        for j in range(i, c):
            if dp[j] and i + j <= MAX:
                if dp[j + i] == 0:
                    dp[j + i] = dp[j] + dp[i]
                else:
                    dp[j + i] = min(dp[j + i], dp[j] + dp[i])
m = (MAX+1)
for i in range(c,MAX+1):
    if dp[i] == 0:
        continue
    if m > dp[i]:
        m = dp[i]
print(m)