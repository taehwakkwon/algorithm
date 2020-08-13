import sys
sys.stdin = open('input.txt')

def func(a,b,c):
    print(a,b)
    if b == 0:
        return 1
    if b % 2:
        return (a*func(a,b-1,c))%c
    else:
        return (func(a,b//2,c) * func(a,b//2,c))%c

a, b, c = map(int, input().split())
print(func(a,b,c))


'''
sys.setrecursionlimit(10**7)
a, b, c = map(int, input().split())
res = 1
b = bin(b)[2:]
for i in range(len(b)):
    print(res,a)
    if b[i] == '1':
        res = (res*a)%c
        a *= a
    else:
        a *= a
print(res%c)
'''
'''
import sys

sys.setrecursionlimit(10**7)
cnt = 0
def divncon(a,b,c):
    global cnt
    cnt += 1
    if b == 0:
        return 1
    if b % 2 == 0:
        if numbers[b]:
            return numbers[b]
        else:

        return (divncon(a,b//2,c)%c)*(divncon(a,b//2,c)%c)
    else:
        return a * divncon(a,b - 1,c)


a, b, c = map(int, input().split())
numbers = [0]*(b+1)
print(divncon(a,b,c)%12)
print(cnt)
'''