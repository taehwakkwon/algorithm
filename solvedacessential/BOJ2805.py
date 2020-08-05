import sys
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


if __name__ == "__main__":
    n, m = map(int, input().split())
    trees = sorted(list(map(int, input().split())), reverse = True)
    print(binary_search(m))