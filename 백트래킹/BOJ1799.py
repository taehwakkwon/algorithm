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
    else:
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0 or left[i + j] == 1 or right[i - j + n] == 1:
                    continue
                else:
                    board[i][j] = 0
                    left[i + j] = right[i - j + n] = 1
                    dfs(i,j,s + 1)
                    board[i][j] = 1
                    left[i + j] = right[i - j + n] = 0


M = 0
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
left = [0]*(2*n+1)
right = [0]*(2*n+1)
dfs(0,0,0)
print(M)

print(time.time()-start)


