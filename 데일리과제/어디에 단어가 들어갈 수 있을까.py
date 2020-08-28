import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for i in range(n):
        r_cnt, c_cnt = 0, 0
        for j in range(n):
            if board[i][j] == 0:
                if r_cnt == k:
                    res += 1
                r_cnt = 0
            else:
                r_cnt += 1

            if board[j][i] == 0:
                if c_cnt == k:
                    res += 1
                c_cnt = 0
            else:
                c_cnt += 1
        if r_cnt == k:
            res += 1
        if c_cnt == k:
            res += 1
    print('#%d %d' %(tc, res))




