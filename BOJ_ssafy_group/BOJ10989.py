import sys

sys.stdin = open('input.txt')
from sys import stdin, stdout

n = int(stdin.readline().rstrip())
numbers = [0]*10001
for i in range(n):
    numbers[int(stdin.readline().rstrip())] += 1


for i in range(10001):
    if numbers[i]:
        stdout.write(('%d\n' %i)*numbers[i])