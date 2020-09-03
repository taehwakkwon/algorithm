import sys
#sys.stdin = open('input.txt')


import sys
sys.setrecursionlimit(10**7)
def dot(mat_A,mat_B):
    mat_C = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                mat_C[i][j] += mat_A[i][k] * mat_B[k][j]
            if mat_C[i][j] < 0:
                mat_C[i][j] = -(abs(mat_C[i][j])%1000000007)
            else:
                mat_C[i][j] %= 1000000007
    return mat_C

def solve(n):
    if n == 0:
        return 1
    if n == 2:
        return 3
    if dp[n] != 0:
        return dp[n]
    dp[n] = (4*solve(n - 2) - solve(n-4))%1000000007
    return dp[n]
dp = [1, 0, 3] + [0] * 10 ** 6
solve(10000)

for i in range(0,10001,2):
    N = 2
    B = i#int(input())
    mat = [[4,-1], [1,0]]
    res = [[0]*N for _ in range(N)]
    if B % 2:
        print(0)
    else:
        B = B//2
        for i in range(N):
            res[i][i] = 1
        for i in range(len(bin(B))-2):
            if B&1<<i:
                res = dot(res, mat)
                mat = dot(mat, mat)
            else:
                mat = dot(mat, mat)
        print(dp[B * 2], (res[0][0] + res[0][1]) % 1000000007)
        if dp[B * 2] != (res[0][0] + res[0][1]) % 1000000007:
            print(-1)
