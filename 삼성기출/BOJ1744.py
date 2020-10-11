import sys
sys.stdin = open('../now/input.txt')
n = int(input())
numbers = sorted([int(input()) for _ in range(n)])
idx = 0
ans = 0
while idx < n and numbers[idx] <= 0:
    if idx + 1 < n and numbers[idx] * numbers[idx + 1] >= numbers[idx] + numbers[idx + 1]:
        ans += (numbers[idx] * numbers[idx + 1])
        idx += 1
    else:
        ans += numbers[idx]
    idx += 1
jdx = n - 1

while jdx >= idx:
    if jdx > idx and numbers[jdx] * numbers[jdx - 1] >= numbers[jdx] + numbers[jdx - 1]:
        ans += (numbers[jdx] * numbers[jdx - 1])
        jdx -= 1
    else:
        ans += numbers[jdx]
    jdx -= 1

print(ans)