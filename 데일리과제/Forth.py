import sys
sys.stdin = open('sample_input.txt')


operator = ['*', '/', '+', '-']
T = int(input())
for t in range(1, T + 1):
    equ = list(input().split())
    if equ:
        equ.pop()
    stack = []
    for i in range(len(equ)):
        if equ[i].isdecimal():
            stack.append(equ[i])
        else:
            if len(stack) > 1:
                a, b = int(stack.pop()), int(stack.pop())
                if equ[i] == '*':
                    stack.append(b*a)
                elif equ[i] == '/':
                    if a == 0:
                        print('#%d error' % t)
                        break
                    stack.append(b/a)
                elif equ[i] == '+':
                    stack.append(b + a)
                else:
                    stack.append(b - a)
            else:
                print('#%d error' %t)
                break
    else:
        if len(stack) > 1:
            print('#%d error' % t)
        else:
            print('#%d %d' %(t, stack[0]))
