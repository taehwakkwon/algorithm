import sys
sys.stdin = open('input.txt')

import math
if __name__ == "__main__":
    m, M = map(int, input().split())
    numbers = [False]*(M - m + 1)
    n_list = []
    for i in range(2, int(M**0.5)+1):
        pp = i ** 2
        flag = True
        for p in n_list:
            if p % pp == 0:
                flag = False
        else:
            n_list.append(pp)

        if flag:
            for k in range(math.ceil(m / (i**2)), M//(i**2)+1):
                if numbers[pp * k - m] == True:
                    continue
                numbers[pp * k - m] = True

    print(numbers.count(False))