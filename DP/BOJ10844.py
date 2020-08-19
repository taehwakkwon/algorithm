import sys
sys.stdin = open('input.txt')

n = int(input())
denominator = 10**9
cnt = 0
dp = [[0]*10 for _ in range(101)]
dp[0] = [0] + [1]*9
for i in range(1,n):
    dp[i][0] = (dp[i - 1][1])%denominator
    for j in range(1,9):
        dp[i][j] = (dp[i - 1][j-1] + dp[i - 1][j+1])%denominator
    dp[i][9] = (dp[i - 1][8])%denominator
print(sum(dp[n-1])%denominator)


'''
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
'''