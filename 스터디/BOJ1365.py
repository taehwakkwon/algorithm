import sys

sys.stdin = open('input.txt')
from collections import defaultdict

'''
n = int(input())
numbers = list(map(int, input().split()))

dp = [1]*(n+1)
for i in range(1,n):
    M = 0
    m = 0
    for j in range(i-1,-1,-1):
        if numbers[i] > numbers[j]:
            if dp[j] > M:
                M = dp[j]

print(n - max(dp))
'''


def binarysearch(left, right, num):
    while left <= right:
        mid = (left + right) // 2
        if li[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return left


from bisect import bisect_left

n = int(input())
numbers = list(map(int, input().split()))
li = [numbers[0]]

for i in range(1, n):
    if li[-1] <= numbers[i]:
        li.append(numbers[i])
    else:
        li[bisect_left(li, numbers[i])] = numbers[i]
print(n - len(li))
