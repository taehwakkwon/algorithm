import sys
sys.stdin = open('input.txt')

n = int(input())
now = [500,500]
road = []

min_x, min_y = 1000,1000
max_x, max_y = 0, 0

for i in range(n-1):
    a, b = map(int,input().split())
    #동서남북
    if a == 1:
        now[1] += b
    elif a == 2:
        now[1] -= b
    elif a == 3:
        now[0] += b
    else:
        now[0] -= b
    min_y = min(now[0], min_y)
    min_x = min(now[1], min_x)
    max_y = max(now[0], max_y)
    max_x = max(now[1], max_x)

    road.append(tuple(now[:]))


square = [max_y, min_y, max_x, min_x]
points = [(max_y,max_x), (max_y,min_x),(min_y,max_x),(min_y,min_x)]
big = 1
for i in range(0,4,2):
    big*=(square[i]-square[i+1])

for i in range(len(road)-1,-1,-1):
    if road[i] in points:
        road.pop(i)

dic = {}
for i in range(len(road)):
    for j in range(2):
        dic[road[i][j]] = dic.get(road[i][j], 0) + 1

rest = []
for key, value in dic.items():
    if value == 1:
        rest.append(key)
for i in range(len(road)):
    if road[i][0] == rest[0]:
        break
else:
    road.append((rest[1], rest[0]))

min_x, min_y = 1000,1000
max_x, max_y = 0, 0
for y, x in road:
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)
print((big - (max_y-min_y)*(max_x-min_x))*n)

