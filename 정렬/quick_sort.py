
def quickSort(array, begin, end):
    if begin < end:
        p = partition(array, begin, end)
        quickSort(array, begin, p - 1)
        quickSort(array, p + 1, end)

def partition(array, left, right):
    pivot = (left + right) // 2
    L = left
    R = right
    while L < R:
        while L < R and array[L] < array[pivot]:
            L += 1
        while L < R and array[R] >= array[pivot]:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
                array[L], array[R]  = array[R], array[L]
    array[pivot], array[R] = array[R], array[pivot]
    return R
