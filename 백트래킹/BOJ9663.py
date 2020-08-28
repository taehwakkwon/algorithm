import time
import sys
sys.setrecursionlimit(10 ** 7)
def dfs(s):
    global cnt
    if s == N:
        cnt += 1
    for i in range(N):
        flag = True
        for j in range(s):
            if board[j][i] == 1 or board[i][j] == 1:
                flag = False
                break
        if flag:
            for j in range(min(i, s) + 1):
                if board[s - j][i - j] == 1:
                    flag = False
                    break

        if flag:
            for j in range(min(N - i, s + 1)):
                if board[s - j][i + j] == 1:
                    flag = False
                    break

        if flag == False:
            continue
        board[s][i] = 1
        dfs(s + 1)
        board[s][i] = 0

start = time.time()
cnt = 0
N = int(input())
board = [[0]*N for _ in range(N)]
dfs(0)
print(cnt)
print(time.time()-start)



