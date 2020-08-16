import sys
<<<<<<< HEAD
import math
sys.stdin = open('input.txt','r')
=======
sys.stdin = open('input.txt','r')
import time
def count_cut(h):
    cnt = 0
    i = 0
    while n > i and trees[i] > h:
        cnt += trees[i] - h
        i += 1
    return cnt

def binary_search(target):
    start = 0
    end = trees[0]
    while start <= end:
        mid = (start + end) // 2
        count = count_cut(mid)
        if count == target:
            return mid
        elif count > target:
            start = mid + 1
        else:
            end = mid - 1
    if count > m:
        for i in range(mid+1,trees[0]+1):
            count = count_cut(i)
            if count == m:
                return i
            if count < m:
                return i - 1
        else:
            return trees[0]
    else:
        for i in range(mid-1, -1, -1):
            count = count_cut(i)
            if count == m:
                return i
            if count > m:
                return i
        else:
            return 0

>>>>>>> 33da9fd9c7f6f90040c922ff00c3fbb487d2d25d

if __name__ == "__main__":
    n, m = map(int, input().split())
    trees = sorted(list(map(int, input().split())), reverse = True)
<<<<<<< HEAD
    right = len(trees) - 1
    mid = right // 2
    h = trees[mid]
    cut = 0
    history = []
    while True:
        for i in range(mid):
            cut += (trees[i] - h)
            if cut < m:
                right = mid
                mid = right // 2
                break
        else:
            mid += mid // 2
            right = mid * 2
        if mid in history:
            print(trees[mid])
            break
        history.append(mid)
=======
    print(binary_search(m))
>>>>>>> 33da9fd9c7f6f90040c922ff00c3fbb487d2d25d
