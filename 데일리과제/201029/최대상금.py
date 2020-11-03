import sys
sys.stdin = open('input.txt')

from itertools import combinations, permutations
def selection_sort():
    global swap
    for i in range(n-1):
        min_idx = i
        for j in range(i, n):
            if numbers[i] < numbers[j]:
                min_idx = j
        if min_idx != i:
            numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx]
            swap -= 1


T = int(input())
for t in range(1, T+1):
    numbers, swap = input().split()
    numbers = list(map(int, list(numbers)))
    swap = int(swap)
    n = len(numbers)

    res = 0
    if swap < n-1:
        permu = list(permutations(list(combinations(range(n), 2)), swap))
        for per in permu:
            tmp = numbers[:]
            for i, j in per:
                tmp[i], tmp[j] = tmp[j], tmp[i]
            res = max(res,int(''.join(map(str,tmp))))
    else:
        selection_sort()
        swap %= 2
        permu = list(permutations(list(combinations(range(n), 2)), swap))
        for per in permu:
            tmp = numbers[:]
            for i, j in per:
                tmp[i], tmp[j] = tmp[j], tmp[i]
            res = max(res, int(''.join(map(str, tmp))))
    print('#%d %d' %(t,res))
