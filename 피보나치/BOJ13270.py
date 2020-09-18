import sys
#sys.stdin = open('input.txt')

cnt = 0
n = int(input())
dp_m = [float('inf')]*(n+1)
dp_M = [0]*(n+1)

MAX = 30
fibo =[0,2,3] + [0]*MAX
M, m = 0, n+1
for i in range(3,MAX):
    fibo[i] = fibo[i-1]+fibo[i-2]

for i in range(1, n+1):
    if fibo[i] > n:
        break
    dp_M[fibo[i]] = max(i, dp_M[fibo[i]])
    dp_m[fibo[i]] = min(i, dp_m[fibo[i]])
print(dp_M)
print(dp_m)
for i in range(1, n+1):
    if dp_M[i] != 0:
        for idx,j in enumerate(range(i,n+1, dp_M[i]), start=1):
            print(dp_M[j], dp_M[i] * idx)
            dp_M[j] = max(dp_M[j], dp_M[i]*idx)

    print()
    if dp_m[i] != float('inf'):
        for idx, j in enumerate(range(i, n + 1, dp_m[i]), start=1):
            print(dp_m[j], dp_m[i] * idx)
            dp_m[j] = min(dp_m[j], dp_m[i]*idx)


print(fibo)
print(dp_m)
print(dp_M)
print(dp_m[n],dp_M[n])

