import sys
sys.stdin = open('input.txt')

MAX = 3000
c, n = map(int,input().split())
dp = [0]*(MAX+1)
for i in range(n):
    cost, tourist = map(int, input().split())
    dp[cost] = tourist

for i in range(MAX):
    if dp[i]:
        for j in range(MAX):
            if i + j <= MAX and dp[j] > 0:
                dp[j + i] = max(dp[j + i], dp[j] + dp[i])
print(sum(dp[:1000]))
#7500500
for i in range(MAX+1):
    if dp[i] == 0:
        continue
    if dp[i] >= c:
        print(i)
        break