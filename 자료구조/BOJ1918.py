import sys
sys.stdin = open('input.txt')


alphabet = list(map(chr, range(ord('A'),ord('Z')+1)))
icp = {'*':2, '/':2, '+':1, '-':1, '(':0, '(': -1}
isp = {'*':2, '/':2, '+':1, '-':1, '(':3, '(': -1}
operator = []


equ = list(input())
n = len(equ)
res = ''
for i in range(n):
    if equ[i] in alphabet:
        res += equ[i]
    else:
        if equ[i] == ')':
            while True:
                p = operator.pop()
                if p == '(':
                    break
                res += p
        elif equ[i] == '(':
            operator.append('(')
        else:
            p = ' '
            while operator and icp[equ[i]] <= isp[operator[-1]]:
                p = operator.pop()
                if p != '(':
                    res += p
            operator.append(equ[i])

while operator:
    p = operator.pop()
    if p != '(':
        res += p


print(res)
