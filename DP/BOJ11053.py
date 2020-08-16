n = int(input())
numbers = list(map(int, input().split()))
dp = [1]*(n+1)
for i in range(1,n):
    M = 0
    for j in range(i-1,-1,-1):
        if numbers[i] > numbers[j]:
            if dp[j] > M:
                M = dp[j]
        dp[i] = M + 1
print(max(dp))