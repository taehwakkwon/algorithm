import sys
sys.stdin = open('input.txt')
n = int(input())
numbers = list(map(int, input().split()))
ch = [0]*n
dp = numbers[:]
for i in range(n):
    M = 0
    for j in range(i-1,-1,-1):
        if numbers[i] > numbers[j] and dp[i] > dp[j]:
            M = numbers[j]
        dp[i] += M
        print(dp)
print(dp)