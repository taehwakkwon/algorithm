import sys
sys.stdin = open('input.txt')
def solve(n):
    if n <= 10:
        return numbers[n]
    if numbers[n] != 0:
        return numbers[n]
    numbers[n] = solve(n-1) + solve(n-5)
    return numbers[n]

numbers = [0,1,1,1,2,2,3,4,5,7,9] + [0]*10000
T = int(input())
for t in range(T):
    print(solve(int(input())))
