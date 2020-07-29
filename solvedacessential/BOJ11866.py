import sys
sys.stdin = open('input.txt','r')

import sys
input = sys.stdin.readline
from collections import deque


n,k = map(int, input().split())
numbers = deque(list(range(1,n+1)))
res = []
while numbers:
    numbers.rotate(-(k-1))
    left = numbers.popleft()
    res.append(left)
print('<%s>' %str(res)[1:-1])