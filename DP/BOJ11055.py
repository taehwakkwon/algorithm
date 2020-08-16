import sys
sys.stdin = open('input.txt')
n = int(input())
numbers = list(map(int, input().split()))
ch = [0]*n
dp = numbers[:]
for i in range(n):
    for j in range(i-1,-1,-1):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + numbers[i])
print(max(dp))