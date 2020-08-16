import sys
sys.stdin = open('input.txt')
def prime(numbers):
    for i in range(2,int(M**0.5)+1):
        if numbers[i] == 0:
            for j in range(i+i,M+1,i):
                numbers[j] = 1
    return numbers



T = int(input())
nums = [int(input()) for _ in range(T)]
M = 10000
numbers = [0]*(M+1)
prime_numbers = prime(numbers)
prime_numbers[:2] = [1,1]
for num in nums:
    left = num//2
    right = num - left
    while left <= right:
        if prime_numbers[left] == 0 and prime_numbers[num-left] == 0:
            print(*(left,right))
            break
        left -= 1
        right = num - left

