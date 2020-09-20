import sys
#sys.stdin = open('input.txt')

a = int(input())
M = 0
for i in range(a+1):
    res = [a, i]
    while res[-2]-res[-1] >= 0:
        res.append(res[-2]-res[-1])
    if M < len(res):
        result = []
        result.extend(res[:])
        M = len(result)
print(len(result))
print(*result)


