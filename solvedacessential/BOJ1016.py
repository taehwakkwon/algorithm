import time
start = time.time()  # 시작 시간 저장

import sys
sys.stdin = open('input.txt')

import math
if __name__ == "__main__":
    m, M = map(int, input().split())
    numbers = [False]*(M - m + 1)
    for i in range(2, int(math.sqrt(M))+1):
        for k in range(math.ceil(m / (i**2)), M//(i**2)+1):
            numbers[i ** 2 * k - m] = True
    print(numbers.count(False))
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간


'''
#더 빠른 방법법
def prme(m, n):
    nn = int(n**0.5)
    prime_numbers = [True] * (nn+1)
    for i in range(2, int(nn**0.5) + 1):
        if prime_numbers[i] == True:
            for j in range(i + i,nn + 1, i):
                prime_numbers[j] = False
    prime_pow = []

    for i in range(2, nn+1):
        if prime_numbers[i] == True:
            prime_pow.append(i**2)

    length = n - m + 1
    cnt = 0
    seive = [True] * length
    for pp in prime_pow:
        r = m % pp
        if r == 0:
            num = 0
        else:
            num = (pp-r)
        while num < length:
            seive[num] = False
            num = num + pp
    return seive.count(True)

m, M = map(int, input().split())
print(prime(m,M))

'''