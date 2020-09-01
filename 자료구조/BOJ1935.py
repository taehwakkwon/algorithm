import sys
sys.stdin = open('input.txt')

operator = ['*','/','+','-']
n = int(input())
equ = list(input())
alphabet = {chr(x) : 0 for x in range(ord('A'), ord('Z')+1)}
for i in range(n):
    alphabet[chr(i+ord('A'))] = int(input())

for i in range(len(equ)):
    if equ[i] in alphabet:
        equ[i] = alphabet[equ[i]]

pivot = 0
while pivot < len(equ):
    if equ[pivot] == '*':
        a, b = equ.pop(pivot-1), equ.pop(pivot-2)
        pivot -= 2
        equ[pivot] = b*a
    elif equ[pivot] == '/':
        a, b = equ.pop(pivot - 1), equ.pop(pivot - 2)
        pivot -= 2
        equ[pivot] = b / a
    elif equ[pivot] == '+':
        a, b = equ.pop(pivot - 1), equ.pop(pivot - 2)
        pivot -= 2
        equ[pivot] = b + a
    elif equ[pivot] == '-':
        a, b = equ.pop(pivot - 1), equ.pop(pivot - 2)
        pivot -= 2
        equ[pivot] = b - a
    else:
        pivot += 1
print('%.2f'  %equ[0])