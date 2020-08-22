import sys
sys.stdin = open('input.txt')
def fibo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b % 1000000000, (a + b) % 1000000000
    return a

print(fibo(int(input())))

#