import sys
sys.stdin = open('input.txt')

import sys
n, k = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [0]*(n + 1)

for i in range(n):
    dp[i + 1] = dp[i] + numbers[i]

left = 0
right = 1
cnt = 0

while right < n:
    diff = dp[right] - dp[left]
    print(diff, right, left)
    if left == right:
        right += 1
    elif diff == k:
        cnt += 1
    elif diff < k:
        right += 1
    else:
        left += 1
print(cnt)
