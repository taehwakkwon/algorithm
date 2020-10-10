import sys
sys.stdin = open('../now/input.txt')

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
from collections import deque
def body(r,c,flag):
    if flag:
        snake.append((r,c))
    else:
        snake.popleft()
        snake.append((r,c))


def move(r,c,direc, time):
    global M
    if time in dic:
        if dic[time] == 'L':
            if direc == [0,1] or direc == [0,-1]:
                direc[0], direc[1] = -direc[1], -direc[0]
            else:
                direc[0], direc[1] = direc[1], direc[0]
        else:
            if direc == [0, 1] or direc == [0, -1]:
                direc[0], direc[1] = direc[1], direc[0]
            else:
                direc[0], direc[1] = -direc[1], -direc[0]

    if 0 <= r + direc[0] < n and 0 <= c + direc[1] < n:
        r += direc[0]
        c += direc[1]
        if (r,c) in snake:
            M = max(M, time)
            return
        if apple.get((r,c),False) == True:
            body(r,c,True)
            apple[(r,c)] = False
        else:
            body(r,c,False)
    else:
        M = max(M, time)
        return
    move(r,c,direc,time + 1)


n = int(input())
k = int(input())
apple = {}
for i in range(k):
    a, b = map(int, input().split())
    apple[(a-1,b-1)] = True

l = int(input())
dic = dict()
for i in range(l):
    a, b = input().split()
    dic[int(a)] = b

M = 0
snake = deque([(0,0)])
direc = [0,1]
move(0,0,direc,0)
print(M+1)