import sys
sys.stdin = open('자리배정.txt')


import sys
c, r = map(int, input().split())
k = int(input())
total = c*r

if k == 1:
    print(1, 1)
elif k > c*r:
    print(0)
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
                    print(x + 1,  r - y)
                    sys.exit() #파이썬 프로그램 종료하는 함수입니다.





#위, 오른쪽, 아래, 왼쪽