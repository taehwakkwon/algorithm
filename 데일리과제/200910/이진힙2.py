import sys
sys.stdin = open('input.txt')
def heapify(v):
    global flag
    if v > n:
        return
    else:
        if v//2 > 0 and heap[v] < heap[v//2]:
            heap[v], heap[v//2] = heap[v//2], heap[v]
        heapify(v * 2)
        heapify(v * 2 + 1)


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    heap = [0] + list(map(int, input().split()))
    parent = 0
    flag = True
    for i in range(n):
        heapify(1)
    sum = 0
    while n:
        n //= 2
        sum += heap[n]
    print('#%d %d' %(t, sum))