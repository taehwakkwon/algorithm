import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
n = int(input())
y = [0]
x = [0]
for i in range(n):
    #0 가로, 1 세로
    a, b = map(int, input().split())
    if a == 0:
        x.append(b)
    else:
        y.append(b)
x.append(h)
y.append(w)
x.sort()
y.sort()
res = []
for i in range(len(y)-1):
    for j in range(len(x)-1):
        res.append((y[i+1]-y[i])*(x[j+1]-x[j]))
print(max(res))
