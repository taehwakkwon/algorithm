import sys
sys.stdin = open('input.txt')

n = int(input())
now = [500,500]
road = []

x = set([])
y = set([])
d = []
for i in range(6):
    a, b = map(int,input().split())
    d.append(a)
    #동서남북
    if a == 1:
        now[1] += b
    elif a == 2:
        now[1] -= b
    elif a == 3:
        now[0] += b
    else:
        now[0] -= b
    y.add(now[0])
    x.add(now[1])


    road.append(tuple(now[:]))
big_rect = (max(y)-min(y))*(max(x)-min(x))
points = [(max(y),min(x)),(max(y),max(x)),(min(y),min(x)),(min(y),max(x))]
small = list((set(road) - set(points)))
small.extend(list(set(points)-set(road)))
x = y = 0
for i in range(1,4):
    x = max(x, abs(small[i-1][0] - small[i][0]))
    y = max(y, abs(small[i - 1][1] - small[i][1]))
print((big_rect-x*y)*n)
#
# points = [(a,b),(c,a),(c,d),(a,d)]
# big_rect = (c-a)*(d-b)
# diff = set(road)-set(points)
# y = set([])
# x = set([])
# for r, c in diff:
#     y.add(r)
#     x.add(c)
# y = list(y)
# x = list(x)
# print(n*(big_rect - abs(y[0]-y[1])*abs(x[0]-x[1])))