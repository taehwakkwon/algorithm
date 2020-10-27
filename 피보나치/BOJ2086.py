import sys
sys.stdin = open('../now/input.txt')

def mat_mul(a,b):
    new_mat = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
         #   new_mat[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % 1000000000
            for k in range(2):
                new_mat[i][j] += (a[i][k] * b[k][j])
            new_mat[i][j] %= 1000000000
    return new_mat

def fibo(n):
    res = [[1,0],[0,1]]
    mat = [[1,1],[1,0]]
    for i in range(n.bit_length()):
        if n & (1<<i):
            res = mat_mul(res,mat)
            mat = mat_mul(mat,mat)
        else:
            mat = mat_mul(mat, mat)
    return res[1][0]

a, b = map(int, input().split())
print((1000000000+fibo(b+2) - fibo(a+1))%1000000000)
# print(fibo(a))
# print(fibo(b+1)-fibo(a))