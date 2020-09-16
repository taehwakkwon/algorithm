import sys
sys.stdin = open('input.txt')

import time
start = time.time()
def cal(r,c,s):
    global cnt
    total = 0
    for idx , val in enumerate(sub_tr[:s+1]): #높이
        total += (triangle[r + idx][c + val - 1] - triangle[r+idx][c - 1])
    return total

t = 0
while True:
    t += 1
    inputs = list(map(int, input().split()))
    if inputs == [0]:
        break
    line = inputs[0]
    n = len(inputs[1:])

    sub_tr = list(range(1,2*line-1,2))

    triangle = []
    inputs = inputs[1:]
    M = max(inputs + [sum(inputs)])
    i = 1
    while i**2 <= n:
        triangle.append([0] + inputs[(i-1)**2:i**2])
        i += 1
    for i in range(line):
        for j in range(1,len(triangle[i])):
            triangle[i][j] += triangle[i][j-1]
    for k in range(1, len(sub_tr)):
        for i in range(len(triangle)-k):
            for j in range(len(triangle[i])):
                if j > 0 and j % 2 == 1:
                    M = max(M,cal(i,j,k))
    print('%d. %d' %(t, M))
    print(time.time()-start)
