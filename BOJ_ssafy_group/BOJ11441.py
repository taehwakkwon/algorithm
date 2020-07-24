import sys
sys.stdin = open('input.txt','r')

import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = [0,a[0]]
for i in range(1,N):
    b.append(b[i]+a[i])
m = int(sys.stdin.readline())
sections = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
for x,y in sections:
    print(b[y]-b[x-1])


