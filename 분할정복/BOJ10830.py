import sys
sys.stdin = open('input.txt','r')

import sys

def dot(mat_A,mat_B):
    mat_C = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                mat_C[i][j] += mat_A[i][k] * mat_B[k][j]
            mat_C[i][j] %= 1000
    return mat_C


N, B = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
res = [[0]*N for _ in range(N)]
for i in range(N):
    res[i][i] = 1

for i in range(len(bin(B))-2):
    if B&1<<i:
        res = dot(res, mat)
        mat = dot(mat, mat)
    else:
        mat = dot(mat, mat)
for r in res:
    print(*r)