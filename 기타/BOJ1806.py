import sys
input = sys.stdin.readline
N, S = map(int, input().split())
numbers = list(map(int, input().split()))
sum = numbers[0]
m = sys.maxsize
left, right = 0, 0
while left <= right and right < N:
    if sum >= S:
        m = min(right-left,m)
        sum -= numbers[left]
        left += 1
    else:
        right += 1
        if right < N:
            sum += numbers[right]
if m == sys.maxsize:
    print(0)
else:
    print(m+1)