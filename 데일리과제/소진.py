import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):

#1. 피연산자를 만나면 스택에 PUSH함
#2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에 POP하여 연산하고 연산결과를 다시 스택에 PUSH함
#3. 수식이 끝나면 마지막으로 스택을 PUSH함

    arr = list((input().split()))
    stack = []

    res = 0
    for i in range(len(arr)):
        if arr[i] == '.':
            if len(stack) > 1:
                res = "error"
            break

        elif arr[i] == '+' or arr[i] == '-' or arr[i] == '*' or arr[i] == '/':
            if len(stack) >= 2:
                x, y = int(stack.pop()), int(stack.pop())

                if arr[i] == '+':
                    res = y + x
                    stack.append(res)

                elif arr[i] == '-':
                    res = y - x
                    stack.append(res)

                elif arr[i] == '*':
                    res = y * x
                    stack.append(res)

                elif arr[i] == '/':
                    res = y // x
                    stack.append(res)
            else:
                res = "error"
                break

        else:
            stack.append(arr[i])
    print("#%d" %tc, res)
