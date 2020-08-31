import sys
sys.stdin = open('input.txt')


alphabet = list(map(chr, range(ord('A'),ord('Z')+1)))
operator = ['+','-','*','/']

N = int(input())
equ = list(input())
for i in range(N):
    equ[equ.index(alphabet[i])] = int(input())
i = 0
res = float('inf')
print(equ)
while i < len(equ):

print(res)
print(equ)