import sys
sys.stdin = open('input.txt')

import sys
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [numbers[0]]
M = numbers[0]
for i in range(1,n):
    dp.append(max(dp[-1]+numbers[i], numbers[i]))
    if M < dp[-1]:
        M = dp[-1]
print(M)

#입력값이 음수만 있을 때를 생각못함..