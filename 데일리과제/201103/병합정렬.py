
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2

    left = merge_sort(arr[:mid])

    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    global cnt
    result = []
    i = j = 0
    if left[-1] > right[-1]:
        cnt += 1
    while i < len(left) or j < len(right):

        if i < len(left) and j < len(right):
            if left[i] < right[i]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif j < len(right):
            result.append(right[j])
            j+=1
        elif i < len(left):
            result.append(left[i])
            i += 1
    return result



T = int(input())
for t in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    numbers = merge_sort(numbers)
    print(numbers)
    print('#%d %d %d'%(t,numbers[n//2],cnt))
