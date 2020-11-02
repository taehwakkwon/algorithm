import sys
sys.stdin = open('input.txt')

def merge_sort(m):
    if len(m) <= 1:
        return m
    mid = len(m)//2
    left = merge_sort(m[:mid])
    right = merge_sort(m[mid:])
    return merge(left, right, m)


def merge(left, right, m):
    global cnt
    i = j = k = 0
    if left[len(left) - 1] > right[len(right) - 1]:
        cnt += 1

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            m[k] = left[i]
            i += 1
        else:
            m[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        m[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        m[k] = right[j]
        j += 1
        k += 1
    return m

T = int(input())
for t in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    merge_sort(numbers)
    print('#%d %d %d' %(t, numbers[n//2] ,cnt))