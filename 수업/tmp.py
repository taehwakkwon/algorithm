import sys
import time
#sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**7)

def fibo_1(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fibo_1(n-1) + fibo_1(n-2)

def fibo_2(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if fib[n]:
        return fib[n]
    fib[n] = fibo_2(n-1) + fibo_2(n-2)
    return fib[n]

if __name__ == "__main__":
    start = time.time()
    n = 10
    print(fibo_1(n))
    print('피보나치재귀',time.time()-start)
    start = time.time()
    n = 1000
    fib = [0]*(n+1)
    print(fibo_2(n))
    print('피보나치재귀 메모리제이션', time.time() - start)

'''
T = int(input())
cnt = 0
def total_num(k, n):
    global cnt
    cnt += 1
    if n == 0:
        return 0
    if result[k][n]:
        return result[k][n]
    else:
        result[k][n] = total_num(k-1, n) + total_num(k, n-1)
        return result[k][n]

for test_case in range(1,T+1):
    k = int(input())
    n = int(input())
    result = [[0]*(n+1) for i in range(k+1)]
    result[0] = list(range(n+1))

    print(total_num(k, n))
    print(time.time() - start)
    print(cnt)




start = time.time()

T = int(input())
cnt = 0
def total_num(k, n):
    global cnt
    if k==0:
        cnt += 1
        return n
    else:
        result = 0
        for i in range(1,n+1):
            cnt += 1
            result += total_num(k-1, i)
        return result

for test_case in range(1,T+1):
    k = int(input())
    n = int(input())

    print(total_num(k, n))
    print(time.time() - start)
    print(cnt)
'''