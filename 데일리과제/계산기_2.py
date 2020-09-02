import sys
#sys.stdin = open('sample_input.txt')

isp = {'*':2, '/':2, '+':1, '-':1, '(':0}
icp = {'*':2, '/':2, '+':1, '-':1, '(':3}
digits = list(map(str, range(1, 10)))
#['1','2','3',~~]
#952*1++33*+
'(6+5*(2-8)/2)'
T = 10
for t in range(1, 1 + 1):
    n = len('(6+5*(2-8)/2)') #int(input())
    equ = '(6+5*(2-8)/2)'#input()
    res = ''
    stack = []
    for i in range(n):
        if equ[i] in digits: #숫자일 때
            res += equ[i]
        else:#연산자일 때
            if equ[i] == ')':
                p = stack.pop()
                while p != '(':
                    res += p
                    p = stack.pop()
            elif stack == [] or isp[stack[-1]] < icp[equ[i]]:

                stack.append(equ[i])
            elif isp[stack[-1]] >= icp[equ[i]]:
                while icp[equ[i]] <= isp[stack[-1]]:
                    res += stack.pop()

                stack.append(equ[i])
    while stack:
        p = stack.pop()
        if p != '(':
            res += p
    print(res)

