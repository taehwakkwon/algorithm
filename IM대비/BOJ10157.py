import sys
sys.stdin = open('input.txt')




def solution2():
    total = c*r
    if k == 1:
        return (1,1)
    elif k > c*r:
        return (0,)
    else:
        concert = [[0]*c for _ in range(r)]
        cnt = 1
        y, x = r - 1, 0
        concert[y][x] = cnt #이놈때문에 if k == 1 조건 필요합니다ㅠ
        while total - cnt > 0:
            for dy, dx in [(-1,0), (0, 1), (1, 0), (0,-1)]:
                while 0 <= y + dy < r and 0 <= x + dx < c and concert[y+dy][x+dx] == 0:
                    cnt += 1
                    concert[y + dy][x + dx] = cnt
                    y += dy
                    x += dx
                    if cnt == k:
                        return (x + 1,  r - y)


def solution():
    c, r = map(int, input().split())
    k = int(input())
    total = c * r
    if k == 1:
        return (1,1)
    elif k > total:
        return 0,
    elif k > 0:
        i = 1
        while 2*i*(c+r-2*i) + 1 <= k:
            i += 1
        cnt = 2*(i-1)*(c+r-2*(i-1)) + 1
        y, x = i, i
        if cnt == k:
            return (x,y)
        while cnt != k:
            if k - cnt > r - 2*i + 1:
                y += r - 2*i + 1
                cnt += r - 2*i + 1
            else:
                return (x, y + k - cnt)

            if k - cnt > c - 2*i + 1:
                x += c - 2*i + 1
                cnt += c - 2*i + 1
            else:
                return (x + k - cnt, y)

            if k - cnt > r - 2*i + 1:
                y -= (r - 2*i) + 1
                cnt += r - 2*i + 1
            else:
                return (x, y - (k - cnt))

            if k - cnt > c - 2*i + 1:
                x -= (c - 2*i) + 1
                cnt += c - 2*i + 1
            else:
                return (x - (k - cnt), y)


print(*solution())
