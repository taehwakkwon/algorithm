import sys
sys.stdin = open('input.txt','r')

import sys
palindrome = input()
n = len(palindrome)
if palindrome == palindrome[::-1]:
    print(n)

else:
    for i in range(n):
        if palindrome[i:] == palindrome[:i-1:-1]:
            print(i+n)
            break
    else:
        print(n*2)
