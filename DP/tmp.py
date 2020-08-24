import sys
def rest(number):
    if number < 0:
        return -(-number%1000000000)
    else:
        return number%1000000000


def fibo(n):
    if n >= 0:
        a, b = 0, 1
        for i in range(n):
            a, b = (a + b)%1000000000, a%1000000000
        return a
    if n < 0:
        a, b = 0, 1
        for i in range(-n):
            a, b = rest(b - a), rest(a)
        return a
res = fibo(int(input()))
if res < 0:
    print(-1)
    print(abs(res)%1000000000)
elif res == 0:
    print(0)
    print(0)
else:
    print(1)
    print(res)