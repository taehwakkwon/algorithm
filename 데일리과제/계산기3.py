import sys
sys.stdin = open('sample_input.txt')


T = 1

for tc in range(1, 1 + T):
    n = len("3+(4+5)*6+7")#int(input())
    equ = "3+(4+5)*6+7"#input()
    stack_operator = []
    res = ''
    i = 0
    while i < n:
        if equ[i].isdigit():
            res += equ[i]
        else:
            if equ[i] == ')':
                for j in range(len(stack_operator) - 1, -1, -1):
                    if stack_operator[j] == '(':
                        stack_operator.pop()
                        break
                    else:
                        res += stack_operator.pop()
            elif stack_operator and equ[i] == '*' and stack_operator[-1] == '*':
                res += stack_operator.pop()
            elif stack_operator and equ[i] == '+' and (stack_operator[-1] == '+' or stack_operator[-1] == '*'):
                res += stack_operator.pop()

            stack_operator.append(equ[i])
        i += 1
    else:
        print(stack_operator)
        while stack_operator:
            res += stack_operator.pop()
    print(res)

#345+6*+7+