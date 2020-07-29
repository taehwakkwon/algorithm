import sys
sys.stdin = open('input.txt','r')

import sys
from collections import deque

input = sys.stdin.readline

def deque_fuc(order,n = 0):
    if order == 'push_front':
        queue.appendleft(n)

    if order == 'push_back':
        queue.append(n)
    if order == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    if order == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
            queue.pop()
    if order == 'size':
        print(len(queue))
    if order == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    if order == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)


if __name__ == "__main__":
    t = int(input())
    queue = deque([])
    for i in range(t):
        inputs = input().split()
        if len(inputs) > 1:
            deque_fuc(inputs[0],int(inputs[1]))
        else:
            deque_fuc(inputs[0])
