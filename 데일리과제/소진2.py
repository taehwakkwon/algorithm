import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for tc in range(1, T+1):

#1. 피연산자를 만나면 스택에 PUSH함
#2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에 POP하여 연산하고 연산결과를 다시 스택에 PUSH함
#3. 수식이 끝나면 마지막으로 스택을 PUSH함

    arr = list((input().split()))
    stack = []
    cnt = 0
    res = 0
    for i in range(len(arr)):

        if arr[i] == '+' or arr[i] == '-' or arr[i] == '*' or arr[i] == '/':
            if len(stack) >= 2:
                x, y = int(stack.pop()), int(stack.pop())

                if arr[i] == '+':
                    res = y + x
                    stack.append(res)
                    cnt += 1
                elif arr[i] == '-':
                    res = y - x
                    stack.append(res)
                    cnt += 1
                elif arr[i] == '*':
                    res = y * x
                    stack.append(res)
                    cnt += 1
                elif arr[i] == '/' and x != 0:
                    res = y // x
                    stack.append(res)
                    cnt += 1
            else:
                res = "error"
                break

        elif arr[i] == '.':
            if len(stack) > 1:
                res = "error"
            break
            cnt += 1

        else:
            stack.append(arr[i])

        if arr[0] == '+' or arr[0] == '-' or arr[0] == '/' or arr[0] == '*' or arr[0] == '.':
            res = "error"


    print("#%d" %tc, res)