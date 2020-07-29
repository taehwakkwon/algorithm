import sys
sys.stdin = open('input.txt','r')

import sys
input = sys.stdin.readline
n = int(input())
numbers = [int(input()) for _ in range(n)]
stack = []
result = []
res = []
idx = 0
for i in range(1,max(numbers)+1):
    if numbers[idx] >= i:
        stack.append(i)
        res.append('+')

    while stack and stack[-1] == numbers[idx]:
        left = stack.pop()
        result.append(left)
        res.append('-')
        idx += 1
if result == numbers:
    for r in res:
        print(r)
else:
    print('NO')