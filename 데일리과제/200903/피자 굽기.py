#import sys
#sys.stdin = open('input.txt')

from collections import deque
def solve():
    cnt = 0
    while True:
        for i in range(n):
            if oven[i] == 0 and cheese:
                cnt += 1
                oven[i] = cheese.popleft()
                check[i] = cnt
            else:
                oven[i] //= 2
                if oven[i] == 0 and cheese:
                    cnt += 1
                    oven[i] = cheese.popleft()
                    check[i] = cnt
                if not cheese and [True if i == 0 else False for i in oven].count(True) == n - 1:
                    return check[[True if i == 0 else False for i in oven].index(False)]

T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    cheese = deque(list(map(int, input().split())))
    oven = [0]*n
    check = [0]*n
    print('#%d' %t, solve())