import sys
sys.stdin = open('input.txt')


n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
for i in range(1,len(a)):
    a[i] += a[i-1]
p1,p2 = 0,1
cnt = 0
while p2 <= n:
    if a[p2]-a[p1] < m:
        p2 += 1
    elif a[p2] - a[p1] == m:
        cnt += 1
        p2 += 1
    else:
        p1 += 1
print(cnt)