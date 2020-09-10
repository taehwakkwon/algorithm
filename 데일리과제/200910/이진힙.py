import sys
sys.stdin = open('input.txt')

def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount
    parent = cur//2
    while parent and heap[cur] < heap[parent]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur//2

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    li = list(map(int, input().split()))
    heapcount = 0
    sum = 0
    heap = [0]*(n+1)
    for i in range(n):
        heappush(li[i])

    while n:
        n //= 2
        sum += heap[n]
    print('#%d %d' %(t, sum))
    print(heap)
#[11, 14, 18, 40, 57, 45, 63, 52]
'''
[2, 3, 5, 7, 4, 6]
[1, 3, 4, 16, 23, 12]
[0, 11, 14, 18, 40, 52, 45, 63, 57]


'''

