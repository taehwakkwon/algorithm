import sys
sys.stdin = open('input.txt')

import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    number = int(input())
    if number:
        heapq.heappush(heap,-number)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
