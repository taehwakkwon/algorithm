import sys
sys.stdin = open('input.txt')
def where(a,b):
    if a == 1:
        return (0, b)
    elif a == 2:
        return (h, b)
    elif a == 3:
        return (b, 0)
    else:
        return (b, w)


road = []

w, h = map(int, input().split())
for i in range(w):
    road.append((0,i))
for i in range(h):
    road.append((i,w))
for i in range(w,0,-1):
    road.append((h,i))
for i in range(h,0,-1):
    road.append((i,0))

n = int(input())
loc = []
for i in range(n):
    a, b = map(int, input().split())
    #a : 북, 남, 서, 동
    loc.append(tuple(where(a,b)))
y, x = tuple(map(int, input().split()))
idx = road.index(where(y,x))

s = 0
for r, c in loc:
    f = road.index((r,c))
    s += min(abs(f - idx), len(road) - abs(f-idx))
print(s)



