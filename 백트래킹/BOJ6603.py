import sys
sys.stdin = open('input.txt')


import sys
def solve(v, s):
    if v == 6:
        print(*res)
        return
    else:
        for i in range(s, n):
            res[v] = numbers[i]
            solve(v + 1, i + 1)


while True:
    numbers = list(map(int, sys.stdin.readline().split()))
    if numbers == [0]:
        break
    k = numbers.pop(0)
    numbers.sort()
    n = len(numbers)
    res = [0]*6
    solve(0, 0)
    print()
