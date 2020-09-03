def dot(mat_A,mat_B):
    mat_C = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                mat_C[i][j] += mat_A[i][k] * mat_B[k][j]
            mat_C[i][j] %= 1000000007
    return mat_C

N = 2
B = int(input())
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
    print((res[0][0] + res[0][1])% 1000000007)