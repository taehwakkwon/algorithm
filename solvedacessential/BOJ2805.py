import sys
import math
sys.stdin = open('input.txt','r')

if __name__ == "__main__":
    n, m = map(int, input().split())
    trees = sorted(list(map(int, input().split())), reverse = True)
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
