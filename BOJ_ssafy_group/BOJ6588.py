import sys
input = sys.stdin.readline

def prime(numbers):
    M = max(numbers)
    num_list = list(range(M))
    num_list[1] = 0
    for i in range(2,int(M**0.5)+1):
        if num_list[i]:
            for j in range(i*2,M,i):
                num_list[j] = 0
    return num_list



if __name__ == "__main__":
    numbers = []
    while True:
        n = int(input())
        if n == 0:
            break
        numbers.append(n)
    prime_numbers = prime(numbers)

    for num in numbers:
        m,M = 3,3

        for i in range(3,num//2+1,2):
            if prime_numbers[num-i] + prime_numbers[i] == num:
                if (num-2*i) >= (M-m):
                    m,M = i,num-i
            if num - 2*i < M - m:
                break

        print('%d = %d + %d' % (num,prime_numbers[m],prime_numbers[M]))