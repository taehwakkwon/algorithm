import sys
sys.stdin = open('../now/input.txt')

import sys
sys.setrecursionlimit(10**7)
def check(r, c, s):
    for p in range(s):
        for q in range(s):
            if board[r + p][c + q] == 1:
                continue
            else:
                return False
    return True


def solve(r,c,cnt,b_sum):
    global m
    if b_sum == 0:
        m = min(m, cnt)
        return
    if cnt > m or r == 10:
        return
    if c == 10:
        solve(r+1,0,cnt,b_sum)
    else:
        if board[r][c] == 0:
            solve(r,c+1,cnt, b_sum)
        else:
            for size in range(5,0,-1):
                if papers[size] > 0 and r + size <= 10 and c + size <= 10 and check(r,c, size):
                    for p in range(size):
                        for q in range(size):
                            board[r+p][c+q] = 0
                    papers[size] -= 1
                    solve(r, c+1, cnt + 1, b_sum-size**2)
                    papers[size] += 1

                    for p in range(size):
                        for q in range(size):
                            board[r+p][c+q] = 1


n = 10
papers = [5]*6
board = [list(map(int, input().split())) for _ in range(10)]
ones = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            ones += 1

m = 1000
solve(0,0,0,ones)
if m == 1000:
    print(-1)
else:
    print(m)