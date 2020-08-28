def matrix_multiplication(m1, m2):
    # only 2 by 2 matrix
    a = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
    b = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
    c = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
    d = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
    return [[a, b], [c, d]]


def matrix_square(matrix):
    return matrix_multiplication(matrix, matrix)

def solve(N):
    stack = []

    while N > 1:
        if N % 2:
            stack.append('+')
        stack.append('x')
        N //= 2
    base_matrix = [[1, 1], [1, 0]]
    while stack:
        tmp = stack.pop()
        if tmp == '+':
            base_matrix = matrix_multiplication(base_matrix, fibo_matrix)
        else:
            base_matrix = matrix_square(base_matrix)
    return base_matrix[1][0] % 1000000007


fibo = [[0], [1]]
fibo_matrix = [[1, 1], [1, 0]]
#N = int(input())

print(solve(0))
def fibo(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b % 1000000007, (a + b) % 1000000007
    return a
