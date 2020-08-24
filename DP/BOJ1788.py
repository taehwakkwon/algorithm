import sys
#sys.stdin = open('input.txt')
import sys
sys.setrecursionlimit(10**7)
def fibo(n):
    if n < 0:
        if dp[n] != 0:
            return dp[n]
        else:
            dp[n] = (fibo(n + 2) - fibo(n + 1))%1000000000
        return dp[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = (fibo(n - 1) + fibo(n - 2))%1000000000
        return dp[n]


dp = [0] * 2000002
res = fibo(int(input()))
if res < 0:
    print(-1)
    print(-res)
elif res == 0:
    print(0)
    print(0)
else:
    print(1)
    print(res)