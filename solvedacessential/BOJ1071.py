import sys
sys.setrecursionlimit(10**6)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: return factorial(n-1)*n

n,r = map(int,input().split())
print(factorial(n)//(factorial(r)*factorial(n-r)))