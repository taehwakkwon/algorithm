import sys
sys.stdin = open('input.txt')

def check_palindrome(string):
    left = 0
    N = len(string)
    right = N - 1
    cnt = 0
    while left <= right:
        if cnt > 1:
            return cnt
        if string[left] == string[right]:
            pass
        else:
            if string[left+1] == string[right]:
                string.pop(left)
            elif string[left] == string[right-1]:
                string.pop(right)
            else:
                string.pop(0)
                string.pop()
        left += 1
        right -= 1
    if N - len(string) > 1:
        return 2
    else:
        return N - len(string)

n = int(input())
for i in range(n):
    print(check_palindrome(list(input())))











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