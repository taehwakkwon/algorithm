#import sys
#sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T + 1):
    strings = input()
    stack = []
    for i in range(len(strings)):
        if not stack or stack[-1] != strings[i]:
            stack.append(strings[i])
        elif stack and stack[-1] == strings[i]:
            stack.pop()

    print('#%d %d' %(tc, len(stack)))

