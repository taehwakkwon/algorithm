MAX = 1000*100+1
c, n = map(int,input().split())
dp = [0]*(MAX+1)
for i in range(n):
    cost, tourist = map(int, input().split())
    for j in range(cost, MAX):
        dp[j] = max(dp[j], dp[j - cost] + tourist)

for i in range(1, MAX+1):
    if dp[i] >= c:
        print(i)
        break