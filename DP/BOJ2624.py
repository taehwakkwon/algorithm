import sys
sys.stdin = open('input.txt')

import sys
cnt = 0
res = []
result = []
T = int(sys.stdin.readline())
k = int(sys.stdin.readline())
dp = [[0]*(k+1) for _ in range(T+1)]
total = 0
for i in range(k):
    coin, n = map(int, input().split())
    total += coin*n
    for j in range(1,n+1):
        if j == 1:
            dp[coin * j][k] += 1
        if coin*j <= T:
            dp[coin*j][i] = 1


def solve(y,x,s, left):
    global cnt
    if s == T:
        cnt += 1
    if y == k and x == T + 1 or s > T or left + s < T:
        return
    else:
        for i in range(y,k):
            for j in range(x, T + 1):
                if dp[j][i]:
                    solve(i+1,j+1,s,left - j)
                    solve(i+1,j+1,s+j, left - j)
                    if s + j <= T:
                        dp[s+j][k] += 1

def solve(y,x,s):
    print(dp[x][y])
    if y > k:
        return 0
    if dp[x][y] != 0:
        return dp[x][y]
    else:
        for i in range(y, k):
            for j in range(T + 1):
                if s + j <= T:
                    print(dp[s + j])
                    dp[s + j][k] += solve(i + 1, 0, s + j)
            return dp[s + j][k]

solve(0, 1, 0)
print(dp)
print(cnt)
#print(dp)






#2147483648