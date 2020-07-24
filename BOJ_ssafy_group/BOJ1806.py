import sys
sys.stdin = open('input.txt','r')

import sys
from collections import deque
input = sys.stdin.readline
N,S = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.append(0)
queue = deque([])
sum = 0
m = float('inf')
for number in numbers:
    if sum == S and m > len(queue):
        m = len(queue)
    if sum > S:
        left = queue.popleft()
        sum -= left
    else:
        queue.append(number)
        sum += number

if sum == S:
    print(m)
elif sum - queue[0] == S:
    queue.popleft()
    print(len(queue))
else:
    print(0)
print(queue)