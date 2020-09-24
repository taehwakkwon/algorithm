import sys
sys.stdin = open('input.txt')


import sys

def solution():
    c, r = map(int, input().split())
    k = int(input())
    total = c * r
    if k == 1:
        return (1,1)
    elif k > total:
        return 0,
    else:
        i = 1
        while 2*i*(c+r-2*i) + 1 < k:
            i += 1
        cnt = 2*(i-1)*(c+r-2*(i-1)) + 1
        y, x = i, i
        if cnt == k:
            return (x,y)
        while cnt != k:
            if k - cnt > r - 2*i:
                y += r - 2*i
                cnt += r - 2*i
            else:
                return (x, y + k - cnt)

            if k - cnt > c - 2*i:
                x += c - 2*i
                cnt += c - 2*i
            else:
                return (x + k - cnt, y)

            if k - cnt > r - 2*i:
                y -= (r - 2*i)
                cnt += r - 2*i
            else:
                return (x, y - (k - cnt))

            if k - cnt > c - 2*i:
                x -= (c - 2*i)
                cnt += c - 2*i
            else:
                return (x - (k - cnt), y)

print(*solution())