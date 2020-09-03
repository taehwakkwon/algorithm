import sys
sys.stdin = open('input.txt')
import time

start = time.time()
import sys
def dfs(r, c, s):
    global M
    if r == c == n - 1:
        if M < s:
            M = s
        return
    else:
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    for p, q in combinations_right[i + j]:
                        board[p][q] -= 1
                    for p, q in combinations_left[i - j + n]:
                        board[p][q] -= 1
                    dfs(i,j,s + 1)
                    for p, q in combinations_right[i + j]:
                        board[p][q] += 1
                    for p, q in combinations_left[i - j + n]:
                        board[p][q] += 1
        return


M = 0
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
combinations_right = {}
combinations_left = {}
for i in range(n):
    for j in range(n):
        combinations_right[i+j] = combinations_right.get(i+j, []) + [(i, j)]
        combinations_left[i - j + n] = combinations_left.get(i - j + n, []) + [(i, j)]
dfs(0,0,0)
print(M)



print(time.time()-start)


