import sys
sys.stdin = open('input.txt')

import sys
def solve(a, b):
    if (a, b) == (0,0):
        sys.exit()
    cnt = 0
    flag = False
    n1, n2 = 1, 1
    while n1 <= b:
        if n1 >= a:
            flag = True
        if flag:
            cnt += 1
        n1, n2 = n1 + n2, n1
    print(cnt)


while True:
    a, b = map(int, input().split())
    solve(a, b)
