import sys
sys.stdin = open('input.txt','r')

n = int(input())
numbers = list(map(int, input().split()))
dp = [1]*(n+1)
for i in range(1,n):
    M = 0
    for j in range(i-1,-1,-1):
        if numbers[i] < numbers[j]:
            if dp[j] > M:
                M = dp[j]
        dp[i] = max(dp[:i])
print(max(dp))

n = int(input())
numbers = list(map(int, input().split()))
dp = [1] * n
check = [0] * n
for i in range(n):
    M = 0
    for j in range(i+1, n):
        if numbers[i] > numbers[j]:
            dp[j] += 1
            check[i] = numbers[j]
        print(dp)
        print(check)

print(max(dp))