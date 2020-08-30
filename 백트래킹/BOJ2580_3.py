import sys
sys.stdin = open('input.txt')
import time

start = time.time()
def check(r,c,k):
    if k in board[r]:
        return False
    for i in range(9):
        if k == board[i][c]:
            return False
    for p in range(3):
        for q in range(3):
            if board[r//3*3+p][c//3*3+q] == k:
                return False
    return True


def dfs():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for k in range(1,10):
                    if check(i,j,k):
                        board[i][j] = k
                        dfs()
                        #if dfs(zero - 1):return 1
                        board[i][j] = 0
                return
    for r in board:
        print(*r)
    print(time.time()-start)
    sys.exit()



board = [list(map(int, input().split())) for _ in range(9)]
dfs()
