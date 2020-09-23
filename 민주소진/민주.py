import sys
sys.stdin = open('input.txt')

n = int(input())
num = list(map(int, input().split()))
cnt = 1
max = 0
for i in range(1, n):
    if num[i-1] <= num[i]:
        cnt += 1
    else:
        cnt = 1
    if max < cnt:
        max = cnt
cnt = 1
for i in range(1, n):
    if num[i-1] >= num[i]:
        cnt += 1
    else:
        cnt = 1
    if max < cnt :
        max = cnt
print(max)