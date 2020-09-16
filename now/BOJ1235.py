import sys
sys.stdin = open('input.txt')

n = int(input())
numbers = [input() for _ in range(n)]
M = len(numbers[0])
for i in range(1, M+1):
    group = set([])
    for num in numbers:
        group.add(num[-i:])
    if len(group) == n:
        print(i)
        break
