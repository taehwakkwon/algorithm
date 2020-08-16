import sys
sys.setrecursionlimit(10**7)
def fibo(n):
    a,b = 0,1
    for _ in range(n):
        a, b = b%10000000, (a+b)%10000000
    return a

if __name__ == "__main__":
    n = int(input())
    print(fibo(n%(15*(10**2))))