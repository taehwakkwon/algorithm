import sys
sys.stdin = open('sample_input.txt')

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
            if equ[i] == '(':
                operator.append('(')

            if equ[i] == '+':
                operator.append('+')


            if equ[i] == '*':
                operator.append('*')


            if equ[i] == ')':
                operator

3+(4+5+3*2)*6+7
34532*++6*+7+
345+6*+7+
