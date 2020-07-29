import sys
sys.stdin = open('input.txt','r')

import sys
from collections import deque

input = sys.stdin.readline

def queue_fuc(order,n = 0):
    if order == 'push':
        queue.append(n)
    if order == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
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
            queue_fuc(inputs[0],int(inputs[1]))
        else:
            queue_fuc(inputs[0])
