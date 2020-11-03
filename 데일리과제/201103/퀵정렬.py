#
import sys
sys.stdin = open('input.txt')
def quick_sort(arr,left,right):
    if left < right:
        pivot = partition(arr, left, right)

        quick_sort(arr,left,pivot-1)

        quick_sort(arr, pivot+1, right)

def partition(arr, left, right):
    i = left
    j = right
    pivot = arr[left]

    while i <= j:
        while i <= j and arr[i] <= pivot: i += 1
        while arr[j] > pivot: j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j


T= int(input())
for t in range(1,T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers = qs(numbers)
    print('#%d %d' %(t, numbers[n//2]))

