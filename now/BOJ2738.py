import sys
sys.stdin = open('input.txt')
n, m = map(int, input().split())
mat_a = [list(map(int, input().split())) for _ in range(n)]
mat_b = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        mat_a[i][j] += mat_b[i][j]

for r in mat_a:
    print(*r)