<<<<<<< HEAD
=======
import sys
sys.stdin = open('input.txt')

import sys
n, k = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [0]
cnt = 0
dic = {}
for i in range(n):
    dp.append(dp[-1] + numbers[i])
    dic[dp[-1]] = dic.get(dp[-1],0) + 1

for i in range(1, n+1):
    diff = dp[i] - k
    cnt += dic.get(diff, 0)
    dic[diff] = 0
print(cnt)
'''
psum[i] - psum[j] = k
psum[j] = psum[i] - k
'''
>>>>>>> 096be07168d3d9712c23a9a06f99d001e4ccf667
