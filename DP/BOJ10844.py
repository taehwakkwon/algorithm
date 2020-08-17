import sys
sys.stdin = open('input.txt')

n = int(input())
denominator = 10**9
cnt = 0
dp = [[0]*10 for _ in range(101)]
dp[0] = [1]*10
for i in range(1,n):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
    dp[i][2] = dp[i - 1][1] + dp[i - 1][3]
    dp[i][3] = dp[i - 1][2] + dp[i - 1][4]
    dp[i][4] = dp[i - 1][3] + dp[i - 1][5]
    dp[i][5] = dp[i - 1][4] + dp[i - 1][6]
    dp[i][6] = dp[i - 1][5] + dp[i - 1][7]
    dp[i][7] = dp[i - 1][6] + dp[i - 1][8]
    dp[i][8] = dp[i - 1][7] + dp[i - 1][9]
    dp[i][9] = dp[i - 1][8]
print(dp)

def dfs(v,s):
    global cnt
    if v >= n:
        cnt += 1
        return
    else:
        s % denominator
        adder = s % 10
        if adder + 1 < 10:
            dfs(v + 1, s * 10 + adder + 1)
        if adder - 1 >= 0:
            dfs(v + 1, s * 10 + adder - 1)


n = int(input())
denominator = 10**9
cnt = 0
for i in range(1,10):
    dfs(1, i)
print(cnt)