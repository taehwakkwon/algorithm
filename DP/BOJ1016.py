def prime(m, n):
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
        seive[num::pp] = [False]*(M//pp - (m-1)//pp)
        # while num < length:
        #     seive[num] = False
        #     num = num + pp
    return seive.count(True)

m, M = map(int, input().split())
print(prime(m,M))
