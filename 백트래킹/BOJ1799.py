import sys
sys.stdin = open('input.txt')
import time

start = time.time()
# 0 0  0 1  0 2  0 3  0 4
# 1 0  1 1  1 2  1 3  1 4
# 2 0  2 1  2 2  2 3  2 4
# 3 0  3 1  3 2  3 3  3 4
# 4 0  4 1  4 2  4 3  4 4
def check(r,c):
    for i in range(len(bishop)):
        if abs(r - bishop[i][0]) == abs(c - bishop[i][1]):
            return False
    return True


def dfs(r,c):
    global M
    if M < len(bishop):
        M = len(bishop)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and check(i,j):
                bishop.append((i,j))
                if dfs(i, j): return
                bishop.pop()
    return


M = 0
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
bishop = []
dfs(0,0)
print(M)



print(time.time()-start)


