import sys
sys.stdin = open('../now/input.txt')
import time
start = time.time()

r1,c1,r2,c2 = map(int, input().split())
dic = {}
m = min(abs(r1),abs(r2),abs(c1),abs(c2))
M = max(abs(r1),abs(r2),abs(c1),abs(c2))
start = []
for r in range(r1,r2+1):
    for c in range(c1,c2+1):
        dic[(r,c)] = 0
        start.append(max(abs(r),abs(c)))
start = list(set(start))

for i in start:
    num = (2*i+1)**2
    if (i,i) in dic:
        dic[(i,i)] = num
    r = c = i
    for dr, dc in [(0,-1),(-1,0),(0,1),(1,0)]:
        for q in range(2*i):
            r += dr
            c += dc
            num -= 1
            if r1 <= r <= r2 and c1 <= c <= c2 and dic[(r,c)] == 0:
                dic[(r,c)] = num


l = len(str(max(dic.values())))
for r in range(r1,r2+1):
    for c in range(c1,c2+1):
        print(' '* (l - len(str(dic[(r, c)]))), dic[(r, c)],sep='', end=' ')
    print()

print(time.time()-start)