# import sys
# sys.stdin = open('input.txt')
def binary(numbers):
    numbers = numbers[::-1]
    res = []
    idx = 0
    num = 0
    for i in range(len(numbers)):
        if idx == 7:
            res.append(num)
            idx = 0
            num = 0
        if numbers[i] == 1:
            num += 2**idx
        idx += 1
    else:
        res.append(num)
    return res[::-1]

numbers = list(map(int, input()))
print(*binary(numbers))