import sys
sys.stdin=open('input.txt')
import time
start = time.time()
n = int(input())
M = 0
infos = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda  x: x[1])
room = []
for p,q in infos:
    for i in range(len(room)):
        if room[i][0] >= q:
            room[i][0] = p
            break
        if room[i][1] <= p:
            room[i][1] = p
            break
    else:
        room.append([p,q])

print(len(room))
print(time.time()-start)