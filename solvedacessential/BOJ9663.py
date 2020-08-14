import sys
sys.stdin = open('input.txt')
def check(x,y):
    for i, j in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
        k, l = x, y
        while 0 <= k < n and 0 <= l < n:
            if board[k][l] == 0:
                k += i
                l += j
                continue
            else:
                return False
    return True

def dfs(v,x,y,q):
    global cnt, board
    if check(x,y) == False:
        board[x][y] = 0
        q -= 1
        return
    if v >= n:
        cnt += 1
        board = [[0] * n for _ in range(n)]
        return
    else:
        for i in range(n):
            for j in range(n):
                board[i][j] = 1
                dfs(v+1,i,j, q + 1)

n = int(input())
board = [[0]*n for _ in range(n)]
cnt = 0
dfs(0,0,0,0)
print(board)
print(cnt)


