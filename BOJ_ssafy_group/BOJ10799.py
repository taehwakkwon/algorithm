import sys
sys.stdin = open('input.txt','r')
def solution(arrangement):
    stack = 0
    cut = False
    pre_str = ''
    answer = 0
    for idx in arrangement:
        if pre_str + idx == '()':
            stack -= 1
            answer += stack
        elif idx == '(':
            stack += 1
        elif idx == ')':
            stack -= 1
            answer += 1
        pre_str = idx
    return answer
print(solution(input()))