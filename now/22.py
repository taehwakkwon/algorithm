import sys
sys.stdin = open('input.txt')

def dot(mat_A,mat_B):
    mat_C = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            mat_C[i][j] = (mat_A[i][0] * mat_B[0][j] + mat_A[i][1] * mat_B[1][j])%1000000000
    return mat_C


n = int(input())
print(n)
b = bin(n)[::-1][:-2]
A = [[1,1],[1,0]]
res = [[1,0],[0,1]]
for i in range(len(b)):
    if b[i] == '0':
        A = dot(A,A)
    else:
        res = dot(res, A)
        A = dot(A,A)
print(res)
print(res[1][0])