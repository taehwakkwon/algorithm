import sys
sys.stdin = open('input.txt')

n = int(input())
k = int(input())
for j in range(k):
    a, b = map(int, input().split())
    if a > (n+1) // 2:
        a = n + 1 - a
    if b > (n+1) // 2:
        b = n + 1 - b
    if b < a:
        a,b = b,a

    if b > 3*(a//3) + a % 3:
        print([1,2,3][a%3 - 1])
    else:
        print([1,2,3][b%3 - 1])

    # numbers = [1,2,3]*(a // 3) + [1,2,3][:a % 3]
    # if b > len(numbers):
    #     print(numbers[-1])
    # else:
    #     print(numbers[b - 1])