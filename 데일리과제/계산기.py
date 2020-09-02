import sys
sys.stdin = open('sample_input.txt')

isp = {'*':2, '/':2, '+':1, '-':1, '(':0}
icp = {'*':2, '/':2, '+':1, '-':1, '(':3}
#'(6+5*(2-8)/2)'

T = 10
for t in range(1, T + 1):
    n = len('(6+5*(2-8)/2)')# int(input())
    equ = '(6+5*(2-8)/2)'#list(input())
    res = ''
    stack = []
    for i in range(n):
        if equ[i].isdigit():
            res += equ[i]
        else:
            if equ[i] == ')':
                p = ' '
                while p != '(':
                    p = stack.pop()
                    if p != '(':
                        res += p
            elif stack == [] or icp[equ[i]] > isp[stack[-1]]:
                stack.append(equ[i])
            elif stack and icp[equ[i]] <= isp[stack[-1]]:
                while icp[equ[i]] <= isp[stack[-1]]:
                    res += stack.pop()
                stack.append(equ[i])
    else:
        while stack:
            p = stack.pop()
            if p != '(':
                res += p

    print(res)



