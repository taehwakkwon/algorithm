import sys
sys.stdin = open('input.txt')

def check_palindrome(string):
    left = -1
    right = len(string)
    cnt = 0
    while left <= right:
        left += 1
        right -= 1
        if string[left] == string[right]:
            pass
        else:
            if string[left+1:right+1] == string[left+1:right+1][::-1]:
                return 1
            elif string[left:right] == string[left:right][::-1]:
                return 1
            else:
                return 2
    else:
        return 0

n = int(input())
for i in range(n):
    print(check_palindrome(input()))

import sys
sys.setrecursionlimit(숫자)