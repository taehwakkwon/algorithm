import sys
sys.stdin = open('input.txt')


def solution(n):
    tri = ''
    while n:
        tri += str(n % 3)
        n //= 3
    return tri


print(solution(45))