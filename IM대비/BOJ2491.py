import sys
sys.stdin = open('input.txt')

M = 0
n = int(input())
numbers = list(map(int, input().split()))
dp_up = [1]*n
dp_dowm = [1]*n

for i in range(1, n):
    if numbers[i-1] <= numbers[i]:
        dp_up[i] = max(dp_up[i] + 1, dp_up[i-1] + 1)
    if numbers[i-1] >= numbers[i]:
        dp_dowm[i] = max(dp_dowm[i] + 1, dp_dowm[i-1]+1)
print(max(max(dp_up),max(dp_dowm)))
