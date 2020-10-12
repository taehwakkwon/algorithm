import sys
sys.stdin = open('../now/input.txt')

#수식의 길이 19 -> dfs 가능
#0 < 숫자 <=9
#이중괄호 불가
import sys
sys.setrecursionlimit(10**7)
def dfs(v,b):
    global M
    #print(v,b)
    if v >= n // 2:
        new_equ = []
        ch = [0]*n
        for i in range(n//2):
            if 1 << i & b:
                if equ[2*i+1] == '+':
                    new_equ.append(equ[2*i] + equ[2*i+2])
                elif equ[2*i+1] == '-':
                    new_equ.append(equ[2*i] - equ[2*i+2])
                else:
                    new_equ.append(equ[2 * i] * equ[2 * i + 2])
                ch[2 * i] = ch[2 * i + 1] = ch[2 * i + 2] = 1
            else:
                for j in range(2*i, 2*(i+1)):
                    if ch[j] == 0:
                        new_equ.append(equ[j])
                        ch[j] = 1
        for j in range(n):
            if ch[j] == 0:
                new_equ.append(equ[j])

        res = new_equ[0]
        for i in range(1, len(new_equ),2):
            if new_equ[i] == '+':
                res += new_equ[i+1]
            elif new_equ[i] == '-':
                res -= new_equ[i+1]
            else:
                res *= new_equ[i+1]
        M = max(res,M)
        return
    else:
        dfs(v + 1, b)
        dfs(v + 2, b | 1 << v)

M = -float('inf')
n = int(input())
equ = list(input())
for i in range(len(equ)):
    if equ[i].isdigit():
        equ[i] = int(equ[i])
dfs(0,0)
print(M)