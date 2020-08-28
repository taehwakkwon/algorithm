import sys
sys.stdin = open('sample_input.txt')
t = int(input())
def solve(m):
    global cnt
    for o in range(n):
        for j in range(n-k+1):
            if m[o][j:j+k] == [1] * k:
                if j+k == n:
                    if j-1 >= 0 :
                        if m[o][j-1] == 0 :
                            cnt += 1
                    else :
                        cnt += 1
                elif m[o][j+k] == 0 :
                    if j - 1 >= 0:
                        if m[o][j - 1] == 0:
                            cnt += 1
                    else:
                        cnt += 1
            else:
                continue

for tc in range(1, t+1):
    n, k = map(int,input().split())
    # ta = [([0] * (n)) for _ in range(n)]
    m = [list(map(int,input().split())) for _ in range(n)] # 가로

    # 세로 리스트 받기
    x = []
    for p in range(n):
        se = []
        for i in range(n):
            se.append(m[i][p])
        x.append(se)

    cnt = 0
    solve(m)
    solve(x)

    print(cnt)






t = int(input())
for tc in range(1, t+1):
    n, k = map(int,input().split())
    # ta = [([0] * (n)) for _ in range(n)]
    m = [list(map(str,input().split())) for _ in range(n)] # 가로

    # 세로 리스트 받기
    x = []
    for k in range(n):
        se = []
        for i in range(n):
            se.append(m[i][k])
        x.append(se)



t = int(input())
for tc in range(1, t+1):
    n, k = map(int,input().split())
    # ta = [([0] * (n)) for _ in range(n)]
    m = [list(map(str,input().split())) for _ in range(n)]
    # print(n[1][1])
    # print(m)
#     x = []
    cnt = 0
    for j in range(n):
        for i in range(n - k + 1):
            if m[j][:i+k] == ['0']*i + ['1']*k:
                if i + k == n:
                    cnt += 1
                elif i + k + 1 < n and m[j][i + k + 1] == '0':
                    cnt += 1
    for j in range(n):
        for i in range(n - k + 1):
            if m[:i + k][j] == ['0'] * i + ['1'] * k:
                if i + k == n:
                    cnt += 1
                elif i + k + 1 < n and m[i + k + 1][j] == '0':
                    cnt += 1

    print(cnt)




#1 2
#2 6
#3 6
#4 0
#5 14
#6 2
#7 45
#8 0
#9 98
#10 7

def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n - 2)


def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if dp[n] != 0:
        return arr[n]
    arr[n] = fibo(n-1) + fibo(n - 2)
    return dp[n]


dp = [0] * 100

# 기저 사례
def f(n):
    if n == 1: return 1
    if n == 2: return 3

    # 일반사례
    if memo[n]:
        return memo[n]

    memo[n] = f(n - 1) + f(n - 2) * 2

    return memo[n]