import sys
sys.stdin = open('input.txt')

n = int(input())
numbers = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*i for i in range(1,n+1)]

dp[-1] = numbers[-1][:]
for i in range(n-2,-1,-1):
    for j in range(i+1):
        dp[i][j] = max(dp[i][j], dp[i+1][j] + numbers[i][j], dp[i+1][j+1] + numbers[i][j])
print(dp[0][0])