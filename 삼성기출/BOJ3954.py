import sys
sys.stdin = open('../now/input.txt')

#8bit + pointer

MAX_LOOP = 5*10**7
divide = 1<<8
T = int(input())
for t in range(T):
    sm, sc, si = map(int, input().split()) #메모리크기, 코드의 크기, 입력의 크기
    program = input()
    inputs = input()
    dic = dict()
    reverse_dic = dict()
    stack = []
    for idx, char in enumerate(program):
        if char == '[':
            stack.append(idx)
        elif char == ']':
            dic[idx] = stack.pop()
            dic[dic[idx]] = idx

    memory = [0]*sm

    pointer = idx = pivot = char_pivot = 0
    n = len(program)

    while idx < MAX_LOOP and pivot < n:
        if program[pivot] == '-': #일때 -1 255
            memory[pointer] = (memory[pointer] - 1) % divide
        elif program[pivot] == '+':# 255 -> 256
            memory[pointer] = (memory[pointer] + 1) % divide
        elif program[pivot] == '<':
            pointer = (pointer - 1) % sm
        elif program[pivot] == '>':
            pointer = (pointer + 1) % sm
        elif program[pivot] == '[':
            if memory[pointer] == 0:
                pivot = dic[pivot]
            else:
                stack.append(pivot)
        elif program[pivot] == ']':
            if memory[pointer] != 0:
                pivot = dic[pivot]
            else:
                stack.pop()
        elif program[pivot] == '.':
            pass
        elif program[pivot] == ',':
            if char_pivot == si:
                memory[pointer] = 255
            else:
                memory[pointer] = ord(inputs[char_pivot])
                char_pivot += 1
        idx += 1
        pivot += 1
    if idx == MAX_LOOP:
        while pivot not in dic:
            pivot += 1
        print('Loops %d %d' %(stack[0],dic[stack[0]]))
    else:
        print('Terminates')




