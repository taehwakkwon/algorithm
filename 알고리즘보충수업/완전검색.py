#C(n,r) = C(n-1,r-1) + C(n-1,r)
import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T + 1):
    N, M = map(int,input().split())
    Russian_flag = [list(input()) for _ in range(N)]
    m = float('inf')

    for i in range(1, N - 1):
        for j in range(i + 1, N):
            W_cnt, B_cnt, R_cnt = 0, 0, 0
            for k in range(i):
                W_cnt += (M-Russian_flag[k].count('W'))
            for k in range(i, j):
                B_cnt += (M-Russian_flag[k].count('B'))
            for k in range(j, N):
                R_cnt += (M-Russian_flag[k].count('R'))
            if m > W_cnt + B_cnt + R_cnt:
                m = W_cnt + B_cnt + R_cnt
    print('#%d %d'%(t, m))

