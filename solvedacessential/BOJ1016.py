import sys
sys.stdin = open('input.txt')

import math
if __name__ == "__main__":
    m, M = map(int, input().split())
    numbers = [False]*(M - m + 1)
    for i in range(2,math.ceil(math.sqrt(M))+1):
        for k in range(m//(i**2),math.ceil(M/(i**2))+1):
            if 0 <= i ** 2 * k - m <= M - m:
                numbers[i ** 2 * k - m] = True
    print(numbers.count(False))




#1, 2, 3, 5, 6, 7, 10
