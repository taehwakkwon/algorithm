import sys
sys.stdin = open('input.txt','r')

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0] = board[0]
for i in range(1,len(dp)):
    for j in range(len(dp[i])):
        dp[i][j] = dp[i-1][j] + board[i][j]

ans = []
for i in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    tmp = 0
    for y in range(y1-1,y2):
        tmp += dp[x2-1][y]
        if x1 <= 1:
            pass
        else:
            tmp -= dp[x1-2][y]
    ans.append(tmp)
for p in ans:
    print(p)
