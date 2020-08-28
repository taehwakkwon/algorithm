# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    parentheses = {'(':')',')':'(','{':'}','}':'{','[':']',']':'['}
    stack = []
    for string in input():
        if stack and parentheses[stack[-1]] == string:
            stack.pop()
        elif string in parentheses:
            stack.append(string)
    if stack:
        print('#%d %d' %(tc, 0))
    else:
        print('#%d %d' % (tc, 1))
