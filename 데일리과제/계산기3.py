import sys
sys.stdin = open('sample_input.txt')

def calculator(equ):
    pivot = 0
    while pivot < len(equ):
        if equ[pivot] == '*':
            a, b = equ.pop(pivot - 1), equ.pop(pivot - 2)
            pivot -= 2
            equ[pivot] = float(b) * float(a)
        elif equ[pivot] == '/':
            a, b = equ.pop(pivot - 1), equ.pop(pivot - 2)
            pivot -= 2
            equ[pivot] = float(b) / float(a)
        elif equ[pivot] == '+':
            a, b = equ.pop(pivot - 1), equ.pop(pivot - 2)
            pivot -= 2
            equ[pivot] = float(b) + float(a)
        elif equ[pivot] == '-':
            a, b = equ.pop(pivot - 1), equ.pop(pivot - 2)
            pivot -= 2
            equ[pivot] = float(b) - float(a)
        else:
            pivot += 1
    return equ[0]


operator = ['*','/','+','-']
icp = {'*':2, '/':2, '+':1, '-':1, '(': 3}
isp = {'*':2, '/':2, '+':1, '-':1, '(': 0}

print(icp, isp)
T = 10
for t in range(1, T + 1):
    n = int(input())
    equ = input()
    res = ''
    operator = []
    for i in range(n):
        if equ[i].isdigit():
            res += equ[i]
        else:
            if equ[i] == ')':
                while True:
                    print(operator)
                    p = operator.pop()
                    if p == '(':
                        break
                    res += p
            elif equ[i] == '(':
                operator.append('(')
            else:
                p = ' '
                while operator and icp[equ[i]] > isp[operator[-1]]:
                    p = operator.pop()
                    if p != '(':
                        res += p
                operator.append(equ[i])
    else:
        while operator:
            p = operator.pop()
            if p != '(':
                res += p
    res = calculator(list(res))

    print('#%d %d' % (t, res))

# 3+(4+5+3*2)*6+7
# 34532*++6*+7+
# 345+6*+7+
